"""
Day13 练习2 - 线程基础与线程安全 (答案)
由浅入深掌握多线程编程、线程池、线程安全与锁、模块导入

参考源码: day13/P08_Thread.py
         day13/P09_Custom_Thread.py
         day13/P10_Thread_Pool.py
         day13/P11_Thread_No_Safe.py
版本: v1.0
最后更新: 2026-07-13
"""

import threading
import time
import concurrent.futures


# ============================================================
#                      第一部分: 基础题 [必做]
# ============================================================

# ----- 题1: 线程基本概念辨析 [必做] -----
# 知识点: thread basics, GIL

answer_1_1 = "进程"       # 线程被包含在进程中
answer_1_2_a = "内存空间"  # 同一进程内的线程共享内存空间
answer_1_2_b = "全局变量"  # 同一进程内的线程共享全局变量/资源
answer_1_3 = "Python"     # GIL 限制同一时刻只有一个线程执行 Python 字节码
answer_1_4_a = "小"       # 线程开销比进程小
answer_1_4_b = "快"       # 线程创建和切换比进程快

print("题1 答案:")
print(f"  1) {answer_1_1}")
print(f"  2) {answer_1_2_a} 和 {answer_1_2_b}")
print(f"  3) {answer_1_3}")
print(f"  4) 开销{answer_1_4_a}，速度{answer_1_4_b}")
print()


# ----- 题2: threading.Thread 创建线程代码预测 [必做] -----
# 知识点: threading.Thread, current_thread().name, start(), join()

def print_numbers(label, count):
    for i in range(count):
        print(f"  [{threading.current_thread().name}] {label}: {i}")
        time.sleep(0.1)

def predict_thread_basic():
    t1 = threading.Thread(target=print_numbers, args=("A", 3), name="Worker-1")
    t2 = threading.Thread(target=print_numbers, args=("B", 3), name="Worker-2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"  [{threading.current_thread().name}] 所有线程结束")

# 答案:
# 1) 会。两个线程同时启动，由于有 time.sleep(0.1)，它们会交替执行
# 2) 最后一行的线程名是: MainThread（主线程）
# 3) join() 的作用: 阻塞当前线程（主线程），等待被 join 的线程执行完毕后再继续

answer_2_1 = "会。两个线程同时启动，由于有 sleep，输出会交替出现"
answer_2_2 = "MainThread（主线程）"
answer_2_3 = "阻塞主线程，等待 t1 和 t2 执行完毕后再继续执行主线程后续代码"

print("题2 答案:")
print(f"  1) {answer_2_1}")
print(f"  2) {answer_2_2}")
print(f"  3) {answer_2_3}")
print()

# 验证:
# predict_thread_basic()


# ----- 题3: 线程池 ThreadPoolExecutor 用法 [必做] -----
# 知识点: concurrent.futures.ThreadPoolExecutor, submit(), future.result()

def square(n):
    time.sleep(0.2)
    return n ** 2

def predict_thread_pool():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(square, i) for i in range(5)]
        results = [f.result() for f in futures]
    print(f"  结果: {results}")

# 答案:
# 1) max_workers=3 表示线程池中最多有 3 个线程同时工作
# 2) 提交了 5 个任务，但只有 3 个线程，所以第 4、5 个任务会 等待前面的任务完成后再执行
# 3) executor.submit() 返回的对象类型是 Future（concurrent.futures.Future）
# 4) with 语句结束时会自动调用 executor.shutdown(wait=True)，等待所有任务完成

answer_3_1 = "3"
answer_3_2 = "等待前面的任务完成后才执行（排队）"
answer_3_3 = "Future（concurrent.futures.Future）"
answer_3_4 = "executor.shutdown(wait=True)"

# 预测输出: [0, 1, 4, 9, 16]
# 顺序与提交顺序一致，因为 futures 按提交顺序收集，result() 也按顺序获取

print("题3 答案:")
print(f"  1) {answer_3_1}")
print(f"  2) {answer_3_2}")
print(f"  3) {answer_3_3}")
print(f"  4) {answer_3_4}")
print(f"  输出: [0, 1, 4, 9, 16]")
print()

# 验证:
# predict_thread_pool()


# ----- 题4: 线程安全问题演示 [必做] -----
# 知识点: Race Condition（竞争条件）

def unsafe_increment():
    global g_num
    for _ in range(100000):
        g_num += 1  # 不是原子操作！

