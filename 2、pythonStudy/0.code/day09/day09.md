# Day 09 学习笔记

## 9.1 封装（Encapsulation）

### 9.1.1 什么是封装

封装是面向对象编程的三大特性之一，用于**隐藏对象的内部实现细节**，只暴露必要的接口。

### 9.1.2 私有属性和方法

Python 使用**双下划线 `__`** 实现私有化（名称改写 Name Mangling）。

```python
class Person:
    __home = "earth"  # 私有类属性，实际存储为 _Person__home
    _test = "单下划线，约定私有（可访问）"

    def __init__(self, name, age):
        self.__name = name  # 私有实例属性，实际存储为 self._Person__name
        self.age = age

    def __eat(self):  # 私有方法
        print("eating")

    def eat_1(self):  # 公开方法，内部可以调用私有方法
        print("eating")
        print(self.__home)  # 内部访问私有属性
        self.__eat()        # 内部调用私有方法
```

### 9.1.3 名称改写（Name Mangling）

```python
# 外部访问私有属性（通过改写后的名字）
print(Person._Person__home)  # earth

zs = Person("zs", 18)
print(zs._Person__name)  # zs（不推荐这样做）

# 单下划线：约定私有，但可以访问
print(zs._test)  # 这是测试的，不是强制的私有化可以访问
```

### 9.1.4 命名风格对比

| 命名方式 | 示例 | 含义 |
|---------|------|------|
| 无下划线 | `name` | 公开属性 |
| 单下划线 | `_test` | 约定私有（可访问） |
| 双下划线 | `__name` | 名称改写（强制私有） |

---

## 9.2 @property 装饰器

### 9.2.1 什么是 @property

`@property` 将**方法转换为属性**，让方法调用不需要加括号。

```python
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print(f"{self.name} eats!")

zsf = Person("zsf")
zsf.eat  # 不需要加括号，输出：zsf eats!
```

### 9.2.2 getter 和 setter

```python
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        # getter：读取属性时触发
        if self.__name == "zsf":
            print("换个名字")
            self.__name = "zwj"
        return self.__name

    @name.setter
    def name(self, name):
        # setter：给属性赋值时触发
        if name == "ssss":
            name = "aaaa"
        self.__name = name

zsf = Person("zsf")
print(zsf.name)      # 触发 getter
zsf.name = "ssss"    # 触发 setter
print(zsf.name)      # 触发 getter
```

### 9.2.3 @property 的作用

| 作用 | 说明 |
|------|------|
| **方法变属性** | 调用时不需要加括号 |
| **数据验证** | 在 setter 中检查数据合法性 |
| **只读属性** | 只定义 getter，不定义 setter |
| **隐藏实现** | 外部不需要知道内部是私有属性 |

---

## 9.3 封装实战：信用卡类

```python
class CreditCard:
    def __init__(self, name):
        self.name = name
        self.__password = None
        self.__balance = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if password != "888888":
            print("密码输入有误")
        else:
            print("密码输入正确")
            self.__password = password

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            print("理性消费，信用卡爆了")
        else:
            print("消费成功")
            self.__balance = balance

c1 = CreditCard("mzl")
c1.password = "666666"  # 密码输入有误
c1.password = "888888"  # 密码输入正确
c1.balance = -100       # 理性消费，信用卡爆了
c1.balance = 100        # 消费成功
```

---

## 9.4 __str__ 方法

### 9.4.1 什么是 __str__

`__str__` 是 Python 的**魔术方法**，用于定义对象的**字符串表示**，在 `print()` 或 `str()` 时自动调用。

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.age}岁的{self.name}"

wf = Student("wf", 20)
print(wf)  # 20岁的wf（自动调用 __str__）
```

### 9.4.2 面向对象关系设计

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__bf = None  # 男朋友

    @property
    def bf(self):
        return self.__bf

    @bf.setter
    def bf(self, bf):
        self.__bf = bf

    def __str__(self):
        return f"{self.age}岁的{self.name}带着他的男朋友{self.__bf.name}浪漫的走在宏福科技园"

class BoyFriend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

wf = Student("wf", 20)
xb = BoyFriend("wxb", 25)
wf.bf = xb  # 将对象作为属性传入
print(wf)   # 20岁的wf带着他的男朋友wxb浪漫的走在宏福科技园
```

---

## 9.5 继承（Inheritance）

### 9.5.1 什么是继承

继承是面向对象的三大特性之一，子类可以**继承父类的属性和方法**，实现代码复用。

### 9.5.2 基本语法

