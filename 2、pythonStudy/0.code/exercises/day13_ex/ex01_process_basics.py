"""
Day13 练习1 - 进程基础
由浅入深掌握多进程编程、进程池、进程间通信

参考源码: day13/P03_Process.py
         day13/P04_Custom_Process.py
         day13/P05_Process_Pool.py
         day13/P06_Process_No_Share.py
         day13/P07_Process_Share.py
版本: v1.0
最后更新: 2026-07-13
"""

import multiprocessing
import os
import random
import time


# ============================================================
#                      第一部分: 基础题 [必做]
# ============================================================

# ----- 题1: 并发与并行概念辨析 [必做] -----
# 知识点: concurrency vs parallelism
# 填空: 用"并发"或"并行"完成以下描述

# 1) 多个任务在同一时间段内交替执行，但不一定同时运行，称为 ______并发
# 2) 多个任务在同一时刻真正同时执行（需要多核 CPU），称为 ______并行
# 3) 单核 CPU 上的多进程属于 ______并行（宏观上看同时，微观上是交替的）
# 4) 多核 CPU 上的多进程可以实现真正的 ______并发

answer_1_1 = "并发"  # TODO: 填入"并发"或"并行"
answer_1_2 = "并行"  # TODO
answer_1_3 = "并行"  # TODO
answer_1_4 = "并发"  # TODO

print("题1: 请完成并发与并行概念辨析")
print()


# ----- 题2: 同步与异步概念辨析 [必做] -----
# 知识点: synchronous vs asynchronous
# 填空: 用"同步"或"异步"完成以下描述

# 1) 调用一个函数后，必须等待它执行完毕才能继续下一步，称为 ______ 调用
# 2) 调用一个函数后，不等待它执行完毕就继续做其他事情，通过回调或通知获得结果，称为 ______ 调用
# 3) 在餐厅点菜后一直站在柜台等菜做好再端走 = ______
# 4) 在餐厅点菜后先回座位，菜好了服务员送来 = ______

answer_2_1 = "同步"  # TODO
answer_2_2 = "异步"  # TODO
answer_2_3 = "同步"  # TODO
answer_2_4 = "异步"  # TODO

print("题2: 请完成同步与异步概念辨析")
print()


# ----- 题3: 进程创建与基本输出预测 [必做] -----
# 知识点: multiprocessing.Process, start(), join()
# 预测以下代码的输出结果（注意: 进程执行顺序不确定，关注"主进程最后打印"的保证机制）

def greet(name):
    print(f"  子进程: 你好, {name}!")

def predict_process_basic():
    p = multiprocessing.Process(target=greet, args=("Python",))
    p.start()
    p.join()  # 等待子进程结束
    print("  主进程: 子进程已结束")

# 预测输出:
# ____子进程:你好，Python ！
# ____
# 说明 join() 的作用: ____阻塞主进程，让主进程在子进程执行完毕后再执行

print("题3: 预测进程创建输出，join() 的作用是什么？")
print()


# ----- 题4: os.getpid() 和 os.getppid() 预测 [必做] -----
# 知识点: os.getpid(), os.getppid()
# 预测以下代码的输出（关注 PID 值之间的关系）

def show_pid():
    print(f"  子进程 PID={os.getpid()}, 父进程 PPID={os.getppid()}")

def predict_pid():
    print(f"  主进程 PID={os.getpid()}")
    p = multiprocessing.Process(target=show_pid)
    p.start()
    p.join()

# 预测输出中，子进程的 PPID 与主进程的 PID 是什么关系？
# ____子进程的PPID应该等于主进程的PID，因为主进程是子进程的父进程

# 取消注释在 main 中运行验证:
# predict_pid()

print("题4: 预测 PID 输出，父子进程 PID 关系")
print()


# ============================================================
#                      第二部分: 进阶题 [必做]
# ============================================================

# ----- 题5: apply vs apply_async 区别 [必做] -----
# 知识点: multiprocessing.Pool, apply(), apply_async()
# 预测以下两段代码的行为差异

def task(n):
    print(f"  任务{n} 开始, PID={os.getpid()}")
    time.sleep(0.5)
    print(f"  任务{n} 结束")
    return n * 10

# 代码A - apply（同步）:
def predict_apply():
    pool = multiprocessing.Pool(3)
    results = []
    for i in range(3):
        r = pool.apply(task, args=(i,))
        results.append(r)
    pool.close()
    pool.join()
    print(f"  结果: {results}")

