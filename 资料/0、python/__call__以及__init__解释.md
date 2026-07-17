# Python 中的 `__call__` 方法

`__call__` 是 Python 的一个特殊方法（dunder method），它让**类的实例可以像函数一样被调用**。

## 基本用法

```python
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

add5 = Adder(5)
print(add5(10))   # 输出: 15  — 实例被当作函数调用
print(add5(3))    # 输出: 8
```

当执行 `add5(10)` 时，Python 实际上调用的是 `add5.__call__(10)`。

## 主要用途

### 1. 创建可调用对象（有状态的函数）
普通函数是无状态的，而带有 `__call__` 的类实例可以保持内部状态：

```python
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### 2. 实现装饰器类
```python
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"调用 {self.func.__name__}，参数: {args}")
        result = self.func(*args, **kwargs)
        print(f"返回值: {result}")
        return result

@Logger
def add(a, b):
    return a + b

add(3, 5)
# 输出:
# 调用 add，参数: (3, 5)
# 返回值: 8
```

### 3. 策略模式 / 回调函数
```python
class MultiplyBy:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

operations = [MultiplyBy(2), MultiplyBy(3), MultiplyBy(5)]
for op in operations:
    print(op(10))  # 20, 30, 50
```

## 与普通函数的区别

| 特性 | 普通函数 | `__call__` 类实例 |
|------|---------|-------------------|
| 状态保持 | 需要闭包或全局变量 | 自然通过实例属性保持 |
| 可配置性 | 参数固定 | 构造时传入配置，调用时只传核心参数 |
| 可继承 | 不支持 | 支持继承、重写 |

## 判断是否为可调用对象

```python
class MyCallable:
    def __call__(self):
        pass

obj = MyCallable()
print(callable(obj))  # True
```

**总结**：`__call__` 的核心价值在于**让对象既是"东西"（有状态）又是"动作"（可调用）**，这在需要记忆状态、配置灵活的场景中非常实用。

---

# `__call__` 与 `__init__` 的区别

两者在类中的位置完全不同：

## 调用时机

| | `__init__` | `__call__` |
|---|---|---|
| **触发时机** | 创建实例时：`obj = MyClass()` | 把实例当函数调用时：`obj()` |
| **作用** | 初始化实例属性 | 定义实例被调用时的行为 |
| **调用次数** | 每个实例一次（构造时） | 无限次（每次调用实例都触发） |

```python
class Demo:
    def __init__(self, name):
        print(f"__init__ 被调用，name={name}")
        self.name = name

    def __call__(self, x):
        print(f"__call__ 被调用，x={x}，name={self.name}")
        return self.name * x

# __init__ 在这里触发
d = Demo("Hi")        # 输出: __init__ 被调用，name=Hi

# __call__ 在这里触发
d(3)                  # 输出: __call__ 被调用，x=3，name=Hi
d(2)                  # 输出: __call__ 被调用，x=2，name=Hi
```

## 类比理解

- `__init__` 是**出厂设置**：买一台计算器时设定精度
- `__call__` 是**每次使用**：每次按键计算时才真正执行运算

```python
class Calculator:
    def __init__(self, precision=2):
        """构造时设置配置"""
        self.precision = precision

    def __call__(self, a, b, op):
        """每次调用才执行计算"""
        import math
        result = {"+": a+b, "-": a-b, "*": a*b, "/": a/b}[op]
        return round(result, self.precision)

calc = Calculator(precision=3)  # __init__: 设定精度为3位
print(calc(10, 3, "/"))         # __call__: 执行 10/3 → 3.333
print(calc(2, 5, "*"))          # __call__: 执行 2*5  → 10
```

**一句话总结**：`__init__` 定义**这个对象是什么**（初始化），`__call__` 定义**这个对象做什么**（被调用时的行为）。

---

# 用 `__call__` + 字典存储和对比调用参数

核心思路：每次调用实例时，把参数存入内部字典，后续调用时可以对比是否已存在相同的参数组合。

## 示例：缓存计算结果（Memoization）

```python
class CachedAdd:
    def __init__(self):
        self.cache = {}  # 字典存储历史调用记录

    def __call__(self, a, b):
        key = (a, b)     # 用参数元组作为字典的键
        if key in self.cache:
            print(f"命中缓存: {a} + {b}")
        else:
            self.cache[key] = a + b
            print(f"新计算并缓存: {a} + {b}")
        return self.cache[key]

