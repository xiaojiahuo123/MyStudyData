"""
Day07 练习1 - 闭包、匿名函数与文件操作（答案版）
"""

# ----- 题1: 作用域链 -----
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
# ✅ 答案:
# inner: x=30
# outer: x=20
# global: x=10

print()

# ----- 题2: global 关键字 -----
count = 0

def increment():
    global count
    count += 1

increment()
increment()
increment()
print(f"count = {count}")  # ✅ 答案: 3

print()

# ----- 题3: nonlocal 关键字 -----
def outer():
    num = 10
    def inner():
        nonlocal num
        num += 5
    inner()
    inner()
    print(f"num = {num}")

outer()  # ✅ 答案: num = 20

print()

# ----- 题4: 闭包基础 -----
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
add10 = make_adder(10)
print(add5(3))    # ✅ 答案: 8
print(add10(3))   # ✅ 答案: 13
print(add5(100))  # ✅ 答案: 105

print()

# ----- 题5: lambda 基础 -----
square = lambda x: x ** 2
print(square(4))     # ✅ 答案: 16
print(square(10))    # ✅ 答案: 100

add = lambda a, b: a + b
print(add(3, 5))     # ✅ 答案: 8

print()

# ----- 题6: map 函数 -----
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, nums))
print(f"result = {result}")  # ✅ 答案: [2, 4, 6, 8, 10]

print()

# ----- 题7: filter 函数 -----
nums = [1, -2, 3, -4, 5, -6]
result = list(filter(lambda x: x > 0, nums))
print(f"正数: {result}")  # ✅ 答案: [1, 3, 5]

print()

# ----- 题8: 递归 - 阶乘 -----
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # ✅ 答案: 120
print(factorial(0))   # ✅ 答案: 1
print(factorial(1))   # ✅ 答案: 1

print()

# ----- 题9: 递归 - 斐波那契数列 -----
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i), end=" ")
print()  # ✅ 答案: 0 1 1 2 3 5 8

print()

# ----- 题10: 闭包实现计数器 - 参考实现 -----
def make_counter(start=0):
    # 参考实现:
    count = start
    def counter():
        nonlocal count
        current = count
        count += 1
        return current
    return counter

counter = make_counter(0)
print(counter())  # 预期: 0
print(counter())  # 预期: 1
print(counter())  # 预期: 2

print()

# ----- 题11: reduce 函数 -----
from functools import reduce

nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, nums)
print(f"求和: {result}")   # ✅ 答案: 15

result2 = reduce(lambda x, y: x * y, nums)
print(f"求积: {result2}")  # ✅ 答案: 120

print()

# ----- 题12: sorted 与 lambda -----
students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 18, "score": 92},
    {"name": "王五", "age": 22, "score": 78},
]

by_age = sorted(students, key=lambda s: s["age"])
print(f"按年龄排序: {[s['name'] for s in by_age]}")  # ✅ 答案: ['李四', '张三', '王五']

by_score = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"按成绩降序: {[s['name'] for s in by_score]}")  # ✅ 答案: ['李四', '张三', '王五']

print()

# ----- 题13: 文件写入与读取 - 参考实现 -----
scores = "张三 85\n李四 92\n王五 78\n"

# 参考实现1: 写入文件
with open("test_scores.txt", "w", encoding="utf-8") as f:
    f.write(scores)

# 参考实现2: 读取文件
with open("test_scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

print()

# ----- 题14: 闭包的陷阱 -----
def make_multipliers():
    return [lambda x: x * i for i in range(5)]

multipliers = make_multipliers()
results = [m(2) for m in multipliers]
print(f"results = {results}")
# ✅ 答案: [8, 8, 8, 8, 8]（不是 [0, 2, 4, 6, 8]）
# 解释: 闭包中的变量 i 是延迟绑定的，当调用时 i 已经是 4 了
# 所有 lambda 都引用了同一个变量 i，循环结束后 i=4
# 如果要得到期望结果，需要:
# [lambda x, i=i: x * i for i in range(5)]

print()

# ----- 题15: 递归深度与尾递归 - 参考实现 -----
def factorial_tail(n, acc=1):
    # 参考实现:
    if n <= 1:
        return acc
    return factorial_tail(n - 1, n * acc)

print(factorial_tail(5))  # 预期: 120

print()

# ----- 题16: 综合应用 - 装饰器雏形 -----
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数返回: {result}")
        return result
    return wrapper

def add(a, b):
    return a + b

logged_add = logger(add)
result = logged_add(3, 5)
# ✅ 答案:
# 调用函数: add
# 函数返回: 8

print()

# ----- 题17: 调试修复 - 参考答案 -----
# BUG 1 修复: lambda 只能包含表达式，不能包含 return 语句
square = lambda x: x ** 2  # 正确写法

# BUG 2 修复: 递归需要基准条件
def count_down(n):
    if n < 0:  # 添加基准条件
        return
    print(n)
    return count_down(n - 1)

# BUG 3 修复: "r" 模式只能读取，写入需要用 "w" 模式
f = open("data.txt", "w")  # 修复: 使用 "w" 模式
f.write("hello")
f.close()
