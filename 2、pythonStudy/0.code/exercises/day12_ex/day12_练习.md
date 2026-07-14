# Day12 练习知识点总结

## 1. 浅拷贝与深拷贝

### 1.1 浅拷贝（copy.copy）

浅拷贝只复制**外层容器**，内层元素仍共享引用：

```python
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

original[0][0] = 99
print(shallow)  # [[99, 2], [3, 4]]  ← 内层列表被修改了
print(shallow[0] is original[0])  # True  ← 内层是同一个对象
```

### 1.2 深拷贝（copy.deepcopy）

深拷贝**递归复制所有嵌套对象**，与原对象完全独立：

```python
original2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(original2)

original2[0][0] = 99
print(deep)  # [[1, 2], [3, 4]]  ← 不受影响
print(deep[0] is original2[0])  # False  ← 内层也是独立的
```

### 1.3 元组的拷贝特殊性

**`copy.copy()` 对元组直接返回原对象**，无论内部元素是否可变：

```python
t1 = ([1, 2], [3, 4])
t2 = copy.copy(t1)
print(t1 is t2)        # True  ← 同一个对象
print(t1[0] is t2[0])  # True  ← 内部元素也是同一个

t3 = copy.deepcopy(t1)
print(t1 is t3)        # False ← 深拷贝才创建新对象
print(t1[0] is t3[0])  # False
```

**原因**：Python 认为元组是不可变类型（不能增删元素），`copy.copy()` 直接返回原对象。只有 `deepcopy` 才会创建全新对象。

### 1.4 非容器类型的拷贝

不可变非容器类型（int、str、float）调用 `copy.copy` 直接返回原对象：

```python
a = 42
b = copy.copy(a)
print(a is b)  # True，不可变类型无需拷贝
```

### 1.5 总结

| 对象类型 | `copy.copy()` | `copy.deepcopy()` |
|---------|---------------|-------------------|
| 不可变非容器（int/str） | 返回原对象 | 返回原对象 |
| 纯不可变元组 `(1, 2)` | 返回原对象 | 返回原对象 |
| 含可变元素的元组 `([1],)` | 返回**原对象** | 创建全新对象 |
| 可变容器（list/dict） | 新容器，内层共享 | 完全独立 |

---

## 2. 迭代器

### 2.1 iter() 与 next()

```python
nums = [10, 20, 30]
it = iter(nums)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# next(it)  →  抛出 StopIteration
```

- `iter()` 将可迭代对象转为迭代器
- `next()` 逐个取值，取完后抛出 `StopIteration`

### 2.2 自定义迭代器类

实现 `__iter__()` 和 `__next__()` 协议即可：

```python
class Countdown:
    def __init__(self, data):
        self.index = data + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index - 1 == 0:
            raise StopIteration
        self.index -= 1
        return self.index
```

**常见错误**：
- 忘记修改 `self.index` → 无限循环
- 先减再返回 vs 先返回再减 → 序列不同

### 2.3 迭代器的内存优势

迭代器按需生成（惰性求值），不一次性存储所有元素：

```python
import sys

data_list = [x ** 2 for x in range(100_000)]  # 列表：占用大量内存
data_gen = (x ** 2 for x in range(100_000))   # 生成器：只占用几十字节

print(sys.getsizeof(data_list))  # ~800KB
print(sys.getsizeof(data_gen))   # ~200字节
```

**适用场景**：需要遍历大量数据但不需要全部存储时用生成器；需要随机访问或多次遍历时用列表。

---

## 3. 生成器

### 3.1 yield 执行流程

```python
def countdown(n):
    print(f">>> countdown 开始, n={n}")
    while n > 0:
        yield n
        n -= 1
    print(">>> 发射!")

gen = countdown(3)
print(next(gen))  # "countdown 开始" → 3
print(next(gen))  # 2
print(next(gen))  # 1
next(gen)         # "发射!" → StopIteration
```

**执行顺序**：
1. 调用生成器函数时，函数体**不执行**，返回生成器对象
2. 第一次 `next()` 时才开始执行，到 `yield` 暂停并返回值
3. 后续 `next()` 从暂停处继续
4. 循环结束后执行剩余代码，抛出 `StopIteration`

### 3.2 send() 方法

`send(value)` 既恢复执行，又向生成器内部发送数据：

```python
def accumulator():
    total = 0
    while True:
        value = yield total     # yield 返回 total，同时接收 send 的值
        if value is None:
            break
        total += value

acc = accumulator()
print(next(acc))          # 0（必须先 next 激活到 yield 处）
print(acc.send(10))       # 10
print(acc.send(20))       # 30
print(acc.send(30))       # 60
```

**关键**：第一次必须调用 `next()` 或 `send(None)`，因为生成器还没执行到 `yield`，没有地方接收 `send()` 发送的值。

### 3.3 生成器表达式

```python
list_comp = [x ** 2 for x in range(5)]  # 列表推导式 → list
gen_expr = (x ** 2 for x in range(5))   # 生成器表达式 → generator

print(type(gen_expr))  # <class 'generator'>
print(list(gen_expr))  # [0, 1, 4, 9, 16]
```

直接 `print(gen_expr)` 不会显示数值，而是显示生成器对象的内存地址。

---

## 4. 作用域 LEGB

### 4.1 LEGB 查找顺序

```
L (Local)       局部作用域 → 函数内部
E (Enclosing)   嵌套作用域 → 外层函数
G (Global)      全局作用域 → 模块级别
B (Built-in)    内建作用域 → Python 内置
```