def predict_race_condition():
    global g_num
    g_num = 0
    threads = [threading.Thread(target=unsafe_increment) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"  最终 g_num = {g_num}")

# 答案:
# 1) 如果没有竞争条件，3个线程各加100000次，最终结果应该是 300000
# 2) 实际运行结果可能是 小于 期望值
# 3) 产生这个问题的原因是 g_num += 1 不是 原子操作，它包含 三 步:
#    步骤1: 读取 g_num 的当前值
#    步骤2: 将值加 1
#    步骤3: 将结果写回 g_num
#    在步骤1和步骤3之间，其他线程可能修改了 g_num，导致数据丢失
# 4) 解决这个问题需要使用 Lock（锁）

answer_4_1 = "300000"
answer_4_2 = "等于或小于"
answer_4_3_a = "原子操作"
answer_4_3_b = "三"  # 读取、加1、写回
answer_4_4 = "Lock（锁）"

print("题4 答案:")
print(f"  1) {answer_4_1}")
print(f"  2) {answer_4_2}")
print(f"  3) {answer_4_3_a}，包含 {answer_4_3_b} 步（读取、加1、写回）")
print(f"  4) {answer_4_4}")
print()

# 验证（结果可能每次不同）:
# predict_race_condition()


# ============================================================
#                      第二部分: 进阶题 [必做]
# ============================================================

# ----- 题5: Lock 加锁保护共享变量 [必做] -----
# 知识点: threading.Lock, acquire(), release()

lock = threading.Lock()

def safe_increment():
    global g_num_safe
    for _ in range(100000):
        lock.acquire()
        g_num_safe += 1
        lock.release()

def predict_with_lock():
    global g_num_safe
    g_num_safe = 0
    threads = [threading.Thread(target=safe_increment) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"  最终 g_num_safe = {g_num_safe}")

# 答案:
# 1) 使用 Lock 后，最终结果一定是 300000
# 2) lock.acquire() 的作用: 获取锁。如果锁已被其他线程持有，则当前线程阻塞等待
# 3) lock.release() 的作用: 释放锁。让其他等待的线程可以获取锁
# 4) 如果忘记调用 lock.release() 会导致 死锁（Deadlock），其他线程永远无法获取锁

answer_5_1 = "300000"
answer_5_2 = "获取锁，如果锁已被占用则阻塞等待"
answer_5_3 = "释放锁，允许其他线程获取"
answer_5_4 = "死锁（Deadlock），其他线程永远等待"

print("题5 答案:")
print(f"  1) {answer_5_1}")
print(f"  2) {answer_5_2}")
print(f"  3) {answer_5_3}")
print(f"  4) {answer_5_4}")
print()

# 验证:
# predict_with_lock()


# ----- 题6: with lock 上下文管理器 [必做] -----
# 知识点: with lock 自动获取和释放锁

# 写法A: 手动 acquire/release
def style_a():
    global counter_a
    lock.acquire()
    counter_a += 1
    lock.release()

# 写法B: with 上下文管理器
def style_b():
    global counter_b
    with lock:
        counter_b += 1

# 答案:
# 1) 写法A和写法B的功能是等价的，都是获取锁 -> 执行操作 -> 释放锁
# 2) with lock 的优势是: 即使 with 块内发生 异常（Exception），锁也会被自动 释放（release）
#    写法A中如果 lock.acquire() 和 lock.release() 之间发生异常，锁不会被释放，导致死锁
# 3) 推荐使用写法 B，因为更安全、更简洁

answer_6_1 = "是，功能等价"
answer_6_2_a = "异常（Exception）"
answer_6_2_b = "释放（release）"
answer_6_3 = "B"

print("题6 答案:")
print(f"  1) {answer_6_1}")
print(f"  2) 即使发生 {answer_6_2_a}，锁也会被自动 {answer_6_2_b}")
print(f"  3) 推荐写法 {answer_6_3}")
print()


# ----- 题7: 进程 vs 线程对比辨析 [必做] -----
# 知识点: 进程vs线程区别

# 答案:
# 维度            | 进程 (Process)              | 线程 (Thread)
# ---------------|-----------------------------|-------------------
# 资源分配         | 资源分配的基本单位             | CPU 调度的基本单位
# 内存空间         | 每个进程独立内存空间           | 同一进程内线程共享内存空间
# 创建/切换开销    | 大，需要分配独立资源           | 小，共享进程资源
# 并发性           | 可以真正并行（多核）           | 受 GIL 限制，不能并行执行 Python 字节码
# 独立性           | 进程间相互独立                | 线程间相互依赖（一个崩溃可能影响整个进程）
# 通信方式         | Queue, Pipe, Manager         | 共享变量（需加锁保证安全）
# GIL 影响        | 不受 GIL 影响                | 受 GIL 影响

