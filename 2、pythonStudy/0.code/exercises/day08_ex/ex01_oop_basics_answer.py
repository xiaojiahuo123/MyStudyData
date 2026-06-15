"""
Day08 练习1 - 面向对象编程基础（答案版）
"""

# ----- 题1: 类的定义与实例化 -----
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: 汪汪汪！")

dog1 = Dog("旺财", 3)
dog2 = Dog("小白", 2)

print(dog1.name)   # ✅ 答案: 旺财
print(dog2.age)    # ✅ 答案: 2
dog1.bark()        # ✅ 答案: 旺财: 汪汪汪！

print()

# ----- 题2: __init__ 方法 -----
class Student:
    def __init__(self, name, score=0):
        print(f"正在创建学生: {name}")
        self.name = name
        self.score = score

s1 = Student("张三")       # ✅ 答案: 正在创建学生: 张三
s2 = Student("李四", 95)   # ✅ 答案: 正在创建学生: 李四
print(f"{s1.name}: {s1.score}")  # ✅ 答案: 张三: 0
print(f"{s2.name}: {s2.score}")  # ✅ 答案: 李四: 95

print()

# ----- 题3: self 参数 -----
class Cat:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"我是{self.name}")

    def call_other(self, other):
        print(f"我是{self.name}，我在叫{other.name}")

cat1 = Cat("橘猫")
cat2 = Cat("黑猫")

cat1.introduce()           # ✅ 答案: 我是橘猫
cat1.call_other(cat2)      # ✅ 答案: 我是橘猫，我在叫黑猫
Cat.introduce(cat1)        # ✅ 答案: 我是橘猫

print()

# ----- 题4: 类属性 vs 实例属性 -----
class Person:
    species = "人类"

    def __init__(self, name):
        self.name = name

p1 = Person("张三")
p2 = Person("李四")

print(p1.species)      # ✅ 答案: 人类
print(p2.species)      # ✅ 答案: 人类
print(p1.name)         # ✅ 答案: 张三

p1.species = "智人"     # 创建实例属性，不是修改类属性
print(p1.species)      # ✅ 答案: 智人（实例属性）
print(p2.species)      # ✅ 答案: 人类（类属性不变）
print(Person.species)  # ✅ 答案: 人类（类属性不变）

print()

# ----- 题5: 实例方法 -----
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value
        return self

    def multiply(self, value):
        self.result *= value
        return self

calc = Calculator()
calc.add(5).add(3).multiply(2)
print(f"result = {calc.result}")  # ✅ 答案: 16（(0+5+3)*2=16）

print()

# ----- 题6: 类方法 -----
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
print(MyClass.get_count())  # ✅ 答案: 3

print()

# ----- 题7: 静态方法 -----
class MathUtil:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathUtil.factorial(n - 1)

print(MathUtil.is_even(4))      # ✅ 答案: True
print(MathUtil.is_even(7))      # ✅ 答案: False
print(MathUtil.factorial(5))    # ✅ 答案: 120

print()

# ----- 题8: 实例方法 vs 类方法 vs 静态方法 -----
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
print(t.instance_method())    # ✅ 答案: 实例方法: 我是实例变量, 我是类变量
print(t.class_method())       # ✅ 答案: 类方法: 我是类变量
print(Test.class_method())    # ✅ 答案: 类方法: 我是类变量
print(t.static_method())      # ✅ 答案: 静态方法: 不访问类或实例变量
print(Test.static_method())   # ✅ 答案: 静态方法: 不访问类或实例变量

print()

# ----- 题9: __slots__ 限制属性 -----
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x)      # ✅ 答案: 1
print(p.y)      # ✅ 答案: 2

# p.z = 3       # ✅ 答案: 会报错 AttributeError: 'Point' object has no attribute 'z'

print()

# ----- 题10: 设计一个银行账户类 - 参考实现 -----
class BankAccount:
    bank_name = "Python银行"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"存入{amount}，余额: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("余额不足")
        else:
            self.balance -= amount
            print(f"取出{amount}，余额: {self.balance}")

    def get_balance(self):
        return self.balance

acc = BankAccount("张三", 1000)
print(acc.bank_name)     # Python银行
acc.deposit(500)          # 存入500，余额: 1500
acc.withdraw(200)         # 取出200，余额: 1300
acc.withdraw(2000)        # 余额不足
print(acc.get_balance())  # 1300

print()

# ----- 题11: __del__ 方法 -----
class Temp:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 被创建")

    def __del__(self):
        print(f"{self.name} 被销毁")

print("开始")
t1 = Temp("对象1")
t2 = Temp("对象2")
t1 = None
print("中间")
t2 = None
print("结束")
# ✅ 答案:
# 开始
# 对象1 被创建
# 对象2 被创建
# 对象1 被销毁
# 中间
# 对象2 被销毁
# 结束

print()

# ----- 题12: 类属性与实例属性的查找顺序 -----
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

print(bird.sound)   # ✅ 答案: 叽叽喳喳（Bird 类的类属性）
print(bird.legs)    # ✅ 答案: 2（Bird 类的类属性）
print(dog.sound)    # ✅ 答案: ...（Animal 父类的类属性）
print(dog.legs)     # ✅ 答案: 4（Animal 父类的类属性）

print()

# ----- 题13: 类方法创建实例（工厂模式） -----
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

print(d1)  # ✅ 答案: 2026年6月14日
print(d2)  # ✅ 答案: 2026年12月25日
print(type(d1) == type(d2))  # ✅ 答案: True

print()

# ----- 题14: self 的本质 -----
class Foo:
    def __init__(self, value):
        self.value = value

    def show(self):
        return f"value = {self.value}"

f = Foo(42)
print(f.show())          # ✅ 答案: value = 42
print(Foo.show(f))       # ✅ 答案: value = 42
print(Foo.show(Foo(99))) # ✅ 答案: value = 99

print()

# ----- 题15: 综合应用 - 参考实现 -----
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, score):
        self.students.append({"name": name, "score": score})

    def get_average(self):
        if not self.students:
            return 0
        total = sum(s["score"] for s in self.students)
        return total / len(self.students)

    def get_top_student(self):
        if not self.students:
            return None
        top = max(self.students, key=lambda s: s["score"])
        return top["name"]

    @classmethod
    def from_dict_list(cls, dict_list):
        manager = cls()
        for d in dict_list:
            manager.add_student(d["name"], d["score"])
        return manager

sm = StudentManager()
sm.add_student("张三", 85)
sm.add_student("李四", 92)
sm.add_student("王五", 78)
print(f"平均分: {sm.get_average()}")    # 85.0
print(f"最高分: {sm.get_top_student()}")  # 李四

sm2 = StudentManager.from_dict_list([
    {"name": "赵六", "score": 90},
    {"name": "钱七", "score": 88}
])
print(f"平均分: {sm2.get_average()}")   # 89.0

print()

# ----- 题16: 调试修复 - 参考答案 -----
# BUG 1 修复: __init__ 不能有返回值（只能返回 None）
class Bad1:
    def __init__(self, name):
        self.name = name
        # 去掉 return self.name

# BUG 2 修复: 实例方法必须有 self 参数
class Bad2:
    def __init__(self):
        self.value = 10

    def show(self):  # 添加 self 参数
        print(self.value)

# BUG 3 修复: 类方法第一个参数应该是 cls
class Bad3:
    count = 0

    @classmethod
    def increment(cls):  # 改为 cls
        cls.count += 1
