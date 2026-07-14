"""
Day14 练习1 - 线程安全与锁
由浅入深掌握 Lock、线程安全编程模式

参考源码: day14/P01_Thread_Safe.py
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

# ----- 题1: Lock 基本操作预测 [必做] -----
# 知识点: threading.Lock(), acquire(), release()
# 预测以下代码的输出结果

lock = threading.Lock()
print(lock.acquire())           # ____ 第一次 acquire 的返回值
print(lock.locked())            # ____ 锁当前是否被持有
lock.release()                  # 释放锁
print(lock.locked())            # ____ 释放后锁的状态

print()

# ----- 题2: with lock 上下文管理器 [必做] -----
# 知识点: with lock 自动 acquire/release，等价于 try-finally
# 预测以下两种写法的输出是否相同

lock2 = threading.Lock()
counter = 0

def increment_with_lock():
    global counter
    for _ in range(100000):
        with lock2:             # 等价于 lock2.acquire() ... lock2.release()
            counter += 1

# 对比写法: 手动 acquire/release
def increment_manual():
    global counter
    for _ in range(100000):
        lock2.acquire()
        counter += 1
        lock2.release()

# 问题: 如果 3 个线程同时执行 increment_with_lock()，最终 counter 的值是多少？ ____
# 问题: 如果 3 个线程同时执行 increment_manual()，最终 counter 的值是多少？ ____
# 问题: 如果去掉 with lock2 / acquire / release，直接 counter += 1（3线程），结果会怎样？ ____

print()

# ----- 题3: 实现一个线程安全的计数器类 [必做] -----
# 知识点: 在类中使用 Lock 保护共享状态
# TODO: 补全 SafeCounter 类，使其在多线程环境下安全计数

class SafeCounter:
  def __init__(self):
        self._count = 0
        # TODO: 初始化一个锁对象

  def increment(self):
    # TODO: 使用锁保护 self._count += 1
    pass
  def decrement(self):
    # TODO: 使用锁保护 self._count -= 1
    pass
  @property
  def value(self):
   # TODO: 返回当前计数值（读操作也需要加锁吗？思考一下）
   return self._count

# 验证: 多线程并发修改
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

# ----- 题4: 多窗口卖票系统 - 线程安全版 [必做] -----
# 知识点: 基于 P01_Thread_Safe.py 的售票模型，用 with lock 改写
# TODO: 使用 with lock 语法改写以下售票逻辑，使 3 个窗口安全卖票

ticket_num = 20
ticket_lock = threading.Lock()

def sell_tickets(window_name):
    """每个窗口循环卖票，直到票卖完"""
    global ticket_num
    while True:
        # TODO: 使用 with ticket_lock 保护以下代码块
        # 条件检查和卖票操作必须是原子的
        if ticket_num <= 0:
            break
        time.sleep(0.01)        # 模拟卖票耗时
        ticket_num -= 1
        print(f"{window_name} 卖了1张票, 还剩 {ticket_num} 张")

# 注意: 以上代码在不加锁的情况下有竞态条件 (race condition)
# 请分析: 如果去掉锁，可能出现什么问题？____

print()

# ----- 题5: 读写分离模式辨析 [必做] -----
# 知识点: 读操作是否需要加锁？写操作呢？
# 分析以下场景，判断哪些需要加锁，哪些不需要

shared_config = {"debug": False, "max_retries": 3}
config_lock = threading.Lock()

# 场景 A: 只读取字典中的一个值
def read_debug_flag():
    return shared_config["debug"]     # 场景A: 是否需要加锁？ ____

# 场景 B: 更新字典中的多个键（需要保证一致性）
def update_config(debug, retries):
    with config_lock:
        shared_config["debug"] = debug
        shared_config["max_retries"] = retries  # 场景B: 是否需要加锁？ ____

# 场景 C: 读取后根据值做决策
def check_and_act():
    if shared_config["debug"]:        # 场景C: 先读后判断，是否需要加锁？ ____
        print("调试模式已开启")

# 场景 D: 复合操作 - 读后写
retry_count = 0
retry_lock = threading.Lock()

def increment_retry():
    global retry_count
    retry_count += 1                  # 场景D: 是否需要加锁？ ____
    # 提示: retry_count += 1 实际上是 读-改-写 三步操作

print()

# ----- 题6: 线程安全的共享数据结构 [必做] -----
# 知识点: 使用 Lock 保护列表的 append 和 pop 操作
# TODO: 实现一个线程安全的共享列表

class SharedList:
    """线程安全的共享列表，支持 append、pop 和 len"""
    def __init__(self):
        self._data = []
        # TODO: 初始化锁

    def append(self, item):
        # TODO: 线程安全地添加元素

    def pop(self):
        # TODO: 线程安全地弹出最后一个元素
        # 注意: 列表为空时应返回 None 而不是抛异常

    def __len__(self):
        # TODO: 返回列表长度

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

# ----- 题7: 死锁场景分析 [选做] -----
# 知识点: 死锁 (Deadlock) 的产生条件与避免策略
# 分析以下代码，解释为什么会产生死锁

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1_func():
    """线程1: 先获取 lock_a，再获取 lock_b"""
    lock_a.acquire()
    print("线程1: 已获取 lock_a，等待 lock_b...")
    time.sleep(0.1)             # 制造等待窗口
    lock_b.acquire()
    print("线程1: 已获取 lock_a 和 lock_b")
    lock_b.release()
    lock_a.release()

def thread2_func():
    """线程2: 先获取 lock_b，再获取 lock_a"""
    lock_b.acquire()
    print("线程2: 已获取 lock_b，等待 lock_a...")
    time.sleep(0.1)             # 制造等待窗口
    lock_a.acquire()
    print("线程2: 已获取 lock_b 和 lock_a")
    lock_a.release()
    lock_b.release()

# 问题: 如果线程1和线程2同时运行，会发生什么？ ____
# 问题: 如何通过调整锁的获取顺序来避免死锁？ ____

print()

# ----- 题8: 生产者-消费者队列模式 [选做] -----
# 知识点: queue.Queue 是线程安全的，自带锁机制
# TODO: 使用 queue.Queue 实现生产者-消费者模式

task_queue = queue.Queue(maxsize=5)  # 最多容纳 5 个任务
stop_event = threading.Event()

def producer(name):
    """生产者: 向队列中放入任务"""
    for i in range(8):
        task = f"{name}-任务{i}"
        # TODO: 将 task 放入队列（使用 put 方法，会自动阻塞直到队列有空间）
        print(f"{name} 生产了 {task}")
    print(f"{name} 生产完毕")

def consumer(name):
    """消费者: 从队列中取出任务处理"""
    while not stop_event.is_set():
        try:
            # TODO: 从队列中取出任务，设置超时 1 秒
            # 提示: queue.get(timeout=1)，超时会抛 queue.Empty 异常
            task = None  # 替换为实际代码
            print(f"{name} 处理了 {task}")
        except queue.Empty:
            continue  # 超时则继续循环
    print(f"{name} 消费者退出")

# 问题: 为什么 queue.Queue 是线程安全的？它内部使用了什么机制？ ____
# 问题: 如果把 Queue 换成普通 list，用 Lock 保护 append/pop，能否实现同样功能？ ____

print()

# ----- 题9: 调试修复题 [选做] -----
# 知识点: 识别并修复线程安全问题
# BUG: 以下代码有 2 处线程安全问题，请找出并修复

balance = 0
balance_lock = threading.Lock()

def deposit(amount):
    """存款操作"""
    global balance
    # BUG: 这里缺少了什么？
    balance += amount
    print(f"存款 {amount}, 余额: {balance}")

def withdraw(amount):
    """取款操作 - 需要检查余额是否充足"""
    global balance
    # BUG: 锁的范围不对，检查和扣减不在同一个原子操作中
    balance_lock.acquire()
    can_withdraw = balance >= amount
    balance_lock.release()

    if can_withdraw:
        balance_lock.acquire()
        balance -= amount
        print(f"取款 {amount}, 余额: {balance}")
        balance_lock.release()
    else:
        print(f"余额不足, 当前余额: {balance}, 需要: {amount}")

def test_bank():
    """测试: 10个线程各存100，5个线程各取50"""
    global balance
    balance = 1000  # 初始余额
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

# 注意: 不要实际运行此函数，它会因为线程安全问题产生不确定结果
# test_bank()  # 取消注释可自行测试

# 问题: deposit 函数缺少什么？ ____
# 问题: withdraw 函数的 "先检查再扣减" 模式有什么问题？ ____（提示: TOCTOU 竞态）
# TODO: 请在下方写出修复后的 deposit 和 withdraw 函数