# 代码B - apply_async（异步）:
def predict_apply_async():
    pool = multiprocessing.Pool(3)
    futures = []
    for i in range(3):
        f = pool.apply_async(task, args=(i,))
        futures.append(f)
    pool.close()
    pool.join()
    results = [f.get() for f in futures]
    print(f"  结果: {results}")

# 问题:
# 1) apply 是 ______（同步/异步），任务会 ______（阻塞/不阻塞）主进程
# 2) apply_async 是 ______（同步/异步），任务 ______（会/不会）阻塞主进程
# 3) 代码A中3个任务的执行方式是: ______（逐个执行 / 同时执行）
# 4) 代码B中3个任务的执行方式是: ______（逐个执行 / 同时执行）

answer_5_1 = "同步，阻塞"  # TODO
answer_5_2 = "异步，不阻塞"  # TODO
answer_5_3 = "逐个执行"  # TODO
answer_5_4 = "同时执行"  # TODO

# 取消注释在 main 中运行验证:
# predict_apply()
# print("---")
# predict_apply_async()

print("题5: apply vs apply_async 区别辨析")
print()

# ----- 题6: 进程间数据不共享 [必做] -----
# 知识点: 每个进程独立内存空间
# 预测以下代码的输出结果

def add_to_list(shared_list):
    for i in range(3):
        shared_list.append(i)
    print(f"  子进程 PID={os.getpid()}, list={shared_list}")

