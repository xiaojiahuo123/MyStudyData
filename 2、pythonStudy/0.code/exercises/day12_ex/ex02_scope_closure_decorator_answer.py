"""
Day12 练习2 - 作用域、闭包与装饰器 (参考答案)
由浅入深掌握 LEGB 规则、闭包原理、装饰器编程

参考源码: day12/P04_Scope.py
         day12/P05_Enclosing.py
         day12/P06_Decorator.py
版本: v1.0
最后更新: 2026-07-13
"""

import functools
import time

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
        print(f"  inner 中 x = {x}")

    inner()
    print(f"  outer 中 x = {x}")

outer()
print(f"  模块级 x = {x}")
# ✅ 答案:
#   inner 中 x = local
#   outer 中 x = enclosing
#   模块级 x = global
#
#   LEGB 查找顺序:
#   inner() 中找到了 Local 变量 x = "local"
#   outer() 中找到了 Enclosing 变量 x = "enclosing"
#   模块级找到了 Global 变量 x = "global"
#   每层函数都有自己的 x，互不影响

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
# ✅ 答案: count = 3
#   global 声明让函数内的 count 指向模块级的 count 变量
#   每次调用 increment() 都会修改全局的 count
#   如果去掉 global，count += 1 会报 UnboundLocalError
#   因为 Python 看到赋值操作会将 count 视为局部变量，但又找不到其定义

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
# ✅ 答案:
#   第1次调用: 1
#   第2次调用: 2
#   第3次调用: 3
#
#   count 变量保存在 make_counter 的函数帧中
#   nonlocal 让 counter() 能够修改外层的 count
#   每次调用 c()，count 都递增 1
#   make_counter() 返回后，其局部变量通过闭包被 counter 引用，不会被销毁

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
print(f"double 是否有 __closure__: {double.__closure__ is not None}")
print(f"闭包变量值: {double.__closure__[0].cell_contents}")
# ✅ 答案:
#   double(5) = 10  (5 * 2)
#   triple(5) = 15  (5 * 3)
#   double.__closure__ 不为 None，说明 double 是一个闭包
#   __closure__[0].cell_contents = 2，保存了外层变量 n 的值
#
#   闭包的本质: make_multiplier(2) 执行完毕后，
#   其局部变量 n=2 通过 __closure__ 被 multiplier 函数引用，不会被回收


# ============================================================
#                    第二部分: 进阶题
# ============================================================
print("\n" + "=" * 50)
print("        第二部分: 进阶题")
print("=" * 50)

# ----- 题5: 闭包工厂函数 [必做] -----
# 知识点: 利用闭包实现带状态的函数工厂
print("\n----- 题5: 闭包工厂函数 -----")
# 参考实现: create_accumulator

def create_accumulator():
    """创建累加器，每次调用传入值并返回当前总和"""
    total = 0

    def accumulator(value):
        nonlocal total
        total += value
        return total

    return accumulator

# 测试
acc = create_accumulator()
print(f"acc(10) = {acc(10)}")   # 10
print(f"acc(20) = {acc(20)}")   # 30
print(f"acc(30) = {acc(30)}")   # 60


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
# ✅ 答案:
#   bad 装饰后:  __name__ = wrapper, __doc__ = None
#   good 装饰后: __name__ = say_hello_good, __doc__ = 打招呼(被 good 装饰)
#
#   没有 @wraps 时，函数的元信息被 wrapper 的元信息覆盖
#   使用 @functools.wraps(func) 后，原函数的 __name__, __doc__, __module__
#   等属性被复制到 wrapper 上，保持了被装饰函数的"身份"

# ----- 题7: 简单装饰器实现 [必做] -----
# 知识点: 装饰器(decorator)本质是一个接收函数并返回新函数的可调用对象
print("\n----- 题7: 简单装饰器实现 -----")
# 参考实现: timer 装饰器

def timer(func):
    """打印函数执行耗时的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__} 耗时: {elapsed:.4f} 秒")
        return result
    return wrapper

# 测试
@timer
def slow_function():
    time.sleep(0.5)
    return "完成"

result = slow_function()
print(f"  结果: {result}")


# ----- 题8: 带计数功能的装饰器 [必做] -----
# 知识点: 装饰器可以通过闭包为被装饰函数添加额外状态
print("\n----- 题8: 带计数功能的装饰器 -----")
# 参考实现: count_calls 装饰器

def count_calls(func):
    """记录函数调用次数的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

