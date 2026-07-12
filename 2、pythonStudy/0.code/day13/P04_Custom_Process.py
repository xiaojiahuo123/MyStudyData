"""
    该案例演示了自定义进程类
"""
import multiprocessing
import os


# import multiprocessing
# import os
#
# def worker(name):
#     print(f"进程 {name}, PID: {os.getpid()}")
#
# if __name__ == '__main__':
#     p = multiprocessing.Process(target=worker, args=("子进程1",))  # args作为传给执行函数的关键字参数，必须是元组
#     p.start()
#     p.join()

# import multiprocessing
# import os
#
# def worker():
#     print(f"子进程 PID: {os.getpid()}, 父进程 PID: {os.getppid()}")
#
# if __name__ == '__main__':
#     print(f"主进程 PID: {os.getpid()}")
#     p = multiprocessing.Process(target=worker)
#     p.start()
#     p.join(timeout=10)
#     #最多等10秒 ，超时后不再等待子进程，继续执行主进程
#     #但是子进程还在后台执行，这相当于阻塞主进程10秒来等待子进程
#     print(f"子进程退出码: {p.exitcode}")



class Worker(multiprocessing.Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print(self)
        print(f"当前进程id{os.getpid()},名称是{self.name},父进程的id{os.getppid()}执行了")

if __name__ == '__main__':
    # 创建进程对象
    for i in range(5):
        p = Worker("my_p_"+str(i))
        p.start()
