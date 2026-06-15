"""
Day06 练习2 - 函数参数与拷贝的底层原理（答案版）
"""

import sys
import copy

# ----- 题1: id() 的本质 -----
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}")
print(f"a is b: {a is b}")   # ✅ 答案: True（同一对象）
print(f"a is c: {a is c}")   # ✅ 答案: False（不同对象）
print(f"a == c: {a == c}")   # ✅ 答案: True（值相等）

print()

# ----- 题2: 可变对象的 id 不变性 -----
lst = [1, 2, 3]
print(f"修改前 id = {id(lst)}")

lst.append(4)
print(f"append后 id = {id(lst)}")   # ✅ 答案: 相同（原地修改）
print(f"lst = {lst}")               # ✅ 答案: [1, 2, 3, 4]

lst[0] = 99
print(f"修改后 id = {id(lst)}")     # ✅ 答案: 相同

print()

# ----- 题3: 不可变对象的 id 变化 -----
s = "hello"
print(f"修改前 id = {id(s)}")

s = s + " world"
print(f"拼接后 id = {id(s)}")   # ✅ 答案: 不同（创建新对象）
print(f"s = {s}")

a = 256
b = 256
print(f"a is b: {a is b}")     # ✅ 答案: True（小整数缓存 -5~256）

c = 257
d = 257
print(f"c is d: {c is d}")     # ✅ 答案: 通常 False（在脚本中可能 True，交互式中 False）

print()

# ----- 题4: 引用计数 -----
a = [1, 2, 3]
print(f"引用计数(初始): {sys.getrefcount(a)}")   # ✅ 答案: 2（a + getrefcount参数）

b = a
print(f"引用计数(b=a后): {sys.getrefcount(a)}")  # ✅ 答案: 3

c = a
print(f"引用计数(c=a后): {sys.getrefcount(a)}")  # ✅ 答案: 4

del b
print(f"引用计数(del b后): {sys.getrefcount(a)}")  # ✅ 答案: 3

print()

# ----- 题5: 浅拷贝的 C 实现原理 -----
original = [1, [2, 3], 4]
shallow = original.copy()

print(f"容器是否相同: {original is shallow}")       # ✅ 答案: False
print(f"子列表是否相同: {original[1] is shallow[1]}")  # ✅ 答案: True
print(f"整数是否相同: {original[0] is shallow[0]}")    # ✅ 答案: True

print()

# ----- 题6: PyFunctionObject 结构体 -----
def my_func(a, b=10, *args, c=20, **kwargs):
    """这是一个测试函数"""
    pass

print(f"__name__: {my_func.__name__}")
print(f"__defaults__: {my_func.__defaults__}")       # ✅ 答案: (10,)
print(f"__kwdefaults__: {my_func.__kwdefaults__}")   # ✅ 答案: {'c': 20}
print(f"__code__.co_varnames: {my_func.__code__.co_varnames}")  # ✅ 答案: ('a', 'b', 'args', 'c', 'kwargs')
print(f"__code__.co_argcount: {my_func.__code__.co_argcount}")  # ✅ 答案: 2

print()

# ----- 题7: 函数的 __defaults__ 是可变的 -----
def greet(name, msg="你好"):
    return f"{name}, {msg}"

print(greet("Alice"))              # ✅ 答案: Alice, 你好
print(f"__defaults__: {greet.__defaults__}")

greet.__defaults__ = ("早上好",)
print(greet("Bob"))                # ✅ 答案: Bob, 早上好

print()

# ----- 题8: 深拷贝的递归实现 -----
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

print(f"original[0] id = {id(original[0])}")
print(f"deep[0] id     = {id(deep[0])}")
print(f"是否相同: {original[0] is deep[0]}")   # ✅ 答案: False

deep[0][0] = 999
print(f"original = {original}")  # ✅ 答案: [[1, 2], [3, 4]]
print(f"deep     = {deep}")      # ✅ 答案: [[999, 2], [3, 4]]

print()

# ----- 题9: 参数传递的本质 -----
def test_assignment(x):
    print(f"函数内: id(x)={id(x)}, x={x}")
    x = [99, 100]
    print(f"赋值后: id(x)={id(x)}, x={x}")

lst = [1, 2, 3]
print(f"函数外: id(lst)={id(lst)}, lst={lst}")
test_assignment(lst)
print(f"调用后: id(lst)={id(lst)}, lst={lst}")  # ✅ 答案: [1, 2, 3]（不受影响）

