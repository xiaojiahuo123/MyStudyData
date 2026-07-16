# Day13 知识点总结

## 1. 相关概念

### 1.1 并发与并行

| 概念     | 说明                           |
| ------ | ---------------------------- |
| **并发** | 单个 CPU 处理多个任务，各任务交替执行（时间片轮转） |
| **并行** | 多个 CPU 同时执行多个任务，真正的同时执行      |

### 1.2 同步与异步

| 概念     | 说明                        |
| ------ | ------------------------- |
| **同步** | 多个任务排队执行，第一个任务执行完毕后才执行下一个 |
| **异步** | 多个任务同时执行，相互之间互不影响         |

***

## 2. 进程（Process）

### 2.1 进程的概念

- 进程是操作系统进行**资源分配**的基本单位
- 操作系统中一个正在运行的程序或软件就是一个进程
- 每个进程都有自己**独立的一块内存空间**
- 一个进程崩溃后，在保护模式下不会对其他进程产生影响
- 多进程是指在操作系统中同时运行多个程序

### 2.2 创建进程对象

#### 方式一：使用 `multiprocessing.Process`

```python
import multiprocessing
import os

def write_file():
    with open('test.txt', 'a') as f:
        while True:
            f.write('hello world\n')
            f.flush()           # 手动刷写缓冲区
            time.sleep(0.5)

def read_file():
    with open('test.txt', 'r') as f:
        while True:
            time.sleep(0.5)
            line = f.readline()
            print(line)

if __name__ == '__main__':
    # 创建子进程
    p1 = multiprocessing.Process(target=write_file)
    p2 = multiprocessing.Process(target=read_file)

    # 启动进程
    p1.start()
    p2.start()
```

> **注意**：`if __name__ == '__main__'` 是必须的，Windows 下多进程必须在主模块中创建。

#### 方式二：自定义进程类

继承 `multiprocessing.Process`，重写 `run()` 方法：

```python
import multiprocessing
import os

class Worker(multiprocessing.Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # run() 方法中定义进程执行的任务
        print(f"当前进程id: {os.getpid()}, 名称: {self.name}, 父进程id: {os.getppid()}")

if __name__ == '__main__':
    for i in range(5):
        p = Worker("my_p_" + str(i))
        p.start()
```

**常用方法/属性：**

| 方法/属性          | 说明                     |
| -------------- | ---------------------- |
| `start()`      | 启动进程                   |
| `join()`       | 阻塞等待进程结束(阻塞主进程等待子进程执行) |
| `run()`        | 重写此方法定义进程任务            |
| `os.getpid()`  | 获取当前进程 ID              |
| `os.getppid()` | 获取父进程 ID               |

### 2.3 进程池（Pool）

一次性创建多个进程对象放到池中，需要时直接从池里取，避免频繁创建和销毁进程。

```python
import os
import time
import multiprocessing

def func():
    for i in range(10):
        print(f"当前进程id:{os.getpid()}, 打印了{i}")
        time.sleep(0.5)

if __name__ == '__main__':
    process_num = 5
    pool = multiprocessing.Pool(process_num)

    for i in range(process_num):
        # pool.apply(func)       # 同步：阻塞，逐个执行
        pool.apply_async(func)   # 异步：非阻塞，同时执行

    pool.close()  # 关闭进程池，不再接受新任务
    pool.join()   # 阻塞主进程，等待所有子进程执行完毕
    print("done")
```

| 方法                  | 说明            |
| ------------------- | ------------- |
| `Pool(n)`           | 创建大小为 n 的进程池  |
| `apply(func)`       | 同步执行，阻塞直到任务完成 |
| `apply_async(func)` | 异步执行，非阻塞，立即返回 |
| `close()`           | 关闭进程池         |
| `join()`            | 等待所有子进程结束     |

### 2.4 进程间数据不共享

每个进程有**独立的内存空间**，进程间变量互不影响：