```python
class Person:
    """人的类"""
    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating")

class YellowRace(Person):  # 继承 Person
    color = "yellow"

class WhiteRace(Person):   # 继承 Person
    color = "white"

class BlackRace(Person):   # 继承 Person
    color = "black"

zsf = YellowRace("zsf")
print(zsf.color)  # yellow（子类属性）
print(zsf.home)   # earth（父类属性）
zsf.eat()         # eating（父类方法）
```

### 9.5.3 继承的好处

| 好处 | 说明 |
|------|------|
| **代码复用** | 子类可以直接使用父类的属性和方法 |
| **扩展性** | 子类可以在父类基础上添加新功能 |
| **多态基础** | 继承是实现多态的前提 |

---

## 9.6 多继承（Multiple Inheritance）

### 9.6.1 什么是多继承

Python 支持一个类**同时继承多个父类**。

```python
class Person:
    home = "earth"
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("eating...")

class YellowRace(Person):
    color = "yellow"
    def run(self):
        print("run...yel")

class Student(Person):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def study(self):
        print("study...")
    def run(self):
        print("run...stu")

class ChineseStudent(YellowRace, Student):  # 多继承
    country = "china"

zsf = ChineseStudent("zsf", 80)
print(zsf.country)  # china
print(zsf.color)    # yellow
print(zsf.home)     # earth
zsf.study()         # study...
zsf.run()           # run...yel（按照 MRO 顺序）
```

### 9.6.2 MRO（方法解析顺序）

Python 使用 **C3 线性化算法**确定多继承时的方法查找顺序。

```python
# 查看 MRO 顺序
print(ChineseStudent.__mro__)
# (<class 'ChineseStudent'>, <class 'YellowRace'>, <class 'Student'>, <class 'Person'>, <class 'object'>)
```

**MRO 顺序**：ChineseStudent → YellowRace → Student → Person → object

---

## 9.7 super() 方法

### 9.7.1 什么是 super()

`super()` 用于**调用父类的方法**，实现代码复用。

### 9.7.2 调用父类方法的两种方式

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} eating")

class Student(Person):
    def __init__(self, name, age, grade):
        # 方式1：通过 super() 调用（推荐）
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        # 方式2：通过父类名调用
        Person.eat(self)
        print(f"{self.name} studying")
```

### 9.7.3 super() 在多继承中的应用

```python
class ChineseStudent(YellowPerson, Student):
    country = "China"

    def xuexi(self):
        super().eat()    # 按 MRO 顺序调用
        super().run()    # 按 MRO 顺序调用
        super().study()  # 按 MRO 顺序调用
        print(super().home)
```

---

## 9.8 方法重写（Override）

### 9.8.1 什么是方法重写

子类可以**重新定义父类的方法**，实现不同的行为。

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("父类中的eat方法")

class ChineseStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def eat(self):  # 重写父类方法（Python 直接重写，没有专门注解）
        print(f"{self.name}用筷子吃饭")

zwj = ChineseStudent("zwj", 20, "一年级")
zwj.eat()  # zwj用筷子吃饭
```

### 9.8.2 Python vs Java 的方法重写

| 特性 | Python | Java |
|------|--------|------|
| **重写方式** | 直接定义同名方法 | 使用 `@Override` 注解 |
| **调用父类方法** | `super().方法()` | `super.方法()` |
| **强制检查** | 无 | 编译器检查 |

---

## 9.9 多态（Polymorphism）深入解析

### 9.9.1 什么是多态

**多态**是指**同一接口，不同实现**。父类引用指向子类对象，调用同名方法时，执行的是子类重写后的方法。

### 9.9.2 多态的三个必要条件

```
┌─────────────────────────────────────────────────────────┐
│  多态的三个条件：                                         │
├─────────────────────────────────────────────────────────┤
│  1. 有继承关系                                           │
│  2. 子类重写父类方法                                      │
│  3. 父类引用指向子类对象                                  │
└─────────────────────────────────────────────────────────┘
```

### 9.9.3 经典多态示例（对比 Java）

#### Python 版本

```python
class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def speak(self):  # 重写父类方法
        print("Woof!")

class Cat(Animal):
    def speak(self):  # 重写父类方法
        print("Meow!")

# 多态：同一个方法，不同表现
def animal_speak(animal):
    animal.speak()  # 不关心具体类型，只关心有没有 speak 方法

dog = Dog()
cat = Cat()

animal_speak(dog)  # Woof!
animal_speak(cat)  # Meow!
```