print()

# ----- 题10: 不定长参数的内部结构 -----
def inspect_args(*args, **kwargs):
    print(f"args 类型: {type(args).__name__}, 值: {args}")
    print(f"kwargs 类型: {type(kwargs).__name__}, 值: {kwargs}")
    print(f"args id: {id(args)}")

inspect_args(1, 2, 3, name="Alice", age=20)
# ✅ 答案:
# args 类型: tuple, 值: (1, 2, 3)
# kwargs 类型: dict, 值: {'name': 'Alice', 'age': 20}

print()

# ----- 题11: 浅拷贝 vs 深拷贝的性能对比 -----
import copy
import time

big_list = [[i] for i in range(10000)]

start = time.perf_counter()
for _ in range(1000):
    shallow = copy.copy(big_list)
t_shallow = time.perf_counter() - start

start = time.perf_counter()
for _ in range(1000):
    deep = copy.deepcopy(big_list)
t_deep = time.perf_counter() - start

print(f"浅拷贝耗时: {t_shallow:.4f}s")
print(f"深拷贝耗时: {t_deep:.4f}s")
print(f"深拷贝/浅拷贝 = {t_deep/t_shallow:.1f}x")  # ✅ 答案: 通常 10-100 倍

print(f"shallow[0] is big_list[0]: {shallow[0] is big_list[0]}")  # ✅ 答案: True
print(f"deep[0] is big_list[0]: {deep[0] is big_list[0]}")        # ✅ 答案: False

print()

# ----- 题12: __code__ 对象深入 -----
def complex_func(a, b, /, c, d=10, *args, e, f=20, **kwargs):
    x = a + b
    return x

code = complex_func.__code__
print(f"co_argcount: {code.co_argcount}")              # ✅ 答案: 4（a, b, c, d）
print(f"co_posonlyargcount: {code.co_posonlyargcount}")  # ✅ 答案: 2（a, b）
print(f"co_kwonlyargcount: {code.co_kwonlyargcount}")    # ✅ 答案: 2（e, f）
print(f"co_varnames: {code.co_varnames}")                # ✅ 答案: ('a', 'b', 'c', 'd', 'e', 'f', 'args', 'kwargs', 'x')

print()

# ----- 题13: 参数解包的内部过程 -----
def show(a, b, c):
    print(f"a={a}, b={b}, c={c}")

t = (1, 2, 3)
show(*t)                    # ✅ 答案: a=1, b=2, c=3

d = {"a": 10, "b": 20, "c": 30}
show(**d)                   # ✅ 答案: a=10, b=20, c=30

show(1, *[2], **{"c": 3})  # ✅ 答案: a=1, b=2, c=3

# show(*[1, 2, 3, 4])      # ✅ 答案: TypeError，参数个数不匹配

print()

# ----- 题14: 函数参数的 __annotations__ -----
def annotated_func(a: int, b: str = "hello") -> bool:
    return True

print(f"__annotations__: {annotated_func.__annotations__}")  # ✅ 答案: {'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'bool'>}
print(annotated_func("not_int", 123))  # ✅ 答案: True（类型注解不阻止错误类型）

print()

# ----- 题15: 引用计数与循环引用 -----
import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None

a = Node("A")
b = Node("B")
a.ref = b
b.ref = a

print(f"a 引用计数: {sys.getrefcount(a)}")  # ✅ 答案: 3（a变量 + b.ref + getrefcount参数）
print(f"b 引用计数: {sys.getrefcount(b)}")  # ✅ 答案: 3

del a
del b
gc.collect()
print("gc.collect() 执行完毕")

print()

# ----- 题16: 调试修复 -----
# BUG 1 修复: 使用 deepcopy
def process_data(data):
    temp = copy.deepcopy(data)  # 修复
    temp[0][0] = 999
    return temp

original = [[1, 2], [3, 4]]
result = process_data(original)
print(f"original = {original}")  # [[1, 2], [3, 4]]

# BUG 2 修复: getrefcount 的参数本身增加一次引用，所以初始值是 2 而非 1
a = [1, 2, 3]
b = a
del b
print(f"a 引用计数: {sys.getrefcount(a)}")  # 2（a变量 + getrefcount参数）
