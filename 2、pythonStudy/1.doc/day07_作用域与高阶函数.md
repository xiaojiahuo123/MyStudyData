# Day 07 学习笔记

## 7.1 global 关键字

### 7.1.1 什么是 global

`global` 关键字用于在**函数内部声明一个变量是全局变量**，从而允许在函数内修改全局作用域中的变量。

### 7.1.2 为什么需要 global

Python 中，如果在函数内部直接给变量赋值，Python 会将其视为**局部变量**，而不是修改全局变量。

```python
count = 0

def increment():
    count += 1  # ❌ 错误！UnboundLocalError
    # 等同于 count = count + 1，右边的 count 还未定义

increment()
```

### 7.1.3 global 的用法

```python
count = 0

def increment():
    global count  # 声明 count 是全局变量
    count += 1

increment()
increment()
increment()
print(f"count = {count}")  # 3
```

### 7.1.4 执行过程

```
初始状态:
┌─────────────────────────────────┐
│  全局作用域                       │
├─────────────────────────────────┤
│  count = 0                       │
└─────────────────────────────────┘

increment() 第一次调用后:
┌─────────────────────────────────┐
│  全局作用域                       │
├─────────────────────────────────┤
│  count = 1                       │
└─────────────────────────────────┘

increment() 第三次调用后:
┌─────────────────────────────────┐
│  全局作用域                       │
├─────────────────────────────────┤
│  count = 3                       │
└─────────────────────────────────┘
```

### 7.1.5 global 的使用场景

| 场景 | 说明 |
|------|------|
| **计数器** | 在函数中累加全局计数器 |
| **状态管理** | 函数需要修改全局状态标志 |
| **配置修改** | 函数需要修改全局配置变量 |
| **缓存** | 函数需要更新全局缓存 |

### 7.1.6 注意事项

```python
# ✅ 正确：使用 global 声明
x = 10
def func():
    global x
    x = 20

# ❌ 避免：过度使用 global
# 全局变量会导致代码难以维护和调试

# ❌ 错误：在嵌套函数中使用 global 修改外层局部变量
def outer():
    count = 0
    def inner():
        global count  # 这会创建新的全局变量，不是 outer 的 count！
        count += 1
    inner()
    print(count)  # 仍然是 0
```

---

## 7.2 nonlocal 关键字

### 7.2.1 什么是 nonlocal

`nonlocal` 关键字用于在**嵌套函数中修改外层（但不是全局）函数的变量**。

### 7.2.2 为什么需要 nonlocal

在嵌套函数中，内层函数可以**读取**外层函数的变量，但不能**修改**。

```python
def outer():
    num = 10
    def inner():
        num += 5  # ❌ 错误！UnboundLocalError
    inner()
    print(num)

outer()
# nonlocal 只在"修改"时才需要
```

### 7.2.3 nonlocal 的用法

```python
def outer():
    num = 10
    def inner():
        nonlocal num  # 声明 num 是外层函数的变量
        num += 5
    inner()
    inner()
    print(f"num = {num}")

outer()  # num = 20
```

### 7.2.4 执行过程

```
outer() 调用时:
┌─────────────────────────────────┐
│  outer 作用域                    │
├─────────────────────────────────┤
│  num = 10                        │
└─────────────────────────────────┘

inner() 第一次调用后:
┌─────────────────────────────────┐
│  outer 作用域                    │
├─────────────────────────────────┤
│  num = 15                        │
└─────────────────────────────────┘

inner() 第二次调用后:
┌─────────────────────────────────┐
│  outer 作用域                    │
├─────────────────────────────────┤
│  num = 20                        │
└─────────────────────────────────┘
```

### 7.2.5 nonlocal 的使用场景

| 场景 | 说明 |
|------|------|
| **闭包** | 在闭包中修改外层函数的变量 |
| **装饰器** | 在装饰器中维护状态 |
| **计数器** | 在嵌套函数中使用计数器 |
| **状态机** | 在内部函数中修改状态 |

### 7.2.6 nonlocal vs global 对比

| 特性 | nonlocal | global |
|------|----------|--------|
| **作用范围** | 外层函数（非全局） | 全局作用域 |
| **使用场景** | 嵌套函数 | 普通函数 |
| **修改目标** | 外层函数的局部变量 | 全局变量 |
| **声明位置** | 内层函数 | 函数内部 |

### 7.2.7 示例对比