add = CachedAdd()
add(1, 2)   # 新计算并缓存: 1 + 2  → 返回 3
add(1, 2)   # 命中缓存: 1 + 2      → 返回 3
add(3, 4)   # 新计算并缓存: 3 + 4  → 返回 7
print(add.cache)  # {(1, 2): 3, (3, 4): 7}
```

## 示例：参数变化检测

```python
class ParamMonitor:
    def __init__(self):
        self.history = {}   # 存储每次调用的参数
        self.call_count = 0

    def __call__(self, **kwargs):
        self.call_count += 1
        key = f"call_{self.call_count}"
        self.history[key] = kwargs

        # 对比：是否有和当前参数完全相同的旧调用
        for k, v in self.history.items():
            if k != key and v == kwargs:
                print(f"参数与 {k} 完全相同！")
                return

        print(f"新参数组合已记录: {kwargs}")

monitor = ParamMonitor()
monitor(name="Alice", age=20)   # 新参数组合已记录
monitor(name="Bob", age=25)     # 新参数组合已记录
monitor(name="Alice", age=20)   # 参数与 call_1 完全相同！
```

## 示例：频率统计（同样的参数调用了多少次）

```python
class CallCounter:
    def __init__(self):
        self.records = {}

    def __call__(self, *args, **kwargs):
        # 用 frozenset 或 tuple 作为 key
        key = (args, tuple(sorted(kwargs.items())))
        self.records[key] = self.records.get(key, 0) + 1
        return self.records[key]

counter = CallCounter()
counter(1, 2)           # 返回 1（第1次用这些参数调用）
counter(1, 2)           # 返回 2
counter(1, 2)           # 返回 3
counter("hello", 5)     # 返回 1

print(counter.records)
# {((1, 2), ()): 3, (('hello', 5), ()): 1}
```

## 关键点

- **键的选择**：通常用 `tuple(args)` 或 `(args, tuple(sorted(kwargs.items())))` 作为字典键，因为参数可能是不可哈希的 list/dict
- **对比逻辑**：可以在 `__call__` 中自由定义——判断是否已存在、统计频率、返回缓存值等
- **本质**：`__call__` 让实例变成了一个"带内存的函数"，字典就是那块内存

---

# 装饰器类的运作原理：`@` 语法糖拆解

这是装饰器类最核心、也最容易困惑的地方——为什么 `__call__` 里不用显式传入 `func`？

## `@CacheDecorator` 等价于一句赋值

```python
@CacheDecorator
def expensive_add(a, b):
    return a + b
```

**完全等价于**：

```python
def expensive_add(a, b):
    return a + b

expensive_add = CacheDecorator(expensive_add)
#                               ^^^^^^^^^^^^^^^^
#                               原始函数作为参数传入 __init__
```

此时 `expensive_add` 不再是函数，而是一个 **`CacheDecorator` 的实例对象**。

## 分步追踪

```python
# 第1步：@CacheDecorator 触发，Python 执行:
expensive_add = CacheDecorator(expensive_add)
#  ↓ 调用 __init__(self, func)，self.func = 原始函数

# 第2步：后续调用 expensive_add(1, 2) 时
expensive_add(1, 2)
#  ↑ expensive_add 现在是个实例对象！
#  ↑ 对实例加括号 → 触发 __call__(self, 1, 2)
```

## 图解

```
原始:                    装饰后:
expensive_add ──函数──>  expensive_add ──实例──> CacheDecorator 对象
     ↑                                                 │
     │                                            self.func = 原始函数
     │                                                 │
调用: expensive_add(1,2)                         调用: expensive_add(1,2)
     │ 直接执行函数                                     │
     │                                          实例被调用 → __call__(self, 1, 2)
                                                   │
                                              在 __call__ 内部:
                                                  self.func(1, 2)  调用原始函数
```

## 为什么看起来"自动"？

因为 `__call__` 的本质就是：**实例对象 + 括号 → 自动调用 `__call__`**。

`func` 并不是绕过了 `__call__`，而是分两步走：

1. **装饰时**：`func` 传入 `__init__`，存到 `self.func`
2. **调用时**：`a, b` 传入 `__call__`，在内部用 `self.func(a, b)` 间接调用原始函数

`__call__` 能访问 `self.func`，因为它和 `__init__` 共享同一个 `self`（同一个实例）。

## 与函数装饰器的对比

| | 函数装饰器（闭包） | 类装饰器（`__call__`） |
|---|---|---|
| 状态保存 | 通过闭包变量 | 通过 `self` 实例属性 |
| 可读性 | 嵌套函数，层次多时难读 | 类结构清晰，逻辑分离 |
| 可扩展性 | 需要嵌套多层 | 支持继承、方法拆分 |
