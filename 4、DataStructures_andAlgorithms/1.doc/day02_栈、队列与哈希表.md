# Day02 - 栈、队列与哈希表

***

## 1. 栈（Stack）—— 后进先出的线性结构

### 概念

- 栈是一种**线性结构**
- 栈的一端称为**栈顶**，另一端称为**栈底**
- **入栈（压栈）**：从栈顶向栈中添加元素
- **出栈（弹栈）**：通过栈顶从栈中获取元素
- **特点：后进先出（LIFO - Last In First Out）**

### 图示

```
入栈顺序：push(1) → push(2) → push(3)

栈结构：
    ┌───┐
    │ 3 │  ← 栈顶（peek/pop 操作的位置）
    ├───┤
    │ 2 │
    ├───┤
    │ 1 │
    └───┘
```

### 实现方式：数组实现

```python
class Stack:
    def __init__(self):
        self.__items = []  # 用动态数组存储栈中元素
        self.__size = 0    # 栈中元素的个数

    @property
    def size(self):
        """返回栈中元素个数"""
        return self.__size

    def is_empty(self):
        """判断栈是否为空"""
        return self.__size == 0

    def push(self, item):
        """入栈：将元素放到栈中"""
        self.__items.append(item)
        self.__size += 1

    def pop(self):
        """出栈：从栈中将元素删除掉"""
        if self.is_empty():
            raise Exception("栈为空")
        item = self.__items[self.__size - 1]
        del self.__items[self.__size - 1]
        self.__size -= 1
        return item

    def peek(self):
        """获取栈顶元素，但是不出栈"""
        if self.is_empty():
            raise Exception("栈为空")
        return self.__items[self.__size - 1]
```

### 操作方法总结

| 方法 | 功能 | 时间复杂度 |
|------|------|-----------|
| `push(item)` | 入栈/压栈/进栈 | O(1) |
| `pop()` | 出栈/弹栈，返回并删除栈顶元素 | O(1) |
| `peek()` | 获取栈顶元素，但不出栈 | O(1) |
| `size` | 返回栈中元素个数 | O(1) |
| `is_empty()` | 判断栈是否为空 | O(1) |

***

## 2. 队列（Queue）—— 先进先出的线性结构

### 概念

- 队列是一种**线性结构**
- 队列的一端称为**队首**，另一端称为**队尾**
- **入队**：向队尾添加元素
- **出队**：从队首获取队列中元素
- **特点：先进先出（FIFO - First In First Out）**

### 图示

```
入队顺序：enqueue(10) → enqueue(20) → enqueue(30)

队列结构：
    出队 ←  [10] → [20] → [30]  ← 入队
            ↑                   ↑
          队首(head)          队尾(tail)
```

### 实现方式：链表实现

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def enqueue(self, data):
        """入队：向队列中添加元素"""
        new_node = Node(data)
        if self.is_empty():
            # 队列为空，新节点同时作为 head 和 tail
            self.__head = new_node
            self.__tail = new_node
        else:
            # 队列不为空，用 tail.next 追加
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1

    def dequeue(self):
        """出队：从队列中取元素"""
        if self.is_empty():
            raise Exception("队列为空")
        data = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        return data

    def peek(self):
        """访问队首元素"""
        if self.is_empty():
            raise Exception("队列为空")
        return self.__head.data
```

### 操作方法总结

| 方法 | 功能 | 时间复杂度 |
|------|------|-----------|
| `enqueue(data)` | 入队，向队尾添加元素 | O(1) |
| `dequeue()` | 出队，从队首获取并删除元素 | O(1) |
| `peek()` | 访问队首元素，但不出队 | O(1) |
| `size` | 获取队列中元素个数 | O(1) |
| `is_empty()` | 判断队列是否为空 | O(1) |

### 入队操作图示

```
1. 队列为空，入队 A：
   head = None, tail = None
   结果：head → [A] ← tail

2. 队列不为空，入队 B：
   head → [A] ← tail
   tail.next = B，tail = B
   结果：head → [A] → [B] ← tail

3. 继续入队 C：
   head → [A] → [B] ← tail
   tail.next = C，tail = C
   结果：head → [A] → [B] → [C] ← tail
