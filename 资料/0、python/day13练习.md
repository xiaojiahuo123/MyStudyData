# Day13 练习知识点总结

## 1. 并发与并行

| 概念 | 定义 | 关键词 |
|------|------|--------|
| **并发（Concurrency）** | 多个任务在同一时间段内交替执行，不一定同时运行 | 交替执行 |
| **并行（Parallelism）** | 多个任务在同一时刻真正同时执行（需要多核 CPU） | 同时执行 |

- 单核 CPU 上的多进程属于**并发**（宏观同时，微观交替）
- 多核 CPU 上的多进程可以实现真正的**并行**

## 2. 同步与异步

| 概念 | 定义 | 类比 |
|------|------|------|
| **同步（Synchronous）** | 调用后必须等待执行完毕才能继续 | 在柜台等菜做好再端走 |
| **异步（Asynchronous）** | 调用后不等待，通过回调/通知获得结果 | 点菜后回座位，菜好了服务员送来 |

---

## 3. 进程基础

### 3.1 创建进程

```python
import multiprocessing
import os

def greet(name):
    print(f"  子进程: 你好, {name}!")

p = multiprocessing.Process(target=greet, args=("Python",))
p.start()    # 启动子进程
p.join()     # 阻塞主进程，等待子进程结束
print("  主进程: 子进程已结束")
```

### 3.2 join() 的作用

`join()` 让**主进程阻塞**，等待子进程执行完毕后再继续。如果不加 `join()`，主进程可能在子进程之前结束。

### 3.3 PID 关系

```python
def show_pid():
    print(f"  子进程 PID={os.getpid()}, 父进程 PPID={os.getppid()}")

print(f"  主进程 PID={os.getpid()}")
p = multiprocessing.Process(target=show_pid)
p.start()
p.join()
```

- 子进程的 **PPID（父进程 ID）** 等于主进程的 **PID**
- `os.getpid()` → 当前进程 ID
- `os.getppid()` → 父进程 ID

---

## 4. 进程池（Pool）

### 4.1 apply（同步）

```python
pool = multiprocessing.Pool(3)
results = []
for i in range(3):
    r = pool.apply(task, args=(i,))   # 同步：阻塞等待结果
    results.append(r)
pool.close()
pool.join()
```

- `apply` 是**同步**的，任务**阻塞**主进程
- 3 个任务**逐个执行**（即使池子有 3 个进程）

### 4.2 apply_async（异步）

```python
pool = multiprocessing.Pool(3)
futures = []
for i in range(3):
    f = pool.apply_async(task, args=(i,))  # 异步：立即返回
    futures.append(f)
pool.close()
pool.join()
results = [f.get() for f in futures]
```

- `apply_async` 是**异步**的，任务**不阻塞**主进程
- 3 个任务**同时执行**
- 用 `f.get()` 获取结果（在 `pool.join()` 之后）

| | apply | apply_async |
|---|---|---|
| 同步/异步 | 同步 | 异步 |
| 是否阻塞主进程 | 阻塞 | 不阻塞 |
| 执行方式 | 逐个执行 | 同时执行 |
| 获取结果 | 直接返回 | 调用 `.get()` |

---

## 5. 进程间数据不共享

每个进程有**独立的内存空间**，传入的变量是独立副本：

```python
def add_to_list(shared_list):
    shared_list.append(1)
    print(f"  子进程 list={shared_list}")  # [1]

my_list = []
p = multiprocessing.Process(target=add_to_list, args=(my_list,))
p.start()
p.join()
print(f"  主进程 list={my_list}")  # []  ← 不受影响
```

**原因**：子进程拿到的是 `my_list` 的**序列化副本**，修改不会影响主进程的原始数据。

---

## 6. 进程间通信

### 6.1 multiprocessing.Queue（用于 Process）

```python
q = multiprocessing.Queue()
p1 = multiprocessing.Process(target=producer, args=(q,))
p2 = multiprocessing.Process(target=consumer, args=(q,))
```

- `args=(q,)` 传的是 **Queue 对象本身**（不是字符串），底层通过管道通信
- Queue 是**先进先出（FIFO）**
- 生产者放完数据后，消费者继续 `q.get()` 会**阻塞等待**
- 只能用于 `multiprocessing.Process`，**不能**直接用于 `Pool`

### 6.2 Manager().Queue()（用于 Pool）

```python
q = multiprocessing.Manager().Queue()
pool = multiprocessing.Pool(2)
pool.apply_async(producer, args=(q,))
pool.apply_async(consumer, args=(q,))
```

- 底层基于**代理对象（Proxy）**，通过 Manager 服务器进程间接访问
- 可以用于 `Pool` 和 `Process`
- 比 `multiprocessing.Queue` 慢（多了一层服务器进程中转）
- 支持更多共享类型：`list`、`dict`、`Namespace` 等

### 6.3 对比

