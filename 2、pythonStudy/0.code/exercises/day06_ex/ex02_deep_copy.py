"""
Day06 练习2 - 函数参数与拷贝的底层原理
基于 CPython 源码深入理解参数传递、引用计数、浅拷贝/深拷贝的实现

参考源码: python3.13.13/Objects/funcobject.h   (PyFunctionObject 结构体)
         python3.13.13/Objects/listobject.c     (list_slice_lock_held 浅拷贝实现)
         python3.13.13/Lib/copy.py              (copy/deepcopy 实现)
版本: v1.0
最后更新: 2026-06-14
"""

import sys
import copy

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: id() 的本质 - CPython 内存地址 [必做] -----
# 知识点: 在 CPython 中，id(x) 返回对象的内存地址
# 参考: Doc/reference/datamodel.rst:42
#   "For CPython, id(x) is the memory address where x is stored."
# 预测以下代码的输出结果

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}")
print(f"a is b: {a is b}")   # ____true (is 比较的是 id)
print(f"a is c: {a is c}")   # ____flase
print(f"a == c: {a == c}")   # ____ true(== 比较的是值)

print()

# ----- 题2: 可变对象的 id 不变性 [必做] -----
# 知识点: 修改可变对象时，id 不变（原地修改）
# 预测以下代码的输出结果

lst = [1, 2, 3]
print(f"修改前 id = {id(lst)}")

lst.append(4)
print(f"append后 id = {id(lst)}")   # ____我是人，没办法提前预知地址，我能告诉你的是和之前的地址一致
print(f"lst = {lst}")               # ____[1,2,3,4]

lst[0] = 99
print(f"修改后 id = {id(lst)}")     # ____和之前的地址一致

print()

# ----- 题3: 不可变对象的 id 变化 [必做] -----
# 知识点: 修改不可变对象时，会创建新对象（id 变化）
# 预测以下代码的输出结果

s = "hello"
print(f"修改前 id = {id(s)}")

s = s + " world"
print(f"拼接后 id = {id(s)}")   # ____不同 (是否相同？)
print(f"s = {s}")

# 整数小对象缓存（CPython 优化：-5 到 256 的整数被缓存）
a = 256
b = 256
print(f"a is b: {a is b}")     # ____true

c = 257
d = 257
print(f"c is d: {c is d}")     # ____ flase(在交互式环境中通常 False)

print()

# ----- 题4: 引用计数 [必做] -----
# 知识点: CPython 使用引用计数管理对象生命周期
# sys.getrefcount() 返回对象的引用计数（注意：调用时会临时+1）
# 预测以下代码的输出结果

a = [1, 2, 3]
print(f"引用计数(初始): {sys.getrefcount(a)}")   # ___2_ (比预期多1，因为 getrefcount 参数)

b = a  # 增加一个引用
print(f"引用计数(b=a后): {sys.getrefcount(a)}")  # ____3

c = a  # 再增加一个引用
print(f"引用计数(c=a后): {sys.getrefcount(a)}")  # ____4

del b  # 减少一个引用
print(f"引用计数(del b后): {sys.getrefcount(a)}")  # ____3

print()

# ----- 题5: 浅拷贝的 C 实现原理 [必做] -----
# 知识点: list.copy() 底层调用 list_slice_lock_held，只复制指针（Py_NewRef）
# 参考: python3.13.13/Objects/listobject.c:694
#   src = a->ob_item + ilow;
#   dest = np->ob_item;
#   for (i = 0; i < len; i++) {
#       PyObject *v = src[i];
#       dest[i] = Py_NewRef(v);   // 只增加引用计数，不复制对象
#   }
# 预测以下代码的输出结果

original = [1, [2, 3], 4]
shallow = original.copy()

# 验证：容器是新对象
print(f"容器是否相同: {original is shallow}")       # ____flase

# 验证：子对象是共享的（只复制了指针）
print(f"子列表是否相同: {original[1] is shallow[1]}")  # ____true
print(f"整数是否相同: {original[0] is shallow[0]}")    # ____true