```python
# ===== global 示例 =====
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1

# ===== nonlocal 示例 =====
def outer():
    count = 0
    def increment():
        nonlocal count
        count += 1
    increment()
    return count

print(outer())  # 1
```

### 7.2.8 注意事项

```python
# ✅ 正确：使用 nonlocal 声明
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)  # 20

# ❌ 错误：nonlocal 只能用于嵌套函数
x = 10
def func():
    nonlocal x  # SyntaxError!

# ❌ 错误：nonlocal 不能声明全局变量
def func():
    global x  # 这是声明全局变量
    nonlocal x  # SyntaxError!
```

---

## 7.3 global vs nonlocal 总结

| 概念 | global | nonlocal |
|------|--------|----------|
| **定义** | 声明全局变量 | 声明外层函数变量 |
| **作用域** | 全局作用域 | 外层函数作用域 |
| **使用场景** | 普通函数修改全局变量 | 嵌套函数修改外层变量 |
| **记忆口诀** | "global 管全局" | "nonlocal 管外层" |

---

## 7.4 作用域链（Scope Chain）

### 7.4.1 LEGB 规则

Python 查找变量的顺序遵循 **LEGB 规则**：

| 顺序 | 作用域 | 说明 |
|------|--------|------|
| **L** | Local | 局部作用域（函数内部） |
| **E** | Enclosing | 外层函数作用域（嵌套函数） |
| **G** | Global | 全局作用域（模块级别） |
| **B** | Built-in | 内置作用域（Python 内置） |

### 7.4.2 示例

```python
x = "global"  # Global

def outer():
    x = "enclosing"  # Enclosing
    
    def inner():
        x = "local"  # Local
        print(x)  # local (L)
    
    inner()
    print(x)  # enclosing (E)

outer()
print(x)  # global (G)
```

### 7.4.3 作用域图示

```
┌─────────────────────────────────────────────┐
│  Built-in 作用域（len, print, int 等）        │
├─────────────────────────────────────────────┤
│  Global 作用域（模块级别）                    │
│  ┌─────────────────────────────────────────┐│
│  │  Enclosing 作用域（outer 函数）           ││
│  │  ┌─────────────────────────────────────┐││
│  │  │  Local 作用域（inner 函数）          │││
│  │  └─────────────────────────────────────┘││
│  └─────────────────────────────────────────┘│
└─────────────────────────────────────────────┘
```

---

## 7.5 总结

| 关键字 | 用途 | 使用场景 |
|--------|------|----------|
| **global** | 声明全局变量 | 函数内修改全局变量 |
| **nonlocal** | 声明外层函数变量 | 嵌套函数修改外层变量 |

> **记忆口诀**：
> - global 管"全局"，函数内改全局
> - nonlocal 管"外层"，嵌套改外层
> - LEGB 查找顺序：Local → Enclosing → Global → Built-in

---

## 7.6 lambda 表达式

### 7.6.1 什么是 lambda

`lambda` 是 Python 中创建**匿名函数**的关键字，适用于简短的一次性函数。

### 7.6.2 语法格式

```python
lambda 参数列表: 表达式
```

- 只能包含**一个表达式**
- 表达式的结果就是返回值
- 不需要 `return` 关键字

### 7.6.3 基础示例

```python
# 普通函数
def square(x):
    return x ** 2

# 等价的 lambda 表达式
square = lambda x: x ** 2
print(square(4))   # 16
print(square(10))  # 100

# 多个参数
add = lambda a, b: a + b
print(add(3, 5))   # 8
```

### 7.6.4 lambda vs 普通函数

| 特性 | lambda | 普通函数 |
|------|--------|----------|
| **名称** | 匿名 | 有函数名 |
| **表达式** | 只能一个 | 任意多个 |
| **可读性** | 简洁 | 更清晰 |
| **复用性** | 低（一次性） | 高（可复用） |
| **调试** | 困难（无函数名） | 容易 |

### 7.6.5 使用场景

```python
# 1. 排序时指定排序规则
students = [("张三", 85), ("李四", 92), ("王五", 78)]
students.sort(key=lambda x: x[1])  # 按分数排序
print(students)  # [('王五', 78), ('张三', 85), ('李四', 92)]

# 2. 字典排序
scores = {"张三": 85, "李四": 92, "王五": 78}
sorted_scores = sorted(scores.items(), key=lambda x: x[1])
print(sorted_scores)  # [('王五', 78), ('张三', 85), ('李四', 92)]

# 3. 条件过滤
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x > 3, nums))
print(result)  # [4, 5]
```

---

