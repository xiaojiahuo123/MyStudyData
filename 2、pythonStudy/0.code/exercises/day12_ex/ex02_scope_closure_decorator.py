"""
Day12 练习2 - 作用域、闭包与装饰器
由浅入深掌握 LEGB 规则、闭包原理、装饰器编程

参考源码: day12/P04_Scope.py
         day12/P05_Enclosing.py
         day12/P06_Decorator.py
版本: v1.0
最后更新: 2026-07-13
"""

import functools

# ============================================================
#                      第一部分: 基础题
# ============================================================
print("=" * 50)
print("        第一部分: 基础题")
print("=" * 50)

# ----- 题1: LEGB 查找顺序预测 [必做] -----
# 知识点: LEGB 规则——Local -> Enclosing -> Global -> Builtin
print("\n----- 题1: LEGB 查找顺序预测 -----")

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(f"  inner 中 x = {x}")  # local

    inner()
    print(f"  outer 中 x = {x}")  # enclosing

outer()
print(f"  模块级 x = {x}")  # global
# 预测: 三个 print 分别输出什么? 变量查找遵循什么规则?
# ____我在每个print输出后面注释了我认为的输出

# ----- 题2: global 关键字 [必做] -----
# 知识点: global 声明在函数内修改全局变量(global variable)
print("\n----- 题2: global 关键字 -----")

count = 0

def increment():
    global count
    count += 1

increment()
increment()
increment()
print(f"count = {count}")
# 预测: 输出什么? 如果去掉 global 声明会怎样?
# ____3，去掉后函数内的count变为局部变量，每次执行函数都是一个新的局部变量，并在函数执行完毕释放后一起被释放，全局的count还是输出0

# ----- 题3: nonlocal 关键字 [必做] -----
# 知识点: nonlocal 声明在内层函数中修改外层函数的局部变量(enclosing variable)
print("\n----- 题3: nonlocal 关键字 -----")

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

c = make_counter()
print(f"第1次调用: {c()}")
print(f"第2次调用: {c()}")
print(f"第3次调用: {c()}")
# 预测: 每次调用 c() 分别返回什么? count 变量在哪里被保存?
# ____1，2，3  因为这是闭包，counter 函数的 闭包细胞对象 中，可以通过 __closure__ 属性查看
# c.__closure__[0].cell_contents   ，
# - 对象挂在函数对象的 __closure__ 属性上- 只要 c （函数对象）还活着， count 就不会被回收

# ----- 题4: 简单闭包识别 [必做] -----
# 知识点: 闭包(closure) = 内层函数 + 引用的外层变量
print("\n----- 题4: 简单闭包识别 -----")

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")
print(f"double 是否有 __closure__: {double.__closure__ is not None}")  # True，此时不是None
print(f"闭包变量值: {double.__closure__[0].cell_contents}")
# 预测: double(5) 和 triple(5) 各输出什么? __closure__ 中保存了什么?
# ____10，15；保存了闭包的对象，及各自的 n


# ============================================================
#                    第二部分: 进阶题
# ============================================================
print("\n" + "=" * 50)
print("        第二部分: 进阶题")
print("=" * 50)

# ----- 题5: 闭包工厂函数 [必做] -----
# 知识点: 利用闭包实现带状态的函数工厂
print("\n----- 题5: 闭包工厂函数 -----")
# TODO: 实现 create_accumulator() 函数，返回一个累加器闭包
# 每次调用累加器时传入一个值，返回当前累计总和
# 提示: 使用 nonlocal 修改外层的 total 变量

def create_accumulator():
    # TODO: 实现累加器闭包
    total = 0
    def accumulator(x):
        nonlocal total
        total += x
        return total
    return accumulator

# 测试代码 (取消注释以验证):
acc = create_accumulator()
print(f"acc(10) = {acc(10)}")   # 期望: 10
print(f"acc(20) = {acc(20)}")   # 期望: 30
print(f"acc(30) = {acc(30)}")   # 期望: 60


