"""
Day07 练习2 - 闭包与作用域的底层原理
基于 CPython 源码深入理解闭包、cell 对象、作用域链、递归栈

参考源码: python3.13.13/Objects/cellobject.c    (PyCellObject 实现)
         python3.13.13/Objects/funcobject.h      (func_closure 字段)
         python3.13.13/Doc/reference/datamodel.rst (闭包文档)
版本: v1.0
最后更新: 2026-06-14
"""

import sys

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: __closure__ 与 cell 对象 [必做] -----
# 知识点: 闭包的 __closure__ 是一个 cell 对象元组
# 参考: datamodel.rst:563
#   "function.__closure__: None or a tuple of cells that contain bindings
#    for the names specified in the co_freevars attribute of the function's code object."
#   "A cell object has the attribute cell_contents."
# 预测以下代码的输出结果

def outer(x):
    def inner():
        return x
    return inner

fn = outer(42)
print(f"__closure__: {fn.__closure__}")                    # ____cell对象元组
print(f"cell 类型: {type(fn.__closure__[0])}")             # ____cell 类型: <class 'cell'>
print(f"cell_contents: {fn.__closure__[0].cell_contents}") # __  __cell_contents: 42
print(f"__code__.co_freevars: {fn.__code__.co_freevars}")  # ____  __code__.co_freevars: ('x',)

print()

# ----- 题2: cell 对象是可变的 [必做] -----
# 知识点: 可以通过 cell_contents 修改闭包捕获的变量
# 参考: cellobject.c:cell_set_contents
# 预测以下代码的输出结果

def make_counter(start=0):
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter(0)
print(f"初始 cell_contents: {c.__closure__[0].cell_contents}")  # ____0
print(f"调用1: {c()}")  # ____1
print(f"调用2: {c()}")  # ____2

# 直接修改 cell_contents
c.__closure__[0].cell_contents = 100
print(f"修改后调用: {c()}")  # ____101

print()

# ----- 题3: co_freevars 与 co_cellvars [必做] -----
# 知识点: co_cellvars 是被内部函数引用的变量，co_freevars 是从外部函数捕获的变量
# 参考: datamodel.rst:1428
#   "co_cellvars: tuple of names of local variables that are referenced by at least one
#    nested scope before being defined in the current scope"
# 预测以下代码的输出结果

def outer():
    x = 10  # 被 inner 引用 -> 属于 outer 的 co_cellvars
    y = 20  # 未被 inner 引用
    def inner():
        return x
    return inner

fn = outer()
print(f"outer 的 co_cellvars: {outer.__code__.co_cellvars}")   # ____x
print(f"inner 的 co_freevars: {fn.__code__.co_freevars}")     # ____r

print()

# ----- 题4: 作用域查找顺序 - LEGB [必做] -----
# 知识点: Local -> Enclosing -> Global -> Built-in
# 预测以下代码的输出结果

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(f"inner: {x}")
    inner()
    print(f"outer: {x}")

outer()
print(f"global: {x}")
# ____local
# ____enclosing
# ____global

print()

# ----- 题5: global 与 nonlocal 的本质 [必做] -----
# 知识点: global 将变量绑定到模块全局字典，nonlocal 将变量绑定到外层 cell 对象
# 预测以下代码的输出结果

g_var = 0

def test_scopes():
    enclosing_var = 10
    def inner():
        global g_var
        nonlocal enclosing_var
        g_var = 100
        enclosing_var = 20
    inner()
    print(f"enclosing_var: {enclosing_var}")  # ____20
    print(f"g_var: {g_var}")                  # ____100

test_scopes()
print(f"全局 g_var: {g_var}")  # ____100

print()

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题6: 多个闭包共享同一个 cell 对象 [必做] -----
# 知识点: 同一个外层函数返回的多个闭包，引用的是同一个 cell 对象
# 预测以下代码的输出结果

def make_getter_setter():
    value = 0
    def getter():
        return value
    def setter(new_val):
        nonlocal value
        value = new_val
    return getter, setter

getter, setter = make_getter_setter()

# 验证：getter 和 setter 的 cell 对象是否相同
print(f"getter cell: {getter.__closure__[0]}")
print(f"setter cell: {setter.__closure__[0]}")
print(f"同一 cell: {getter.__closure__[0] is setter.__closure__[0]}")  # ____true

setter(42)
print(f"getter(): {getter()}")  # ____42

print()

# ----- 题7: 闭包延迟绑定陷阱 [必做] -----
# 知识点: 闭包中的变量是引用，不是值的拷贝
# 预测以下代码的输出结果

def make_multipliers_wrong():
    return [lambda x: x * i for i in range(5)]

def make_multipliers_right():
    return [lambda x, i=i: x * i for i in range(5)]  #  # i 通过默认参数捕获
# 与上面的 i 值都是捕获的最终值不同，right 使用了 i=i 默认参数，每个函数捕获的是当时 i 的值
# 也就是说，返回的匿名函数的列表中，每个函数的 i 值都是不同的，不会共享同一个 cell 对象

wrong = make_multipliers_wrong()
right = make_multipliers_right()

print(f"wrong[2](2): {wrong[2](2)}")  # ____8
print(f"right[2](2): {right[2](2)}")  # ____4

# 用 __closure__ 解释原因
print(f"wrong[0] 的 i 值: {wrong[0].__closure__[0].cell_contents}")  # ____
# print(f"right[0] 的 i 值: {right[0].__closure__[0].cell_contents}")  # ____
## 正确方式：通过 __defaults__ 查看
print(f"rigth[0] 的 i 值:{right[0].__defaults__[0]}")  # # right：i 是默认参数 → __closure__ 为 None   right[0] 没有闭包（i 是默认参数，不是闭包变量）