print("题7 答案:")
print("  维度            | 进程 (Process)              | 线程 (Thread)")
print("  资源分配         | 资源分配的基本单位             | CPU 调度的基本单位")
print("  内存空间         | 独立内存空间                  | 共享内存空间")
print("  创建/切换开销    | 大                           | 小")
print("  并发性           | 可真正并行                    | 受 GIL 限制")
print("  独立性           | 相互独立                      | 相互依赖")
print("  通信方式         | Queue/Pipe/Manager           | 共享变量+锁")
print("  GIL 影响        | 不受影响                      | 受影响")
print()


# ----- 题8: 模块导入方式 [必做] -----
# 知识点: import, from import, import *

# 答案:
# 问题1: import os 和 from os import getpid 的区别是什么？
#   import os: 导入整个 os 模块，使用时需要 os.getpid()
#   from os import getpid: 只导入 getpid 函数，使用时直接 getpid()
#   前者不会污染当前命名空间，后者可能覆盖同名变量

# 问题2: from os import * 会有什么风险？
#   会导入 os 模块中所有公开的名字（或 __all__ 列表中的名字），可能覆盖当前命名空间中的同名变量
#   例如: 如果当前模块有 open 函数，from os import * 会覆盖它
#   不推荐在生产代码中使用，难以追踪名字来源

# 问题3: import threading as th 这种写法的好处是什么？
#   给模块起别名，简化代码书写，同时避免命名冲突
#   例如: import numpy as np 是常见惯例

# 问题4: 以下代码有什么问题？
#   from multiprocessing import Process
#   from threading import Thread
#   def Process():  # 这会覆盖从 multiprocessing 导入的 Process！
#       pass
#   问题: 自定义函数 Process 覆盖了导入的 Process 类，后续使用 Process() 时调用的是自定义函数而非多进程类

answer_8_1 = "import os 导入整个模块（使用 os.getpid()），from os import getpid 只导入指定函数（直接 getpid()），前者不污染命名空间"
answer_8_2 = "导入所有公开名字，可能覆盖当前命名空间的同名变量，难以追踪名字来源，不推荐使用"
answer_8_3 = "起别名简化书写，避免命名冲突，如 import numpy as np"
answer_8_4 = "自定义的 Process 函数覆盖了从 multiprocessing 导入的 Process 类，后续无法使用多进程功能"

print("题8 答案:")
print(f"  1) {answer_8_1}")
print(f"  2) {answer_8_2}")
print(f"  3) {answer_8_3}")
print(f"  4) {answer_8_4}")
print()


# ============================================================
#                    第三部分: 深入理解题 [选做]
# ============================================================

# ----- 题9: 多线程卖票系统 [选做] -----
# 知识点: 多线程 + Lock 实现生产消费模式

tickets = 100
ticket_lock = threading.Lock()

def sell_tickets(window_name):
    global tickets
    while True:
        ticket_lock.acquire()
        if tickets > 0:
            tickets -= 1
            remaining = tickets
            ticket_lock.release()
            print(f"  [{window_name}] 卖出一张票，剩余 {remaining} 张")
            time.sleep(0.01)  # 模拟卖票耗时
        else:
            ticket_lock.release()
            break

def run_ticket_system():
    global tickets
    tickets = 100
    threads = [
        threading.Thread(target=sell_tickets, args=(f"窗口{i+1}",), name=f"窗口{i+1}")
        for i in range(3)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"  售票结束，剩余 {tickets} 张")

print("题9 答案: 多线程卖票系统已实现")
print("  sell_tickets(): 使用 Lock 保护共享变量 tickets，检查 > 0 后减 1")
print("  3个线程并发卖票，Lock 保证同一时刻只有一个线程修改 tickets")
print()

# 验证:
# run_ticket_system()


# ----- 题10: GIL 的影响分析 [选做] -----
# 知识点: Global Interpreter Lock

# 答案:
# 问题1: 什么是 GIL？它存在于 Python 的哪个层面？
#   GIL (Global Interpreter Lock) 是全局解释器锁，存在于 CPython 解释器层面
#   它是一把互斥锁，确保同一时刻只有一个线程执行 Python 字节码