## 7.7 map 函数

### 7.7.1 什么是 map

`map()` 函数用于对序列中的每个元素应用指定函数，返回一个迭代器。

### 7.7.2 语法格式

```python
map(function, iterable, ...)
```

| 参数 | 说明 |
|------|------|
| `function` | 要应用的函数 |
| `iterable` | 一个或多个可迭代对象 |

### 7.7.3 基础示例

```python
# 对每个元素翻倍
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, nums))
print(result)  # [2, 4, 6, 8, 10]

# 使用普通函数
def double(x):
    return x * 2

result = list(map(double, nums))
print(result)  # [2, 4, 6, 8, 10]

# 多个序列
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = list(map(lambda x, y: x + y, list1, list2))
print(result)  # [11, 22, 33]
```

### 7.7.4 map 执行过程

```
nums = [1, 2, 3, 4, 5]
map(lambda x: x * 2, nums)

执行过程:
┌─────┬─────┬─────┬─────┬─────┐
│  1  │  2  │  3  │  4  │  5  │  ← 输入
└──┬──┴──┬──┴──┬──┴──┬──┴──┬──┘
   │     │     │     │     │
   ▼     ▼     ▼     ▼     ▼
   ×2    ×2    ×2    ×2    ×2    ← 应用函数
   │     │     │     │     │
   ▼     ▼     ▼     ▼     ▼
┌─────┬─────┬─────┬─────┬─────┐
│  2  │  4  │  6  │  8  │ 10  │  ← 输出
└─────┴─────┴─────┴─────┴─────┘
```

---

## 7.8 filter 函数

### 7.8.1 什么是 filter

`filter()` 函数用于根据指定条件过滤序列中的元素，返回一个迭代器。

### 7.8.2 语法格式

```python
filter(function, iterable)
```

| 参数 | 说明 |
|------|------|
| `function` | 过滤条件（返回 True 保留，False 过滤） |
| `iterable` | 要过滤的可迭代对象 |

### 7.8.3 基础示例

```python
# 过滤正数
nums = [1, -2, 3, -4, 5, -6]
result = list(filter(lambda x: x > 0, nums))
print(f"正数: {result}")  # [1, 3, 5]

# 过滤偶数
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(f"偶数: {result}")  # [2, 4, 6]

# 过滤空字符串
words = ["hello", "", "world", "", "python"]
result = list(filter(None, words))  # 使用 None 过滤假值
print(result)  # ['hello', 'world', 'python']
```

### 7.8.4 filter 执行过程

```
nums = [1, -2, 3, -4, 5, -6]
filter(lambda x: x > 0, nums)

执行过程:
┌─────┬─────┬─────┬─────┬─────┬─────┐
│  1  │ -2  │  3  │ -4  │  5  │ -6  │  ← 输入
└──┬──┴──┬──┴──┬──┴──┬──┴──┬──┴──┬──┘
   │     │     │     │     │     │
   ▼     ▼     ▼     ▼     ▼     ▼
  >0?   >0?   >0?   >0?   >0?   >0?  ← 检查条件
   │     │     │     │     │     │
  Yes   No    Yes   No    Yes   No   ← 判断结果
   │           │           │
   ▼           ▼           ▼
┌─────┬─────┬─────┐
│  1  │  3  │  5  │  ← 输出
└─────┴─────┴─────┘
```

---

## 7.9 reduce 函数

### 7.9.1 什么是 reduce

`reduce()` 函数用于对序列进行累积计算，需要从 `functools` 模块导入。

### 7.9.2 语法格式

```python
from functools import reduce
reduce(function, iterable[, initializer])
```

| 参数 | 说明 |
|------|------|
| `function` | 累积函数（接收两个参数） |
| `iterable` | 要处理的可迭代对象 |
| `initializer` | 可选初始值 |

### 7.9.3 基础示例

```python
from functools import reduce

# 计算总和
nums = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, nums)
print(result)  # 15 (1+2+3+4+5)

# 计算乘积
result = reduce(lambda x, y: x * y, nums)
print(result)  # 120 (1*2*3*4*5)

# 使用初始值
result = reduce(lambda x, y: x + y, nums, 10)
print(result)  # 25 (10+1+2+3+4+5)
```

### 7.9.4 reduce 执行过程

