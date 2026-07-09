# Day12 知识点总结

## 1. 浅拷贝与深拷贝

### 1.1 基本概念

| 特性 | 赋值（=） | 浅拷贝（copy） | 深拷贝（deepcopy） |
|------|-----------|----------------|---------------------|
| 本质 | 引用同一对象 | 创建新容器，元素仍引用原对象 | 完全独立的新对象 |
| 原对象变化是否影响 | 是 | 内层元素变化会影响 | 不会 |

### 1.2 copy 模块的使用

```python
import copy

a = [1, 2, [3, 4]]

# 浅拷贝：外层容器独立，内层元素共享引用
b = copy.copy(a)
print(a is b)          # False - 外层容器不同
print(a[2] is b[2])    # True  - 内层列表是同一对象

# 深拷贝：完全独立，互不影响
c = copy.deepcopy(a)
print(a[2] is c[2])    # False - 内层列表也不同
```

### 1.3 特殊情况

**非容器类型**：`copy.copy()` 对非容器类型（int、str、float 等）不做拷贝，直接返回原对象：

```python
a = 10
b = copy.copy(a)
print(a is b)  # True，因为不可变类型无需拷贝
```

**元组的特殊性**：元组本身不可变，如果元组中没有可变元素，浅拷贝直接返回原元组：

```python
t1 = (1, 2, 3)
t2 = copy.copy(t1)
print(t1 is t2)  # True，元组不含可变元素，浅拷贝返回自身

t3 = (1, 2, [3, 4])
t4 = copy.copy(t3)
print(t3 is t4)  # False，含可变元素，浅拷贝创建新元组
```

---

## 2. 迭代器

### 2.1 可迭代对象 vs 迭代器

| 概念 | 判断方式 | 具备方法 |
|------|----------|----------|
| 可迭代对象（Iterable） | `isinstance(obj, Iterable)` | `__iter__()` |
| 迭代器（Iterator） | `isinstance(obj, Iterator)` | `__iter__()` + `__next__()` |

> **关系**：迭代器一定是可迭代对象，但可迭代对象不一定是迭代器。

### 2.2 iter() 与 next()

```python
from collections.abc import Iterable, Iterator

lst = [1, 2, 3]
it = iter(lst)       # 将可迭代对象转为迭代器

print(isinstance(lst, Iterable))  # True  - 列表是可迭代对象
print(isinstance(lst, Iterator))  # False - 列表不是迭代器
print(isinstance(it, Iterator))   # True  - 迭代器对象

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # 抛出 StopIteration
```

### 2.3 自定义迭代器

通过实现 `__iter__()` 和 `__next__()` 方法，将类变为迭代器：

```python
class ReverseIterator:
    """反转迭代器：从后往前遍历"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

ri = ReverseIterator([1, 2, 3, 4, 5])
for item in ri:
    print(item)  # 输出: 5, 4, 3, 2, 1
```

---

## 3. 生成器

### 3.1 创建生成器的两种方式

**方式一：生成器表达式（元组推导式）**

```python
gen = (x ** 2 for x in range(5))
print(type(gen))  # <class 'generator'>

for val in gen:
    print(val)  # 0, 1, 4, 9, 16
```

> 注意：`(x for x in range(5))` 不是元组，而是生成器表达式。`tuple(...)` 可将其转为元组。

**方式二：函数中使用 yield**

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)
print(next(gen))  # 5
print(next(gen))  # 4
```

### 3.2 yield 的执行机制

1. 调用生成器函数时，函数体**不立即执行**，返回生成器对象
2. 每次 `next()` 时执行到 `yield`，**暂停并返回值**
3. 下次 `next()` 时从上次暂停处继续执行
4. 函数结束时抛出 `StopIteration`

### 3.3 send() 方法

`send()` 既恢复执行，又向生成器内部发送数据：

```python
def generator():
    while True:
        received = yield
        print(f"收到: {received}")

g = generator()
next(g)           # 必须先 next() 或 send(None) 激活到 yield 处
g.send("hello")   # 收到: hello
g.send("world")   # 收到: world
```

### 3.4 生成器实现交替执行

```python
def task1():
    for i in range(5):
        print(f"任务1 - 步骤{i}")
        yield  # 暂停，交出控制权

def task2():
    for i in range(5):
        print(f"任务2 - 步骤{i}")
        yield

# 手动交替执行
t1 = task1()
t2 = task2()
for _ in range(5):
    next(t1)
    next(t2)