| | multiprocessing.Queue | Manager().Queue() |
|---|---|---|
| 底层实现 | 管道（Pipe） | 代理对象（Proxy） |
| 适用场景 | Process | Pool 和 Process |
| 速度 | 快 | 慢（有服务器进程中转） |

---

## 7. 自定义进程类

继承 `multiprocessing.Process`，重写 `run()` 方法：

```python
class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()          # 必须调用父类构造
        self.queue = queue

    def run(self):                  # 重写 run()，start() 时自动调用
        for _ in range(5):
            self.queue.put(random.randint(1, 100))
        self.queue.put(None)        # 结束信号

class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            if item is None:        # 遇到结束信号停止
                break
            print(f"  取出: {item}")
```

---

## 8. Python 语法小知识

### 8.1 `_` 在 for 循环中的作用

`_` 是约定俗成的变量名，表示"我不需要这个值，只是想循环固定次数"：

```python
for _ in range(5):            # 循环 5 次，不关心循环变量
    q.put(random.randint(1, 100))

for i in range(5):            # 循环 5 次，同时用到 i
    print(i)                  # 0, 1, 2, 3, 4
```

- `for _ in range(5)` 和 `for i in range(5)` **都是循环 5 次**
- `_` 只是告诉读者"这个值我不用"
- `random.randint(1, 100)` 生成 1-100 的随机整数

### 8.2 random.randint() 生成随机数

```python
import random

random.randint(1, 100)    # 返回 1 到 100 之间的随机整数（包含两端）
```

---

## 9. 线程基础

### 9.1 线程基本概念

- 线程是操作系统能够进行运算调度的**最小单位**，被包含在**进程**中
- 同一进程内的多个线程共享该进程的**内存空间**和**全局变量/资源**
- Python 中由于 **GIL（Global Interpreter Lock）** 的存在，同一时刻只能有一个线程执行 **Python 字节码**
- 线程的开销比进程**小**，创建和切换速度比进程**快**

### 9.2 创建线程

```python
import threading
import time

def print_numbers(label, count):
    for i in range(count):
        print(f"  [{threading.current_thread().name}] {label}: {i}")
        time.sleep(0.1)

t1 = threading.Thread(target=print_numbers, args=("A", 3), name="Worker-1")
t2 = threading.Thread(target=print_numbers, args=("B", 3), name="Worker-2")
t1.start()
t2.start()
t1.join()
t2.join()
print(f"  [{threading.current_thread().name}] 所有线程结束")
```

- 两个线程的输出**会交替出现**（并发执行）
- 最后一行的线程名是 **MainThread**（主线程）
- `join()` 的作用：阻塞主线程，等待子线程执行完毕

### 9.3 线程池 ThreadPoolExecutor

```python
import concurrent.futures

def square(n):
    time.sleep(0.2)
    return n ** 2

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(square, i) for i in range(5)]
    results = [f.result() for f in futures]
print(f"  结果: {results}")
```

- `max_workers=3` 表示线程池中最多有 **3 个线程同时工作**
- 提交 5 个任务但只有 3 个线程，第 4、5 个任务会**等待前面的线程空闲后执行**
- `executor.submit()` 返回的对象类型是 **Future**
- `with` 语句结束时会自动调用 **shutdown()** 关闭线程池

**任务多于线程数时的执行过程**（5 个任务，3 个线程）：

```
线程1: [square(0)] ──完成── [square(3)] ──完成──
线程2: [square(1)] ──完成── [square(4)] ──完成──
线程3: [square(2)] ──完成──  空闲
```

1. 前 3 个任务立即被 3 个线程认领，**同时执行**
2. 第 4、5 个任务进入**等待队列**，没有空闲线程
3. 当任意线程执行完毕后，从队列中取下一个任务继续执行
4. `f.result()` 会**阻塞直到该任务完成**才返回结果
5. **不会报错，不会丢失任务**，只是后面的任务要等——这正是线程池控制并发数量的意义

---

## 10. 线程安全

### 10.1 竞争条件（Race Condition）

```python
g_num = 0

def unsafe_increment():
    global g_num
    for _ in range(100000):
        g_num += 1  # 不是原子操作！

threads = [threading.Thread(target=unsafe_increment) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"  最终 g_num = {g_num}")  # 不等于 300000！
```

- 预期 300000，实际**等于或小于**期望值
- `g_num += 1` 不是**原子操作**，包含 **3 步**：读取、加1、写回
- 多线程同时执行时可能互相覆盖，导致数据丢失
- 解决方案：使用 **Lock（锁）**

### 10.2 Lock 加锁

```python
lock = threading.Lock()

def safe_increment():
    global g_num_safe
    for _ in range(100000):
        lock.acquire()      # 获取锁（阻塞等待）
        g_num_safe += 1
        lock.release()      # 释放锁

# 结果一定是 300000
```

- `lock.acquire()` → **获取锁**，如果锁已被其他线程持有，则阻塞等待
- `lock.release()` → **释放锁**，让其他线程可以获取
- 如果忘记调用 `lock.release()` → **死锁**，其他线程永远等待