```
nums = [1, 2, 3, 4, 5]
reduce(lambda x, y: x + y, nums)

执行过程:
第1次: x=1, y=2 → 3
第2次: x=3, y=3 → 6
第3次: x=6, y=4 → 10
第4次: x=10, y=5 → 15

┌─────┬─────┬─────┬─────┬─────┐
│  1  │  2  │  3  │  4  │  5  │
└──┬──┴──┬──┴──┬──┴──┬──┴──┬──┘
   │     │     │     │     │
   └──┬──┘     │     │     │
      ▼        │     │     │
      3 ──────┬┘     │     │
             ▼        │     │
             6 ───────┬┘     │
                     ▼        │
                    10 ───────┬┘
                              ▼
                             15  ← 最终结果
```

---

## 7.10 sorted 函数

### 7.10.1 什么是 sorted

`sorted()` 函数返回一个新的排序列表，不修改原序列。

### 7.10.2 语法格式

```python
sorted(iterable, *, key=None, reverse=False)
```

| 参数 | 说明 |
|------|------|
| `iterable` | 要排序的可迭代对象 |
| `key` | 排序依据的函数 |
| `reverse` | 是否降序（默认 False 升序） |

### 7.10.3 基础示例

```python
# 基本排序
nums = [3, 1, 4, 1, 5, 9]
result = sorted(nums)
print(result)  # [1, 1, 3, 4, 5, 9]

# 降序排序
result = sorted(nums, reverse=True)
print(result)  # [9, 5, 4, 3, 1, 1]

# 按长度排序
words = ["banana", "apple", "cherry"]
result = sorted(words, key=len)
print(result)  # ['apple', 'banana', 'cherry']

# 按字典值排序
students = [("张三", 85), ("李四", 92), ("王五", 78)]
result = sorted(students, key=lambda x: x[1])
print(result)  # [('王五', 78), ('张三', 85), ('李四', 92)]
```

### 7.10.4 sorted vs sort

| 特性 | sorted() | list.sort() |
|------|----------|-------------|
| **返回值** | 新列表 | None（原地排序） |
| **原列表** | 不变 | 被修改 |
| **适用对象** | 任何可迭代对象 | 只能是列表 |
| **返回类型** | 始终是列表 | None |

---

## 7.11 enumerate 函数

### 7.11.1 什么是 enumerate

`enumerate()` 函数用于在遍历时同时获取索引和值。

### 7.11.2 语法格式

```python
enumerate(iterable, start=0)
```

| 参数 | 说明 |
|------|------|
| `iterable` | 要遍历的可迭代对象 |
| `start` | 索引起始值（默认 0） |

### 7.11.3 基础示例

```python
# 基本用法
fruits = ["苹果", "香蕉", "橙子"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 输出:
# 0: 苹果
# 1: 香蕉
# 2: 橙子

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# 输出:
# 1: 苹果
# 2: 香蕉
# 3: 橙子
```

### 7.11.4 执行过程

```
fruits = ["苹果", "香蕉", "橙子"]
enumerate(fruits)

执行过程:
┌─────────┬─────────┐
│  index  │  value  │
├─────────┼─────────┤
│    0    │  苹果   │
│    1    │  香蕉   │
│    2    │  橙子   │
└─────────┴─────────┘
```

---

## 7.12 zip 函数

### 7.12.1 什么是 zip

`zip()` 函数用于将多个可迭代对象"拉链"式组合在一起。

### 7.12.2 语法格式

```python
zip(*iterables, strict=False)
```

| 参数 | 说明 |
|------|------|
| `*iterables` | 一个或多个可迭代对象 |
| `strict` | 是否要求长度一致（Python 3.10+） |

### 7.12.3 基础示例

```python
# 基本用法
names = ["张三", "李四", "王五"]
scores = [85, 92, 78]
result = list(zip(names, scores))
print(result)  # [('张三', 85), ('李四', 92), ('王五', 78)]

# 多个序列
names = ["张三", "李四", "王五"]
scores = [85, 92, 78]
grades = ["良好", "优秀", "良好"]
result = list(zip(names, scores, grades))
print(result)  # [('张三', 85, '良好'), ('李四', 92, '优秀'), ('王五', 78, '良好')]

# 解压
pairs = [('张三', 85), ('李四', 92), ('王五', 78)]
names, scores = zip(*pairs)
print(names)   # ('张三', '李四', '王五')
print(scores)  # (85, 92, 78)
```

### 7.12.4 执行过程