```

***

## 3. 栈的应用 —— 括号匹配

### 题目描述（LeetCode 20）

给定一个只包括 `(`，`)`，`[`，`]`，`{`，`}` 的字符串 s，判断字符串是否有效。

有效字符串需满足：
- 左括号必须用相同类型的右括号闭合
- 左括号必须以正确的顺序闭合
- 每个右括号都有一个对应的相同类型的左括号

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `"()"` | true | |
| `"()[]{}"` | true | |
| `"(]"` | false | |
| `"([])"` | true | |

### 解题思路

- 遇到**左括号**则**入栈**
- 遇到**右括号**则**出栈**一个左括号与之匹配
- 如果能够匹配则继续，如果匹配失败或者栈为空则返回 False

### 代码实现

```python
class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            match char:
                case "(" | "[" | "{":
                    # 左括号入栈
                    stack.append(char)
                case ")":
                    if (not stack) or (stack.pop() != "("):
                        return False
                case "]":
                    if (not stack) or (stack.pop() != "["):
                        return False
                case "}":
                    if (not stack) or (stack.pop() != "{"):
                        return False
        return True if not stack else False
```

### 执行过程示例

```
输入：s = "([])"

处理 '('：stack = ['(']
处理 '['：stack = ['(', '[']
处理 ']'：
  - stack 不为空
  - stack.pop() = '['，匹配成功
  - stack = ['(']
处理 ')'：
  - stack 不为空
  - stack.pop() = '('，匹配成功
  - stack = []

最后：stack 为空，返回 True
```

***

## 4. 哈希表（HashTable）—— 数组 + 链表的结合体

### 概念

- 哈希表（散列表）是由**键值对**组成的数据结构
- 可以通过 **key** 快速定位 **value**
- 不是纯数组、也不是纯链表，是**数组和链表的结合体**
- 通过**哈希算法**，对 key 进行 hash 计算，得到 hash 值后对数组容量取模，得到数组下标

### 结构图示

```
哈希表结构：

索引0: None
索引1: (key1,val1) -> (key4,val4) -> None
索引2: (key2,val2) -> None
索引3: (key3,val3) -> (key5,val5) -> (key6,val6) -> None

数组部分：[None, 指针1, 指针2, 指针3]
              ↓        ↓        ↓
           链表1     链表2     链表3
```

### 哈希表存储结构详解

哈希表的，存储了key\value键值对形式的是节点，这些节点是存储在数组(python中是列表)中，如果不发生哈希冲突，他们都是存储在数组或者说列表中对应索引的单独的节点，如果发生了哈希冲突，在同一个索引处，冲突的节点用链表方式连接，因为本身节点就带有next这个指向下一个节点的指针

#### 1. 节点存储键值对

哈希表中的每个元素都是一个**节点**，节点存储了key-value键值对：

```python
class Node:
    def __init__(self, key, value):
        self.key = key      # 键
        self.value = value   # 值
        self.next = None     # 指向下一个节点的指针
```

#### 2. 数组 + 链表结构

哈希表由两部分组成：

- **数组（Python列表）**：作为主干，存储节点的引用
- **链表**：处理哈希冲突时，将多个节点连接起来

```
哈希表 = 数组（Python列表） + 链表（节点连接）

数组（列表）：
┌─────────────────────────────────────┐
│  0   │  1   │  2   │  3   │  ...   │
└─────────────────────────────────────┘
   │      │      │      │
   ▼      ▼      ▼      ▼
 节点   节点   节点   节点/链表
```

#### 3. 两种存储情况

**情况1：无哈希冲突（一个索引一个节点）**

当不同的key通过哈希函数计算后得到不同的index时，每个索引位置只有一个单独的节点：

```
索引0: (key1, val1) -> None
索引1: (key2, val2) -> None
索引2: None
索引3: (key3, val3) -> None
```

**情况2：有哈希冲突（一个索引多个节点，链表连接）**

当不同的key通过哈希函数计算后得到相同的index时，这些节点会用链表连接：

```
索引0: (key1, val1) -> None
索引1: (key2, val2) -> (key4, val4) -> None  # 冲突：key2和key4的hash值相同
索引2: None
索引3: (key3, val3) -> (key5, val5) -> (key6, val6) -> None  # 三个节点冲突
```

#### 4. 节点的next指针作用

- **无冲突时**：`next = None`（链表只有一个节点）
- **有冲突时**：`next` 指向下一个冲突的节点，形成链表

#### 5. 为什么用链表解决冲突

1. **灵活性**：链表可以动态增长，不受数组大小限制
2. **简单性**：只需修改节点的next指针
3. **效率**：插入操作时间复杂度为O(1)（链表头部插入）

#### 6. 代码示例

```python
# 创建哈希表
ht = HashTable()

