# Day10 异常处理

---

## 1. 综合案例：愤怒的小鸟（面向对象复习）

> 对应文件：P01_Game.py

通过"愤怒的小鸟"游戏案例，复习面向对象的**继承**、**多态**、`isinstance` 判断等知识点，同时为后续异常处理做铺垫。

**核心设计：**
- `Birds` 基类：定义共性（名字、颜色、技能描述、飞、叫、使用技能）
- `RedBirds`、`YellowBirds`、`BlueBirds` 子类：各自重写 `fly()` 和 `call()`，体现多态
- `Obstacle` 障碍物类：通过 `isinstance` 判断鸟的类型，决定伤害值

```python
class Birds:
    def __init__(self, name, color, skill_description):
        self.name = name
        self.color = color
        self.skill_description = skill_description

    def use_skill(self):
        print(f"{self.name}使用了{self.skill_description}进行了攻击")

class RedBirds(Birds):
    def __init__(self):
        super().__init__("红火", "红色", "撞击前方障碍物，造成大量伤害")

class Obstacle:
    def be_attacked(self, bird):
        if isinstance(bird, RedBirds):      # 根据类型决定伤害
            damage = 80
        elif isinstance(bird, YellowBirds):
            damage = 50
        else:
            damage = 30 * 3
        self.strength -= damage
```

---

## 2. 异常介绍：try-except

> 对应文件：P02_Exception.py

程序运行时可能发生错误（异常），如果不处理，程序会直接崩溃。`try-except` 可以捕获异常，让程序继续运行。

```python
try:
    result = 3 / 0          # ZeroDivisionError
    print(result)
except:
    print("程序运行的时候发生了异常")

print("程序执行结束")        # 不会因为异常而中断，正常执行
```

**执行流程：**
1. 执行 `try` 块中的代码
2. 如果发生异常，跳到 `except` 块执行
3. 如果没有异常，跳过 `except` 块
4. 无论是否异常，`try-except` 之后的代码继续执行

**不处理异常 vs 处理异常：**
```python
# 不处理 → 程序崩溃
result = 3 / 0              # 直接报错，后续代码不执行
print("这行不会执行")

# 处理 → 程序继续
try:
    result = 3 / 0
except:
    print("出错了")
print("这行会执行")          # 正常输出
```

---

## 3. 异常类型与多分支捕获

> 对应文件：P03_Exception_Type.py

Python 有多种内置异常类型，可以精确捕获特定类型的异常。

**常见异常类型：**

| 异常类型 | 触发场景 |
|---------|---------|
| `ZeroDivisionError` | 除以零 |
| `NameError` | 使用未定义的变量 |
| `TypeError` | 类型操作不当（`"a" + 1`） |
| `ValueError` | 值不合法（`int("abc")`） |
| `IndexError` | 索引越界 |
| `KeyError` | 字典键不存在 |
| `AttributeError` | 属性/方法不存在 |
| `FileNotFoundError` | 文件不存在 |

**多分支捕获：**
```python
try:
    result = 3 / 0
except NameError as e:                  # 精确捕获NameError
    print(e)
except (RuntimeError, TypeError) as e:  # 捕获多种类型（元组写法）
    print(e)
except:                                 # 兜底，捕获所有异常
    print("Unexpected error")
print("End")
```

**执行规则：**
- `except` 分支从上往下匹配，**只执行第一个匹配到的分支**
- `as e` 可以获取异常对象，`e` 包含异常信息
- 不带异常类型的 `except` 是兜底，放在最后

---

## 4. try-except-else

> 对应文件：P04_Else.py

`else` 块在 **没有发生异常时** 执行。

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零！")
else:
    print(f"结果是: {result}")    # 有异常 → 不执行
```

```python
try:
    result = 10 / 1
    print(f"结果是: {result}")    # 输出：结果是: 10.0
except ZeroDivisionError:
    print("除数不能为零！")
```

**为什么要用 else？**
把正常逻辑放在 `else` 中，可以避免 `try` 块中的代码意外捕获到本不该捕获的异常：

```python
# 不好的写法：try中代码太多，可能掩盖问题
try:
    result = 10 / 1
    print(result)           # 如果print本身出错，会被except捕获
except ZeroDivisionError:
    print("除数不能为零")

# 好的写法：else中放正常逻辑
try:
    result = 10 / 1
except ZeroDivisionError:
    print("除数不能为零")
else:
    print(result)           # 只有除法成功才执行，职责清晰