```
names = ["张三", "李四", "王五"]
scores = [85, 92, 78]
zip(names, scores)

执行过程:
names   ──→ ┌─────┐ ┌─────┐ ┌─────┐
            │张三 │ │李四 │ │王五 │
            └──┬──┘ └──┬──┘ └──┬──┘
               │       │       │
               ▼       ▼       ▼
scores  ──→ ┌─────┐ ┌─────┐ ┌─────┐
            │ 85  │ │ 92  │ │ 78  │
            └──┬──┘ └──┬──┘ └──┬──┘
               │       │       │
               └───┬───┘       │
                   └─────┬─────┘
                         ▼
                  [('张三',85),('李四',92),('王五',78)]
```

---

## 7.13 any 和 all 函数

### 7.13.1 any 函数

`any()` 函数检查可迭代对象中是否有任意一个元素为真。

```python
# 有任意一个为真就返回 True
nums = [0, 0, 1, 0]
print(any(nums))  # True (因为有 1)

# 全部为假返回 False
nums = [0, 0, 0]
print(any(nums))  # False

# 检查是否有正数
nums = [-1, -2, 3, -4]
print(any(x > 0 for x in nums))  # True
```

### 7.13.2 all 函数

`all()` 函数检查可迭代对象中是否所有元素都为真。

```python
# 全部为真返回 True
nums = [1, 2, 3, 4]
print(all(nums))  # True

# 有任意一个为假返回 False
nums = [1, 2, 0, 4]
print(all(nums))  # False

# 检查是否全部为正数
nums = [1, 2, 3, 4]
print(all(x > 0 for x in nums))  # True
```

### 7.13.3 any vs all 对比

| 特性 | any() | all() |
|------|-------|-------|
| **逻辑** | 任意一个为真 | 全部为真 |
| **短路** | 找到真立即返回 | 找到假立即返回 |
| **空序列** | 返回 False | 返回 True |
| **类似** | OR (\|\|) | AND (&&) |

---

## 7.14 reversed 函数

### 7.14.1 什么是 reversed

`reversed()` 函数返回一个反向迭代器，不修改原序列。

### 7.14.2 语法格式

```python
reversed(seq)
```

### 7.14.3 基础示例

```python
# 基本用法
nums = [1, 2, 3, 4, 5]
result = list(reversed(nums))
print(result)  # [5, 4, 3, 2, 1]

# 原列表不变
print(nums)  # [1, 2, 3, 4, 5]

# 字符串反转
s = "hello"
result = ''.join(reversed(s))
print(result)  # "olleh"

# 在 for 循环中使用
for num in reversed([1, 2, 3]):
    print(num)  # 3, 2, 1
```

### 7.14.4 reversed vs 切片反转

| 特性 | reversed() | [::-1] |
|------|-----------|--------|
| **返回值** | 迭代器 | 新列表 |
| **内存** | 惰性，节省内存 | 立即创建完整列表 |
| **原序列** | 不变 | 不变 |
| **可重复使用** | 否（迭代器） | 是 |

---

## 7.15 常用函数对比总结

| 函数 | 用途 | 返回值 | 是否修改原序列 |
|------|------|--------|---------------|
| **lambda** | 创建匿名函数 | 函数对象 | - |
| **map** | 对每个元素应用函数 | 迭代器 | 否 |
| **filter** | 根据条件过滤元素 | 迭代器 | 否 |
| **reduce** | 累积计算 | 单个值 | 否 |
| **sorted** | 排序 | 新列表 | 否 |
| **enumerate** | 添加索引 | 迭代器 | 否 |
| **zip** | 组合多个序列 | 迭代器 | 否 |
| **any** | 任意一个为真 | 布尔值 | 否 |
| **all** | 全部为真 | 布尔值 | 否 |
| **reversed** | 反转序列 | 迭代器 | 否 |

---

## 7.16 使用场景总结

| 场景 | 推荐函数 | 示例 |
|------|----------|------|
| **转换数据** | map | `list(map(lambda x: x*2, nums))` |
| **过滤数据** | filter | `list(filter(lambda x: x>0, nums))` |
| **累积计算** | reduce | `reduce(lambda x,y: x+y, nums)` |
| **排序** | sorted / .sort() | `sorted(nums, key=lambda x: x)` |
| **带索引遍历** | enumerate | `for i, v in enumerate(nums)` |
| **组合序列** | zip | `list(zip(list1, list2))` |
| **检查条件** | any / all | `any(x > 0 for x in nums)` |
| **反转序列** | reversed / [::-1] | `list(reversed(nums))` |

---

## 7.17 lambda 排序实战

### 7.17.1 按字典值排序