### 10.3 with lock 上下文管理器

```python
# 写法A: 手动 acquire/release
def style_a():
    lock.acquire()
    counter_a += 1
    lock.release()

# 写法B: with 上下文管理器（推荐）
def style_b():
    with lock:
        counter_b += 1
```

- 两种写法功能**等价**
- `with lock` 的优势：即使 with 块内发生**异常**，锁也会被自动**释放**
- 推荐使用写法 **B**

### 10.4 经典错误：while 判断在锁外面

```python
# ❌ 错误写法：while 判断在锁外面，会卖到负数
def sell_tickets(window_name):
    global tickets
    while tickets >= 0:          # ← 3个线程同时通过检查
        with ticket_lock:        # ← 等拿到锁时 tickets 可能已经是负数了
            tickets -= 1
            print(f"{window_name} 剩余{tickets}张")

# ✅ 正确写法：判断和修改都在锁内
def sell_tickets(window_name):
    global tickets
    while True:
        with ticket_lock:
            if tickets <= 0:     # ← 在锁内判断，不会被其他线程干扰
                break
            tickets -= 1
            print(f"{window_name} 剩余{tickets}张")
```

**原理**：`while tickets >= 0` 在锁外面判断，3 个线程可能同时看到 `tickets=2`，都通过检查后排队拿锁，等拿到锁时 `tickets` 已经被前面的线程减成负数了。**判断和修改必须在同一个锁的保护范围内**。

---

## 11. 进程 vs 线程对比

| 维度 | 进程（Process） | 线程（Thread） |
|------|----------------|----------------|
| 资源分配 | 资源分配的基本单位 | CPU 调度的基本单位 |
| 内存空间 | 每个进程独立内存空间 | 同一进程内线程共享内存空间 |
| 创建/切换开销 | 大，需要分配独立资源 | 小，共享进程资源 |
| 并发性 | 可以真正并行（多核） | 受 GIL 限制，不能真正并行执行 Python 字节码 |
| 独立性 | 进程间相互独立 | 线程间相互依赖（一个崩溃可能影响整个进程） |
| 通信方式 | Queue, Pipe, Manager | 共享变量（需加锁保证安全） |
| GIL 影响 | 不受 GIL 影响 | 受 GIL 影响 |

### 场景选择

| 场景 | 选择 | 理由 |
|------|------|------|
| 爬取 1000 个网页（I/O 密集型） | **多线程** | 大部分时间在等待网络响应，线程开销小、创建快 |
| 100 万张图片矩阵运算（CPU 密集型） | **多进程** | 需要大量计算，多进程可利用多核真正并行，绕过 GIL |
| 同时读写同一个文件 | **多线程** | 线程共享内存空间，配合锁即可保证安全 |
| 多任务共享大字典并实时修改 | **多线程** | 线程天然共享全局变量，配合 Lock 即可安全修改 |

---

## 12. 模块导入方式

| 导入方式 | 用法 | 特点 |
|---------|------|------|
| `import os` | `os.getcwd()` | 最安全，不会命名冲突 |
| `from os import getpid` | `getpid()` | 只导入需要的，直接使用 |
| `import threading as th` | `th.Thread()` | 起别名，简化调用 |
| `from os import *` | `getcwd()` | **不推荐**，可能覆盖已有变量名 |

---

## 13. GIL（Global Interpreter Lock）

- **什么是 GIL**：Python 解释器层面的全局锁，确保同一时刻只有一个线程执行 Python 字节码
- **为什么需要 GIL**：简化 CPython 内存管理，避免引用计数的竞争条件
- **影响**：CPU 密集型任务中多线程无法利用多核优势；I/O 密集型任务影响较小
- **绕过方法**：使用多进程、C 扩展、或换用无 GIL 的 Python 实现

---

## 常见错误总结

| 错误类型 | 示例 | 修复 |
|---------|------|------|
| 忘记 `if __name__ == '__main__'` | 直接写 `p.start()` | 加 `if __name__ == '__main__':` 保护 |
| Pool 忘记 close/join | 只写 `apply_async` | 加 `pool.close(); pool.join()` |
| `multiprocessing.Queue` 传给 Pool | `pool.apply_async(f, args=(q,))` | 改用 `Manager().Queue()` |
| 子进程修改 list 想影响主进程 | 传普通 list | 用 `Manager().list()` |
| `args=(q)` 而非 `args=(q,)` | 少了逗号 | `args=(q,)` 才是元组 |
| 共享变量修改未加锁 | `counter += 1` | 用 `lock.acquire/release` 或 `with lock` |
| Lock 在循环内创建 | 每次调用都创建新锁 | 将 Lock 定义在函数外部，全局共享 |
| ThreadPoolExecutor 忘记关闭 | 没有 `shutdown()` | 用 `with` 语句自动关闭 |
