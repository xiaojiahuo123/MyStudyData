# Day 08 学习笔记

## 8.1 文件操作

### 8.1.1 os.walk 遍历目录

`os.walk()` 用于递归遍历目录下的所有子目录和文件。

```python
import os

for root, dirs, files in os.walk(os.getcwd()):
    print("当前路径：", root)
    print("目录：", dirs)
    print("文件：", files)
    print()
```

| 返回值 | 说明 |
|--------|------|
| `root` | 当前遍历的目录路径 |
| `dirs` | 当前目录下的子目录列表 |
| `files` | 当前目录下的文件列表 |

### 8.1.2 文件拷贝

```python
def file_copy(source_file_path, dest_file_path):
    source_file = open(source_file_path, "rb")
    dest_file = open(dest_file_path, "wb")

    # 每次读取 1024 字节，避免大文件内存溢出
    content = source_file.read(1024)
    while content:
        dest_file.write(content)
        content = source_file.read(1024)

    source_file.close()
    dest_file.close()
```

**优化点**：分块读取（1024字节），而不是一次性读取全部文件内容，适合大文件。

---

## 8.2 面向对象编程简介

### 8.2.1 三种编程范式对比

| 范式 | 特点 | 适用场景 |
|------|------|---------|
| **面向过程** | 按步骤顺序执行 | 简单流程 |
| **面向函数** | 将功能封装为函数 | 可复用功能 |
| **面向对象** | 将数据和行为封装为对象 | 复杂业务逻辑 |

### 8.2.2 示例对比

```python
# 面向过程：直接写步骤
洗("黄瓜")
切("黄瓜")
拌("黄瓜", "调料")

# 面向函数：封装为函数
def 东北大拉皮():
    洗("黄瓜")
    切("黄瓜")
    拌("黄瓜", "调料")

# 面向对象：封装为类
class 菜:
    def __init__(self, name):
        self.name = name
    def 洗(self, clm):
        print(f"{self.name}洗{clm}")
    def 切(self, clm):
        print(f"{self.name}切{clm}")

dlp = 菜("东北大拉皮")
dlp.洗("黄瓜")
dlp.切("黄瓜")
```

---

## 8.3 类的定义与对象创建

### 8.3.1 基本语法

```python
class Student:
    '''这是一个学生类'''
    # 类属性：所有实例共享
    school = "atguigu"

    # 构造方法：创建对象时自动调用
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age

    # 实例方法
    def study(self):
        print(f"{self.age}岁的{self.name}正在学习")

# 创建对象
mzl = Student("mzl", 23)
print(mzl.name)    # mzl
print(mzl.school)  # atguigu（访问类属性）
mzl.study()        # 23岁的mzl正在学习
```

### 8.3.2 类的成员组成

```
类
├── 类属性（所有实例共享）
├── __init__（构造方法）
└── 方法
    ├── 实例方法（第一个参数是 self）
    ├── 类方法（@classmethod，第一个参数是 cls）
    └── 静态方法（@staticmethod，无默认参数）
```

---

## 8.4 __init__ 和 self 详解

### 8.4.1 __init__ 是什么

`__init__` 是 Python 类的**构造方法**，在创建对象时**自动调用**，用于初始化对象的属性。

### 8.4.2 self 是什么

`self` 代表**当前对象本身**，Python 自动传入，不需要手动传参。

### 8.4.3 代码示例

```python
class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("旺财")

# 等价于：
# 1. 创建空对象
# 2. 自动调用 dog.__init__("旺财")
# 3. 执行 self.name = "旺财"（self 就是 dog）
# 4. 结果：dog.name = "旺财"
```

### 8.4.4 与 Java 的对比

```python
# Python
class Dog:
    def __init__(self, name):
        self.name = name
```

```java
// Java 等价写法
class Dog {
    String name;
    Dog(String name) {
        this.name = name;  // this 等价于 Python 的 self
    }
}
```

**`self` = Java 中的 `this`**

### 8.4.5 执行流程

```
dog = Dog("旺财")
      │
      ▼
┌─────────────────────────────────────────────┐
│  1. 创建空对象 dog                           │
│  2. 自动调用 dog.__init__("旺财")            │
│  3. 执行 self.name = "旺财"                  │
│     (self 就是 dog，等价于 dog.name = "旺财") │
│  4. 结果：dog.name = "旺财"                  │
└─────────────────────────────────────────────┘
```

---

## 8.5 类属性 vs 实例属性

### 8.5.1 定义与区别

| 特性 | 类属性 | 实例属性 |
|------|--------|---------|
| **定义位置** | 类内部，方法外部 | `__init__` 方法内 |
| **访问方式** | `类名.属性` 或 `对象.属性` | `对象.属性` |
| **共享性** | 所有实例共享 | 每个实例独立 |
| **生命周期** | 随类存在 | 随对象存在 |

### 8.5.2 代码示例

```python
class Dog:
    # 类属性：所有实例共享
    home = "earth"

    def __init__(self, name, age):
        # 实例属性：每个实例独立
        self.name = name
        self.age = age

xh = Dog("xh", 2)
bg = Dog("bg", 3)

# 访问类属性
print(xh.home)  # earth
print(bg.home)   # earth
print(Dog.home)  # earth

# 访问实例属性
print(xh.name)   # xh
print(bg.name)   # bg

# 动态添加实例属性
xh.color = "white"
print(xh.color)  # white
# print(bg.color)  # ❌ AttributeError：bg 没有 color 属性
```

### 8.5.3 注意事项