```

---

## 4. 命名空间

命名空间是变量名到对象的映射关系（字典结构）。

### 4.1 命名空间类型

| 命名空间 | 说明 | 示例 |
|----------|------|------|
| 内建命名空间 | 内置函数和关键字 | `print`、`len`、`True` |
| 全局命名空间 | 模块级别定义的变量 | 模块顶层的变量和函数 |
| 函数命名空间 | 函数调用时创建 | 函数内的局部变量 |
| 类命名空间 | 类定义时创建 | 类属性 |
| 实例命名空间 | 实例化时创建 | 实例属性 |

---

## 5. 作用域 LEGB

Python 查找变量的顺序遵循 **LEGB 规则**：

```
L (Local)       局部作用域 → 函数内部
E (Enclosing)   嵌套作用域 → 外层函数
G (Global)      全局作用域 → 模块级别
B (Built-in)    内建作用域 → Python 内置
```

### 示例

```python
x = "全局"

def outer():
    x = "嵌套"
    def inner():
        x = "局部"
        print(x)  # 输出: 局部 (L)
    inner()

outer()
```

### global 与 nonlocal

```python
count = 0

def func():
    global count      # 声明使用全局变量
    count += 1

def outer():
    x = 10
    def inner():
        nonlocal x    # 声明使用外层函数变量
        x += 1
    inner()
    print(x)  # 11
```

---

## 6. 闭包

### 6.1 闭包的三个条件

1. 有嵌套函数（函数内定义函数）
2. 内层函数引用了外层函数的变量
3. 外层函数返回内层函数对象

### 6.2 闭包示例

```python
def outer(msg):
    def inner():
        print(f"消息: {msg}")  # 引用外层变量 msg
    return inner              # 返回内层函数

fn = outer("hello")
fn()  # 消息: hello
# 此时 outer 已执行完毕，但 msg 变量被 inner 引用，仍然存活
```

### 6.3 验证闭包

通过 `__closure__` 属性判断函数是否为闭包：

```python
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5)

print(add5.__closure__)              # (<cell at 0x...>,)
print(add5.__closure__[0].cell_contents)  # 5
```

---

## 7. 装饰器

装饰器本质上是一个函数，接收被装饰函数作为参数，返回一个新的函数（通常增强其功能）。

### 7.1 闭包装饰器

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("函数执行前")
        result = func(*args, **kwargs)
        print("函数执行后")
        return result
    return wrapper
```

### 7.2 @ 语法糖

```python
@my_decorator
def say_hello():
    print("Hello!")

# 等价于: say_hello = my_decorator(say_hello)
say_hello()
# 输出: 函数执行前 → Hello! → 函数执行后
```

### 7.3 多层装饰器

```python
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def greet():
    return "Hello"

# 等价于: bold(italic(greet))
print(greet())  # <b><i>Hello</i></b>
```

> 装饰器从下往上装饰，从上往下执行：先 `italic` 装饰，再 `bold` 装饰。

### 7.4 带参装饰器

带参装饰器需要**三层函数嵌套**：

```python
def repeat(times):                # 第一层：接收装饰器参数
    def decorator(func):          # 第二层：接收被装饰函数
        def wrapper(*args, **kwargs):  # 第三层：替代原函数
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg)

say("hello")
# 输出: hello × 3 次
```

### 7.5 类装饰器

利用 `__call__` 方法，让类的实例可以像函数一样被调用：

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("类装饰器: 执行前")
        result = self.func(*args, **kwargs)
        print("类装饰器: 执行后")
        return result

@MyDecorator
def say_hi():
    print("Hi!")

say_hi()
# 输出: 类装饰器: 执行前 → Hi! → 类装饰器: 执行后
```

### 7.6 装饰器保留原函数信息

使用 `functools.wraps` 保留被装饰函数的元信息：

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # 保留原函数名、文档字符串等
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """这是文档字符串"""
    pass

print(example.__name__)  # example（不加 wraps 则为 wrapper）
print(example.__doc__)   # 这是文档字符串
```

---

## 总结

| 知识点 | 核心要点 |
|--------|----------|
| 浅拷贝/深拷贝 | 浅拷贝只复制外层，深拷贝完全独立；非容器类型和纯元组不拷贝 |
| 迭代器 | 需要 `__iter__()` + `__next__()`；`StopIteration` 表示遍历结束 |
| 生成器 | `yield` 暂停/恢复；`send()` 可发送数据；惰性求值节省内存 |
| 命名空间 | 内建/全局/函数/类/实例，变量名到对象的映射 |
| 作用域 | LEGB 查找顺序：局部 → 嵌套 → 全局 → 内建 |
| 闭包 | 内层函数引用外层变量并被返回；`__closure__` 验证 |
| 装饰器 | 本质是高阶函数；支持 @语法糖、多层嵌套、带参、类装饰器 |