print()

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题6: PyFunctionObject 结构体 [必做] -----
# 知识点: Python 函数对象在 C 层的结构
# 参考: python3.13.13/Include/cpython/funcobject.h
#   typedef struct {
#       PyObject_HEAD
#       PyObject *func_globals;    // 全局变量字典
#       PyObject *func_code;       // 代码对象
#       PyObject *func_defaults;   // 默认参数元组
#       PyObject *func_kwdefaults; // 关键字默认参数字典
#       PyObject *func_closure;    // 闭包元组（cell 对象）
#       ...
#   } PyFunctionObject;
# 通过函数的属性观察其内部结构

def my_func(a, b=10, *args, c=20, **kwargs):
    """这是一个测试函数"""
    pass

print(f"__name__: {my_func.__name__}")
print(f"__defaults__: {my_func.__defaults__}")       # ____ (位置默认值)
print(f"__kwdefaults__: {my_func.__kwdefaults__}")   # ____ (关键字默认值)
print(f"__code__.co_varnames: {my_func.__code__.co_varnames}")  # ____
print(f"__code__.co_argcount: {my_func.__code__.co_argcount}")  # ____

print()

# ----- 题7: 函数的 __defaults__ 是可变的 [必做] -----
# 知识点: 修改 __defaults__ 会改变函数的默认参数行为
# 参考: funcobject.h 中 func_defaults 字段

def greet(name, msg="你好"):
    return f"{name}, {msg}"

print(greet("Alice"))              # ____
print(f"__defaults__: {greet.__defaults__}")

# 修改默认值
greet.__defaults__ = ("早上好",)
print(greet("Bob"))                # ____
print(f"__defaults__: {greet.__defaults__}")

print()

# ----- 题8: 深拷贝的递归实现 [必做] -----
# 知识点: copy.deepcopy() 递归复制所有子对象
# 参考: Lib/copy.py 中的 deepcopy 函数
# 预测以下代码中 id 的变化

import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

print(f"original[0] id = {id(original[0])}")
print(f"deep[0] id     = {id(deep[0])}")
print(f"是否相同: {original[0] is deep[0]}")   # ____flase

# 修改深拷贝不影响原对象
deep[0][0] = 999
print(f"original = {original}")  # ____[[1, 2], [3, 4]]
print(f"deep     = {deep}")      # ____[[999, 2], [3, 4]]

print()

# ----- 题9: 参数传递的本质 - 即赋值 [必做] -----
# 知识点: Python 参数传递等价于在函数体内执行了一次赋值操作
# 即 func(x) 等价于在函数体内执行了 x = <传入的对象>
# 预测以下代码的输出结果

def test_assignment(x):
    print(f"函数内: id(x)={id(x)}, x={x}")
    x = [99, 100]  # 重新赋值，x 指向新对象
    print(f"赋值后: id(x)={id(x)}, x={x}")

lst = [1, 2, 3]
print(f"函数外: id(lst)={id(lst)}, lst={lst}")
test_assignment(lst)
print(f"调用后: id(lst)={id(lst)}, lst={lst}")  # ____原本地址，[1, 2, 3]

print()

# ----- 题10: 不定长参数的内部结构 [必做] -----
# 知识点: *args 在 CPython 中被打包为元组，**kwargs 被打包为字典
# 预测以下代码的输出结果

def inspect_args(*args, **kwargs):
    print(f"args 类型: {type(args).__name__}, 值: {args}")
    print(f"kwargs 类型: {type(kwargs).__name__}, 值: {kwargs}")

    # 元组和字典的 id 证明是新创建的对象
    print(f"args id: {id(args)}")

inspect_args(1, 2, 3, name="Alice", age=20)
# ____
# ____

# 验证：每次调用都会创建新的元组对象
t1 = inspect_args(1, 2)
# 再次调用，args 的 id 是否相同？ ____

print()

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题11: 浅拷贝 vs 深拷贝的性能对比 [选做] -----
# 知识点: 浅拷贝只复制指针（O(n)），深拷贝递归复制（O(n*m)）
# 通过 id 验证浅拷贝的子对象共享

import copy
import time

# 创建一个嵌套列表
big_list = [[i] for i in range(10000)]

