# Day12 知识点总结

## 1. 浅拷贝与深拷贝

### 1.1 基本概念

| 特性        | 赋值（=）  | 浅拷贝（copy）      | 深拷贝（deepcopy） |
| --------- | ------ | -------------- | ------------- |
| 本质        | 引用同一对象 | 创建新容器，元素仍引用原对象 | 完全独立的新对象      |
| 原对象变化是否影响 | 是      | 内层元素变化会影响      | 不会            |

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
print(t1 is t2)  # True，浅拷贝返回自身

t3 = (1, 2, [3, 4])
t4 = copy.copy(t3)
print(t3 is t4)  # True，无论是否含可变元素，浅拷贝都返回自身（元组是不可变类型）
```

***

## 2. 迭代器

### 2.1 可迭代对象 vs 迭代器

| 概念              | 判断方式                        | 具备方法                        |
| --------------- | --------------------------- | --------------------------- |
| 可迭代对象（Iterable） | `isinstance(obj, Iterable)` | `__iter__()`                |
| 迭代器（Iterator）   | `isinstance(obj, Iterator)` | `__iter__()` + `__next__()` |

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

***

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

###### 示例

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
print(f"初始化 next(): {next(acc)}") # 0
print(f"send(10): {acc.send(10)}") # 10
print(f"send(20): {acc.send(20)}") # 30
print(f"send(30): {acc.send(30)}") # 60
```

#### 🟢 第1回合：`next(acc)` 启动生成器

text

```python
调用者: next(acc)
生成器内部:
  total = 0
  进入 while True:
    执行 value = yield total   ← 此时 total = 0
    在这里暂停！并把 0 扔给调用者。
  ⏸️ 暂停位置: value = yield total 的等号右侧，等待接收值
调用者收到: 0
```



📊 **变量状态**：`total = 0`，生成器停在 `yield` 处。

------

#### 🟡 第2回合：`acc.send(10)`

text

```python
调用者: send(10)  →  把 10 传给生成器
生成器被唤醒:
  上次暂停的 yield 表达式得到值 10 → value = 10
  判断 value is None? 否
  total += value  → total = 0 + 10 = 10
  循环，再次执行 value = yield total  →  total = 10
  产出 10，暂停，等待下一次 send
调用者收到: 10
```



📊 **变量状态**：`total` 变为 10，生成器再次停在 `yield`。

------

#### 🟠 第3回合：`acc.send(20)`

text

```python
调用者: send(20)  →  把 20 传给生成器
生成器被唤醒:
  value = 20  （来自 yield 表达式的值）
  total += 20  → total = 10 + 20 = 30
  执行 value = yield total  → 产出 total = 30
  暂停，等待下一次 send
调用者收到: 30   ← 这就是为什么你注释的 20 是错的
```



📊 **变量状态**：`total = 30`。

------

#### 🔴 第4回合：`acc.send(30)`

text

```python
调用者: send(30)  →  把 30 传给生成器
生成器被唤醒:
  value = 30
  total += 30  → total = 30 + 30 = 60
  执行 value = yield total  → 产出 60
  暂停，等待下一次 send
调用者收到: 60   ← 所以也不是你注释的 30
```



📊 **变量状态**：`total = 60`。

------

#### 🧩 一张图总结“消息传递”规则

text

```python
           send(10) 发给生成器
调用者  ──────────────────→  生成器内部
                              yield 表达式 = 10  (value 收到 10)
                              ... 计算 total ...
           ←──────────────────  yield total 产出 (如 10/30/60)
              生成器产出值 返回给调用者
```



- **`next(acc)`** 等价于 `send(None)`，只会让生成器跑到 `yield` 并产出右边的值，不会往 `yield` 里送有用数据。
- **`send(x)`** 做了两件事：
  1. 把 `x` 交给生成器（成为暂停处 `yield` 表达式的结果）。
  2. 继续运行到下一个 `yield`，并把 `yield` 右边的表达式值返回给调用者。
- 所以你收到的**永远是 `yield` 后面那个 `total` 的最新值**，而不是你刚 `send` 进去的数。

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

***

## 4. 命名空间

命名空间是变量名到对象的映射关系（字典结构）。

### 4.1 命名空间类型

| 命名空间   | 说明        | 示例                   |
| ------ | --------- | -------------------- |
| 内建命名空间 | 内置函数和关键字  | `print`、`len`、`True` |
| 全局命名空间 | 模块级别定义的变量 | 模块顶层的变量和函数           |
| 函数命名空间 | 函数调用时创建   | 函数内的局部变量             |
| 类命名空间  | 类定义时创建    | 类属性                  |
| 实例命名空间 | 实例化时创建    | 实例属性                 |

