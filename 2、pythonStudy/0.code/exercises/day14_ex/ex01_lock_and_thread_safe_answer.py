"""
Day14 练习1 - 线程安全与锁（答案版）
版本: v1.0
最后更新: 2026-07-13
"""

import threading
import time
import queue


# ============================================================
#                      第一部分: 基础题 (40%)
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: Lock 基本操作预测 -----
# 知识点: threading.Lock(), acquire(), release()

lock = threading.Lock()
print(lock.acquire())           # ____ 答案: True（acquire 成功返回 True）
print(lock.locked())            # ____ 答案: True（锁已被持有）
lock.release()
print(lock.locked())            # ____ 答案: False（释放后锁空闲）

print()

# ----- 题2: with lock 上下文管理器 -----
# 知识点: with lock 自动 acquire/release，等价于 try-finally

lock2 = threading.Lock()
counter = 0

def increment_with_lock():
    global counter
    for _ in range(100000):
        with lock2:
            counter += 1

def increment_manual():
    global counter
    for _ in range(100000):
        lock2.acquire()
        counter += 1
        lock2.release()

# 问题: 如果 3 个线程同时执行 increment_with_lock()，最终 counter 的值是多少？
# ____ 答案: 300000（3 * 100000，with lock 保证每次自增是原子操作）

# 问题: 如果 3 个线程同时执行 increment_manual()，最终 counter 的值是多少？
# ____ 答案: 300000（与 with lock 版本等价，只是写法不同）

# 问题: 如果去掉 with lock2 / acquire / release，直接 counter += 1（3线程），结果会怎样？
# ____ 答案: 结果不确定，通常小于 300000。因为 counter += 1 是 "读-改-写" 三步操作，
#            多线程并发执行时可能出现竞态条件，导致部分自增丢失。

print()

# ----- 题3: 实现一个线程安全的计数器类 -----
# 知识点: 在类中使用 Lock 保护共享状态

class SafeCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()      # 初始化一个锁对象

    def increment(self):
        with self._lock:                    # 使用 with lock 保护
            self._count += 1

    def decrement(self):
        with self._lock:
            self._count -= 1

    @property
    def value(self):
        # 读操作也需要加锁（int 赋值在 CPython 中虽然是原子的，
        # 但为了代码的可移植性和明确的语义，建议加锁）
        with self._lock:
            return self._count

# 验证
def test_safe_counter():
    counter = SafeCounter()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=lambda: [counter.increment() for _ in range(10000)])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"期望值: 100000, 实际值: {counter.value}")  # 期望输出 100000

test_safe_counter()
print()


# ============================================================
#                     第二部分: 进阶题 (35%)
# ============================================================