```

---

## 5. try-except-else-finally

> 对应文件：P05_Finally.py

`finally` 块 **无论是否发生异常都会执行**，通常用于资源清理（关闭文件、断开连接等）。

**完整结构：**
```python
try:
    result = 3 / 0
except ZeroDivisionError as e:
    print(e)            # 执行 → 捕获到异常
else:
    print(result)       # 跳过 → 有异常不执行else
finally:
    print("finally")    # 执行 → 无论如何都执行

print("End")
```

**执行顺序总结：**

| 情况 | try | except | else | finally |
|------|-----|--------|------|---------|
| 没有异常 | 执行 | 跳过 | 执行 | 执行 |
| 有异常且被捕获 | 执行（到异常行） | 执行 | 跳过 | 执行 |
| 有异常但没被捕获 | 执行（到异常行） | 跳过 | 跳过 | 执行 |

---

## 6. raise 手动抛出异常

> 对应文件：P06_Raise.py

### 解释器自动抛出 vs 手动raise

**解释器自动抛出（运行时错误）：**
```python
1 / 0                       # ZeroDivisionError
"a" + 1                     # TypeError
"hello".xyz()               # AttributeError
```
这些都是代码本身有bug，解释器帮你检测到并抛出。

**手动raise（业务逻辑检查）：**
```python
def add(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise TypeError("参数类型错误")  # 代码语法没问题，但不符合业务要求
```
这里语法上完全合法，`add(1, 2.0)` 不会报错，会返回 `3.0`。但从业务角度要求两个参数都是int，所以需要手动抛出。

### 核心区别

| | 解释器自动抛出 | 手动raise |
|--|---------------|----------|
| 原因 | 代码有语法/运行时错误 | 代码没错误，但不符合业务规则 |
| 例子 | `1/0`、`"a"+1` | 参数不合法、权限不足、余额不足 |
| 不抛出会怎样 | 程序崩溃 | 程序继续运行，但结果可能不正确 |

### 实际场景

```python
# 场景1：余额不足（解释器不会报错，需要你手动判断）
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("余额不足")
    return balance - amount

# 场景2：权限不足
def delete_file(user, filename):
    if user.role != "admin":
        raise PermissionError("无删除权限")

# 场景3：参数验证
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError("年龄不合法")
```

### 不使用raise会怎样

```python
def add(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        return None  # 不抛出，静默返回None

# 调用方不知道参数有问题
result = add(1, "hello")
print(result)          # None
print(result + 1)      # TypeError: NoneType + int
                       # 错误被延迟暴露，更难排查
```

### 总结

```
解释器自动抛出 → 代码有bug（语法错误、类型错误等）
手动raise     → 代码没问题，但业务规则不允许（参数不合法、权限不足、余额不足等）

raise的本质：你比解释器更清楚什么是"错误"，所以你主动定义错误条件。
```

---

## 7. assert 断言

> 对应文件：P07_assert.py

`assert` 是一种简化的参数验证方式，**条件为False时抛出 `AssertionError`**。

```python
def int_add(x, y):
    assert isinstance(x, int) and isinstance(y, int), "参数类型错误"
    return x + y

print(int_add(1, 2))        # 3
print(int_add("1", "2"))    # AssertionError: 参数类型错误
```

### assert vs raise

```python
# assert 写法（简洁）
assert isinstance(x, int), "参数类型错误"

# 等价于 raise 写法（更灵活）
if not isinstance(x, int):
    raise AssertionError("参数类型错误")
```

| | assert | raise |
|--|--------|-------|
| 写法 | 一行搞定 | 需要 if + raise |
| 灵活性 | 只能抛 AssertionError | 可以抛任意异常类型 |
| 用途 | 快速参数校验、调试 | 业务逻辑、正式代码 |

> **注意**：`assert` 可以被 `python -O` 优化模式禁用，因此不适合用于正式的业务验证。正式代码推荐用 `raise`。

---

## 8. 自定义异常

> 对应文件：P08_Custom_Exception.py

当内置异常类型不能满足需求时，可以自定义异常类，**继承 `Exception`** 即可。

```python
class MyException(Exception):
    def __init__(self, value):
        self.value = value

try:
    raise MyException("这是我自己定义的异常")  # 手动抛出自定义异常
except MyException as e:
    print(f"发生异常了{e}")
```

**执行流程：**
1. 进入 `try` 块
2. 执行 `raise MyException(...)` → 主动抛出异常
3. `try` 块剩余代码**跳过**，跳到 `except`
4. 匹配到 `MyException`，执行 `except` 块

**自定义异常的实际用途：**
```python
class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortage = amount - balance

    def __str__(self):
        return f"余额不足：余额{self.balance}，需要{self.amount}，缺少{self.shortage}"

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientBalanceError as e:
    print(e)  # 余额不足：余额100，需要200，缺少100
```

---

## 9. 异常的传递

> 对应文件：P09_Exception_Pass.py

异常会沿着调用栈**向上传层传递**，直到被 `try-except` 捕获。

### 嵌套 try-except 的传递

```python
try:                                    # 第一层
    try:                                # 第二层
        try:                            # 第三层
            print(1 / 0)               # ZeroDivisionError 发生在这里
        except NameError as e:          # 第三层：不匹配（不是NameError）
            print("第三层", e)
    except TypeError as e:              # 第二层：不匹配（不是TypeError）
        print("第二层", e)
except Exception as e:                  # 第一层：Exception匹配所有异常 ✅
    print("第一层", type(e), e)         # 输出：第一层 <class 'ZeroDivisionError'> ...
```

**规则：** 异常从内层往外层传递，直到找到匹配的 `except`。如果所有层都没捕获，程序崩溃。

### 函数调用中的传递

```python
def m1():
    m2()

def m2():
    m3()

def m3():
    print(1/0)          # ZeroDivisionError

m1()                    # 异常从 m3 → m2 → m1 → 顶层，没有被捕获则程序崩溃
```

**如果用 try-except 包裹调用：**
```python
try:
    m1()                # m3中发生的异常会传递到这里被捕获
except ZeroDivisionError as e:
    print(f"捕获到异常：{e}")
```

---

## 10. with 上下文管理器

> 对应文件：P10_With.py

`with` 可以**自动管理资源**（如文件），保证资源在使用后被正确释放。

### 问题：手动关闭文件不可靠

```python
# 写法1：close()可能不被执行
try:
    file = open("test.txt", "w")
    file.write(a)       # a未定义 → NameError
    file.close()        # ← 被跳过！文件没有关闭
finally:
    print("文件是否关闭：", file.closed)  # False
```

### 解决方案：嵌套 try-finally

```python
# 写法2：保证关闭，但代码繁琐
try:
    file = open("test.txt", "w")
    try:
        file.write(a)
    finally:
        file.close()            # 无论是否异常都执行 ✅
finally:
    print("文件是否关闭：", file.closed)  # True
```

### 最佳方案：with

```python
# 写法3：with 自动关闭 ✅
try:
    with open("test.txt", "w") as file:
        file.write(a)
finally:
    print("文件是否关闭：", file.closed)  # True
```

### with 的实现原理：上下文管理器协议

`with` 依赖对象的两个魔术方法：`__enter__()` 和 `__exit__()`。

```python
with open("test.txt", "w") as file:
    file.write("hello")
```

等价于：
```python
file = open("test.txt", "w").__enter__()   # 进入时调用
try:
    file.write("hello")
finally:
    open("test.txt", "w").__exit__()        # 退出时必定调用
```

**自定义上下文管理器：**
```python
class MyFile:
    def __init__(self, filename):
        self.filename = filename
        print("打开文件")

    def __enter__(self):
        print("进入 with 块")
        return self                         # 返回值赋给 as 后面的变量

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("离开 with 块，自动清理资源")
        return False                        # False 不吞异常

    def write(self, content):
        print(f"写入: {content}")

with MyFile("test.txt") as f:
    f.write("hello")

# 输出：
# 打开文件
# 进入 with 块
# 写入: hello
# 离开 with 块，自动清理资源
```

### 总结

```
with 对象 as 变量:
    代码块

1. 调用 对象.__enter__()   → 返回值赋给 变量
2. 执行 代码块
3. 无论是否异常，都调用 对象.__exit__()  ← 自动关闭的原理
```

---

## 全章总结

```
try-except          → 捕获异常，防止程序崩溃
except 异常类型      → 精确捕获特定异常
as e                → 获取异常对象
else                → 没有异常时执行
finally             → 无论如何都执行（资源清理）
raise               → 手动抛出异常（业务规则验证）
assert              → 简化的断言检查（调试用）
自定义异常           → 继承Exception，定义业务专属异常
异常传递             → 异常沿调用栈向上传递，直到被捕获
with                → 上下文管理器，自动管理资源的获取和释放
```