# 测试浅拷贝速度
start = time.perf_counter()
for _ in range(1000):
    shallow = copy.copy(big_list)
t_shallow = time.perf_counter() - start

# 测试深拷贝速度
start = time.perf_counter()
for _ in range(1000):
    deep = copy.deepcopy(big_list)
t_deep = time.perf_counter() - start

print(f"浅拷贝耗时: {t_shallow:.4f}s")
print(f"深拷贝耗时: {t_deep:.4f}s")
print(f"深拷贝/浅拷贝 = {t_deep/t_shallow:.1f}x")  # ____ (大约多少倍？)

# 验证浅拷贝的子对象共享
print(f"shallow[0] is big_list[0]: {shallow[0] is big_list[0]}")  # ____
print(f"deep[0] is big_list[0]: {deep[0] is big_list[0]}")        # ____

print()

# ----- 题12: __code__ 对象深入 [选做] -----
# 知识点: 函数的代码对象包含编译后的字节码信息
# 预测以下代码的输出结果

def complex_func(a, b, /, c, d=10, *args, e, f=20, **kwargs):
    x = a + b
    return x

code = complex_func.__code__
print(f"co_argcount (位置参数数): {code.co_argcount}")      # ____
print(f"co_posonlyargcount (仅位置参数): {code.co_posonlyargcount}")  # ____
print(f"co_kwonlyargcount (仅关键字参数): {code.co_kwonlyargcount}")  # ____
print(f"co_varnames (所有局部变量): {code.co_varnames}")    # ____

print()

# ----- 题13: 参数解包的内部过程 [选做] -----
# 知识点: * 解包和 ** 解包在 CPython 中的实现
# 预测以下代码能否正常运行

def show(a, b, c):
    print(f"a={a}, b={b}, c={c}")

# 情况1: 元组解包
t = (1, 2, 3)
show(*t)                    # ____1，2，3

# 情况2: 字典解包
d = {"a": 10, "b": 20, "c": 30}
show(**d)                   # ____10，20，30

# 情况3: 混合解包
show(1, *[2], **{"c": 3})  # ____1，2，3

# 情况4: 会报错吗？
# show(*[1, 2, 3, 4])      # ____ (参数个数不匹配)

print()

# ----- 题14: 函数参数的 __annotations__ [选做] -----
# 知识点: 类型注解存储在 __annotations__ 字典中（不影响运行）
# 预测以下代码的输出结果

def annotated_func(a: int, b: str = "hello") -> bool:
    return True

print(f"__annotations__: {annotated_func.__annotations__}")  # ____
print(annotated_func("not_int", 123))  # ____ (类型注解不阻止错误类型)

print()

# ----- 题15: 综合应用 - 引用计数与循环引用 [选做] -----
# 知识点: 循环引用会导致引用计数无法归零，需要 gc 模块处理
# 预测以下代码的输出结果

import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None

a = Node("A")
b = Node("B")
a.ref = b
b.ref = a  # 循环引用: a -> b -> a

print(f"a 引用计数: {sys.getrefcount(a)}")  # ____
print(f"b 引用计数: {sys.getrefcount(b)}")  # ____

del a
del b
# 此时对象并未真正销毁（循环引用），需要 gc
gc.collect()
print("gc.collect() 执行完毕")

print()

# ----- 题16: 调试修复 - 找出以下代码中的 2 个 BUG [选做] -----
# 修复以下代码，使其能正确运行

# BUG 1: 浅拷贝导致嵌套对象被意外修改
import copy

def process_data(data):
    """处理数据，不应该修改原数据"""
    temp = copy.copy(data)  # BUG: 浅拷贝对嵌套列表无效
    temp[0][0] = 999
    return temp

original = [[1, 2], [3, 4]]
result = process_data(original)
print(f"original = {original}")  # 应该是 [[1, 2], [3, 4]]，实际是？

# BUG 2: 引用计数误解
a = [1, 2, 3]
b = a
# 期望：删除 b 后 a 的引用计数回到初始值
del b
print(f"a 引用计数: {sys.getrefcount(a)}")  # 实际值是否符合预期？
# 提示: getrefcount 的参数本身也会增加一次引用