# 无冲突情况
ht.put("apple", 10)   # hash("apple") % 4 = 1
ht.put("banana", 20)  # hash("banana") % 4 = 2
ht.put("cherry", 30)  # hash("cherry") % 4 = 3

# 有冲突情况（假设hash值相同）
ht.put("dog", 40)     # hash("dog") % 4 = 1  # 与"apple"冲突
ht.put("cat", 50)     # hash("cat") % 4 = 1  # 也与"apple"冲突

# 显示结果
ht.display()
# 输出：
# 索引为0:None
# 索引为1:(apple,10)->(dog,40)->(cat,50)->None  # 链表连接
# 索引为2:(banana,20)->None
# 索引为3:(cherry,30)->None
```

### 核心概念

| 概念 | 说明 |
|------|------|
| 哈希函数 | `hash(key) % capacity`，将 key 映射到数组下标 |
| 负载因子 | `元素个数 / 数组容量`，默认 0.7 |
| 扩容 | 当负载因子超过阈值时，数组容量翻倍 |

### 哈希函数详解

#### 什么是哈希函数
- **定义**：将任意长度的输入（key）转换为固定长度输出（哈希值）的函数
- **代码实现**：`def __hash(self, key): return hash(key) % self.__capacity`
- **作用**：计算键值对的key对应数组的索引位置

#### 哈希函数的工作原理

1. **调用内置hash函数**：`hash(key)` 将key转换为一个整数哈希值
2. **取模运算**：`% self.__capacity` 确保结果在有效索引范围内（0到capacity-1）
3. **返回索引**：得到数组下标，用于存储或查找键值对

#### 示例说明

假设数组容量为8，要存储key为"apple"的键值对：

```python
hash("apple") = 123456789  # 假设的哈希值
index = 123456789 % 8 = 5  # 数组索引为5
```

#### 哈希函数的特性

1. **确定性**：相同的key总是产生相同的哈希值
2. **高效性**：计算时间复杂度为O(1)
3. **均匀性**：好的哈希函数能让数据均匀分布在数组中
4. **抗碰撞性**：不同的key尽量产生不同的哈希值

#### 为什么需要哈希函数

- **快速定位**：通过O(1)时间复杂度直接找到存储位置
- **数据分布**：让数据均匀分布在数组中，避免聚集
- **减少冲突**：不同的key尽量映射到不同的索引

#### 哈希函数与负载因子的关系

当负载因子超过阈值时，`self.__capacity`会增大，此时相同key计算出的索引会改变，这就是为什么扩容后需要**重新哈希**所有元素。

```python
# 扩容前：capacity=4
hash("apple") % 4 = 1

# 扩容后：capacity=8
hash("apple") % 8 = 5  # 索引可能改变
```

### 负载因子详解

#### 什么是负载因子
- **定义**：`负载因子 = 已存储元素个数 / 哈希表数组容量`
- **代码中的设置**：`self.__load_factor = 0.7`，表示当哈希表填充率达到70%时触发扩容
- **计算公式**：`load_factor = size / capacity`

#### 负载因子的作用

1. **平衡空间与时间效率**
   - 负载因子太小（如0.3）：浪费内存空间，但查找速度快
   - 负载因子太大（如0.9）：内存利用率高，但冲突增多，查找变慢

2. **控制哈希冲突率**
   - 哈希冲突会导致链表变长或探测序列增加
   - 保持适中的负载因子可以减少冲突，维持O(1)的平均时间复杂度

3. **触发自动扩容**
   - 当负载因子超过阈值时，哈希表会自动扩容（通常是2倍）
   - 扩容后重新计算所有元素的位置，分散冲突

#### 为什么需要负载因子

- **性能保障**：避免哈希表过度拥挤导致性能退化
- **空间优化**：避免过早扩容浪费内存
- **动态调整**：根据实际使用情况自动优化存储结构

#### 实际应用示例

```python
# 当 添加元素后 元素个数/容量 > 负载因子时
if (self.__size + 1) / self.__capacity > self.__load_factor:
    self.__resize()  # 执行扩容操作
