"""
Day08 练习2 - 面向对象编程的底层原理（答案版）
"""

import sys

# ----- 题1: type 和 object 的关系 -----
class MyClass:
    pass

obj = MyClass()

print(f"type(MyClass): {type(MyClass)}")   # ✅ 答案: <class 'type'>
print(f"type(obj): {type(obj)}")           # ✅ 答案: <class 'MyClass'>
print(f"isinstance(MyClass, type): {isinstance(MyClass, type)}")  # ✅ 答案: True
print(f"isinstance(obj, object): {isinstance(obj, object)}")      # ✅ 答案: True
print(f"type is object: {type is object}")  # ✅ 答案: False
print(f"type(type): {type(type)}")         # ✅ 答案: <class 'type'>

print()

# ----- 题2: __new__ 和 __init__ 的调用顺序 -----
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
# ✅ 答案:
# 1. __new__ 被调用
#    创建了实例: xxx
# 2. __init__ 被调用
#    self 的 id: xxx（与 __new__ 返回的相同）

print()

# ----- 题3: __new__ 不返回 cls 实例时 -----
class Weird:
    def __new__(cls):
        print("__new__ 执行")
        return "不是 Weird 的实例"

    def __init__(self):
        print("__init__ 执行")
        self.x = 10

w = Weird()
print(f"type(w): {type(w)}")  # ✅ 答案: <class 'str'>
print(f"w: {w}")              # ✅ 答案: 不是 Weird 的实例
# ✅ 答案: __init__ 没有执行

print()

# ----- 题4: 实例属性存储在 __dict__ 中 -----
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(f"__dict__: {p.__dict__}")  # ✅ 答案: {'name': 'Alice', 'age': 25}
print(f"p.name 通过 __dict__: {p.__dict__['name']}")  # ✅ 答案: Alice

p.email = "alice@example.com"
print(f"__dict__ 更新后: {p.__dict__}")  # ✅ 答案: {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}

print()

# ----- 题5: 类属性 vs 实例属性的存储位置 -----
class Dog:
    species = "犬科"

    def __init__(self, name):
        self.name = name

d = Dog("旺财")

print(f"Dog.__dict__['species']: {Dog.__dict__['species']}")   # ✅ 答案: 犬科
print(f"d.__dict__: {d.__dict__}")                              # ✅ 答案: {'name': '旺财'}
print(f"'species' in d.__dict__: {'species' in d.__dict__}")    # ✅ 答案: False
print(f"'name' in d.__dict__: {'name' in d.__dict__}")          # ✅ 答案: True

print()

# ----- 题6: 属性查找顺序 -----
class Verbose:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        print(f"__getattr__ 被调用: {attr}")
        raise AttributeError(f"'{type(self).__name__}' 没有属性 '{attr}'")

v = Verbose("test")
print(f"v.name = {v.name}")  # ✅ 答案: test（直接从 __dict__ 获取）

try:
    v.unknown
except AttributeError as e:
    print(f"错误: {e}")  # ✅ 答案: __getattr__ 被调用: unknown

print()

# ----- 题7: __slots__ 的内存优化原理 -----
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

print(f"WithDict 有 __dict__: {hasattr(d, '__dict__')}")   # ✅ 答案: True
print(f"WithSlots 有 __dict__: {hasattr(s, '__dict__')}")  # ✅ 答案: False

try:
    s.z = 3
except AttributeError as e:
    print(f"错误: {e}")  # ✅ 答案: 'WithSlots' object has no attribute 'z'

print()

# ----- 题8: __del__ 的调用时机 -----
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"[创建] {self.name}")

    def __del__(self):
        print(f"[销毁] {self.name}")

print("--- 开始 ---")
r1 = Resource("资源1")    # [创建] 资源1
r2 = r1
print(f"r1 引用计数: {sys.getrefcount(r1)}")  # ✅ 答案: 3

print("--- del r1 ---")
del r1  # 不会销毁，r2 还在引用
print("--- del r2 ---")
del r2  # 引用计数归零，调用 __del__
print("--- 结束 ---")
# ✅ 答案:
# --- 开始 ---
# [创建] 资源1
# r1 引用计数: 3
# --- del r1 ---
# --- del r2 ---
# [销毁] 资源1
# --- 结束 ---

print()

# ----- 题9: 类方法和静态方法的 C 实现 -----
class Test:
    class_var = "I am class var"

    @classmethod
    def class_method(cls):
        return f"cls is {cls.__name__}"

    @staticmethod
    def static_method():
        return "no self, no cls"