print()

# ----- 题8: 递归调用栈 [必做] -----
# 知识点: 递归函数每次调用都会创建新的栈帧
# sys.getrecursionlimit() 返回最大递归深度

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"递归深度限制: {sys.getrecursionlimit()}")
print(f"factorial(5): {factorial(5)}")  # ____

# 使用 sys.setrecursionlimit() 可以修改递归深度限制
# 但不建议设置过大，可能导致栈溢出

print()

# ----- 题9: lambda 函数的 __code__ [必做] -----
# 知识点: lambda 也是函数对象，拥有 __code__、__closure__ 等属性
# 预测以下代码的输出结果

square = lambda x: x ** 2
add = lambda a, b: a + b

print(f"square.__name__: {square.__name__}")       # ____square
print(f"square.__code__.co_varnames: {square.__code__.co_varnames}")  # ____x
print(f"add.__code__.co_argcount: {add.__code__.co_argcount}")       # ____2 这是参数个数

print()

# ----- 题10: map/filter/reduce 的惰性求值 [必做] -----
# 知识点: map 和 filter 返回迭代器（惰性），reduce 直接返回结果
# 预测以下代码的输出结果

nums = [1, 2, 3, 4, 5]

m = map(lambda x: x * 2, nums)
f = filter(lambda x: x > 3, nums)

print(f"map 类型: {type(m)}")       # ____map
print(f"filter 类型: {type(f)}")    # ____filter

# 迭代器只能遍历一次
print(f"map 结果: {list(m)}")       # ____[2,4,6,8,10]
print(f"再次 list(m): {list(m)}")   # ____[] (迭代器已耗尽)

print()

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题11: 闭包 vs 类的对比 [选做] -----
# 知识点: 闭包可以实现类似"类"的状态保持
# 预测以下代码的输出结果

# 方式1: 用闭包实现
def make_stack():
    items = []
    def push(item):
        items.append(item)
    def pop():
        return items.pop()
    def size():
        return len(items)
    return push, pop, size

push, pop, size = make_stack()
push(1)
push(2)
push(3)
print(f"pop: {pop()}")       # ____3
print(f"size: {size()}")     # ____2

print()

# ----- 题12: 嵌套作用域中的变量遮蔽 [选做] -----
# 知识点: 内层变量可以遮蔽外层变量，但不会修改外层变量
# 预测以下代码的输出结果

x = 100

def outer():
    x = 200
    def inner():
        x = 300  # 遮蔽，不是修改
        print(f"inner x: {x}")
    inner()
    print(f"outer x: {x}")

outer()
print(f"global x: {x}")
# ____300
# ____200
# ____100

print()

# ----- 题13: 函数作为一等公民 - __code__ 比较 [选做] -----
# 知识点: 函数对象可以被赋值、传递、比较
# __code__ 对象可以用来判断两个函数是否等价

def func_a(x):
    return x + 1

def func_b(x):
    return x + 1

func_c = func_a

print(f"func_a is func_b: {func_a is func_b}")           # ____
print(f"func_a is func_c: {func_a is func_c}")           # ____
print(f"func_a.__code__ is func_b.__code__: {func_a.__code__ is func_b.__code__}")  # ____

print()

# ----- 题14: 闭包中的变量是 cell 对象，不是值 [选做] -----
# 知识点: 修改外层变量后，所有引用该 cell 的闭包都会看到新值
# 预测以下代码的输出结果

def make_funcs():
    val = 10
    def get_val():
        return val
    def set_val(new_val):
        nonlocal val
        val = new_val
    return get_val, set_val

get, set = make_funcs()
print(f"初始: {get()}")  # ____

set(20)
print(f"set(20)后: {get()}")  # ____

# 验证 cell 对象
print(f"cell_contents: {get.__closure__[0].cell_contents}")  # ____

set(30)
print(f"cell_contents 变化: {get.__closure__[0].cell_contents}")  # ____

print()

# ----- 题15: 综合应用 - 装饰器的底层原理 [选做] -----
# 知识点: 装饰器 = 高阶函数 + 闭包
# 预测以下代码的输出结果

def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} 耗时: {end - start:.6f}s")
        return result
    return wrapper

@timer_decorator
def slow_sum(n):
    return sum(range(n))

result = slow_sum(1000000)
print(f"结果: {result}")
# ____
# ____

# 验证：wrapper 的闭包中捕获了 func
print(f"wrapper 的闭包: {slow_sum.__closure__}")
print(f"捕获的函数: {slow_sum.__closure__[0].cell_contents.__name__}")  # ____

print()

# ----- 题16: 调试修复 - 找出以下代码中的 2 个 BUG [选做] -----
# 修复以下代码，使其能正确运行

# BUG 1: nonlocal 使用错误 - 变量未在外层函数中定义
def outer():
    x = 0
    def inner():
        nonlocal x  # BUG: x 未在 outer 中定义
        x = 10
    inner()

# BUG 2: 闭包中修改可变对象不需要 nonlocal，但修改绑定需要
def make_list_manager():
    items = []
    def add_item(item):
        items.append(item)  # 这行没问题
    def clear_items():
        items = []  # BUG: 这是重新赋值，不是修改
    return add_item, clear_items

add, clear = make_list_manager()
add(1)
add(2)
clear()
print(f"items: {add.__closure__[0].cell_contents}")  # 预期: []