```python
# 通过类名添加类属性
Dog.kemu = "quanke"
print(Dog.kemu)  # quanke

# 通过对象添加的是实例属性，不是类属性
zsf = Student("zsf", 81)
zsf.home = "Myhome"  # 这是添加实例属性，不会修改类属性
print(zsf.home)      # Myhome
print(Student.home)  # home（类属性不变）
```

---

## 8.6 实例方法、类方法、静态方法

### 8.6.1 三种方法对比

| 方法类型 | 装饰器 | 第一个参数 | 调用方式 |
|----------|--------|-----------|---------|
| **实例方法** | 无 | `self`（实例） | `对象.方法()` |
| **类方法** | `@classmethod` | `cls`（类） | `类名.方法()` 或 `对象.方法()` |
| **静态方法** | `@staticmethod` | 无默认参数 | `类名.方法()` 或 `对象.方法()` |

### 8.6.2 实例方法

```python
class Student:
    school = "atguigu"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法：第一个参数是 self
    def eat(self):
        print(self.school)  # 可以访问类属性
        print(self.name)    # 可以访问实例属性
        print(self.age)

zwj = Student("zwj", 30)
zwj.eat()  # 自动传入 self=zwj
```

### 8.6.3 类方法

```python
class Student:
    school = "atguigu"

    @classmethod  # 类方法装饰器
    def get_info(cls):
        print(cls.school)   # cls 代表类本身
        print(cls.__doc__)

# 通过类名调用
Student.get_info()

# 通过对象调用（不推荐）
zwj = Student("zwj", 30)
zwj.get_info()
```

### 8.6.4 静态方法

```python
class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b

# 静态方法不需要 self 或 cls
print(MathUtil.add(10, 20))  # 30
```

### 8.6.5 动态添加方法

```python
import types

def drink(self):
    print("drinking")

class Student:
    pass

# 方式1：通过类名添加（所有实例可用）
Student.drink = drink
zwj = Student()
zwj.drink()  # drinking

# 方式2：通过 types.MethodType 绑定（仅当前实例可用）
zcs = Student()
zcs.drink = types.MethodType(drink, zcs)
zcs.drink()  # drinking
```

---

## 8.7 动态删除属性与方法

### 8.7.1 删除方式

| 方式 | 语法 | 说明 |
|------|------|------|
| `del` 语句 | `del 对象.属性名` | 删除属性 |
| `delattr()` 函数 | `delattr(对象, "属性名")` | 删除属性 |

### 8.7.2 代码示例

```python
class Student:
    home = "atguigu"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat")

zs = Student("zs", 20)

# 删除实例属性
del zs.name
# print(zs.name)  # ❌ AttributeError

# 删除类属性
del Student.home
# print(Student.home)  # ❌ AttributeError

# 删除方法
delattr(zs, "eat")  # ❌ 报错！eat 是类方法，不在实例上
zs.eat()             # 仍然可以调用

# 正确删除类方法
del Student.eat
# zs.eat()  # ❌ AttributeError
```

### 8.7.3 注意事项

**`delattr` 只能删除对象自身的属性**，不能删除从类继承的方法。要删除类方法，需要对**类**操作而不是对**实例**操作。

---

## 8.8 __slots__ 限制属性

### 8.8.1 什么是 __slots__

`__slots__` 用于**限制实例可以添加的属性和方法**，防止动态添加未定义的属性。

### 8.8.2 代码示例

```python
import types

class Person:
    __slots__ = ("name", "age", "eat")  # 只允许这些属性和方法

    def __init__(self, name=None):
        self.name = name

def eat(self):
    print(f"{self.name}在吃饭")

def drink(self):
    print(f"{self.name}在喝水")

p = Person("张三")

# ✅ 允许的属性
p.age = 10
print(p.age)  # 10

# ❌ 不允许的属性
# p.weight = 100  # AttributeError: 'Person' object has no attribute 'weight'

# ✅ 允许的方法（通过 types.MethodType 绑定）
p.eat = types.MethodType(eat, p)
p.eat()  # 张三在吃饭

# ❌ 不允许的方法
# p.drink = types.MethodType(drink, p)  # AttributeError
```

### 8.8.3 __slots__ 的作用

| 作用 | 说明 |
|------|------|
| **限制属性** | 只允许 `__slots__` 中定义的属性名 |
| **节省内存** | 不使用 `__dict__`，减少内存占用 |
| **提高性能** | 属性访问速度更快 |
| **防止误操作** | 避免拼写错误导致的动态属性 |

### 8.8.4 注意事项

```python
# __slots__ 只影响当前类，不影响子类
class Student(Person):
    pass

s = Student()
s.weight = 100  # ✅ 子类可以添加任意属性（如果没有自己的 __slots__）
```

---

## 8.9 总结

| 概念 | 核心要点 |
|------|----------|
| **类** | 对象的模板，包含属性和方法 |
| **对象** | 类的实例，拥有独立的属性值 |
| **self** | 代表当前对象本身，等价于 Java 的 this |
| **__init__** | 构造方法，创建对象时自动调用 |
| **类属性** | 所有实例共享，定义在方法外 |
| **实例属性** | 每个实例独立，定义在 __init__ 内 |
| **实例方法** | 第一个参数是 self |
| **类方法** | @classmethod，第一个参数是 cls |
| **静态方法** | @staticmethod，无默认参数 |
| **__slots__** | 限制实例可添加的属性 |

> **记忆口诀**：
> - self 指实例，cls 指类
> - 类属性共享，实例属性独立
> - 实例方法用 self，类方法用 cls，静态方法都不用