```python
import multiprocessing
import os

def func(list1):
    for i in range(10):
        list1.append(i)
        print(f"当前进程id:{os.getpid()}", list1)

if __name__ == "__main__":
    list1 = []
    p1 = multiprocessing.Process(target=func, args=(list1,))
    p2 = multiprocessing.Process(target=func, args=(list1,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("done", os.getpid(), list1)  # 主进程的 list1 仍为空 []
```

> **结果**：每个子进程各自维护一份 `list1` 的拷贝，主进程的 `list1` 始终为空。

### 2.5 进程间通信 — Queue

使用 `multiprocessing.Queue` 或 `multiprocessing.Manager().Queue()` 实现进程间数据共享：

```python
import multiprocessing
import os
import random
import time

# 生产者：向队列中放数据
def func1(qu):
    while True:
        num = random.randint(1, 50)
        qu.put(num)
        print(f"进程id {os.getpid()} 向队列中放入了数据 {num}")
        time.sleep(0.3)

# 消费者：从队列中取数据
def func2(qu):
    while True:
        num = qu.get()
        print(f"进程id {os.getpid()} 从队列取出了数据 {num}")

if __name__ == '__main__':
    qu = multiprocessing.Manager().Queue(50)
    pool = multiprocessing.Pool(2)
    pool.apply_async(func1, args=(qu,))
    pool.apply_async(func2, args=(qu,))
    pool.close()
    pool.join()
```

| 方法               | 说明              |
| ---------------- | --------------- |
| `Queue(maxsize)` | 创建队列，可指定最大容量    |
| `put(item)`      | 向队列中放入数据（队满时阻塞） |
| `get()`          | 从队列中取出数据（队空时阻塞） |

> **两种 Queue 的区别**：
>
> - `multiprocessing.Queue()`：适用于 `Process` 创建的进程
> - `multiprocessing.Manager().Queue()`：适用于进程池（`Pool`）创建的进程

***

## 3. 线程（Thread）

### 3.1 线程的概念

- 线程是处理器**任务调度和执行**的基本单位
- 一个进程至少有一个线程，也可以运行多个线程
- 多个线程之间**共享进程的内存空间**
- 线程运行出错异常后，如果没有捕获，会导致**整个进程崩溃**
- 多线程是指在同一进程中同时执行多个任务

### 3.2 进程 vs 线程

| 特性   | 进程            | 线程             |
| ---- | ------------- | -------------- |
| 本质   | 资源分配的基本单位     | 任务调度和执行的基本单位   |
| 内存   | 独立内存空间        | 共享进程内存         |
| 开销   | 创建/切换开销大      | 创建/切换开销小       |
| 崩溃影响 | 一个进程崩溃不影响其他进程 | 一个线程崩溃导致整个进程崩溃 |
| 通信   | 需要 IPC（队列等）   | 直接共享变量         |

### 3.3 创建线程对象

#### 方式一：使用 `threading.Thread`

```python
import threading
import time

def func():
    flag = 0
    while True:
        print(threading.current_thread().name, f"{flag}" * 5)
        flag = flag ^ 1  # 0 和 1 交替切换
        time.sleep(0.5)

if __name__ == '__main__':
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("done")
```

#### 方式二：自定义线程类

继承 `threading.Thread`，重写 `run()` 方法：

```python
import threading
import time

class Worker(threading.Thread):
    def run(self):
        flag = 0
        while True:
            print(threading.current_thread().name, f"{flag}" * 5)
            flag = flag ^ 1
            time.sleep(0.5)

if __name__ == '__main__':
    t1 = Worker(name="线程1")
    t2 = Worker(name="线程2")
    t1.start()
    t2.start()
```

**常用方法/属性：**

| 方法/属性                   | 说明          |
| ----------------------- | ----------- |
| `start()`               | 启动线程        |
| `join()`                | 阻塞等待线程结束    |
| `run()`                 | 重写此方法定义线程任务 |
| `current_thread().name` | 获取当前线程名称    |

### 3.4 线程池（ThreadPoolExecutor）

