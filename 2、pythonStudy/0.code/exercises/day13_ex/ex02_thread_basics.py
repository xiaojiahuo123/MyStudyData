"""
Day13 练习2 - 线程基础与线程安全
由浅入深掌握多线程编程、线程池、线程安全与锁、模块导入

参考源码: day13/P08_Thread.py
         day13/P09_Custom_Thread.py
         day13/P10_Thread_Pool.py
         day13/P11_Thread_No_Safe.py
版本: v1.0
最后更新: 2026-07-13
"""
import os
import threading
import time
import concurrent.futures


# ============================================================
#                      第一部分: 基础题 [必做]
# ============================================================

# ----- 题1: 线程基本概念辨析 [必做] -----
# 知识点: thread basics, GIL
# 填空: 用合适的术语完成以下描述

# 1) 线程是操作系统能够进行运算调度的最小单位，它被包含在 ______ 中
# 2) 同一进程内的多个线程共享该进程的 ______ 和 ______
# 3) Python 中由于 GIL（Global Interpreter Lock）的存在，同一时刻只能有一个线程执行 ______ 字节码
# 4) 线程的开销比进程 ______（大/小），创建和切换速度比进程 ______（快/慢）

answer_1_1 = "进程"  # TODO: 填入"进程"
answer_1_2_a = "内存空间"  # TODO: 填入"内存空间"
answer_1_2_b = "全局变量/资源"  # TODO: 填入"全局变量/资源"
answer_1_3 = "Python"  # TODO: 填入"Python"
answer_1_4_a = "小"  # TODO: 填入"大"或"小"
answer_1_4_b = "快"  # TODO: 填入"快"或"慢"

print("题1: 请完成线程基本概念辨析")
print()


# ----- 题2: threading.Thread 创建线程代码预测 [必做] -----
# 知识点: threading.Thread, current_thread().name, start(), join()
# 预测以下代码的输出结果

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

# 问题:
# 1) 两个线程的输出是否会交替出现？____会（会/不会）
# 2) 最后一行的线程名是: ____MainThread
# 3) join() 的作用是: ____阻塞主进程

answer_2_1 = ""  # TODO
answer_2_2 = ""  # TODO
answer_2_3 = ""  # TODO

# 取消注释在 main 中运行验证:
# predict_thread_basic()

print("题2: 预测线程创建代码输出")
print()


# ----- 题3: 线程池 ThreadPoolExecutor 用法 [必做] -----
# 知识点: concurrent.futures.ThreadPoolExecutor, submit(), future.result()
# 预测以下代码的输出结果

def square(n):
    time.sleep(0.2)
    return n ** 2

def predict_thread_pool():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(square, i) for i in range(5)]
        results = [f.result() for f in futures]
    print(f"  结果: {results}")

# 问题:
# 1) max_workers=3 表示线程池中最多有 ____ 个线程同时工作
# 2) 提交了 5 个任务，但只有 3 个线程，所以第 4、5 个任务会 ____
# 3) executor.submit() 返回的对象类型是 ____
# 4) with 语句结束时会自动调用 ____

answer_3_1 = "3"  # TODO
answer_3_2 = "等待有空闲线程了再执行"  # TODO
answer_3_3 = "列表"  # TODO
answer_3_4 = "关闭线程池"  # TODO

# 预测输出:
# ____

# 取消注释在 main 中运行验证:
# predict_thread_pool()

print("题3: 预测线程池 ThreadPoolExecutor 输出")
print()


# ----- 题4: 线程安全问题演示 [必做] -----
# 知识点: Race Condition（竞争条件）
# 预测以下代码的最终结果

def unsafe_increment():
    global g_num
    for _ in range(100000):
        g_num += 1  # 这行不是原子操作！

def predict_race_condition():
    global g_num
    g_num = 0
    threads = [threading.Thread(target=unsafe_increment) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"  最终 g_num = {g_num}")

# 问题:
# 1) 如果没有竞争条件，3个线程各加100000次，最终结果应该是 ____300000
# 2) 实际运行结果可能是 ____（等于/小于/大于/等于或小于）期望值
# 3) 产生这个问题的原因是 g_num += 1 不是 ______（原子操作/可迭代对象），它包含 ______ 步
# 4) 解决这个问题需要使用 ____