print("=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题4: 多窗口卖票系统 - 线程安全版 -----
# 知识点: 基于 P01_Thread_Safe.py 的售票模型，用 with lock 改写

ticket_num = 20
ticket_lock = threading.Lock()

def sell_tickets(window_name):
    """每个窗口循环卖票，直到票卖完"""
    global ticket_num
    while True:
        with ticket_lock:                           # 使用 with lock 保护
            if ticket_num <= 0:
                break
            time.sleep(0.01)
            ticket_num -= 1
            print(f"{window_name} 卖了1张票, 还剩 {ticket_num} 张")

# 分析: 如果去掉锁，可能出现什么问题？
# ____ 答案: 多个窗口可能同时读到 ticket_num > 0，然后同时执行 ticket_num -= 1，
#            导致卖出的票数超过总票数（超卖），或者出现负数票。
#            这就是典型的竞态条件 (Race Condition)。

print()

# ----- 题5: 读写分离模式辨析 -----
# 知识点: 读操作是否需要加锁？写操作呢？

shared_config = {"debug": False, "max_retries": 3}
config_lock = threading.Lock()

# 场景 A: 只读取字典中的一个值
def read_debug_flag():
    return shared_config["debug"]
# ____ 答案: 在 CPython 中，单个字典键的读取是原子操作（受 GIL 保护），
#            一般不需要加锁。但为了代码的明确性和可移植性，敏感场景下建议加锁。

# 场景 B: 更新字典中的多个键（需要保证一致性）
def update_config(debug, retries):
    with config_lock:
        shared_config["debug"] = debug
        shared_config["max_retries"] = retries
# ____ 答案: 必须加锁！两个赋值操作之间如果不加锁，其他线程可能读到不一致的状态
#            （例如 debug 已更新但 max_retries 还是旧值）。

# 场景 C: 读取后根据值做决策
def check_and_act():
    if shared_config["debug"]:
        print("调试模式已开启")
# ____ 答案: 如果对 "读取-判断-执行" 的一致性有要求，则需要加锁。
#            否则在判断和执行之间，其他线程可能修改了 debug 的值。

# 场景 D: 复合操作 - 读后写
retry_count = 0
retry_lock = threading.Lock()

def increment_retry():
    global retry_count
    retry_count += 1
# ____ 答案: 必须加锁！retry_count += 1 等价于 retry_count = retry_count + 1，
#            包含 读取旧值、加1、写回 三步，属于典型的 "读-改-写" 非原子操作。
#            正确写法:
#            with retry_lock:
#                retry_count += 1

print()

# ----- 题6: 线程安全的共享数据结构 -----
# 知识点: 使用 Lock 保护列表的 append 和 pop 操作

class SharedList:
    """线程安全的共享列表，支持 append、pop 和 len"""
    def __init__(self):
        self._data = []
        self._lock = threading.Lock()

    def append(self, item):
        with self._lock:
            self._data.append(item)

    def pop(self):
        with self._lock:
            if self._data:
                return self._data.pop()
            return None

    def __len__(self):
        with self._lock:
            return len(self._data)

# 验证
def test_shared_list():
    slist = SharedList()
    def producer():
        for i in range(1000):
            slist.append(i)
    threads = [threading.Thread(target=producer) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"期望长度: 5000, 实际长度: {len(slist)}")

test_shared_list()
print()


# ============================================================
#                    第三部分: 深入理解题 (25%) [选做]
# ============================================================

print("=" * 50)
print("第三部分: 深入理解题 [选做]")
print("=" * 50)

# ----- 题7: 死锁场景分析 -----
# 知识点: 死锁 (Deadlock) 的产生条件与避免策略

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1_func():
    """线程1: 先获取 lock_a，再获取 lock_b"""
    lock_a.acquire()
    print("线程1: 已获取 lock_a，等待 lock_b...")
    time.sleep(0.1)
    lock_b.acquire()
    print("线程1: 已获取 lock_a 和 lock_b")
    lock_b.release()
    lock_a.release()

def thread2_func():
    """线程2: 先获取 lock_b，再获取 lock_a"""
    lock_b.acquire()
    print("线程2: 已获取 lock_b，等待 lock_a...")
    time.sleep(0.1)
    lock_a.acquire()
    print("线程2: 已获取 lock_b 和 lock_a")
    lock_a.release()
    lock_b.release()

# 问题: 如果线程1和线程2同时运行，会发生什么？
# ____ 答案: 会发生死锁 (Deadlock)。
#            线程1持有 lock_a 等待 lock_b，线程2持有 lock_b 等待 lock_a，
#            两个线程互相等待对方释放锁，形成循环等待，程序卡死。
#            死锁的四个必要条件: 互斥、占有且等待、不可抢占、循环等待。

# 问题: 如何通过调整锁的获取顺序来避免死锁？
# ____ 答案: 让所有线程按相同顺序获取锁。例如都先获取 lock_a 再获取 lock_b:
#
#            def thread2_func_fixed():
#                lock_a.acquire()     # 先 lock_a
#                time.sleep(0.1)
#                lock_b.acquire()     # 再 lock_b
#                print("线程2: 已获取 lock_a 和 lock_b")
#                lock_b.release()
#                lock_a.release()

print()

# ----- 题8: 生产者-消费者队列模式 -----
# 知识点: queue.Queue 是线程安全的，自带锁机制

task_queue = queue.Queue(maxsize=5)
stop_event = threading.Event()

def producer(name):
    """生产者: 向队列中放入任务"""
    for i in range(8):
        task = f"{name}-任务{i}"
        task_queue.put(task)            # put 会自动阻塞直到队列有空间
        print(f"{name} 生产了 {task}")
    print(f"{name} 生产完毕")

def consumer(name):
    """消费者: 从队列中取出任务处理"""
    while not stop_event.is_set():
        try:
            task = task_queue.get(timeout=1)   # 超时1秒，超时抛 queue.Empty
            print(f"{name} 处理了 {task}")
            task_queue.task_done()              # 标记任务已完成
        except queue.Empty:
            continue
    print(f"{name} 消费者退出")

# 问题: 为什么 queue.Queue 是线程安全的？它内部使用了什么机制？
# ____ 答案: queue.Queue 内部使用了 threading.Condition（条件变量）配合 mutex（互斥锁）
#            来保护队列的入队和出队操作。put() 和 get() 方法在操作队列内部数据时
#            会自动加锁，同时还支持阻塞等待（队列满时 put 阻塞，队列空时 get 阻塞）。

# 问题: 如果把 Queue 换成普通 list，用 Lock 保护 append/pop，能否实现同样功能？
# ____ 答案: 可以实现基本的线程安全，但缺少 Queue 的阻塞等待功能。
#            需要自己用 Condition 或 Event 实现 "队列满等待" 和 "队列空等待"。
#            queue.Queue 是更成熟、更方便的解决方案。

print()

# ----- 题9: 调试修复题 -----
# 知识点: 识别并修复线程安全问题

balance = 0
balance_lock = threading.Lock()

def deposit(amount):
    """存款操作"""
    global balance
    # 修复: 使用 with lock 保护余额修改
    with balance_lock:
        balance += amount
        print(f"存款 {amount}, 余额: {balance}")

def withdraw(amount):
    """取款操作 - 需要检查余额是否充足"""
    global balance
    # 修复: 将检查和扣减放在同一个锁的临界区内，避免 TOCTOU 竞态
    with balance_lock:
        if balance >= amount:
            balance -= amount
            print(f"取款 {amount}, 余额: {balance}")
        else:
            print(f"余额不足, 当前余额: {balance}, 需要: {amount}")

def test_bank():
    """测试: 10个线程各存100，5个线程各取50"""
    global balance
    balance = 1000
    threads = []
    for _ in range(10):
        threads.append(threading.Thread(target=deposit, args=(100,)))
    for _ in range(5):
        threads.append(threading.Thread(target=withdraw, args=(50,)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"最终余额: {balance}")  # 期望: 1000 + 10*100 - 5*50 = 1750

# 取消注释可自行测试:
# test_bank()

# 问题: deposit 函数缺少什么？
# ____ 答案: 缺少对 balance += 1 的锁保护。多线程并发存款可能导致余额计算错误。

# 问题: withdraw 函数的 "先检查再扣减" 模式有什么问题？
# ____ 答案: 这是经典的 TOCTOU (Time of Check to Time of Use) 竞态条件。
#            "检查余额" 和 "扣减余额" 分别在两次 acquire/release 中，
#            中间的窗口期其他线程可能修改了余额。
#            例如: 线程A检查余额=100够取50，释放锁；
#            线程B也检查余额=100够取80，执行取80，余额变20；
#            线程A再获取锁执行取50，余额变-30，透支了！
#            修复: 将检查和扣减放在同一个 with balance_lock 块内。
