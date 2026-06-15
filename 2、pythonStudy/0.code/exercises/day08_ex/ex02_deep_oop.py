"""
Day08 练习2 - 面向对象编程的底层原理
基于 CPython 源码深入理解类、实例、__new__/__init__、__slots__、描述符

参考源码: python3.13.13/Objects/typeobject.c   (type_new, slot_tp_new, slot_tp_init)
         python3.13.13/Doc/reference/datamodel.rst (__new__, __init__, __del__ 文档)
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

# ----- 题1: type 和 object 的关系 [必做] -----
# 知识点: 所有类都是 type 的实例，所有类都继承自 object
# 参考: typeobject.c 中 type_new 函数创建类
# 预测以下代码的输出结果

class MyClass:
    pass

obj = MyClass()

print(f"type(MyClass): {type(MyClass)}")   # ____
print(f"type(obj): {type(obj)}")           # ____
print(f"isinstance(MyClass, type): {isinstance(MyClass, type)}")  # ____
print(f"isinstance(obj, object): {isinstance(obj, object)}")      # ____
print(f"type is object: {type is object}")  # ____
print(f"type(type): {type(type)}")         # ____

print()

# ----- 题2: __new__ 和 __init__ 的调用顺序 [必做] -----
# 知识点: __new__ 创建实例，__init__ 初始化实例
# 参考: typeobject.c:1978-1996
#   obj = type->tp_new(type, args, kwds);  // 先调用 __new__
#   if (type->tp_init != NULL) {
#       int res = type->tp_init(obj, args, kwds);  // 再调用 __init__
#   }
# 预测以下代码的输出顺序

class Demo:
    def __new__(cls, *args, **kwargs):
        print("1. __new__ 被调用")
        instance = super().__new__(cls)
        print(f"   创建了实例: {id(instance)}")
        return instance

    def __init__(self, value):
        print("2. __init__ 被调用")
        self.value = value
        print(f"   self 的 id: {id(self)}")

d = Demo(42)
# ____
# ____
# ____
# ____

print()

# ----- 题3: __new__ 不返回 cls 实例时 __init__ 不会被调用 [必做] -----
# 知识点: 如果 __new__ 返回的不是 cls 的实例，__init__ 不会执行
# 参考: datamodel.rst:1883
#   "If __new__ does not return an instance of cls, then the new instance's
#    __init__ method will not be invoked."
# 预测以下代码的输出结果

class Weird:
    def __new__(cls):
        print("__new__ 执行")
        return "不是 Weird 的实例"  # 返回字符串

    def __init__(self):
        print("__init__ 执行")  # 会执行吗？
        self.x = 10

w = Weird()
print(f"type(w): {type(w)}")  # ____
print(f"w: {w}")              # ____
# ____

print()

# ----- 题4: 实例属性存储在 __dict__ 中 [必做] -----
# 知识点: 实例属性存储在实例的 __dict__ 字典中
# 预测以下代码的输出结果

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(f"__dict__: {p.__dict__}")  # ____
print(f"p.name 通过 __dict__: {p.__dict__['name']}")  # ____

# 动态添加属性
p.email = "alice@example.com"
print(f"__dict__ 更新后: {p.__dict__}")  # ____

print()

# ----- 题5: 类属性 vs 实例属性的存储位置 [必做] -----
# 知识点: 类属性存储在 类.__dict__ 中，实例属性存储在 实例.__dict__ 中
# 预测以下代码的输出结果

class Dog:
    species = "犬科"  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性

d = Dog("旺财")

print(f"Dog.__dict__['species']: {Dog.__dict__['species']}")   # ____
print(f"d.__dict__: {d.__dict__}")                              # ____
print(f"'species' in d.__dict__: {'species' in d.__dict__}")    # ____
print(f"'name' in d.__dict__: {'name' in d.__dict__}")          # ____

print()

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题6: 属性查找顺序 - 描述符协议 [必做] -----
# 知识点: 属性查找顺序: 数据描述符 > 实例__dict__ > 非数据描述符 > 类__dict__
# 预测以下代码的输出结果

class Verbose:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        print(f"__getattr__ 被调用: {attr}")
        raise AttributeError(f"'{type(self).__name__}' 没有属性 '{attr}'")

v = Verbose("test")
v.name  # 直接从 __dict__ 获取，不会调用 __getattr__
print(f"v.name = {v.name}")  # ____

# 不存在的属性会触发 __getattr__
try:
    v.unknown
except AttributeError as e:
    print(f"错误: {e}")  # ____

print()

# ----- 题7: __slots__ 的内存优化原理 [必做] -----
# 知识点: __slots__ 用描述符替代 __dict__，节省内存
# 参考: typeobject.c:3628 (type_new_slots_impl)
# 预测以下代码的输出结果

class WithDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

d = WithDict(1, 2)
s = WithSlots(1, 2)

print(f"WithDict 有 __dict__: {hasattr(d, '__dict__')}")   # ____
print(f"WithSlots 有 __dict__: {hasattr(s, '__dict__')}")  # ____
print(f"WithDict.__dict__ 大小: {sys.getsizeof(d.__dict__)}")

# WithSlots 不能动态添加属性
try:
    s.z = 3
except AttributeError as e:
    print(f"错误: {e}")  # ____

print()

# ----- 题8: __del__ 的调用时机 - 引用计数 [必做] -----
# 知识点: __del__ 在引用计数归零时调用
# 参考: datamodel.rst:1935
#   "del x doesn't directly call x.__del__() --- the former decrements
#    the reference count for x by one, and the latter is only called when
#    x's reference count reaches zero."
# 预测以下代码的输出顺序

class Resource:
    def __init__(self, name):
        self.name = name
        print(f"[创建] {self.name}")

    def __del__(self):
        print(f"[销毁] {self.name}")

print("--- 开始 ---")
r1 = Resource("资源1")
r2 = r1  # r2 也引用同一个对象
print(f"r1 引用计数: {sys.getrefcount(r1)}")  # ____

print("--- del r1 ---")
del r1  # 引用计数 -1，但 r2 还在引用，不会销毁
print("--- del r2 ---")
del r2  # 引用计数归零，__del__ 被调用
print("--- 结束 ---")
# ____
# ____
# ____
# ____
# ____
# ____
# ____

print()

# ----- 题9: 类方法和静态方法的 C 实现 [必做] -----
# 知识点: @classmethod 和 @staticmethod 是描述符
# 参考: typeobject.c:10265 (FLSLOT 宏注册 __init__)
# 参考: funcobject.h 中 PyClassMethod_Type 和 PyStaticMethod_Type
# 预测以下代码的输出结果

class Test:
    class_var = "I am class var"

    @classmethod
    def class_method(cls):
        return f"cls is {cls.__name__}"

    @staticmethod
    def static_method():
        return "no self, no cls"

# 类方法可以通过类和实例调用
print(Test.class_method())          # ____
print(Test().class_method())        # ____

# 静态方法也可以通过类和实例调用
print(Test.static_method())         # ____
print(Test().static_method())       # ____

# 查看类型
print(f"type(Test.class_method): {type(Test.__dict__['class_method'])}")   # ____
print(f"type(Test.static_method): {type(Test.__dict__['static_method'])}") # ____

print()

# ----- 题10: 实例方法的绑定 [必做] -----
# 知识点: 通过实例访问方法时，方法会被"绑定"（bound method）
# 预测以下代码的输出结果

class Calculator:
    def add(self, a, b):
        return a + b

c = Calculator()

# 类上的方法是普通函数
print(f"type(Calculator.add): {type(Calculator.add)}")  # ____

# 实例上的方法是绑定方法
print(f"type(c.add): {type(c.add)}")  # ____

# 绑定方法的 __self__ 属性
print(f"c.add.__self__: {c.add.__self__}")  # ____
print(f"c.add.__self__ is c: {c.add.__self__ is c}")  # ____

print()

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题11: 元类 - type 是所有类的元类 [选做] -----
# 知识点: type 不仅是类型，还是元类（metaclass）
# 预测以下代码的输出结果

class MyClass:
    x = 10

# 以下两种方式等价
obj1 = MyClass()
obj2 = MyClass.__new__(MyClass)
MyClass.__init__(obj2)

print(f"obj1.x: {obj1.x}")  # ____
print(f"obj2.x: {obj2.x}")  # ____

# type() 动态创建类
DynamicClass = type('DynamicClass', (object,), {'x': 42})
print(f"DynamicClass.x: {DynamicClass.x}")  # ____
print(f"type(DynamicClass): {type(DynamicClass)}")  # ____

print()

# ----- 题12: MRO（方法解析顺序） [选做] -----
# 知识点: Python 使用 C3 线性化算法确定方法解析顺序
# 预测以下代码的输出结果

class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(A):
    def who(self):
        return "C"

class D(B, C):
    pass

d = D()
print(f"D 的 MRO: {[cls.__name__ for cls in D.__mro__]}")  # ____
print(f"d.who(): {d.who()}")  # ____

print()

# ----- 题13: __repr__ 和 __str__ 的区别 [选做] -----
# 知识点: __repr__ 面向开发者，__str__ 面向用户
# __repr__ 是 __str__ 的后备

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))    # ____
print(str(p))     # ____
print(p)          # ____ (print 调用 __str__)

# 没有 __str__ 时，回退到 __repr__
class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2({self.x}, {self.y})"

p2 = Point2(3, 4)
print(str(p2))    # ____ (调用了哪个？)

print()

# ----- 题14: 继承中的 __init__ 调用链 [选做] -----
# 知识点: 子类 __init__ 必须显式调用父类 __init__
# 预测以下代码的输出结果

class Animal:
    def __init__(self, name):
        print(f"Animal.__init__({name})")
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        print(f"Dog.__init__({name}, {breed})")
        super().__init__(name)  # 必须显式调用
        self.breed = breed

d = Dog("旺财", "金毛")
print(f"name: {d.name}, breed: {d.breed}")
# ____
# ____

# 如果不调用 super().__init__ 会怎样？
class Cat(Animal):
    def __init__(self, color):
        print(f"Cat.__init__({color})")
        # 没有调用 super().__init__()！
        self.color = color

c = Cat("白色")
try:
    print(c.name)
except AttributeError as e:
    print(f"错误: {e}")  # ____

print()

# ----- 题15: __contains__、__iter__、__len__ 协议 [选做] -----
# 知识点: Python 的 dunder 方法实现了各种协议

class Bag:
    def __init__(self, *items):
        self._items = list(items)

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

bag = Bag(1, 2, 3, 4, 5)
print(f"3 in bag: {3 in bag}")       # ____
print(f"len(bag): {len(bag)}")       # ____
print(f"list(bag): {list(bag)}")     # ____
print(f"sum(bag): {sum(bag)}")       # ____

print()

# ----- 题16: 综合应用 - 实现一个不可变类 [选做] -----
# 知识点: 综合运用 __slots__、__new__、__init__、__setattr__
# 要求: 实现一个不可变的 Point 类

class ImmutablePoint:
    __slots__ = ('_x', '_y')

    def __new__(cls, x, y):
        instance = super().__new__(cls)
        # 在 __new__ 中直接设置属性（绕过 __setattr__）
        object.__setattr__(instance, '_x', x)
        object.__setattr__(instance, '_y', y)
        return instance

    def __setattr__(self, name, value):
        raise AttributeError("ImmutablePoint 不可修改")

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return f"ImmutablePoint({self.x}, {self.y})"

p = ImmutablePoint(3, 4)
print(f"p = {p}")          # ____
print(f"p.x = {p.x}")      # ____

try:
    p.x = 10
except AttributeError as e:
    print(f"修改失败: {e}")  # ____

print()

# ----- 题17: 调试修复 - 找出以下代码中的 3 个 BUG [选做] -----
# 修复以下代码，使其能正确运行

# BUG 1: __init__ 有返回值
class BadInit:
    def __init__(self, value):
        self.value = value
        return value  # 错误: __init__ 不能有返回值

# BUG 2: __new__ 必须返回实例
class BadNew:
    def __new__(cls):
        print("创建实例")  # 忘记 return super().__new__(cls)

# BUG 3: 子类 __del__ 没有调用父类 __del__
class Parent:
    def __del__(self):
        print("Parent.__del__")

class Child(Parent):
    def __del__(self):
        print("Child.__del__")  # 应该调用 super().__del__()
