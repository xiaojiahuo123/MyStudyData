"""
Day07 练习1 - 闭包、匿名函数与文件操作
由浅入深掌握作用域、闭包、递归、匿名函数及文件操作

参考源码: day07/P03_Scope.py
         day07/P04_Closure.py
         day07/P06_GlobalAndNonlocal.py
         day07/P07_Factorial.py
         day07/P08_Anonymity_Function.py
         day07/P11_File.py
版本: v1.0
最后更新: 2026-06-14
"""

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 作用域链 [必做] -----
# 知识点: 局部作用域 -> 嵌套作用域 -> 全局作用域 -> 内建作用域
# 预测以下代码的输出结果

x = 10

def outer():
    x = 20
    def inner():
        x = 30
        print(f"inner: x={x}")
    inner()
    print(f"outer: x={x}")

outer()
print(f"global: x={x}")
# ____30
# ____20
# ____10

print()

# ----- 题2: global 关键字 [必做] -----
# 知识点: 在函数内修改全局变量需要使用 global 声明
# 预测以下代码的输出结果

count = 0

def increment():
    global count
    count += 1

increment()
increment()
increment()
print(f"count = {count}")  # ____3

print()

# ----- 题3: nonlocal 关键字 [必做] -----
# 知识点: 在嵌套函数中修改外层函数的变量需要使用 nonlocal
# 预测以下代码的输出结果

def outer():
    num = 10
    def inner():
        nonlocal num
        num += 5
    inner()
    inner()
    print(f"num = {num}")

outer()  # ____20

print()

# ----- 题4: 闭包基础 [必做] -----
# 知识点: 内部函数引用了外部函数的变量，外部函数返回内部函数
# 预测以下代码的输出结果

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
add10 = make_adder(10)
print(add5(3))    # ____8
print(add10(3))   # ____13
print(add5(100))  # ____105

print()

# ----- 题5: lambda 基础 [必做] -----
# 知识点: lambda 表达式创建匿名函数
# 预测以下代码的输出结果

square = lambda x: x ** 2
print(square(4))     # ____16
print(square(10))    # ____100

add = lambda a, b: a + b
print(add(3, 5))     # ____8

print()

# ----- 题6: map 函数 [必做] -----
# 知识点: map() 对序列中每个元素应用函数
# 预测以下代码的输出结果

nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, nums))
print(f"result = {result}")  # ____[2,4,6,8,10]

print()

# ----- 题7: filter 函数 [必做] -----
# 知识点: filter() 对序列中元素进行过滤
# 预测以下代码的输出结果

nums = [1, -2, 3, -4, 5, -6]
result = list(filter(lambda x: x > 0, nums))
print(f"正数: {result}")  # ____[1,3,5]

print()

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题8: 递归 - 阶乘 [必做] -----
# 知识点: 递归函数需要基准条件和递归调用
# 预测以下代码的输出结果

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # ____120
print(factorial(0))   # ____1
print(factorial(1))   # ____1

print()

# ----- 题9: 递归 - 斐波那契数列 [必做] -----
# 知识点: 递归实现斐波那契数列
# 预测以下代码的输出结果

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i), end=" ")
print()  # ____

print()

# ----- 题10: 闭包实现计数器 [必做] -----
# 知识点: 闭包可以捕获并保存外部函数的状态
# 完成以下代码，使计数器每次调用时返回递增的值

def make_counter(start=0):
    # TODO: 实现计数器，每次调用返回 start, start+1, start+2, ...
    count = start # 因为后续的counter()函数还要使用start,就能够避免释放他（生命周期管理）
    def counter():
        nonlocal count
        current = count  # 函数执行完毕，但 count 被保留
        count += 1
        return current
    return counter

# 验证
counter = make_counter(0)  # 闭包捕获的变量存储在函数的 __closure__ 属性中
print(counter.__closure__)
print(counter())  # 预期: 0
print(counter())  # 预期: 1
print(counter.__closure__[0].cell_contents)
print(counter())  # 预期: 2

# ----- 题11: reduce 函数 [必做] -----
# 知识点: reduce() 对序列元素进行累积运算
# 预测以下代码的输出结果

from functools import reduce

nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, nums)
print(f"求和: {result}")   # ____15

result2 = reduce(lambda x, y: x * y, nums)
print(f"求积: {result2}")  # ____120

print()

# ----- 题12: sorted 与 lambda [必做] -----
# 知识点: 使用 lambda 作为排序的 key 函数
# 预测以下代码的输出结果

students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 18, "score": 92},
    {"name": "王五", "age": 22, "score": 78},
]

