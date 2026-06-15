"""
Day08 练习1 - 面向对象编程基础
由浅入深掌握类的定义、属性、方法、self、__init__、__slots__

参考源码: day08/P04_Class_Demo.py
         day08/P05_Class.py
         day08/P06_Self.py
         day08/P07_Attribute.py
         day08/P08_Method.py
         day08/P10_Slots.py
版本: v1.0
最后更新: 2026-06-14
"""

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 类的定义与实例化 [必做] -----
# 知识点: 使用 class 关键字定义类，通过类名()创建实例
# 预测以下代码的输出结果

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: 汪汪汪！")

dog1 = Dog("旺财", 3)
dog2 = Dog("小白", 2)

print(dog1.name)   # ____
print(dog2.age)    # ____
dog1.bark()        # ____

print()

# ----- 题2: __init__ 方法 [必做] -----
# 知识点: __init__ 是构造方法，在创建对象时自动调用
# 预测以下代码的输出结果

class Student:
    def __init__(self, name, score=0):
        print(f"正在创建学生: {name}")
        self.name = name
        self.score = score

s1 = Student("张三")
s2 = Student("李四", 95)
print(f"{s1.name}: {s1.score}")  # ____
print(f"{s2.name}: {s2.score}")  # ____

print()

# ----- 题3: self 参数 [必做] -----
# 知识点: self 代表实例对象本身，调用方法时自动传入
# 预测以下代码的输出结果

class Cat:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"我是{self.name}")

    def call_other(self, other):
        print(f"我是{self.name}，我在叫{other.name}")

cat1 = Cat("橘猫")
cat2 = Cat("黑猫")

cat1.introduce()           # ____
cat1.call_other(cat2)      # ____
# Cat.introduce(cat1)      # 等价于 cat1.introduce()，输出？ ____

print()

# ----- 题4: 类属性 vs 实例属性 [必做] -----
# 知识点: 类属性所有实例共享，实例属性每个实例独立
# 预测以下代码的输出结果

class Person:
    species = "人类"  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性

p1 = Person("张三")
p2 = Person("李四")

print(p1.species)    # ____
print(p2.species)    # ____
print(p1.name)       # ____

p1.species = "智人"   # 这是创建实例属性，不是修改类属性
print(p1.species)    # ____
print(p2.species)    # ____
print(Person.species)  # ____

print()

# ----- 题5: 实例方法 [必做] -----
# 知识点: 实例方法第一个参数是 self，只能通过实例调用
# 预测以下代码的输出结果

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value
        return self  # 返回 self 支持链式调用

    def multiply(self, value):
        self.result *= value
        return self

calc = Calculator()
calc.add(5).add(3).multiply(2)
print(f"result = {calc.result}")  # ____

print()

# ----- 题6: 类方法 [必做] -----
# 知识点: @classmethod 装饰器定义类方法，第一个参数是 cls
# 预测以下代码的输出结果

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

a = MyClass()
b = MyClass()
c = MyClass()
print(MyClass.get_count())  # ____

print()

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题7: 静态方法 [必做] -----
# 知识点: @staticmethod 不需要 self 或 cls，只是逻辑上属于类的函数
# 预测以下代码的输出结果

class MathUtil:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathUtil.factorial(n - 1)

print(MathUtil.is_even(4))      # ____
print(MathUtil.is_even(7))      # ____
print(MathUtil.factorial(5))    # ____

print()

# ----- 题8: 实例方法 vs 类方法 vs 静态方法 [必做] -----
# 知识点: 三种方法的调用方式和访问权限不同
# 预测以下代码能否正常运行

class Test:
    class_var = "我是类变量"

    def __init__(self):
        self.instance_var = "我是实例变量"

    def instance_method(self):
        return f"实例方法: {self.instance_var}, {self.class_var}"

    @classmethod
    def class_method(cls):
        return f"类方法: {cls.class_var}"

    @staticmethod
    def static_method():
        return "静态方法: 不访问类或实例变量"

t = Test()
print(t.instance_method())    # ____
print(t.class_method())       # ____
print(Test.class_method())    # ____
print(t.static_method())      # ____
print(Test.static_method())   # ____

print()

# ----- 题9: __slots__ 限制属性 [必做] -----
# 知识点: __slots__ 可以限制实例只能拥有指定的属性，节省内存
# 预测以下代码能否正常运行

class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x)      # ____
print(p.y)      # ____

# p.z = 3       # 这行会报错吗？ ____

print()

# ----- 题10: 设计一个银行账户类 [必做] -----
# 知识点: 综合运用类属性、实例属性、实例方法
# TODO: 实现 BankAccount 类