```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # "local" (L)
    inner()
    print(x)      # "enclosing" (E)
outer()
print(x)          # "global" (G)
```

### 4.2 global 关键字

在函数内修改**全局变量**必须声明 `global`：

```python
count = 0
def increment():
    global count     # 声明使用全局变量
    count += 1       # 不加 global 会报 UnboundLocalError
```

### 4.3 nonlocal 关键字

在内层函数中修改**外层函数的局部变量**必须声明 `nonlocal`：

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count  # 声明使用外层变量
        count += 1
        return count
    return counter
```

---

## 5. 闭包

### 5.1 闭包的三个条件

1. 有嵌套函数
2. 内层函数引用了外层函数的变量
3. 外层函数返回内层函数对象

### 5.2 闭包变量的存储位置

闭包变量保存在函数的**闭包细胞对象**中：

```python
c = make_counter()
print(c.__closure__)                      # (<cell at 0x...>,)
print(c.__closure__[0].cell_contents)     # 0  ← count 就在这里
```

外层函数执行完毕后，局部变量 `count` 本应销毁，但因被内层函数引用，Python 将其移入闭包细胞对象中保留。只要函数对象还活着，闭包变量就不会被回收。

### 5.3 闭包工厂函数

利用闭包实现带状态的函数工厂：

```python
def create_accumulator():
    total = 0
    def accumulator(x):
        nonlocal total
        total += x
        return total
    return accumulator    # 注意：不能写 return accumulator()

acc = create_accumulator()
print(acc(10))  # 10
print(acc(20))  # 30
print(acc(30))  # 60
```

**常见错误**：`return accumulator()` 会立即调用函数并缺少参数，应该返回函数对象本身 `return accumulator`。

### 5.4 闭包陷阱：循环中的闭包

```python
# ❌ Bug 版本：所有闭包共享同一个 i
def create_multipliers_bug():
    multipliers = []
    for i in range(5):
        def multiplier(x):
            return x * i    # i 是循环结束后的值 4
        multipliers.append(multiplier)
    return multipliers

# 结果：所有函数都返回 x * 4

# ✅ 修复：用默认参数捕获当前值
def create_multipliers_fixed():
    multipliers = []
    for i in range(5):
        def multiplier(x, i=i):    # 默认参数在定义时求值
            return x * i
        multipliers.append(multiplier)
    return multipliers

# 结果：分别返回 x*0, x*1, x*2, x*3, x*4
```

---

## 6. 装饰器

### 6.1 装饰器本质

装饰器是一个**接收函数并返回新函数**的可调用对象：

```python
def timer(func):
    @functools.wraps(func)       # 保留原函数元信息
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} 耗时: {end - start:.4f} 秒")
        return result
    return wrapper
```

### 6.2 functools.wraps 的作用

保留被装饰函数的 `__name__`、`__doc__` 等元信息：

```python
# 不使用 wraps
@bad_decorator
def say_hello():
    """打招呼"""
    pass
print(say_hello.__name__)  # "wrapper"  ← 丢失了原函数名

# 使用 wraps
@good_decorator
def say_hello():
    """打招呼"""
    pass
print(say_hello.__name__)  # "say_hello"  ← 保留了原函数名
```

### 6.3 函数属性存储状态

装饰器可以通过**函数属性**为被装饰函数添加额外状态：

```python
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1       # 通过函数属性存储计数
        result = func(*args, **kwargs)
        return result
    wrapper.call_count = 0            # 必须在函数定义之后初始化
    return wrapper
```

**关键**：`wrapper.call_count = 0` 必须写在 `def wrapper(...)` 之后、`return wrapper` 之前。如果写在函数内部作为局部变量，需要用 `nonlocal`；用函数属性更简洁。

### 6.4 time.perf_counter()

高精度秒表，用于测量代码执行耗时：

```python
start = time.perf_counter()
# ... 要测量的代码 ...
end = time.perf_counter()
print(f"耗时: {end - start} 秒")
```

- 返回值本身没有意义，只有**两次调用的差值**才有效
- 精度达到纳秒级，比 `time.time()` 更精确

### 6.5 多层装饰器执行顺序

```python
@decorator_A
@decorator_B
@decorator_C
def my_function():
    pass

# 等价于：my_function = A(B(C(my_function)))
```

- **装饰阶段**：从下往上（先 C，再 B，最后 A）
- **执行阶段**：从外往内（A 前 → B 前 → C 前 → 核心 → C 后 → B 后 → A 后）

---

## 常见错误总结

| 错误类型 | 示例 | 修复 |
|---------|------|------|
| 忘记 `nonlocal` | `count += 1`（UnboundLocalError） | 加 `nonlocal count` |
| 返回函数调用 | `return accumulator()` | `return accumulator` |
| 未修改迭代器状态 | `return self.index - 1`（无限循环） | `self.index -= 1; return self.index` |
| `wrapper` 参数不通用 | `def wrapper(name)` | `def wrapper(*args, **kwargs)` |
| 函数属性未初始化 | 使用前未设置 `wrapper.call_count = 0` | 在 `def wrapper` 之后初始化 |
| 闭包陷阱 | 循环中闭包共享变量 | 用默认参数 `i=i` 捕获 |
| `pass` 位置错误 | `return` 之后的 `pass`（死代码） | 删除或移到正确位置 |