# ----- 题6: functools.wraps 保留元信息 [必做] -----
# 知识点: @functools.wraps 保留被装饰函数的 __name__, __doc__ 等
print("\n----- 题6: functools.wraps 保留元信息 -----")

def bad_decorator(func):
    """不使用 wraps 的装饰器"""
    def wrapper(*args, **kwargs):
        print("  [bad] 调用前")
        result = func(*args, **kwargs)
        print("  [bad] 调用后")
        return result
    return wrapper

def good_decorator(func):
    """使用 wraps 的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("  [good] 调用前")
        result = func(*args, **kwargs)
        print("  [good] 调用后")
        return result
    return wrapper

@bad_decorator
def say_hello_bad():
    """打招呼(被 bad 装饰)"""
    print("  Hello!")

@good_decorator
def say_hello_good():
    """打招呼(被 good 装饰)"""
    print("  Hello!")

print(f"bad 装饰后: __name__ = {say_hello_bad.__name__}, __doc__ = {say_hello_bad.__doc__}")
print(f"good 装饰后: __name__ = {say_hello_good.__name__}, __doc__ = {say_hello_good.__doc__}")
# 预测: 两个装饰器对 __name__ 和 __doc__ 的影响有何不同?
# ____bad 装饰后: __name__ = wrapper, __doc__ = None
# ____good 装饰后: __name__ = say_hello_good, __doc__ = 打招呼(被 good 装饰)


# ----- 题7: 简单装饰器实现 [必做] -----
# 知识点: 装饰器(decorator)本质是一个接收函数并返回新函数的可调用对象
print("\n----- 题7: 简单装饰器实现 -----")
# TODO: 实现一个 timer 装饰器，打印函数执行耗时
# 提示: 使用 time.perf_counter() 计时

import time

def timer(func):
    # TODO: 实现计时装饰器
    """使用 wraps 的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()        # 记录开始时间，返回一个高精度的时间戳（浮点数）
        # time.perf_counter() 就是一个高精度秒表，先按一下开始，再按一下结束，两次相减就是经过的时间
        result = func(*args, **kwargs)     # 执行原函数
        end = time.perf_counter()          # 记录结束时间
        print(f"{func.__name__} 耗时: {end - start:.4f} 秒")
        return result
    return wrapper

# 测试代码 (取消注释以验证):
@timer
def slow_function():
    time.sleep(0.5)
    return "完成"

result = slow_function()
print(f"结果: {result}")
# 期望输出类似: slow_function 耗时: 0.50xx 秒


# ----- 题8: 带计数功能的装饰器 [必做] -----
# 知识点: 装饰器可以通过闭包为被装饰函数添加额外状态
print("\n----- 题8: 带计数功能的装饰器 -----")
# TODO: 实现 count_calls 装饰器，记录函数被调用的次数
# 要求: 调用次数存储在 wrapper 函数的属性 wrapper.call_count 中

def count_calls(func):
    # TODO: 实现计数装饰器
    # call_count = 0
    # wrapper.call_count = 0
    def wrapper(*args, **kwargs):
        # nonlocal count
        # count += 1
        wrapper.call_count += 1    # 通过函数属性存储计数
        result = func(*args, **kwargs)
        return result
    wrapper.call_count = 0  # 这里必须卸载函数定义之后，才能在函数对象
    return wrapper


# 测试代码 (取消注释以验证):
@count_calls
def greet(name):
    return f"你好, {name}!"
#
greet("Alice")
greet("Bob")
greet("Charlie")
print(f"函数被调用了 {greet.call_count} 次")
# 期望输出: 函数被调用了 3 次


# ============================================================
#                    第三部分: 深入理解题
# ============================================================
print("\n" + "=" * 50)
print("        第三部分: 深入理解题")
print("=" * 50)