使用 `concurrent.futures.ThreadPoolExecutor` 管理线程：

```python
import concurrent.futures

def func(tname):
    global word
    for i, char in enumerate(word):
        word[i] = chr(ord(char) ^ 1)
        print(f"{tname}: {word}\n", end="")
    return word

if __name__ == "__main__":
    word = list("idmmn!vnsme")

    # 使用 with 语句确保线程被及时清理
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future1 = executor.submit(func, "线程1")
        future2 = executor.submit(func, "线程2")
        future3 = executor.submit(func, "线程3")

        # 获取返回值
        word = future1.result()
        word = future2.result()
        word = future3.result()
        print("".join(word))  # hello world
```

| 方法                                | 说明                    |
| --------------------------------- | --------------------- |
| `ThreadPoolExecutor(max_workers)` | 创建线程池，指定最大线程数         |
| `submit(func, *args)`             | 提交任务到线程池，返回 Future 对象 |
| `future.result()`                 | 获取任务的返回值（阻塞等待）        |

### 3.5 线程安全问题

多个线程共享同一变量时，可能出现**数据竞争**（Race Condition）：

```python
import threading

def func():
    global g_num
    for _ in range(10):
        tmp = g_num + 1    # 读取
        # time.sleep(0.3)  # 加上延迟更容易观察到问题
        g_num = tmp         # 写入
        print(f"当前线程 {threading.current_thread().name}: {g_num}")

if __name__ == '__main__':
    g_num = 0
    threads = [threading.Thread(target=func, name="线程" + str(i)) for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print(f"当前线程 {threading.current_thread().name}", g_num)
    # 预期 30，实际结果可能小于 30
```

**问题原因：**

```
线程1: 读取 g_num=0 → tmp=1（还没写入）
线程2: 读取 g_num=0 → tmp=1（读到旧值）
线程1: 写入 g_num=1
线程2: 写入 g_num=1（覆盖了线程1的写入！）
```

> 读取-修改-写入不是原子操作，多个线程可能同时读到旧值，导致结果丢失。

**解决方案：** 使用**互斥锁**（Lock）保证同一时刻只有一个线程访问共享变量：

```python
import threading

def func():
    global g_num
    for _ in range(10):
        lock.acquire()       # 加锁
        tmp = g_num + 1
        g_num = tmp
        print(f"当前线程 {threading.current_thread().name}: {g_num}")
        lock.release()       # 解锁

if __name__ == '__main__':
    g_num = 0
    lock = threading.Lock()
    threads = [threading.Thread(target=func, name="线程" + str(i)) for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print(f"当前线程 {threading.current_thread().name}", g_num)  # 结果一定是 30
```

或者使用**上下文管理器**简化：

```python
with lock:
    tmp = g_num + 1
    g_num = tmp
```

***

## 4. 模块导入

Python 支持多种模块导入方式：

```python
# 方式一：导入整个模块
import P01_math_operations as op
print(op.add(3, 5))

# 方式二：导入指定函数
from P01_math_operations import add, mult
print(add(3, 5))

# 方式三：导入所有（不推荐，容易命名冲突）
from P01_math_operations import *
print(add(3, 5))
```

***

## 总结

| 知识点   | 核心要点                                                    |
| ----- | ------------------------------------------------------- |
| 并发/并行 | 并发是交替执行，并行是真正同时执行                                       |
| 进程    | 资源分配单位；独立内存；`multiprocessing.Process` 或继承重写 `run()`     |
| 进程池   | `multiprocessing.Pool(n)`；`apply` 同步 / `apply_async` 异步 |
| 进程通信  | 进程间变量不共享；使用 `Queue` 的 `put()`/`get()` 通信                |
| 线程    | 任务调度单位；共享内存；`threading.Thread` 或继承重写 `run()`            |
| 线程池   | `concurrent.futures.ThreadPoolExecutor`；`submit()` 提交任务 |
| 线程安全  | 共享变量存在竞争条件；使用 `threading.Lock` 加锁保护                     |

