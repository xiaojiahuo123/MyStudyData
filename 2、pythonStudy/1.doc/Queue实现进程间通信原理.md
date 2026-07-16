# Queue 实现进程间通信原理

## 1. multiprocessing.Queue 基本用法

`multiprocessing.Queue` 是 Python 提供的跨进程安全的队列，用于进程间数据传递。

```python
import multiprocessing
import os

def producer(q):
    for i in range(3):
        q.put(i * 100)
        print(f"  生产者 PID={os.getpid()} 放入: {i * 100}")

def consumer(q):
    while True:
        item = q.get()
        print(f"  消费者 PID={os.getpid()} 取出: {item}")

q = multiprocessing.Queue()
p1 = multiprocessing.Process(target=producer, args=(q,))
p2 = multiprocessing.Process(target=consumer, args=(q,))
p1.start()
p2.start()
p1.join()
p2.terminate()  # 生产者结束后消费者阻塞在 q.get()，强制结束
```

## 2. args=(q,) 传参原理

`multiprocessing.Process(target=producer, args=(q,))` 中的 `args=(q,)` 传的是 **Queue 对象本身**，不是字符串 "q"。

```python
q = multiprocessing.Queue()   # q 是一个 Queue 对象

# args=(q,) 的意思是：调用 producer(q) 时，把 q 这个对象传进去
p1 = multiprocessing.Process(target=producer, args=(q,))

# 等价于：
producer(q)
```

### 进程不是内存隔离的吗？Queue 怎么传过去的？

`multiprocessing.Queue` 不是普通容器，它内部有**进程间通信机制**（底层使用管道+信号量）。传过去的是一个"通信接口"，而不是复制整个数据。

```
主进程                          子进程 p1              子进程 p2
  │                               │                      │
  ├─ 创建 Queue(q)                │                      │
  │   (底层建立跨进程管道)         │                      │
  │                               │                      │
  ├─ 把 q 传给 p1 ──────────→ q.put(0)                   │
  │                    通过管道发送 ────────→ q.get() 拿到 0
  ├─ 把 q 传给 p2 ───────────────────────────────────────→│
```

**注意**：如果传的是普通 `list`，跨进程时是独立的副本，修改不会同步。必须用 `multiprocessing.Queue` 或 `multiprocessing.Manager().list()`。

---

## 3. 管道（Pipe）

管道是最底层的进程间通信机制，就是**两个进程之间的数据通道**，像一根水管，一端进水、一端出水。

```python
import multiprocessing

# 创建管道：返回两个连接对象（管道的两端）
conn1, conn2 = multiprocessing.Pipe()

def sender(conn):
    conn.send("hello")      # 从 conn2 这一端塞数据

def receiver(conn):
    msg = conn.recv()        # 从 conn1 这一端取数据
    print(msg)               # → "hello"

p1 = multiprocessing.Process(target=sender, args=(conn2,))
p2 = multiprocessing.Process(target=receiver, args=(conn1,))
p1.start()
p2.start()
```

```
进程 A                              进程 B
  │                                    │
  │  conn2.send("hello")  ──水管──→  conn1.recv()  → "hello"
  │                                    │
```

### 管道的特点

| 特性 | 说明 |
|------|------|
| **双向** | 两端都能 send/recv（默认），也可设置 `duplex=False` 单向 |
| **只连接两个进程** | 一对一通信，不能一对多 |
| **速度快** | 底层用操作系统原生管道，比 Queue 少一层封装 |
| **无缓冲管理** | 没有 Queue 的阻塞队列、多生产者协调等功能 |

### 管道和 Queue 的关系

**`multiprocessing.Queue` 底层就是用管道实现的**，在管道基础上加了锁、阻塞、队列管理等功能：

```
multiprocessing.Pipe          multiprocessing.Queue
  原始水管                     自动售货机
  ────────                    ┌──────────┐
  ════════  ← 直接传输        │ 锁/阻塞  │ ← 自动管理
  ────────                    │ 队列逻辑 │
                              │  + 管道  │ ← 底层还是管道
                              └──────────┘
```

---

## 4. Manager().Queue() 与代理对象

### 底层实现对比

| 方式 | 底层实现 | 原理 |
|------|---------|------|
| `multiprocessing.Queue` | **管道（Pipe）** | 直接通过管道传递数据 |
| `multiprocessing.Pipe` | **管道（Pipe）** | 两个进程间的直接双向通道 |
| `Manager().Queue()` | **代理对象（Proxy）** | 通过 Manager 服务器进程间接访问 |

### Manager 的工作方式

Manager 启动一个**独立的服务器进程**，真正的数据结构（Queue、list、dict 等）都存在这个服务器进程中，其他进程拿到的都是**代理对象**，每次操作都通过管道与服务器进程通信。

```
进程 A (生产者)          Manager 服务器进程           进程 B (消费者)
    │                        │                           │
    │   代理对象发送请求 ──→ │  真正的 Queue 在这里       │
    │                        │  接收请求并操作 ────────→  │
    │   代理对象接收结果 ←── │                            │
```

- 比 `multiprocessing.Queue` **慢**（多了一层服务器进程中转）
- 但支持更多类型：`list`、`dict`、`Namespace`、`Lock`、`Semaphore` 等

### 代码示例

```python
from multiprocessing import Manager

with Manager() as manager:
    shared_list = manager.list()       # 代理对象，不是普通 list
    shared_dict = manager.dict()       # 代理对象，不是普通 dict

    p1 = multiprocessing.Process(target=writer, args=(shared_list,))
    p2 = multiprocessing.Process(target=reader, args=(shared_list,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```

---

## 5. 总结

```
通信方式复杂度（从底层到高层）：

操作系统原生管道
    ↓
multiprocessing.Pipe          → 最简单，一对一，最快
    ↓
multiprocessing.Queue         → 一对多，自带锁和阻塞，常用
    ↓
Manager().Queue()             → 通过代理对象，支持更多数据类型，最慢
```

- **一对一**简单通信 → 用 `Pipe`
- **一对多**生产者/消费者 → 用 `multiprocessing.Queue`
- 需要共享 `list`/`dict` 等复杂结构 → 用 `Manager().list()` / `Manager().dict()`