# ----- 题9: 带参装饰器 (三层嵌套) [选做] -----
# 知识点: 带参装饰器 = 装饰器工厂，最外层接收参数，中间层接收函数，最内层是 wrapper
print("\n----- 题9: 带参装饰器 (三层嵌套) -----")
# TODO: 实现一个 repeat(n) 装饰器，让被装饰的函数执行 n 次
# 结构: repeat(n) -> decorator(func) -> wrapper(*args, **kwargs)

def repeat(n):
    # TODO: 实现带参装饰器
    pass

# 测试代码 (取消注释以验证):
# @repeat(3)
# def say_hi():
#     print("  Hi!")
#
# say_hi()
# 期望输出:
#   Hi!
#   Hi!
#   Hi!


# ----- 题10: 多层装饰器叠加执行顺序 [选做] -----
# 知识点: 多层装饰器从下往上装饰(from bottom to top)，从外往内执行
print("\n----- 题10: 多层装饰器叠加执行顺序 -----")

def decorator_A(func):
    def wrapper(*args, **kwargs):
        print("  A 前")
        result = func(*args, **kwargs)
        print("  A 后")
        return result
    return wrapper

def decorator_B(func):
    def wrapper(*args, **kwargs):
        print("  B 前")
        result = func(*args, **kwargs)
        print("  B 后")
        return result
    return wrapper

def decorator_C(func):
    def wrapper(*args, **kwargs):
        print("  C 前")
        result = func(*args, **kwargs)
        print("  C 后")
        return result
    return wrapper

@decorator_A
@decorator_B
@decorator_C
def my_function():
    print("  核心函数执行")

my_function()
# 预测: 完整的输出顺序是什么? 提示: 装饰器相当于 my_function = A(B(C(my_function)))
# ____


# ----- 题11: 类装饰器 (__call__) [选做] -----
# 知识点: 实现 __call__ 的类可以作为装饰器使用
print("\n----- 题11: 类装饰器 (__call__) -----")
# TODO: 用类实现一个 CacheDecorator 装饰器
# 功能: 缓存函数的计算结果，相同参数不重复计算
# 提示: 用字典存储 {参数: 结果}，在 __call__ 中检查

class CacheDecorator:
    # TODO: 实现 __init__ 和 __call__
    pass

# 测试代码 (取消注释以验证):
# @CacheDecorator
# def expensive_add(a, b):
#     print(f"  计算 {a} + {b}...")
#     return a + b
#
# print(f"结果: {expensive_add(1, 2)}")
# print(f"结果: {expensive_add(1, 2)}")  # 第二次不应打印 "计算..."
# print(f"结果: {expensive_add(3, 4)}")
# 期望: 第二次调用 expensive_add(1, 2) 不会打印 "计算..."


# ----- 题12: 调试修复 - 闭包陷阱 [选做] -----
# 知识点: 循环中创建闭包的经典陷阱——所有闭包共享同一个变量
print("\n----- 题12: 调试修复 - 闭包陷阱 -----")

# BUG: 以下代码想创建 5 个函数分别返回 0-4，但结果不正确
def create_multipliers_bug():
    """有 Bug 的版本"""
    multipliers = []
    for i in range(5):
        def multiplier(x):
            return x * i  # BUG: 这里的 i 不是创建时的值，而是最终循环结束的值
        multipliers.append(multiplier)
    return multipliers

bug_funcs = create_multipliers_bug()
print("Bug 版本:")
for f in bug_funcs:
    print(f"  f(10) = {f(10)}", end="")
print()
# 期望: 0 10 20 30 40
# 实际: 40 40 40 40 40

# TODO: 修复 create_multipliers_bug，使其输出正确结果
# 提示: 使用默认参数或工厂函数捕获当前值

def create_multipliers_fixed():
    """修复后的版本"""
    # TODO: 修复闭包陷阱
    pass

# 测试代码 (取消注释以验证):
# fixed_funcs = create_multipliers_fixed()
# print("修复版本:")
# for f in fixed_funcs:
#     print(f"  f(10) = {f(10)}", end="")
# print()
# 期望: 0 10 20 30 40