# 问题2: 为什么 Python 需要 GIL？
#   CPython 的内存管理（引用计数）不是线程安全的
#   GIL 简化了 CPython 的实现，避免了复杂的细粒度锁
#   对于单线程程序，GIL 几乎没有性能损失

# 问题3: GIL 对多线程程序的影响是什么？
#   多线程无法利用多核 CPU 实现真正的并行执行 Python 字节码
#   CPU 密集型任务用多线程反而可能更慢（线程切换开销）
#   I/O 密集型任务受影响较小（等待 I/O 时会释放 GIL）

# 问题4: 如何绕过 GIL 的限制？
#   使用多进程（multiprocessing），每个进程有独立的 Python 解释器和 GIL
#   使用 C 扩展（如 NumPy），在 C 层面释放 GIL
#   使用其他 Python 实现（如 Jython、PyPy STM）

# 问题5: B. 10个线程同时做数学计算
#   CPU 密集型任务受 GIL 影响最大，因为线程需要持续持有 GIL 执行计算
#   I/O 密集型任务（A、C）在等待 I/O 时会释放 GIL，其他线程可以执行

answer_10_1 = "GIL 是全局解释器锁，存在于 CPython 解释器层面，确保同一时刻只有一个线程执行 Python 字节码"
answer_10_2 = "CPython 的内存管理（引用计数）不是线程安全的，GIL 简化了实现，单线程几乎无性能损失"
answer_10_3 = "多线程无法利用多核 CPU 真正并行，CPU 密集型任务用多线程反而可能更慢"
answer_10_4 = "使用多进程（独立解释器）、C 扩展（NumPy 释放 GIL）、其他 Python 实现（Jython）"
answer_10_5 = "B。CPU 密集型任务（数学计算）受 GIL 影响最大，I/O 密集型任务等待时会释放 GIL"

print("题10 答案:")
print(f"  1) {answer_10_1}")
print(f"  2) {answer_10_2}")
print(f"  3) {answer_10_3}")
print(f"  4) {answer_10_4}")
print(f"  5) {answer_10_5}")
print()


# ----- 题11: 调试修复 - 找出以下代码中的 3 个 BUG [选做] -----
# 知识点: 线程安全、Lock 使用、ThreadPoolExecutor 使用

print("题11 答案:")
print()
print("  BUG 1: 共享变量修改未加锁")
print("  问题: counter += 1 不是原子操作，多线程并发执行时会出现竞争条件，")
print("         读取-修改-写回的过程中其他线程可能修改 counter，导致结果不正确")
print("  修复: 使用 threading.Lock() 保护 counter += 1 操作:")
print("         lock = threading.Lock()")
print("         def increment():")
print("             global counter")
print("             for _ in range(1000):")
print("                 with lock:")
print("                     counter += 1")
print()
print("  BUG 2: Lock 在循环内创建导致每个线程用不同的锁")
print("  问题: 每次调用 unsafe_worker() 都创建新的 Lock 对象，")
print("         不同线程使用不同的锁，等于没有加锁")
print("  修复: 将 Lock 定义为全局变量或类属性，所有线程共享同一个锁:")
print("         lock = threading.Lock()  # 模块级全局变量")
print("         def unsafe_worker():")
print("             with lock:")
print("                 # ... 操作共享资源 ...")
print()
print("  BUG 3: ThreadPoolExecutor 忘记使用 with 或 shutdown")
print("  问题: executor 没有关闭，线程池资源不会被释放，可能导致程序不能正常退出")
print("  修复: 使用 with 语句自动管理:")
print("         with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:")
print("             futures = [executor.submit(task, i) for i in range(10)]")
print("             results = [f.result() for f in futures]")
print("         # 或手动调用 executor.shutdown(wait=True)")
print()


# ============================================================
#                         main 入口
# ============================================================
if __name__ == '__main__':
    print("=" * 50)
    print("Day13 练习2 - 线程基础与线程安全 (答案)")
    print("=" * 50)
    print()

    # 可以取消注释运行各题的验证代码:
    # predict_thread_basic()
    # predict_thread_pool()
    # predict_race_condition()
    # predict_with_lock()
    # run_ticket_system()

    print("所有答案已展示完毕。")


# 修改记录:
# v1.0 (2026-07-13): 初始版本，覆盖 Day13 线程相关知识点