answer_4_1 = "100000"  # TODO
answer_4_2 = "小于"  # TODO
answer_4_3_a = ""  # TODO
answer_4_3_b = ""  # TODO  (三步: 读取、加1、写回)
answer_4_4 = ""  # TODO

# 取消注释在 main 中运行验证（结果可能每次不同）:
# predict_race_condition()

print("题4: 预测线程安全问题")
print()


# ============================================================
#                      第二部分: 进阶题 [必做]
# ============================================================

# ----- 题5: Lock 加锁保护共享变量 [必做] -----
# 知识点: threading.Lock, acquire(), release()
# 预测以下代码的最终结果

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

# 问题:
# 1) 使用 Lock 后，最终结果一定是 ____300000
# 2) lock.acquire() 的作用是 ____获取锁
# 3) lock.release() 的作用是 ____释放锁
# 4) 如果忘记调用 lock.release() 会导致 ____死锁

answer_5_1 = ""  # TODO
answer_5_2 = ""  # TODO
answer_5_3 = ""  # TODO
answer_5_4 = ""  # TODO

# 取消注释在 main 中运行验证:
# predict_with_lock()

print("题5: 预测 Lock 加锁后的结果")
print()


# ----- 题6: with lock 上下文管理器 [必做] -----
# 知识点: with lock 自动获取和释放锁
# 比较以下两种写法，预测它们的行为是否相同

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

# 问题:
# 1) 写法A和写法B的功能是否等价？____（是/否）
# 2) with lock 的优势是: 即使 with 块内发生 ______，锁也会被自动 ______
# 3) 推荐使用写法 ____，因为更安全、更简洁

answer_6_1 = "是"  # TODO
answer_6_2_a = "异常"  # TODO
answer_6_2_b = "自动释放"  # TODO
answer_6_3 = "with"  # TODO

print("题6: with lock 与手动 acquire/release 对比")
print()


# ----- 题7: 进程 vs 线程对比辨析 [必做] -----
# 知识点: 进程vs线程区别
# 从以下维度对比进程和线程，填写表格

# 维度            | 进程 (Process)    | 线程 (Thread)
# ---------------|-------------------|-------------------
# 资源分配         |                   |
# 内存空间         |   独立                |共享进程的内存空间
# 创建/切换开销    |     大              |小
# 并发性           |      可以             |不行
# 独立性           |                   |
# 通信方式         |    Queue, Pipe, Manager               |共享变量（需加锁保证安全）
# GIL 影响        |                   |

# TODO: 填写上表（在注释中写答案）

# 答案参考:
# 资源分配: 进程是资源分配的基本单位 | 线程是 CPU 调度的基本单位
# 内存空间: 每个进程独立内存空间 | 同一进程内线程共享内存空间
# 创建/切换开销: 大，需要分配独立资源 | 小，共享进程资源
# 并发性: 可以真正并行（多核） | 受 GIL 限制，不能真正并行执行 Python 字节码
# 独立性: 进程间相互独立 | 线程间相互依赖（一个崩溃可能影响整个进程）
# 通信方式: Queue, Pipe, Manager | 共享变量（需加锁保证安全）
# GIL 影响: 不受 GIL 影响 | 受 GIL 影响

print("题7: 请完成进程 vs 线程对比表格")
print()


# ----- 题8: 模块导入方式 [必做] -----
# 知识点: import, from import, import *
# 回答以下问题

# 问题1: import os 和 from os import getpid 的区别是什么？
# ____

# 问题2: from os import * 会有什么风险？
# ____

# 问题3: import threading as th 这种写法的好处是什么？
# ____

# 问题4: 以下代码有什么问题？
# from multiprocessing import Process
# from threading import Thread
# def Process():
#     pass
# ____

answer_8_1 = ""  # TODO
answer_8_2 = ""  # TODO
answer_8_3 = ""  # TODO
answer_8_4 = ""  # TODO

print("题8: 请回答模块导入相关问题")
print()


# ============================================================
#                    第三部分: 深入理解题 [选做]
# ============================================================

