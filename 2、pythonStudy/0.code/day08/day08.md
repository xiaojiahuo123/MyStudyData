# Day 08 学习笔记

## 8.1 __init__ 和 self 详解

### 8.1.1 __init__ 是什么

`__init__` 是 Python 类的**构造方法**，在创建对象时**自动调用**，用于初始化对象的属性。

### 8.1.2 self 是什么

`self` 代表**当前对象本身**，Python 自动传入，不需要手动传参。

### 8.1.3 代码示例

```python
# 类定义
class Dog:
    def __init__(self, name):
        self.name = name

# 创建对象
dog = Dog("旺财")

# 等价于：
# 1. 创建空对象
# 2. 自动调用 dog.__init__("旺财")
# 3. 执行 self.name = "旺财"（self 就是 dog）
# 4. 结果：dog.name = "旺财"
```

### 8.1.4 逐行解析

| 部分 | 含义 |
|------|------|
| `__init__` | Python 的**构造方法**，创建对象时自动调用 |
| `self` | 代表**当前对象本身**，Python 自动传入 |
| `name` | 构造方法的参数 |
| `self.name = name` | 将参数 `name` 存储为对象的**实例属性** |

### 8.1.5 与 Java 的对比

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

### 8.1.6 执行流程

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

*Day08 学习笔记持续更新中...*
