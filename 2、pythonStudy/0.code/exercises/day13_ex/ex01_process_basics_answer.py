"""
Day13 练习1 - 进程基础 (答案)
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

answer_1_1 = "并发"   # 多个任务在同一时间段内交替执行，但不一定同时运行
answer_1_2 = "并行"   # 多个任务在同一时刻真正同时执行（需要多核 CPU）
answer_1_3 = "并发"   # 单核 CPU 上的多进程，宏观并发微观交替
answer_1_4 = "并行"   # 多核 CPU 上的多进程可以真正并行

print("题1 答案:")
print(f"  1) {answer_1_1}")  # 并发
print(f"  2) {answer_1_2}")  # 并行
print(f"  3) {answer_1_3}")  # 并发
print(f"  4) {answer_1_4}")  # 并行
print()


# ----- 题2: 同步与异步概念辨析 [必做] -----
# 知识点: synchronous vs asynchronous

answer_2_1 = "同步"   # 必须等待函数执行完毕才能继续
answer_2_2 = "异步"   # 不等待执行完毕，通过回调或通知获得结果
answer_2_3 = "同步"   # 站在柜台等 = 同步阻塞
answer_2_4 = "异步"   # 回座位等服务员送 = 异步非阻塞

print("题2 答案:")
print(f"  1) {answer_2_1}")  # 同步
print(f"  2) {answer_2_2}")  # 异步
print(f"  3) {answer_2_3}")  # 同步
print(f"  4) {answer_2_4}")  # 异步
print()


# ----- 题3: 进程创建与基本输出预测 [必做] -----
# 知识点: multiprocessing.Process, start(), join()

def greet(name):
    print(f"  子进程: 你好, {name}!")

def predict_process_basic():
    p = multiprocessing.Process(target=greet, args=("Python",))
    p.start()
    p.join()  # 等待子进程结束
    print("  主进程: 子进程已结束")

# 答案输出:
# 子进程: 你好, Python!
# 主进程: 子进程已结束
# 说明 join() 的作用: 阻塞主进程，等待子进程执行完毕后再继续执行主进程后续代码

print("题3 答案:")
print("  输出:")
print("  子进程: 你好, Python!")
print("  主进程: 子进程已结束")
print("  join() 作用: 阻塞主进程，等待子进程执行完毕后再继续")
print()


# ----- 题4: os.getpid() 和 os.getppid() 预测 [必做] -----
# 知识点: os.getpid(), os.getppid()

def show_pid():
    print(f"  子进程 PID={os.getpid()}, 父进程 PPID={os.getppid()}")

def predict_pid():
    print(f"  主进程 PID={os.getpid()}")
    p = multiprocessing.Process(target=show_pid)
    p.start()
    p.join()

# 答案: 子进程的 PPID 等于主进程的 PID
# 说明: os.getpid() 返回当前进程的进程 ID
#       os.getppid() 返回当前进程的父进程 ID
#       子进程由主进程创建，所以子进程的父进程就是主进程

print("题4 答案:")
print("  子进程的 PPID 等于主进程的 PID")
print("  例如: 主进程 PID=1234, 子进程 PPID=1234")
print()

# 验证:
# predict_pid()


# ============================================================
#                      第二部分: 进阶题 [必做]
# ============================================================

# ----- 题5: apply vs apply_async 区别 [必做] -----
# 知识点: multiprocessing.Pool, apply(), apply_async()

def task(n):
    print(f"  任务{n} 开始, PID={os.getpid()}")
    time.sleep(0.5)
    print(f"  任务{n} 结束")
    return n * 10

# 答案:
# 1) apply 是 同步（synchronous），任务会 阻塞 主进程
#    → 每次调用 pool.apply() 会等到任务完成后才返回
# 2) apply_async 是 异步（asynchronous），任务 不会 阻塞主进程
#    → 调用后立即返回一个 AsyncResult 对象，需要用 .get() 获取结果
# 3) 代码A中3个任务: 逐个执行（串行），因为 apply 是同步的
# 4) 代码B中3个任务: 同时执行（并行），因为 apply_async 是异步的

answer_5_1 = "同步; 阻塞"
answer_5_2 = "异步; 不会"
answer_5_3 = "逐个执行（串行），apply 是同步阻塞的"
answer_5_4 = "同时执行（并行），apply_async 是异步非阻塞的"

print("题5 答案:")
print(f"  1) {answer_5_1}")
print(f"  2) {answer_5_2}")
print(f"  3) {answer_5_3}")
print(f"  4) {answer_5_4}")
print()

# 验证:
# def predict_apply():
#     pool = multiprocessing.Pool(3)
#     results = []
#     for i in range(3):
#         r = pool.apply(task, args=(i,))
#         results.append(r)
#     pool.close()
#     pool.join()
#     print(f"  结果: {results}")
#
# def predict_apply_async():
#     pool = multiprocessing.Pool(3)
#     futures = []
#     for i in range(3):
#         f = pool.apply_async(task, args=(i,))
#         futures.append(f)
#     pool.close()
#     pool.join()
#     results = [f.get() for f in futures]
#     print(f"  结果: {results}")


# ----- 题6: 进程间数据不共享 [必做] -----
# 知识点: 每个进程独立内存空间

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

# 答案输出:
# 子进程1 的 list: [0, 1, 2]  （每个子进程操作的是自己的副本）
# 子进程2 的 list: [0, 1, 2]  （同上）
# 主进程 的 list: []           （空列表）
# 解释: 每个进程都有自己独立的内存空间，子进程创建时会复制主进程的数据，
#       子进程中对 list 的修改只影响子进程自己的副本，不会影响主进程的原始数据。
#       这就是"进程间数据不共享"的含义。

print("题6 答案:")
print("  子进程1 的 list: [0, 1, 2]")
print("  子进程2 的 list: [0, 1, 2]")
print("  主进程 的 list: []")
print("  原因: 每个进程独立内存空间，子进程操作的是数据副本，不影响主进程")
print()

# 验证:
# predict_no_share()


# ----- 题7: Queue 进程间通信 [必做] -----
# 知识点: multiprocessing.Queue, put(), get()

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
    p2.terminate()
    print("  主进程: 结束")

# 答案:
# 1) Queue 中的数据是 先进先出（FIFO, First In First Out）
# 2) 如果生产者已经放完所有数据，消费者继续调用 q.get() 会 阻塞/挂起，一直等待新数据
# 3) multiprocessing.Queue 只能用于 Process（直接创建的进程）
#    Manager().Queue() 可以用于 两者皆可（Process 和 Pool 都支持）

answer_7_1 = "先进先出（FIFO）"
answer_7_2 = "阻塞/挂起，一直等待新数据到来"
answer_7_3_a = "Process"
answer_7_3_b = "两者皆可（Process 和 Pool）"

print("题7 答案:")
print(f"  1) {answer_7_1}")
print(f"  2) {answer_7_2}")
print(f"  3) multiprocessing.Queue: {answer_7_3_a}")
print(f"     Manager().Queue(): {answer_7_3_b}")
print()

# 验证:
# predict_queue()


# ----- 题8: Manager().Queue() vs multiprocessing.Queue() [必做] -----
# 知识点: Manager().Queue() 可用于进程池

def pool_producer(q):
    for i in range(3):
        q.put(i * 100)
        print(f"  [Pool] 生产者 PID={os.getpid()} 放入: {i * 100}")

def pool_consumer(q):
    while True:
        item = q.get()
        print(f"  [Pool] 消费者 PID={os.getpid()} 取出: {item}")

def predict_manager_queue():
    q = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool(2)
    pool.apply_async(pool_producer, args=(q,))
    pool.apply_async(pool_consumer, args=(q,))
    pool.close()
    pool.join()

# 答案:
# 1) 不能
# 2) 原因: multiprocessing.Queue 不能被序列化（pickle）传递给进程池中的工作进程。
#    Pool 使用 pickle 来序列化任务参数，但 multiprocessing.Queue 对象不能被 pickle。
#    Manager().Queue() 返回的是一个代理对象（proxy），可以通过 pickle 传递。
# 3) Manager().Queue() 的底层实现基于 代理对象（Proxy），通过 Manager 服务器进程实现跨进程通信

answer_8_1 = "不能"
answer_8_2 = "multiprocessing.Queue 不能被 pickle 序列化传递给 Pool 的工作进程，Manager().Queue() 返回代理对象可以序列化"
answer_8_3 = "代理对象（Proxy），底层通过 Manager 服务器进程通信"

print("题8 答案:")
print(f"  1) {answer_8_1}")
print(f"  2) {answer_8_2}")
print(f"  3) {answer_8_3}")
print()

# 验证（注意此程序会一直运行，需手动终止）:
# predict_manager_queue()


# ============================================================
#                    第三部分: 深入理解题 [选做]
# ============================================================

# ----- 题9: 自定义进程类 - 生产者-消费者模式 [选做] -----
# 知识点: 继承 multiprocessing.Process，重写 run()

class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for _ in range(5):
            num = random.randint(1, 100)
            self.queue.put(num)
            print(f"  生产者 PID={os.getpid()} 放入: {num}")
            time.sleep(0.1)
        self.queue.put(None)  # 结束信号
        print(f"  生产者完成，发送结束信号")

class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            if item is None:  # 收到结束信号
                print(f"  消费者收到结束信号，退出")
                break
            print(f"  消费者 PID={os.getpid()} 取出: {item}")

print("题9 答案: Producer 和 Consumer 类已实现")
print("  Producer.run(): 循环放入随机数，最后放入 None 作为结束信号")
print("  Consumer.run(): 循环取出数据，遇到 None 则退出循环")
print()

# 验证:
def run_producer_consumer():
    q = multiprocessing.Queue()
    producer = Producer(q)
    consumer = Consumer(q)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print("  生产者-消费者模式完成")


# ----- 题10: 进程 vs 线程选择场景分析 [选做] -----
# 知识点: 进程vs线程区别

# 场景1: 爬取1000个网页（I/O 密集型）
answer_10_1 = "多线程。I/O 密集型任务大部分时间在等待网络响应，线程开销小、创建快、切换成本低，适合大量并发 I/O 操作"

# 场景2: 对100万张图片做矩阵运算（CPU 密集型）
answer_10_2 = "多进程。CPU 密集型任务需要大量计算，多进程可以利用多核 CPU 真正并行计算，绕过 GIL 限制"

# 场景3: 同时读写同一个文件
answer_10_3 = "多线程。线程共享进程的内存空间，对文件的操作天然在同一进程中，配合锁即可保证安全；多进程需要额外的进程间同步机制"

# 场景4: 需要多个任务共享一个大字典并实时修改
answer_10_4 = "多线程。线程天然共享进程内的全局变量（包括字典），配合 Lock 即可安全修改；多进程间数据不共享，需要 Manager 或 Queue 等额外机制"

print("题10 答案:")
print(f"  场景1: {answer_10_1}")
print(f"  场景2: {answer_10_2}")
print(f"  场景3: {answer_10_3}")
print(f"  场景4: {answer_10_4}")
print()


# ----- 题11: 调试修复 - 找出以下代码中的 3 个 BUG [选做] -----
# 知识点: 进程创建、Pool 使用、Queue 使用

print("题11 答案:")
print()
print("  BUG 1: 缺少 __name__ 保护")
print("  问题: Windows 下多进程基于 spawn 方式创建子进程，会重新导入模块，")
print("         没有 if __name__ == '__main__' 保护会导致无限递归创建进程（RuntimeError）")
print("  修复: 将进程创建代码放入 if __name__ == '__main__': 块中")
print()
print("  BUG 2: Pool 忘记 close/join")
print("  问题: 不调用 pool.close() 和 pool.join()，主进程会立即打印 'done' 并退出，")
print("         进程池中的异步任务可能还没执行完就被强制终止")
print("  修复: 在所有任务提交后调用 pool.close() 关闭池，再调用 pool.join() 等待所有任务完成")
print()
print("  BUG 3: multiprocessing.Queue 传给 Pool")
print("  问题: multiprocessing.Queue 对象不能被 pickle 序列化，传给 Pool 的工作进程时会报错")
print("  修复: 改用 multiprocessing.Manager().Queue()，它返回的代理对象可以被序列化传递")
print()


# ============================================================
#                         main 入口
# ============================================================
if __name__ == '__main__':
    print("=" * 50)
    print("Day13 练习1 - 进程基础 (答案)")
    print("=" * 50)
    print()

    # 可以取消注释运行各题的验证代码:
    # predict_pid()
    # predict_process_basic()
    # predict_apply()
    # predict_apply_async()
    # predict_no_share()
    # predict_queue()
    # predict_manager_queue()
    # run_producer_consumer()

    print("所有答案已展示完毕。")


# 修改记录:
# v1.0 (2026-07-13): 初始版本，覆盖 Day13 进程相关知识点