# ----- 题9: 多线程卖票系统 [选做] -----
# 知识点: 多线程 + Lock 实现生产消费模式
# 要求: 模拟3个售票窗口同时卖票，总共100张票，卖完为止
# - 使用共享变量 tickets 表示剩余票数
# - 使用 Lock 保证线程安全
# - 每个线程卖出一张票后打印: "[窗口X] 卖出第Y张，剩余Z张"

# TODO: 实现 sell_tickets 函数和窗口线程
tickets = 100
ticket_lock = threading.Lock()
#
def sell_tickets(window_name):
    global tickets
    counts = 0
    while ( tickets >= 0):
        with ticket_lock:
            if tickets <= 0:    # ← 在锁内判断，不会被其他线程干扰
                break
            tickets -= 1
            time.sleep(2)
            # count = 100 - tickets
            counts += 1
            print(f"窗口{window_name},{os.getpid()}卖出第{counts}张，剩余{tickets}张")
#
def run_ticket_system():
    funters = [threading.Thread(target=sell_tickets,args=(i,)) for i in range(3)]
    for f in funters:
        f.start()
    for f in funters:
        f.join()


# 取消注释在 main 中运行验证:
# run_ticket_system()

print("题9: 请实现多线程卖票系统")
print()


# ----- 题10: GIL 的影响分析 [选做] -----
# 知识点: Global Interpreter Lock
# 回答以下问题

# 问题1: 什么是 GIL？它存在于 Python 的哪个层面？
# ____

# 问题2: 为什么 Python 需要 GIL？
# ____

# 问题3: GIL 对多线程程序的影响是什么？
# ____

# 问题4: 如何绕过 GIL 的限制？
# ____

# 问题5: 以下哪种场景受 GIL 影响最大？
# A. 10个线程同时爬取网页
# B. 10个线程同时做数学计算
# C. 10个线程同时读写文件
# ____

answer_10_1 = ""  # TODO
answer_10_2 = ""  # TODO
answer_10_3 = ""  # TODO
answer_10_4 = ""  # TODO
answer_10_5 = ""  # TODO

print("题10: 请回答 GIL 相关问题")
print()


# ----- 题11: 调试修复 - 找出以下代码中的 3 个 BUG [选做] -----
# 知识点: 线程安全、Lock 使用、ThreadPoolExecutor 使用
# 要求: 阅读代码，找出 BUG 并说明修复方法（不要直接运行）

# BUG 1: 共享变量修改未加锁
# counter = 0
# def increment():
#     global counter
#     for _ in range(1000):
#         counter += 1  # 多线程下不安全
# threads = [threading.Thread(target=increment) for _ in range(5)]
# [t.start() for t in threads]
# [t.join() for t in threads]
# print(counter)  # 预期 5000，实际可能不是
# 问题: ____没有加锁
# 修复: ____利用with自动释放，并加锁

# BUG 2: Lock 在循环内创建导致每个线程用不同的锁
# def unsafe_worker():
#     lock = threading.Lock()  # 每次调用都创建新锁！
#     lock.acquire()
#     # ... 操作共享资源 ...
#     lock.release()
# 问题: ____
# 修复: ____

# BUG 3: ThreadPoolExecutor 忘记使用 with 或 shutdown
# executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
# futures = [executor.submit(task, i) for i in range(10)]
# results = [f.result() for f in futures]
# # executor 没有关闭！
# 问题: ____
# 修复: ____

print("题11: 请找出代码中的 3 个 BUG 并说明修复方法")
print()


# ============================================================
#                         main 入口
# ============================================================
if __name__ == '__main__':
    print("=" * 50)
    print("Day13 练习2 - 线程基础与线程安全")
    print("=" * 50)
    print()

    # 在此处取消注释运行各题的验证代码
    # 例如:
    # predict_thread_basic()
    # predict_thread_pool()
    #       predict_race_condition()
    #       predict_with_lock()
    run_ticket_system()

    print("请完成所有 TODO 后，在此处运行验证代码。")


# 修改记录:
# v1.0 (2026-07-13): 初始版本，覆盖 Day13 线程相关知识点