class BankAccount:
    """银行账户类"""
    bank_name = "Python银行"  # 类属性

    # TODO: 实现 __init__ 方法，初始化 owner（户名）和 balance（余额，默认0）
    def __init__(self, owner, balance=0):
        pass

    # TODO: 实现 deposit 方法，存入金额，打印存入后的余额
    def deposit(self, amount):
        pass

    # TODO: 实现 withdraw 方法，取出金额（余额不足时打印"余额不足"）
    def withdraw(self, amount):
        pass

    # TODO: 实现 get_balance 方法，返回当前余额
    def get_balance(self):
        pass

# 验证
# acc = BankAccount("张三", 1000)
# print(acc.bank_name)     # 预期: Python银行
# acc.deposit(500)          # 预期: 存入500，余额: 1500
# acc.withdraw(200)         # 预期: 取出200，余额: 1300
# acc.withdraw(2000)        # 预期: 余额不足
# print(acc.get_balance())  # 预期: 1300

print()

# ----- 题11: __del__ 方法 [必做] -----
# 知识点: __del__ 在对象被销毁时调用（引用计数为0或程序结束时）
# 预测以下代码的输出顺序

class Temp:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 被创建")

    def __del__(self):
        print(f"{self.name} 被销毁")

print("开始")
t1 = Temp("对象1")
t2 = Temp("对象2")
t1 = None  # 重新赋值后，原来的对象1会被销毁
print("中间")
t2 = None
print("结束")
# ____
# ____
# ____
# ____
# ____
# ____

print()

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题12: 类属性与实例属性的查找顺序 [选做] -----
# 知识点: 属性查找顺序: 实例属性 -> 类属性 -> 父类属性
# 预测以下代码的输出结果

class Animal:
    sound = "..."
    legs = 4

class Bird(Animal):
    sound = "叽叽喳喳"
    legs = 2

class Dog(Animal):
    pass

bird = Bird()
dog = Dog()

print(bird.sound)   # ____
print(bird.legs)    # ____
print(dog.sound)    # ____
print(dog.legs)     # ____

print()

# ----- 题13: 类方法创建实例（工厂模式） [选做] -----
# 知识点: 类方法可以用作工厂方法，以不同方式创建实例
# 预测以下代码的输出结果

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

    def __str__(self):
        return f"{self.year}年{self.month}月{self.day}日"

d1 = Date(2026, 6, 14)
d2 = Date.from_string("2026-12-25")

print(d1)  # ____
print(d2)  # ____
print(type(d1) == type(d2))  # ____

print()

# ----- 题14: self 的本质 [选做] -----
# 知识点: p.method() 等价于 Class.method(p)
# 预测以下代码的输出结果

class Foo:
    def __init__(self, value):
        self.value = value

    def show(self):
        return f"value = {self.value}"

f = Foo(42)
print(f.show())          # ____
print(Foo.show(f))       # ____
print(Foo.show(Foo(99))) # ____

print()

# ----- 题15: 综合应用 - 设计一个学生管理系统 [选做] -----
# 知识点: 综合运用类的所有知识点
# TODO: 实现 StudentManager 类

class StudentManager:
    """学生管理系统"""

    # TODO: 实现 __init__，初始化空的学生列表
    def __init__(self):
        pass

    # TODO: 实现 add_student(name, score)，添加学生到列表
    def add_student(self, name, score):
        pass

    # TODO: 实现 get_average()，返回所有学生的平均分
    def get_average(self):
        pass

    # TODO: 实现 get_top_student()，返回成绩最高的学生名字
    def get_top_student(self):
        pass

    # TODO: 实现 类方法 from_dict_list(dict_list)，从字典列表创建管理器
    # 例如: StudentManager.from_dict_list([{"name": "张三", "score": 85}, ...])
    @classmethod
    def from_dict_list(cls, dict_list):
        pass

# 验证
# sm = StudentManager()
# sm.add_student("张三", 85)
# sm.add_student("李四", 92)
# sm.add_student("王五", 78)
# print(f"平均分: {sm.get_average()}")    # 预期: 85.0
# print(f"最高分: {sm.get_top_student()}")  # 预期: 李四
#
# sm2 = StudentManager.from_dict_list([
#     {"name": "赵六", "score": 90},
#     {"name": "钱七", "score": 88}
# ])
# print(f"平均分: {sm2.get_average()}")   # 预期: 89.0

print()

# ----- 题16: 调试修复 - 找出以下代码中的 3 个 BUG [选做] -----
# 修复以下代码，使其能正确运行

# BUG 1: __init__ 方法有返回值（__init__ 只能返回 None）
class Bad1:
    def __init__(self, name):
        self.name = name
        return self.name  # 错误！

# BUG 2: 实例方法缺少 self 参数
class Bad2:
    def __init__(self):
        self.value = 10

    def show():  # 缺少什么？
        print(self.value)

# BUG 3: 类方法的第一个参数写成了 self 而不是 cls
class Bad3:
    count = 0

    @classmethod
    def increment(self):  # 应该用什么？
        self.count += 1