***

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

***

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

***

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

### 7.3 多层装饰器详解

#### 基本示例

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

#### 执行顺序详解

**关键规则：从下往上装饰，从外往内执行**

```python
@get_int      # 第二层装饰（外层）
@get_abs      # 第一层装饰（内层）
def func(n):
    return sqrt(n)
```

**装饰阶段（从下往上）：**

```python
# 等价于：
func = get_abs(func)    # 第一步：用 get_abs 装饰原始 func
func = get_int(func)    # 第二步：用 get_int 装饰已被 abs 装饰的 func
# 类似 ：func = get_int(get_abs(func)) ,外面一层装饰器接收的是内部一层装饰器返回的结果
# 上层的装饰器接收的是下面一层装饰器执行的结果，虽然是最外层最先执行，但是他是最后执行完毕并释放的
```

**调用阶段（从外往内）：**

```
func(-4)
   │
   ▼
get_int.inner(-4)           # 最外层：等待结果返回后转 int
   │ f 指向 get_abs.inner
   ▼
get_abs.inner(-4)           # 内层：先取绝对值
   │ f 指向原始 sqrt 函数
   │ n = abs(-4) = 4
   │ res = sqrt(4) = 2.0
   ▼
返回 2.0 到 get_int.inner
   │ res = int(2.0) = 2
   ▼
返回最终结果 2
```

**完整代码示例：**

```python
from math import sqrt

# 第一层装饰 --- 加求绝对值功能
def get_abs(f):
    def inner(n):
        n = abs(n)          # 先取绝对值
        res = f(n)          # 调用被装饰的函数
        return res
    return inner

# 第二层装饰 --- 将结果转换为整数
def get_int(f):
    def inner(n):
        res = f(n)          # 调用被装饰的函数（即 get_abs.inner）
        res = int(res)      # 将结果转为整数
        return res
    return inner

@get_int
@get_abs
def func(n):
    return sqrt(n)

print(func(-4))  # 输出：2
# 执行流程：-4 → abs(-4)=4 → sqrt(4)=2.0 → int(2.0)=2
```

#### 三层装饰器示例

```python
def decorator_a(func):
    def wrapper():
        print("A前")
        result = func()
        print("A后")
        return result
    return wrapper

def decorator_b(func):
    def wrapper():
        print("B前")
        result = func()
        print("B后")
        return result
    return wrapper

def decorator_c(func):
    def wrapper():
        print("C前")
        result = func()
        print("C后")
        return result
    return wrapper

@decorator_a
@decorator_b
@decorator_c
def say_hello():
    print("Hello!")

say_hello()
```

输出：

```
A前
B前
C前
Hello!
C后
B后
A后
```

> 理解：装饰像套娃，执行像洋葱（从外到内，再从内到外）。

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

#### 带参装饰器的执行过程

```python
@repeat(3)
def say(msg):
    print(msg)

# 等价于：
# 第一步：repeat(3) 返回 decorator 函数
# 第二步：decorator(say) 返回 wrapper 函数
# 最终：say = wrapper
```

#### 带参装饰器完整示例

```python
import functools

def log(level):                           # 第一层：接收装饰器参数
    def decorator(func):                  # 第二层：接收被装饰函数
        @functools.wraps(func)           # 保留原函数信息
        def wrapper(*args, **kwargs):    # 第三层：替代原函数
            print(f"[{level}] 调用函数: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{level}] 函数返回: {result}")
            return result
        return wrapper
    return decorator

@log("INFO")
def add(a, b):
    """两数相加"""
    return a + b

print(add(3, 5))
# 输出：
# [INFO] 调用函数: add
# [INFO] 函数返回: 8
# 8
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

***

## 总结

| 知识点     | 核心要点                                                  |
| ------- | ----------------------------------------------------- |
| 浅拷贝/深拷贝 | 浅拷贝只复制外层，深拷贝完全独立；非容器类型和纯元组不拷贝                         |
| 迭代器     | 需要 `__iter__()` + `__next__()`；`StopIteration` 表示遍历结束 |
| 生成器     | `yield` 暂停/恢复；`send()` 可发送数据；惰性求值节省内存                 |
| 命名空间    | 内建/全局/函数/类/实例，变量名到对象的映射                               |
| 作用域     | LEGB 查找顺序：局部 → 嵌套 → 全局 → 内建                           |
| 闭包      | 内层函数引用外层变量并被返回；`__closure__` 验证                       |
| 装饰器     | 本质是高阶函数；支持 @语法糖、多层嵌套、带参、类装饰器                          |