print(Test.class_method())          # ✅ 答案: cls is Test
print(Test().class_method())        # ✅ 答案: cls is Test
print(Test.static_method())         # ✅ 答案: no self, no cls
print(Test().static_method())       # ✅ 答案: no self, no cls

print(f"type(Test.class_method): {type(Test.__dict__['class_method'])}")   # ✅ 答案: <class 'classmethod'>
print(f"type(Test.static_method): {type(Test.__dict__['static_method'])}") # ✅ 答案: <class 'staticmethod'>

print()

# ----- 题10: 实例方法的绑定 -----
class Calculator:
    def add(self, a, b):
        return a + b

c = Calculator()

print(f"type(Calculator.add): {type(Calculator.add)}")  # ✅ 答案: <class 'function'>
print(f"type(c.add): {type(c.add)}")  # ✅ 答案: <class 'method'>

print(f"c.add.__self__: {c.add.__self__}")  # ✅ 答案: <__main__.Calculator object at ...>
print(f"c.add.__self__ is c: {c.add.__self__ is c}")  # ✅ 答案: True

print()

# ----- 题11: 元类 -----
class MyClass:
    x = 10

obj1 = MyClass()
obj2 = MyClass.__new__(MyClass)
MyClass.__init__(obj2)

print(f"obj1.x: {obj1.x}")  # ✅ 答案: 10
print(f"obj2.x: {obj2.x}")  # ✅ 答案: 10

DynamicClass = type('DynamicClass', (object,), {'x': 42})
print(f"DynamicClass.x: {DynamicClass.x}")  # ✅ 答案: 42
print(f"type(DynamicClass): {type(DynamicClass)}")  # ✅ 答案: <class 'type'>

print()

# ----- 题12: MRO -----
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
print(f"D 的 MRO: {[cls.__name__ for cls in D.__mro__]}")  # ✅ 答案: ['D', 'B', 'C', 'A', 'object']
print(f"d.who(): {d.who()}")  # ✅ 答案: B

print()

# ----- 题13: __repr__ 和 __str__ -----
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))    # ✅ 答案: Point(3, 4)
print(str(p))     # ✅ 答案: (3, 4)
print(p)          # ✅ 答案: (3, 4)

class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2({self.x}, {self.y})"

p2 = Point2(3, 4)
print(str(p2))    # ✅ 答案: Point2(3, 4)（回退到 __repr__）

print()

# ----- 题14: 继承中的 __init__ 调用链 -----
class Animal:
    def __init__(self, name):
        print(f"Animal.__init__({name})")
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        print(f"Dog.__init__({name}, {breed})")
        super().__init__(name)
        self.breed = breed

d = Dog("旺财", "金毛")
print(f"name: {d.name}, breed: {d.breed}")
# ✅ 答案:
# Dog.__init__(旺财, 金毛)
# Animal.__init__(旺财)
# name: 旺财, breed: 金毛

class Cat(Animal):
    def __init__(self, color):
        print(f"Cat.__init__({color})")
        self.color = color

c = Cat("白色")
try:
    print(c.name)
except AttributeError as e:
    print(f"错误: {e}")  # ✅ 答案: 'Cat' object has no attribute 'name'

print()

# ----- 题15: __contains__、__iter__、__len__ 协议 -----
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
print(f"3 in bag: {3 in bag}")       # ✅ 答案: True
print(f"len(bag): {len(bag)}")       # ✅ 答案: 5
print(f"list(bag): {list(bag)}")     # ✅ 答案: [1, 2, 3, 4, 5]
print(f"sum(bag): {sum(bag)}")       # ✅ 答案: 15

print()

# ----- 题16: 综合应用 - 不可变类 -----
class ImmutablePoint:
    __slots__ = ('_x', '_y')

    def __new__(cls, x, y):
        instance = super().__new__(cls)
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
print(f"p = {p}")          # ✅ 答案: ImmutablePoint(3, 4)
print(f"p.x = {p.x}")      # ✅ 答案: 3

try:
    p.x = 10
except AttributeError as e:
    print(f"修改失败: {e}")  # ✅ 答案: ImmutablePoint 不可修改

print()

# ----- 题17: 调试修复 -----
# BUG 1 修复: __init__ 不能有返回值
class BadInit:
    def __init__(self, value):
        self.value = value
        # 去掉 return value

# BUG 2 修复: __new__ 必须返回实例
class BadNew:
    def __new__(cls):
        print("创建实例")
        return super().__new__(cls)  # 添加 return

# BUG 3 修复: 子类 __del__ 应该调用父类 __del__
class Parent:
    def __del__(self):
        print("Parent.__del__")

class Child(Parent):
    def __del__(self):
        print("Child.__del__")
        super().__del__()  # 添加 super().__del__()