```

#### 负载因子的选择

| 负载因子 | 优点 | 缺点 | 适用场景 |
|----------|------|------|----------|
| 0.5-0.6 | 冲突少，查找快 | 内存利用率低 | 对性能要求极高的场景 |
| 0.7-0.75 | 平衡性能与空间 | 需要适时扩容 | 大多数通用场景 |
| 0.8-0.9 | 内存利用率高 | 冲突多，查找变慢 | 内存受限的场景 |

合理设置负载因子（通常0.6~0.75之间）是哈希表高效运行的关键。过小的负载因子会导致频繁扩容和内存浪费，过大的负载因子会增加冲突率，降低查找效率。

### 实现代码

```python
class Node:
    """链表节点"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.__size = 0
        self.__capacity = 2
        self.__table = [None] * self.__capacity
        self.__load_factor = 0.7

    def __hash(self, key):
        """哈希函数：计算数组下标"""
        return hash(key) % self.__capacity

    def put(self, key, value):
        """添加/更新元素"""
        # 计算数组下标
        index = self.__hash(key)
        new_node = Node(key, value)

        if self.__table[index] is None:
            # 该位置没有元素，直接作为头节点
            self.__table[index] = new_node
        else:
            # 该位置已有元素，遍历链表
            current = self.__table[index]
            while current:
                if current.key == key:
                    # key 相同，更新 value
                    current.value = value
                    return
                if current.next:
                    current = current.next
            # 链表末尾追加
            current.next = new_node
        self.__size += 1

    def get(self, key):
        """根据 key 获取 value"""
        index = self.__hash(key)
        current = self.__table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        """根据 key 删除元素"""
        index = self.__hash(key)
        current = self.__table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.__table[index] = current.next
                self.__size -= 1
                return True
            prev = current
            current = current.next
        return False
```

### 删除操作详解

#### 删除操作的两种情况

**情况1：删除头节点（prev为None）**

当要删除的节点是链表的第一个节点时，`prev`为None：

```python
# 链表状态：(apple,10) -> (dog,40) -> (cat,50) -> None
# 要删除：apple

prev = None  # prev为None，说明是头节点
current = (apple,10)

# 执行：
self.__table[index] = current.next  # 将数组位置指向下一个节点(dog,40)

# 结果：
# 索引1: (dog,40) -> (cat,50) -> None
# 原来的(apple,10)节点没有引用了，会被垃圾回收
```

**特殊情况：链表只有一个节点**

```python
# 链表状态：(apple,10) -> None
# 要删除：apple

prev = None
current = (apple,10)
current.next = None

# 执行：
self.__table[index] = current.next  # self.__table[index] = None

# 结果：
# 索引1: None
# 原来的(apple,10)节点没有引用了，会被垃圾回收
```

**情况2：删除非头节点（prev不为None）**

当要删除的节点不是链表的第一个节点时，`prev`不为None：

```python
# 链表状态：(apple,10) -> (dog,40) -> (cat,50) -> None
# 要删除：dog

# 第一次循环：
prev = None
current = (apple,10)
current.key == key? "apple" == "dog"? ✗
prev = (apple,10)  # 更新prev
current = (dog,40)  # 更新current

# 第二次循环：
prev = (apple,10)
current = (dog,40)
current.key == key? "dog" == "dog"? ✓

# 执行：
prev.next = current.next  # (apple,10).next = (cat,50)

# 结果：
# 索引1: (apple,10) -> (cat,50) -> None
# 原来的(dog,40)节点没有引用了，会被垃圾回收
```

#### 删除操作的关键点

| 情况 | prev状态 | 操作 | 结果 |
|------|----------|------|------|
| 删除头节点（唯一节点） | None | `self.__table[index] = None` | 数组位置变None |
| 删除头节点（有后续节点） | None | `self.__table[index] = current.next` | 数组位置指向下一个节点 |
| 删除中间节点 | 不为None | `prev.next = current.next` | 跳过当前节点 |
| 删除末尾节点 | 不为None | `prev.next = None` | 上一个节点指向None |

#### 垃圾回收机制

Python的垃圾回收机制会自动回收**没有引用的对象**：

```python
# 删除前
apple_node = Node("apple", 10)
self.__table[1] = apple_node  # 有引用

# 删除后
self.__table[1] = None  # apple_node没有引用了
# Python垃圾回收器会自动回收apple_node占用的内存
```

#### 删除操作流程图

```
删除操作流程：
                    ┌─────────────────┐
                    │  计算index      │
                    │  current = 头节点│
                    │  prev = None    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  while current  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ current.key == key? │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
    ┌─────────────────┐           ┌─────────────────┐
    │  相等           │           │  不相等         │
    │  执行删除操作    │           │  prev = current │
    │  return True    │           │  current = next │
    └─────────────────┘           └────────┬────────┘
                                           │
                                           ▼
                                  ┌─────────────────┐
                                  │  继续while循环   │
                                  └─────────────────┘
```

### 哈希冲突解决方法

当不同 key 映射到相同数组索引时，会发生**哈希冲突**。不同语言使用不同方法解决：

#### 1. 链地址法（拉链法）
- **原理**：每个数组位置指向一个链表，冲突的元素追加到链表中
- **优点**：实现简单，冲突多时性能稳定
- **缺点**：链表过长时查询退化为 O(n)
- **使用场景**：Java HashMap、Python dict（早期版本）

```
索引0: None
索引1: (key1,val1) -> (key4,val4) -> None  # 冲突的元素用链表连接
索引2: (key2,val2) -> None
```

#### 2. 开放寻址法
- **原理**：冲突时按规则寻找下一个空闲位置
- **优点**：数据存储在数组中，缓存友好
- **缺点**：容易产生聚集，删除操作复杂
- **使用场景**：Python dict（现代版本）、Go map

```
索引0: None
索引1: (key1,val1)
索引2: (key2,val2)  # 原本应放在索引1，冲突后放到索引2
索引3: (key3,val3)
```

#### 3. 再哈希法
- **原理**：使用多个哈希函数，冲突时用另一个哈希函数计算新位置
- **优点**：不易产生聚集
- **缺点**：计算成本高
- **使用场景**：较少使用

#### 4. 建立公共溢出区
- **原理**：冲突元素放入另一个数组（溢出区）
- **优点**：实现简单
- **缺点**：溢出区过大时性能下降
- **使用场景**：较少使用

### 不同语言的实现差异

| 语言 | 冲突解决方法 | 特点 |
|------|-------------|------|
| **Java** (HashMap) | 链地址法 + 红黑树优化 | 链表长度超过8时转为红黑树 |
| **Python** (dict) | 开放寻址法（伪随机探测） | 现代版本使用开放寻址，性能更好 |
| **Go** (map) | 链地址法 | 使用哈希桶 + 溢出桶 |
| **C++** (unordered_map) | 链地址法 | 可自定义哈希函数 |

### 为什么数组是主干？

1. **随机访问**：通过索引直接访问，O(1) 时间复杂度
2. **连续内存**：数组在内存中连续存储，缓存友好
3. **容量可控**：通过负载因子控制扩容时机

### 操作方法总结

| 方法 | 功能 | 时间复杂度（平均） | 时间复杂度（最坏） |
|------|------|-----------------|-----------------|
| `put(key, value)` | 添加/更新元素 | O(1) | O(n) |
| `get(key)` | 根据 key 获取 value | O(1) | O(n) |
| `remove(key)` | 根据 key 删除元素 | O(1) | O(n) |

### 扩容机制

```python
def __grow(self):
    """扩容数组"""
    self.__capacity *= 2
    self.__table, old_table = [None] * self.__capacity, self.__table
    self.__size = 0

    # 重新哈希所有元素
    for node in old_table:
        current = node
        while current:
            self.put(current.key, current.value)
            current = current.next
```

### 扩容过程图示

```
扩容前（capacity=2，负载因子>0.7）：
索引0: (1,10) -> (3,30) -> None
索引1: (2,20) -> None

扩容后（capacity=4，重新哈希）：
索引0: None
索引1: (1,10) -> None
索引2: (2,20) -> None
索引3: (3,30) -> None
```

***

## 总结：栈 vs 队列

| 特性 | 栈（Stack） | 队列（Queue） |
|------|------------|--------------|
| 原则 | 后进先出（LIFO） | 先进先出（FIFO） |
| 添加 | push（栈顶） | enqueue（队尾） |
| 删除 | pop（栈顶） | dequeue（队首） |
| 实现 | 数组或链表 | 数组或链表 |
| 典型应用 | 括号匹配、函数调用栈 | 任务调度、消息队列 |

***

*持续更新中...*