#### Java 版本对比

```java
class Animal {
    void speak() {
        System.out.println("Animal speaking");
    }
}

class Dog extends Animal {
    @Override
    void speak() {
        System.out.println("Woof!");
    }
}

class Cat extends Animal {
    @Override
    void speak() {
        System.out.println("Meow!");
    }
}

// 多态
public class Main {
    public static void animalSpeak(Animal animal) {
        animal.speak();  // 运行时决定调用哪个方法
    }
    
    public static void main(String[] args) {
        animalSpeak(new Dog());  // Woof!
        animalSpeak(new Cat());  // Meow!
    }
}
```

### 9.9.4 Python 的鸭子类型（Duck Typing）

**Python 的多态更灵活**，不需要严格的继承关系，只要对象有对应的方法即可。

```python
# 没有继承关系的类
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Car:
    def speak(self):
        print("Beep!")

# 鸭子类型：不关心类型，只关心有没有 speak 方法
def make_sound(obj):
    obj.speak()

make_sound(Dog())   # Woof!
make_sound(Cat())   # Meow!
make_sound(Car())   # Beep!
```

**鸭子类型**：
> "如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子。"

### 9.9.5 多态的实现方式

#### 方式1：继承 + 方法重写

```python
class Shape:
    def area(self):
        raise NotImplementedError("子类必须实现 area 方法")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# 多态：同一方法，不同实现
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"面积: {shape.area()}")  # 不同对象调用各自的 area 方法
```

#### 方式2：抽象类（更严格）

```python
from abc import ABC, abstractmethod

class Animal(ABC):  # 抽象类，不能实例化
    @abstractmethod
    def speak(self):  # 抽象方法，子类必须实现
        pass

class Dog(Animal):
    def speak(self):  # 必须实现，否则报错
        print("Woof!")

# animal = Animal()  # ❌ TypeError: Can't instantiate abstract class
dog = Dog()
dog.speak()  # Woof!
```

### 9.9.6 多态 vs 方法重写

| 概念 | 说明 |
|------|------|
| **方法重写** | 子类重新定义父类的方法（技术手段） |
| **多态** | 通过方法重写，实现同一接口不同表现（设计思想） |

```
方法重写是"怎么做"
多态是"为什么做"
```

### 9.9.7 多态的优势

```python
# 没有多态：需要判断类型
def get_area(shape):
    if isinstance(shape, Circle):
        return 3.14 * shape.radius ** 2
    elif isinstance(shape, Rectangle):
        return shape.width * shape.height
    # 每新增一种形状，都要修改这个函数

# 有多态：统一接口
def get_area(shape):
    return shape.area()  # 不关心类型，只关心有没有 area 方法
    # 新增形状不需要修改这个函数
```

| 优势 | 说明 |
|------|------|
| **可扩展性** | 新增类不需要修改已有代码 |
| **可维护性** | 代码更简洁，逻辑更清晰 |
| **灵活性** | 同一接口可以处理不同类型的对象 |

### 9.9.8 Python vs Java 的多态对比

| 特性 | Python | Java |
|------|--------|------|
| **多态实现** | 鸭子类型（更灵活） | 继承 + 接口（更严格） |
| **类型检查** | 运行时检查 | 编译时检查 |
| **抽象类** | `abc.ABC` + `@abstractmethod` | `abstract class` |
| **接口** | 无（用抽象类代替） | `interface` |
| **方法重写** | 直接定义同名方法 | `@Override` 注解 |

### 9.9.9 记忆口诀

```
多态三条件：继承、重写、父类引用
Python 鸭子类型：不看类型看方法
同一接口不同实现，扩展维护都方便
```

---

## 9.10 总结

| 概念 | 核心要点 |
|------|----------|
| **封装** | 隐藏实现细节，只暴露必要接口 |
| **私有化** | 双下划线 `__` 实现名称改写 |
| **@property** | 将方法转换为属性，支持 getter/setter |
| **__str__** | 定义对象的字符串表示 |
| **继承** | 子类继承父类的属性和方法 |
| **多继承** | 一个类可以继承多个父类 |
| **MRO** | 方法解析顺序，C3 线性化算法 |
| **super()** | 调用父类方法 |
| **方法重写** | 子类重新定义父类方法 |
| **多态** | 不同类对同一方法有不同实现 |

> **记忆口诀**：
> - 封装隐藏细节，暴露接口
> - 继承复用代码，扩展功能
> - 多态灵活调用，统一接口
> - 面向对象三特性：封装、继承、多态
