# multiprocessing.Process() 详解

## 1. 函数签名

```python
multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```

### 参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| `group` | `None` | 保留参数，必须为 `None`（与 `threading.Thread` 接口一致） |
| `target` | callable | 子进程中要执行的函数（传入函数对象，不是调用） |
| `name` | str | 进程名称，不指定则自动生成 `Process-1`、`Process-2` 等 |
| `args` | tuple | 传给 `target` 的位置参数，必须是元组形式 |
| `kwargs` | dict | 传给 `target` 的关键字参数 |
| `daemon` | bool | 是否设为守护进程（主进程退出时自动终止） |

### 基本使用

```python
import multiprocessing
import os

def worker(name):
    print(f"进程 {name}, PID: {os.getpid()}")

if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=("子进程1",))
    p.start()
    p.join()
```

---

## 2. 常用方法和属性

### 2.1 实例方法

| 方法 | 说明 |
|------|------|
| `start()` | 启动子进程，调用 `run()` 方法 |
| `run()` | 子进程中执行的方法（可被子类重写） |
| `join(timeout=None)` | 阻塞等待子进程结束，`timeout` 为超时秒数 |
| `is_alive()` | 判断子进程是否还在运行 |
| `terminate()` | 强制终止子进程（发送 SIGTERM 信号） |
| `kill()` | 强制杀死子进程（发送 SIGKILL 信号） |
| `close()` | 释放进程对象持有的资源（Python 3.7+），close 后再调用 start/join 会报 ValueError |

### 2.2 常用属性

| 属性 | 说明 |
|------|------|
| `pid` | 子进程的进程 ID（`start()` 后才有值） |
| `name` | 进程名称 |
| `daemon` | 是否为守护进程 |
| `exitcode` | 子进程的退出码（运行中为 `None`，正常退出为 `0`） |
| `sentinel` | 进程的原生句柄（Linux: 文件描述符，Windows: 进程句柄），可用于 `select.select()` 等待多个进程 |

### 2.3 模块级函数

| 函数 | 说明 |
|------|------|
| `os.getpid()` | 获取当前进程 ID |
| `os.getppid()` | 获取父进程 ID |

```python
import multiprocessing
import os

def worker():
    print(f"子进程 PID: {os.getpid()}, 父进程 PID: {os.getppid()}")

if __name__ == '__main__':
    print(f"主进程 PID: {os.getpid()}")
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
    print(f"子进程退出码: {p.exitcode}")
```

---

## 3. `start()` 与 `run()` 的区别

```python
import multiprocessing

def worker():
    print(f"worker 执行, PID: {os.getpid()}")

if __name__ == '__main__':
    p = multiprocessing.Process(target=worker)

    p.run()    # ❌ 在主进程中直接调用，不会创建子进程
    p.start()  # ✅ 创建新子进程，在子进程中调用 run()
```

| 调用方式 | 执行位置 | 是否创建新进程 |
|---------|---------|---------------|
| `p.run()` | 当前进程 | 否 |
| `p.start()` | 新的子进程 | 是 |

**`start()` 内部流程：**

```
p.start()
  │
  ├── 1. 安全检查（进程是否已关闭、是否已启动过）
  │
  ├── 2. 调用 self._Popen(self) 创建子进程
  │      ├── Windows: _winapi.CreateProcess()  → 启动新 Python 解释器
  │      ├── Linux:    os.fork()               → 复制当前进程
  │      └── 序列化 Process 对象传递给子进程
  │
  ├── 3. 子进程中执行 _bootstrap()
  │      ├── 设置当前进程信息
  │      └── 调用 self.run()
  │           └── 执行 self._target(*self._args, **self._kwargs)
  │
  └── 4. 父进程继续执行 start() 之后的代码
```

---

## 4. `join()` 的实现原理

```python
def join(self, timeout=None):
    # 核心：调用 self._popen.wait(timeout)
    res = self._popen.wait(timeout)
    if res is not None:
        _children.discard(self)  # 从活跃子进程集合中移除
```

**底层实现因平台而异：**

| 平台 | 底层调用 | 说明 |
|------|---------|------|
| Linux | `os.waitpid()` | 系统调用，等待子进程退出 |
| Windows | `_winapi.WaitForSingleObject()` | Windows API，等待进程句柄 |

---

## 5. 自定义进程类

继承 `multiprocessing.Process`，重写 `run()` 方法：

```python
import multiprocessing
import os

class Worker(multiprocessing.Process):
    def __init__(self, name):
        super().__init__()  # 必须调用父类 __init__
        self.name = name

    def run(self):
        """重写 run() 方法，定义子进程执行的任务"""
        print(f"进程 {self.name}, PID: {os.getpid()}, 父进程 PPID: {os.getppid()}")

if __name__ == '__main__':
    workers = [Worker(f"worker-{i}") for i in range(3)]
    for w in workers:
        w.start()
    for w in workers:
        w.join()
```

---


### 5.1 子类化注意事项

**必须调用 `super().__init__()`**：

```python
class Worker(multiprocessing.Process):
    def __init__(self, task_id):
        super().__init__()  # ✅ 必须先调用父类初始化
        self.task_id = task_id  # ✅ 之后再添加自定义属性
        
    def run(self):
        print(self.task_id)  # ✅ 可以访问
```

**常见错误**：

```python
# ❌ 忘记调用 super().__init__()
class BadWorker(multiprocessing.Process):
    def __init__(self, task_id):
        # 忘记 super().__init__()，会导致各种奇怪问题
        self.task_id = task_id
```

**Process 对象不能 pickle**：

