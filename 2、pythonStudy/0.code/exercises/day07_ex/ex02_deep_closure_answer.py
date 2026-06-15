"""
Day07 练习2 - 闭包与作用域的底层原理（答案版）
"""

import sys

# ----- 题1: __closure__ 与 cell 对象 -----
def outer(x):
    def inner():
        return x
    return inner

fn = outer(42)
print(f"__closure__: {fn.__closure__}")                    # ✅ 答案: (<cell at ...: int object at ...>,)
print(f"cell 类型: {type(fn.__closure__[0])}")             # ✅ 答案: <class 'cell'>
print(f"cell_contents: {fn.__closure__[0].cell_contents}") # ✅ 答案: 42
print(f"__code__.co_freevars: {fn.__code__.co_freevars}")  # ✅ 答案: ('x',)

print()

# ----- 题2: cell 对象是可变的 -----
def make_counter(start=0):
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter(0)
print(f"初始 cell_contents: {c.__closure__[0].cell_contents}")  # ✅ 答案: 0
print(f"调用1: {c()}")  # ✅ 答案: 1
print(f"调用2: {c()}")  # ✅ 答案: 2

c.__closure__[0].cell_contents = 100
print(f"修改后调用: {c()}")  # ✅ 答案: 101

print()

# ----- 题3: co_freevars 与 co_cellvars -----
def outer():
    x = 10
    y = 20
    def inner():
        return x
    return inner

fn = outer()
print(f"outer 的 co_cellvars: {outer.__code__.co_cellvars}")   # ✅ 答案: ('x',)
print(f"inner 的 co_freevars: {fn.__code__.co_freevars}")     # ✅ 答案: ('x',)

print()

# ----- 题4: 作用域查找顺序 - LEGB -----
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
# ✅ 答案:
# inner: local
# outer: enclosing
# global: global

print()

# ----- 题5: global 与 nonlocal 的本质 -----
g_var = 0

def test_scopes():
    enclosing_var = 10
    def inner():
        global g_var
        nonlocal enclosing_var
        g_var = 100
        enclosing_var = 20
    inner()
    print(f"enclosing_var: {enclosing_var}")  # ✅ 答案: 20
    print(f"g_var: {g_var}")                  # ✅ 答案: 100

test_scopes()
print(f"全局 g_var: {g_var}")  # ✅ 答案: 100

print()

# ----- 题6: 多个闭包共享同一个 cell 对象 -----
def make_getter_setter():
    value = 0
    def getter():
        return value
    def setter(new_val):
        nonlocal value
        value = new_val
    return getter, setter

getter, setter = make_getter_setter()

print(f"getter cell: {getter.__closure__[0]}")
print(f"setter cell: {setter.__closure__[0]}")
print(f"同一 cell: {getter.__closure__[0] is setter.__closure__[0]}")  # ✅ 答案: True

setter(42)
print(f"getter(): {getter()}")  # ✅ 答案: 42

print()

# ----- 题7: 闭包延迟绑定陷阱 -----
def make_multipliers_wrong():
    return [lambda x: x * i for i in range(5)]

def make_multipliers_right():
    return [lambda x, i=i: x * i for i in range(5)]

wrong = make_multipliers_wrong()
right = make_multipliers_right()

print(f"wrong[2](2): {wrong[2](2)}")  # ✅ 答案: 8（i 最终是 4，所以 2*4=8）
print(f"right[2](2): {right[2](2)}")  # ✅ 答案: 4（i=i 捕获了当前值）

print(f"wrong[0] 的 i 值: {wrong[0].__closure__[0].cell_contents}")  # ✅ 答案: 4
print(f"right[0] 的 i 值: {right[0].__closure__[0].cell_contents}")  # ✅ 答案: 0

print()

# ----- 题8: 递归调用栈 -----
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"递归深度限制: {sys.getrecursionlimit()}")
print(f"factorial(5): {factorial(5)}")  # ✅ 答案: 120

print()

# ----- 题9: lambda 函数的 __code__ -----
square = lambda x: x ** 2
add = lambda a, b: a + b

print(f"square.__name__: {square.__name__}")       # ✅ 答案: <lambda>
print(f"square.__code__.co_varnames: {square.__code__.co_varnames}")  # ✅ 答案: ('x',)
print(f"add.__code__.co_argcount: {add.__code__.co_argcount}")       # ✅ 答案: 2

print()

# ----- 题10: map/filter/reduce 的惰性求值 -----
nums = [1, 2, 3, 4, 5]

m = map(lambda x: x * 2, nums)
f = filter(lambda x: x > 3, nums)

print(f"map 类型: {type(m)}")       # ✅ 答案: <class 'map'>
print(f"filter 类型: {type(f)}")    # ✅ 答案: <class 'filter'>

print(f"map 结果: {list(m)}")       # ✅ 答案: [2, 4, 6, 8, 10]
print(f"再次 list(m): {list(m)}")   # ✅ 答案: []（迭代器已耗尽）

print()

# ----- 题11: 闭包 vs 类的对比 -----
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
print(f"pop: {pop()}")       # ✅ 答案: 3
print(f"size: {size()}")     # ✅ 答案: 2

print()

# ----- 题12: 嵌套作用域中的变量遮蔽 -----
x = 100

def outer():
    x = 200
    def inner():
        x = 300
        print(f"inner x: {x}")
    inner()
    print(f"outer x: {x}")

outer()
print(f"global x: {x}")
# ✅ 答案:
# inner x: 300
# outer x: 200
# global x: 100

print()

# ----- 题13: 函数作为一等公民 -----
def func_a(x):
    return x + 1

def func_b(x):
    return x + 1

func_c = func_a

print(f"func_a is func_b: {func_a is func_b}")           # ✅ 答案: False
print(f"func_a is func_c: {func_a is func_c}")           # ✅ 答案: True
print(f"func_a.__code__ is func_b.__code__: {func_a.__code__ is func_b.__code__}")  # ✅ 答案: False

print()

# ----- 题14: 闭包中的变量是 cell 对象 -----
def make_funcs():
    val = 10
    def get_val():
        return val
    def set_val(new_val):
        nonlocal val
        val = new_val
    return get_val, set_val

get, set = make_funcs()
print(f"初始: {get()}")  # ✅ 答案: 10

set(20)
print(f"set(20)后: {get()}")  # ✅ 答案: 20

print(f"cell_contents: {get.__closure__[0].cell_contents}")  # ✅ 答案: 20

set(30)
print(f"cell_contents 变化: {get.__closure__[0].cell_contents}")  # ✅ 答案: 30

print()

# ----- 题15: 综合应用 - 装饰器的底层原理 -----
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
# ✅ 答案:
# slow_sum 耗时: 0.xxxxxxs
# 结果: 499999500000

print(f"捕获的函数: {slow_sum.__closure__[0].cell_contents.__name__}")  # ✅ 答案: slow_sum

print()

# ----- 题16: 调试修复 -----
# BUG 1 修复: x 应该在 outer 中定义
def outer():
    x = 0  # 添加定义
    def inner():
        nonlocal x
        x = 10
    inner()

# BUG 2 修复: 需要 nonlocal 或修改 cell_contents
def make_list_manager():
    items = []
    def add_item(item):
        items.append(item)
    def clear_items():
        nonlocal items  # 添加 nonlocal
        items.clear()   # 或者用 items.clear() 修改而不是重新赋值
    return add_item, clear_items

add, clear = make_list_manager()
add(1)
add(2)
clear()
print(f"items: {add.__closure__[0].cell_contents}")  # 预期: []