def predict_no_share():
    my_list = []
    p1 = multiprocessing.Process(target=add_to_list, args=(my_list,))
    p2 = multiprocessing.Process(target=add_to_list, args=(my_list,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"  主进程 PID={os.getpid()}, list={my_list}")

# 预测输出:
# 子进程1 的 list: ____[0,1,2]
# 子进程2 的 list: ____[0,1,2]
# 主进程 的 list: ____[]
# 解释为什么主进程的 list 为空: ____子进程的内存是独立创建的，在执行完毕之后释放，而主进程的list[]一直没有变化


# 取消注释在 main 中运行验证:
# predict_no_share()

print("题6: 预测进程间数据不共享行为")
print()


# ----- 题7: Queue 进程间通信 [必做] -----
# 知识点: multiprocessing.Queue, put(), get()
# 预测以下代码的输出结果

def producer(q):
    for i in range(3):
        q.put(i * 100)
        print(f"  生产者 PID={os.getpid()} 放入: {i * 100}")

def consumer(q):
    while True:
        item = q.get()
        print(f"  消费者 PID={os.getpid()} 取出: {item}")

def predict_queue():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    # 生产者结束后消费者会阻塞在 q.get()，这里用 terminate 强制结束
    p2.terminate()
    print("  主进程: 结束")

# 问题:
# 1) Queue 中的数据是 ______（先进先出 / 先进后出）
# 2) 如果生产者已经放完所有数据，消费者继续调用 q.get() 会 ______
# 3) multiprocessing.Queue 和 multiprocessing.Manager().Queue() 的区别是:
#    - multiprocessing.Queue 只能用于 ______（Process / Pool）
#    - Manager().Queue() 可以用于 ______（Process / Pool / 两者皆可）

answer_7_1 = "先进后出"  # TODO
answer_7_2 = "一次性取出"  # TODO
answer_7_3_a = "Process"  # TODO
answer_7_3_b = "Pool"  # TODO

# 取消注释在 main 中运行验证:
# predict_queue()

print("题7: Queue 进程间通信辨析")
print()


# ----- 题8: Manager().Queue() vs multiprocessing.Queue() [必做] -----
# 知识点: Manager().Queue() 可用于进程池
# 预测以下代码能否正常运行

def pool_producer(q):
    for i in range(3):
        q.put(i * 100)
        print(f"  [Pool] 生产者 PID={os.getpid()} 放入: {i * 100}")

def pool_consumer(q):
    while True:
        item = q.get()
        print(f"  [Pool] 消费者 PID={os.getpid()} 取出: {item}")

def predict_manager_queue():
    # 使用 Manager().Queue()
    q = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool(2)
    pool.apply_async(pool_producer, args=(q,))
    pool.apply_async(pool_consumer, args=(q,))
    pool.close()
    pool.join()

# 问题:
# 1) 如果把上面的 multiprocessing.Manager().Queue() 换成 multiprocessing.Queue()，
#    在 Pool 中能否正常工作？____不能（能/不能）
# `multiprocessing.Queue()`：适用于 `Process` 创建的进程
# `multiprocessing.Manager().Queue()`：适用于进程池（`Pool`）创建的进程
# 2) 原因是: ____
# 3) Manager().Queue() 的底层实现基于 ______（管道/共享内存/代理对象）

answer_8_1 = "不能"  # TODO
answer_8_2 = "multiprocessing.Queue()`：适用于 `Process` 创建的进程"  # TODO
answer_8_3 = "代理对象"  # TODO

# 取消注释在 main 中运行验证（注意此程序会一直运行，需手动终止）:
# predict_manager_queue()

print("题8: Manager().Queue() vs multiprocessing.Queue() 辨析")
print()


# ============================================================
#                    第三部分: 深入理解题 [选做]
# ============================================================

# ----- 题9: 自定义进程类 - 生产者-消费者模式 [选做] -----
# 知识点: 继承 multiprocessing.Process，重写 run()
# 要求: 实现 Producer 和 Consumer 类，通过 Queue 通信
# - Producer: 向队列放入 5 个随机数(1-100)，最后放入 None 作为结束信号
# - Consumer: 从队列取出数据，遇到 None 结束

# TODO: 实现 Producer 类
class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for _ in range(5):
          item = random.randint(1, 100)
          self.queue.put(item)
          print(f"题目9，Producer进程{os.getpid()}向队列中放入了数据{item}")
        self.queue.put(None)
        # self.queue.put(list)



# TODO: 实现 Consumer 类
class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for _ in range(5):
            item = self.queue.get()
            if item == None:
                break
            print(f"题目9，Consumer进程{os.getpid()}从队列中取出数据: {item}")



# 取消注释在 main 中运行验证:
def run_producer_consumer():
    import random
    q = multiprocessing.Queue()
    producer = Producer(q)
    consumer = Consumer(q)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print("  生产者-消费者模式完成")

print("题9: 请实现自定义进程类的生产者-消费者模式")
print()


# ----- 题10: 进程 vs 线程选择场景分析 [选做] -----
# 知识点: 进程vs线程区别（资源分配/开销/并发性/独立性/通信）
# 判断以下场景应该用"多进程"还是"多线程"，并简述理由

# 场景1: 爬取1000个网页（I/O 密集型）
answer_10_1 = ""  # TODO: 多进程/多线程? 理由: ____多进程，各自都是独立的任务

# 场景2: 对100万张图片做矩阵运算（CPU 密集型）
answer_10_2 = ""  # TODO: 多进程/多线程? 理由: ____多线程

# 场景3: 同时读写同一个文件
answer_10_3 = ""  # TODO: 多进程/多线程? 理由: ____多线程，同一个文件

# 场景4: 需要多个任务共享一个大字典并实时修改
answer_10_4 = ""  # TODO: 多进程/多线程? 理由: ____多线程，因为是对同一个资源进行修改

print("题10: 请完成进程 vs 线程场景分析")
print()


# ----- 题11: 调试修复 - 找出以下代码中的 3 个 BUG [选做] -----
# 知识点: 进程创建、Pool 使用、Queue 使用
# 要求: 阅读代码，找出 BUG 并说明修复方法（不要直接运行）

# BUG 1: 缺少 __name__ 保护
# import multiprocessing
# def worker():
#     print("working")
# p = multiprocessing.Process(target=worker)
# p.start()
# 问题: ____
# 修复: ____

# BUG 2: Pool 忘记 close/join
# pool = multiprocessing.Pool(4)
# for i in range(4):
#     pool.apply_async(task, args=(i,))
# print("done")
# 问题: ____
# 修复: ____

# BUG 3: multiprocessing.Queue 传给 Pool
# q = multiprocessing.Queue()
# pool = multiprocessing.Pool(2)
# pool.apply_async(producer, args=(q,))
# pool.apply_async(consumer, args=(q,))
# pool.close()
# pool.join()
# 问题: ____
# 修复: ____

print("题11: 请找出代码中的 3 个 BUG 并说明修复方法")
print()


# ============================================================
#                         main 入口
# ============================================================
if __name__ == '__main__':
    print("=" * 50)
    print("Day13 练习1 - 进程基础")
    print("=" * 50)
    print()

    # 在此处取消注释运行各题的验证代码
    # 例如:
    # predict_pid()
    # predict_apply()
    # predict_apply_async()
    # predict_no_share()
    # # test()
    # predict_queue()
    # predict_manager_queue()
    run_producer_consumer()

    print("请完成所有 TODO 后，在此处运行验证代码。")


# 修改记录:
# v1.0 (2026-07-13): 初始版本，覆盖 Day13 进程相关知识点