# 测试
@count_calls
def greet(name):
    return f"你好, {name}!"

greet("Alice")
greet("Bob")
greet("Charlie")
print(f"函数被调用了 {greet.call_count} 次")  # 3


# ============================================================
#                    第三部分: 深入理解题
# ============================================================
print("\n" + "=" * 50)
print("        第三部分: 深入理解题")
print("=" * 50)

# ----- 题9: 带参装饰器 (三层嵌套) [选做] -----
# 知识点: 带参装饰器 = 装饰器工厂，最外层接收参数，中间层接收函数，最内层是 wrapper
print("\n----- 题9: 带参装饰器 (三层嵌套) -----")
# 参考实现: repeat(n) 装饰器

def repeat(n):
    """让函数执行 n 次的带参装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# 测试
@repeat(3)
def say_hi():
    print("  Hi!")

say_hi()
# 输出:
#   Hi!
#   Hi!
#   Hi!
#
# 执行流程: repeat(3) -> decorator(say_hi) -> wrapper
# @repeat(3) 等价于 say_hi = repeat(3)(say_hi)


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
# ✅ 答案: 完整输出顺序:
#   A 前
#   B 前
#   C 前
#   核心函数执行
#   C 后
#   B 后
#   A 后
#
#   装饰顺序: @decorator_A 最后装饰，所以最外层
#   等价于: my_function = A(B(C(my_function)))
#   执行顺序: A 的 wrapper -> B 的 wrapper -> C 的 wrapper -> 原函数
#   记忆: 装饰像洋葱，从外向内进入，再从内向外返回

# ----- 题11: 类装饰器 (__call__) [选做] -----
# 知识点: 实现 __call__ 的类可以作为装饰器使用
print("\n----- 题11: 类装饰器 (__call__) -----")
# 参考实现: CacheDecorator

class CacheDecorator:
    """缓存函数计算结果的类装饰器"""

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

# 测试
@CacheDecorator
def expensive_add(a, b):
    print(f"  计算 {a} + {b}...")
    return a + b

print(f"结果: {expensive_add(1, 2)}")
print(f"结果: {expensive_add(1, 2)}")  # 第二次不会打印 "计算..."
print(f"结果: {expensive_add(3, 4)}")
# 输出:
#   计算 1 + 2...
#   结果: 3
#   结果: 3          (直接返回缓存，不执行函数)
#   计算 3 + 4...
#   结果: 7
#
# 类装饰器的工作方式:
# @CacheDecorator 等价于 expensive_add = CacheDecorator(expensive_add)
# 之后 expensive_add(1, 2) 等价于 CacheDecorator.__call__(1, 2)

# ----- 题12: 调试修复 - 闭包陷阱 [选做] -----
# 知识点: 循环中创建闭包的经典陷阱——所有闭包共享同一个变量
print("\n----- 题12: 调试修复 - 闭包陷阱 -----")

# Bug 版本展示
def create_multipliers_bug():
    """有 Bug 的版本"""
    multipliers = []
    for i in range(5):
        def multiplier(x):
            return x * i
        multipliers.append(multiplier)
    return multipliers

bug_funcs = create_multipliers_bug()
print("Bug 版本:")
for f in bug_funcs:
    print(f"  f(10) = {f(10)}")
# 输出: 40 40 40 40 40 (所有闭包引用同一个 i，最终 i=4)

# 修复版本
def create_multipliers_fixed():
    """修复后的版本: 使用默认参数捕获当前值"""
    multipliers = []
    for i in range(5):
        def multiplier(x, i=i):  # 关键: 默认参数在定义时求值
            return x * i
        multipliers.append(multiplier)
    return multipliers

fixed_funcs = create_multipliers_fixed()
print("修复版本:")
for f in fixed_funcs:
    print(f"  f(10) = {f(10)}")
# 输出: 0 10 20 30 40  ✅
#
# BUG 说明:
# 原代码中所有 multiplier 函数引用的是同一个变量 i
# 循环结束后 i=4，所有函数执行时都使用最终值 4
#
# 修复方法(三种):
# 1. 默认参数: def multiplier(x, i=i)
# 2. 工厂函数: def make_multiplier(i): return lambda x: x * i
# 3. functools.partial: from functools import partial; partial(lambda x, i: x*i, i)