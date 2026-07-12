"""
    该案例演示了生成器
"""

#创建生成器对象--- 使用元组推导式
# generator = (x for x in range(5))  # 创建生成器
# print(generator)  # <generator object <genexpr> at 0x0000026C2066CB80>
# for x in generator:
#     print(x)

print('================================================================')
print("=============================分割================================")
print("================================================================")
#创建生成器对象--- 使用函数创建
# def fibo():
#     a , b = 0,1
#     while True:
#         yield b
#         a, b = b, a+b
#
# f = fibo()
# print(f"注释1s")
# print(type(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

print('================================================================')
print("=============================分割================================")
print("================================================================")
#创建生成器对象--- 使用函数创建  获取函数返回值
# def fibo():
#     a , b ,counter = 0 , 1 , 0
#     while counter < 10:
#         yield b
#         a, b ,counter = b, a+b ,counter + 1
#     return "done"
#     # fibo()因为使用了 yieid 所以正常返回的都是生成器对象，最终在条件不满足的时候，会抛出异常，用return 可以直接将异常信息返回
#
# f = fibo()
# try:
#     while True:
#         print(next(f))
# except StopIteration as e:
#     print(e)

print('================================================================')
print("=============================分割================================")
print("================================================================")

def task1():
    for i in range(5):
        print(f"任务1 - 步骤{i}")
        yield  # 暂停，交出控制权

def task2():
    for i in range(5):
        print(f"任务2 - 步骤{i}")
        yield

# 手动交替执行
t1 = task1()
t2 = task2()
for _ in range(5):
    next(t1)
    next(t2)



print('================================================================')
print("=============================分割================================")
print("================================================================")

# 向生成器发送数值，作为yield表达式的结果
# 案例 : 通过send()发送一个任务id，使生成器交替执行两个任务
def gen():
    task_id = 0
    int_value = 0
    char_value = "A"
    while True:
        match task_id:
            case 0:
                #生成数字序列
                task_id = yield int_value
                int_value += 1
            case 1:
                # 生成字符序列
                task_id = yield char_value
                char_value = chr(ord(char_value) + 1)
            case _:
                yield  # 返回None

f = gen()
print(next(f))
print(f.send(1))
print(f.send(1))
print(f.send(0))
print(f.send(0))
print(f.send(1))
print(f.send(1))
# print(f.send(None))
# print(f.send(1))
# print(f.send(1))


print('================================================================')
print("=============================分割================================")
print("================================================================")

def gen():
    while True:
        received = yield "hello"   # yield返回"hello"，同时接收send的值
        # ② "苹果"赋值给received
        # ③ 打印"收到: 苹果"
        # ④ 循环回来，再次yield "hello"，暂停
        # ⑤ 返回"hello"给调用者
        print(f"收到: {received}")

f = gen()
print(next(f))          # 启动生成器，输出 "hello"
print(f.send("苹果"))    # 发送"苹果"，打印"收到: 苹果"，输出 "hello"
print(f.send("香蕉"))    # 发送"香蕉"，打印"收到: 香蕉"，输出 "hello"