```python
students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 18, "score": 92},
    {"name": "王五", "age": 22, "score": 78},
]

# 按年龄升序排序
by_age = sorted(students, key=lambda s: s["age"])
print(f"按年龄排序: {[s['name'] for s in by_age]}")
# ['李四', '张三', '王五']

# 按成绩降序排序
by_score = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"按成绩降序: {[s['name'] for s in by_score]}")
# ['李四', '张三', '王五']
```

### 7.17.3 多条件排序

```python
# 先按成绩降序，成绩相同按年龄升序
students = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 18, "score": 92},
    {"name": "王五", "age": 22, "score": 78},
    {"name": "赵六", "age": 20, "score": 92},
]

# 使用元组实现多条件排序
result = sorted(students, key=lambda s: (-s["score"], s["age"]))
print([(s['name'], s['score'], s['age']) for s in result])
# [('李四', 92, 18), ('赵六', 92, 20), ('张三', 85, 20), ('王五', 78, 22)]
```

### 7.17.4 lambda 排序技巧总结

| 需求 | lambda 表达式 |
|------|---------------|
| 按值升序 | `lambda x: x` |
| 按值降序 | `lambda x: -x` |
| 按字典值 | `lambda x: x["key"]` |
| 按字符串长度 | `lambda x: len(x)` |
| 忽略大小写 | `lambda x: x.lower()` |
| 多条件排序 | `lambda x: (条件1, 条件2)` |

---

## 7.18 文件操作（with 语句）

### 7.18.1 什么是 with 语句

`with` 语句用于**自动管理资源**（如文件），确保使用后正确关闭，即使发生异常也能保证资源释放。

### 7.18.2 语法格式

```python
with open(文件名, 模式, encoding=编码) as 变量:
    # 使用文件的操作
# 离开 with 块后，文件自动关闭
```

### 7.18.3 文件打开模式

| 模式 | 说明 |
|------|------|
| `"r"` | 只读（默认） |
| `"w"` | 写入（覆盖已有内容） |
| `"a"` | 追加（在末尾添加） |
| `"x"` | 创建（文件已存在则报错） |
| `"r+"` | 读写 |
| `"rb"` | 二进制读取 |
| `"wb"` | 二进制写入 |

### 7.18.4 写入文件

```python
# 将内容写入文件
scores = "张三 85\n李四 92\n王五 78\n"

with open("test_scores.txt", "w", encoding="utf-8") as f:
    f.write(scores)

# 文件会自动关闭，无需手动调用 f.close()
```

### 7.18.5 读取文件

```python
# 读取整个文件内容
with open("test_scores.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 逐行读取
with open("test_scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip() 去除换行符

# 读取所有行到列表
with open("test_scores.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)  # ['张三 85\n', '李四 92\n', '王五 78\n']
```

### 7.18.6 with vs 不使用 with

```python
# ❌ 不推荐：手动管理文件
f = open("test.txt", "w")
try:
    f.write("hello")
finally:
    f.close()  # 必须手动关闭

# ✅ 推荐：使用 with 语句
with open("test.txt", "w") as f:
    f.write("hello")
# 自动关闭，无需手动管理
```

### 7.18.7 with 语句执行流程

```
with open("test.txt", "w") as f:
    f.write("hello")

执行流程:
┌─────────────────────────────────────────────┐
│  1. 打开文件，返回文件对象 f                  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  2. 执行 with 块内的代码                      │
│     f.write("hello")                        │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  3. 离开 with 块，自动调用 f.close()          │
│     即使发生异常也会关闭！                     │
└─────────────────────────────────────────────┘
```

### 7.18.8 实用示例：学生成绩管理

```python
scores = "张三 85\n李四 92\n王五 78\n"

# 1. 写入文件
with open("test_scores.txt", "w", encoding="utf-8") as f:
    f.write(scores)

# 2. 读取并处理
with open("test_scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, score = line.strip().split()
        print(f"{name}: {score}")

# 输出:
# 张三: 85
# 李四: 92
# 王五: 78
```

### 7.18.9 文件操作最佳实践

| 场景 | 推荐方式 |
|------|----------|
| 读取整个文件 | `f.read()` |
| 逐行处理 | `for line in f` |
| 读取所有行 | `f.readlines()` |
| 写入内容 | `f.write()` |
| 追加内容 | `open("a")` |
| 处理大文件 | 逐行读取，避免 `read()` |

> **记忆口诀**：文件操作用 with，自动关闭不用愁！

---

*Day07 学习笔记完成*