by_age = sorted(students, key=lambda s: s["age"])  # 排序后返回的是完整的列表,reverse=FLASE 不写就是默认为flase，即升序
print(by_age)
print(f"按年龄排序: {[s['name'] for s in by_age]}")  # ____['李四', '张三', '王五']

by_score = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"按成绩降序: {[s['name'] for s in by_score]}")  # ____['李四', '张三', '王五']

print()

# ----- 题13: 文件写入与读取 [必做] -----
# 知识点: 文件的打开、写入、读取、关闭操作
# TODO: 完成以下文件操作

# 1. 将以下内容写入文件 "test_scores.txt"
scores = "张三 85\n李四 92\n王五 78\n"

# TODO: 使用 with 语句写入文件
# with __________:
#     __________
with open("test_scores.txt", "w", encoding="utf-8") as f:
    f.write(scores)
    f.close()
# 2. 从文件中读取并打印每一行
# TODO: 使用 with 语句读取文件
# with __________:
#     __________
with open("test_scores.txt", "r", encoding="utf-8") as f:
    print(f.readline())
    f.close()
print("文件操作完成（TODO部分需要学生实现）")

print()

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题14: 闭包的陷阱 [选做] -----
# 知识点: 闭包中变量是延迟绑定的（引用的是变量本身，不是变量的值）
# 预测以下代码的输出结果

def make_multipliers():
    """
    这是为了演示闭包陷阱创建的闭包函数
    :return: 返回匿名函数
    """
    return [lambda x: x * i for i in range(5)]  # 正是因为这里没有X，下面调用的时候也没有给x实际的值
    # 或者说这里的x实际上没办法再调用,因为make_multipliers()函数不接收参数，且x是再匿名函数中的，是闭包的时候保留的
# 此处传输的是列表形式，其中存储的对象是匿名函数
"""
闭包之后再调用才能传入值，所以这里的函数是只创建了但是没有调用，所以是没有执行，直接返回了五个匿名函数的列表，
后面才能直接用列表的推导式直接使用这个匿名函数的列表
"""
# 普通函数
# def func(x):
#     return x * 2
# # 请问下面两行的区别是什么？
# func        # → 函数对象本身（不执行）
# func(3)     # → 执行函数，返回 6
multipliers = make_multipliers()
results = [m(2) for m in multipliers]  # 直接调用闭包函数，返回的是一个列表，每个元素都是一个匿名函数
# 5个函数的 __closure__（闭包的捕获的值的存储） 里存的是 同一个变量 i 的引用 ，不是各自独立的值。
print(f"results = {results}")  # ____[0, 2, 4, 6, 8]
# 提示: 你可能会期望 [0, 2, 4, 6, 8]，但实际结果是什么？为什么？
# [8, 8, 8, 8, 8]
print()

# ----- 题15: 递归深度与尾递归 [选做] -----
# 知识点: Python 默认递归深度限制为 1000
# 思考: 以下代码会发生什么？

# import sys
# print(sys.getrecursionlimit())  # 查看递归深度限制
#
# def infinite_recursion(n):
#     print(n)
#     return infinite_recursion(n + 1)
#
# infinite_recursion(0)  # 会报错: RecursionError

# TODO: 实现一个尾递归风格的阶乘函数（虽然 Python 不优化尾递归）
def factorial_tail(n, acc=1):
    pass  # 学生实现

# 验证
# print(factorial_tail(5))  # 预期: 120

# ----- 题16: 综合应用 - 装饰器雏形 [选做] -----
# 知识点: 综合运用闭包、函数作为参数
# 以下代码演示了装饰器的基本原理，预测输出结果

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")  # func = add  ← 被 wrapper 引用，不会释放 使用了 func  ← 闭包捕获   
        result = func(*args, **kwargs)
        print(f"函数返回: {result}")
        return result
    return wrapper

def add(a, b):
    return a + b

logged_add = logger(add) # logged_add = wrapper（带着 func 一起返回）
result = logged_add(3, 5)
# ____
# ____
# ____

print()

# ----- 题17: 调试修复 - 找出以下代码中的 3 个 BUG [选做] -----
# 修复以下代码，使其能正确运行

# BUG 1: 语法错误 - lambda 不能包含语句
# square = lambda x: x ** 2; return x  # 错误写法

# BUG 2: 逻辑错误 - 递归没有基准条件
def count_down(n):
    print(n)
    return count_down(n - 1)  # 缺少什么？

# BUG 3: 文件操作错误 - 使用了错误的模式
# f = open("data.txt", "r")
# f.write("hello")  # 用 "r" 模式能写入吗？
# f.close()