```python
# ❌ 在 spawn 模式下，Process 对象不能跨进程传递
def spawn_another(p):
    p.start()  # 会报错

# ✅ 应该传递构造参数，在目标进程内创建
def spawn_another(task_id):
    p = Worker(task_id)
    p.start()
```

## 6. Windows vs Linux：进程创建方式

### 6.1 启动方式对比

| 平台 | 默认方式 | 支持的方式 |
|------|---------|-----------|
| **Windows** | `spawn` | 仅 `spawn` |
| **macOS** | `spawn` | `spawn`, `fork` |
| **Linux** | `fork` | `fork`, `spawn`, `forkserver` |

### 6.2 fork 方式（Linux 默认）

```python
# 原理：os.fork() 复制当前进程的整个内存空间
# 子进程获得父进程内存的完整副本（Copy-on-Write）
```

**特点：**
- 速度极快（Copy-on-Write 机制下几乎瞬时）
- **不需要**序列化/反序列化 Process 对象
- **不需要**重新导入模块
- **不需要** `if __name__ == '__main__':` 保护
- **风险**：多线程程序中 fork 可能导致死锁

### 6.3 spawn 方式（Windows 默认）

```python
# 原理：启动一个全新的 Python 解释器进程
# 通过 pickle 序列化 Process 对象传递给子进程
```

**特点：**
- 安全性更好，避免 fork 后的多线程死锁问题
- 启动较慢（需要新 Python 进程 + 模块重新导入）
- **必须**序列化 `target` 函数和参数
- **必须**在 `if __name__ == '__main__':` 保护下创建进程

### 6.4 为什么 Windows 需要 `if __name__ == '__main__':`

```python
# Windows 使用 spawn 方式创建进程时：
# 1. 启动新的 Python 解释器
# 2. 重新导入主模块
# 3. 如果没有 if __name__ == '__main__': 保护
#    模块重新导入时会再次执行 Process() 和 start()
#    导致无限递归创建进程
```

```python
# ❌ 错误写法（Windows 会无限递归）
import multiprocessing
def worker():
    print("hello")
p = multiprocessing.Process(target=worker)
p.start()

# ✅ 正确写法
import multiprocessing
def worker():
    print("hello")
if __name__ == '__main__':
    p = multiprocessing.Process(target=worker)
    p.start()
```

---


### 6.5 使用 Context 指定启动方法

```python
import multiprocessing as mp

# 查看当前启动方法
print(mp.get_start_method())  # Windows: 'spawn', Linux: 'fork'

# 使用 context 方式（不影响全局设置）
ctx = mp.get_context('spawn')
p = ctx.Process(target=worker)  # 这个进程强制用 spawn

# 全局设置（影响所有后续创建的进程）
mp.set_start_method('spawn')
```

**使用场景**：
- Linux 上需要安全的进程隔离时，强制使用 `spawn`
- 需要与特定启动方法兼容的库交互时

## 7. 进程生命周期

```
创建 Process 对象
       │
       ▼
   p.start()           → 状态从 "新建" 变为 "运行"
       │
       ▼
   子进程执行 run()     → is_alive() == True
       │
       ▼
   run() 结束/异常退出  → 状态变为 "终止"
       │
       ▼
   p.join()            → 父进程等待子进程结束
       │
       ▼
   资源回收             → exitcode 有值（0=正常，非0=异常）
```

---

## 8. 守护进程

```python
import multiprocessing
import time

def daemon_worker():
    while True:
        print("守护进程运行中...")
        time.sleep(1)

if __name__ == '__main__':
    p = multiprocessing.Process(target=daemon_worker, daemon=True)
    p.start()
    time.sleep(3)
    print("主进程结束，守护进程将被自动终止")
    # 主进程结束时，daemon=True 的子进程会被强制终止
```

| daemon 值 | 行为 |
|-----------|------|
| `True` | 主进程退出时，子进程自动终止 |
| `False`（默认） | 主进程退出后，子进程继续运行（变为孤儿进程） |

---

## 9. 完整示例

```python
import multiprocessing
import os
import time

class Worker(multiprocessing.Process):
    def __init__(self, task_id, shared_data):
        super().__init__()
        self.task_id = task_id
        self.shared_data = shared_data

    def run(self):
        print(f"[Worker-{self.task_id}] 启动, PID={os.getpid()}")
        for i in range(3):
            print(f"[Worker-{self.task_id}] 处理 {self.shared_data[i]}")
            time.sleep(0.5)
        print(f"[Worker-{self.task_id}] 完成")

if __name__ == '__main__':
    print(f"[主进程] PID={os.getpid()}")

    data = ["任务A", "任务B", "任务C"]

    # 创建并启动多个子进程
    workers = [Worker(i, data) for i in range(3)]
    for w in workers:
        w.start()

    # 等待所有子进程完成
    for w in workers:
        w.join()

    print(f"[主进程] 所有子进程已完成")
    for w in workers:
        print(f"  Worker-{w.task_id} 退出码: {w.exitcode}")
```

---

## 总结

| 要点 | 说明 |
|------|------|
| `Process(target=func)` | 创建进程对象，不执行函数 |
| `start()` | 创建子进程并执行 `run()` |
| `run()` | 子进程实际执行的方法，内部调用 `target(*args, **kwargs)` |
| `join()` | 阻塞等待子进程结束 |
| Windows | 使用 `spawn`，需要 `if __name__ == '__main__':` |
| Linux | 默认 `fork`，复制父进程内存（高效但有风险） |
| 自定义进程 | 继承 `Process`，重写 `run()` 方法 |
| 守护进程 | `daemon=True`，主进程退出时自动终止 |


