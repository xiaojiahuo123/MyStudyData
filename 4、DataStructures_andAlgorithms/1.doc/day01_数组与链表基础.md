## 1. array.array 访问行为 —— 底层存储与Python访问的差异

- `array.array` 内部存储的是原始 C int 数值，紧凑无对象开销
- 但用 Python 访问时（`arr[0]`），Python 自动将原始值包装成 Python int 对象返回
- 小整数（-5 到 256）命中缓存池，所以 `id(arr[0])` 和 `id(1)` 可能相同

| <br />        | 存储时（内存布局）           | 访问时（Python 代码）       |
| ------------- | ------------------- | -------------------- |
| `array.array` | 原始 C int，紧凑无对象开销    | 自动转成 Python int 对象返回 |
| `list`        | Python int 对象的引用/指针 | 直接返回引用指向的对象          |

***

## 2. `[0] * capacity` 预分配数组 —— 模拟底层数组的内存预分配机制

```python
self.__capacity = 5
self.__items = [0] * self.__capacity   # [0, 0, 0, 0, 0]
self.__size = 0                        # 实际元素数为 0
```

- `[0] * capacity` 创建一个用 0 填充的固定大小列表，模拟底层数组的内存预分配
- `0` 只是占位符，表示"空槽位"，后续会被真实数据覆盖
- `__size` 记录实际存储的元素数量（从 0 开始增长）
- `__capacity` 是预分配的总容量（固定不变，除非扩容）

```
capacity=5, size=0:  [0, 0, 0, 0, 0]     ← 全是空槽位
capacity=5, size=3:  [1, 2, 3, 0, 0]     ← 前 3 个是真实数据
                     ↑size=3，只看前 3 个
```

***

## 3. `__str__` 方法（Python 版 toString） —— 对象的字符串表示与自动调用机制

```python
def __str__(self):
    return "对象的字符串表示"
```

- 等价于 Java 的 `toString()` 重写
- `print(obj)` 和 `str(obj)` 时**自动调用**，不需要手动调用
- 不重写时，`print(obj)` 输出 `<类名 object at 0x地址>`

***

## 4. 单向链表（LinkedList）核心概念 —— 节点结构与链表操作的实现原理

### 链表结构 vs 节点结构

```python
class Node:
    """节点类：存储数据和指向下一个节点的链接"""
    def __init__(self, data, next=None):
        self.data = data      # 存储数据
        self.next = next      # 指向下一个节点

class LinkedList:
    """链表类：维护入口节点"""
    def __init__(self):
        self.__head = None    # 头节点，指向第一个节点
        self.__size = 0       # 链表长度
```

### 关键区分

| 角色                  | 职责                      |
| ------------------- | ----------------------- |
| `LinkedList.__head` | 链表类维护的**入口**，指向第一个节点    |
| `Node.next`         | 每个节点自己维护的**链接**，指向下一个节点 |

### 链表结构图示

```
LinkedList（链表类）
    │
    └── __head ──────────────→ Node（第一个节点）
                                    │
                                    ├── data = 1
                                    └── next ──→ Node（第二个节点）
                                                      │
                                                      ├── data = 2
                                                      └── next ──→ Node（第三个节点）
                                                                        │
                                                                        ├── data = 3
                                                                        └── next = None
```

### 形象比喻

```
LinkedList 就像一个"导游"
    └── __head：导游知道第一个景点在哪

Node 就像一个个"景点"
    └── next：每个景点知道下一个景点在哪
```

### 链表基本操作

| 方法                    | 功能       | 时间复杂度 |
| --------------------- | -------- | ----- |
| `insert(index, item)` | 在指定位置插入  | O(n)  |
| `append(item)`        | 在末尾追加    | O(n)  |
| `remove(index)`       | 删除指定位置   | O(n)  |
| `set(index, item)`    | 修改指定位置   | O(n)  |
| `get(index)`          | 获取指定位置   | O(n)  |
| `find(item)`          | 查找元素是否存在 | O(n)  |

### 插入操作图示

```python
# 在头部插入
self.__head = Node(item, self.__head)
# 新节点的 next 指向原来的 head，然后 head 指向新节点

# 在中间插入
node.next = Node(item, node.next)
# 新节点的 next 指向 node.next，然后 node.next 指向新节点
```

```
插入前：head -> [1] -> [2] -> [3] -> None
在位置1插入99：
插入后：head -> [1] -> [99] -> [2] -> [3] -> None
```

***

## 5. 双向链表（Doubly Linked List） —— 双向遍历与O(1)删除的优势

### 与单向链表的核心区别

| 单向链表        | 双向链表                      |
| ----------- | ------------------------- |
| 只能向后遍历      | 可以前后双向遍历                  |
| `node.next` | `node.prev` + `node.next` |
| 删除需要找前驱节点   | 删除不需要找前驱                  |

### 结构定义

```python
class Node:
    """双向链表节点"""
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev    # 指向前一个节点
        self.next = next    # 指向后一个节点

class DoublyLinkedList:
    """双向链表"""
    def __init__(self):
        self.__head = None  # 头节点，指向第一个节点
        self.__tail = None  # 尾节点，指向最后一个节点
        self.__size = 0
```

### 关键区分

| 概念                  | 说明              |
| ------------------- | --------------- |
| `LinkedList.__head` | 链表的入口，指向第一个节点   |
| `LinkedList.__tail` | 链表的出口，指向最后一个节点  |
| `Node.prev`         | 节点内部的链接，指向前一个节点 |
| `Node.next`         | 节点内部的链接，指向后一个节点 |

### 结构图示

```
单向链表：
head -> [1] -> [2] -> [3] -> None

双向链表：
head -> [1] <--> [2] <--> [3] <- tail
        ↑                      ↑
      prev=None              next=None
```

### 节点创建过程

```
1. 创建第一个节点（值为1）：
   head ──→ [1] ←── tail
            ↑
           prev=None, next=None

2. 追加第二个节点（值为2）：
   head ──→ [1] <──→ [2] ←── tail
            ↑         ↑
         prev=None  prev=[1], next=None

3. 追加第三个节点（值为3）：
   head ──→ [1] <──→ [2] <──→ [3] ←── tail
            ↑         ↑         ↑
         prev=None  prev=[1]  prev=[2]
                    next=[3]  next=None
```

### 优缺点对比

| 特性    | 单向链表      | 双向链表       |
| ----- | --------- | ---------- |
| 空间    | 省（一个指针）   | 费（两个指针）    |
| 删除    | O(n) 需找前驱 | O(1) 已知节点时 |
| 反向遍历  | 不支持       | 支持         |
| 实现复杂度 | 简单        | 较复杂        |

### 删除操作优势

```python
# 已知要删除的节点，直接删除
node_to_delete = ...  # 已知节点引用

# 单向链表：需要从头遍历找前驱，O(n)
# 双向链表：直接通过 prev 获取前驱，O(1)
node_to_delete.prev.next = node_to_delete.next
node_to_delete.next.prev = node_to_delete.prev
```

### 典型应用：LRU 缓存

LRU（Least Recently Used）缓存需要频繁移动和删除节点，双向链表的 O(1)删除优势非常明显。

### 核心理解

链表是链表，节点是节点，链表尤其是双向链表，他的头节点和尾节点只是链表中的首尾两个节点，但是每个节点本身存在两个指针，prev指向上一个节点，next指向下一个节点

***

## 6. 链表遍历：`for i in range(index - 1)` 的作用 —— 通过循环次数定位目标节点的原理

### 代码场景

```python
def insert(self, index, item):
    if index == 0:
        self.__head = Node(item, self.__head)
    else:
        node = self.__head
        for i in range(index - 1):  # 找到 index-1 位置的节点
            node = node.next
        node.next = Node(item, node.next)
```

### 核心目的

**找到插入位置的前一个节点**，然后在它后面插入新节点。

### 图示过程

假设要在位置2插入元素99：

```
链表：head -> [1] -> [2] -> [3] -> None
索引：        0      1      2

目标：在位置2插入99
需要找到：位置1的节点（即 index-1 = 1）
```

### 执行过程

```python
# index = 2，要找位置1的节点
node = self.__head  # node 指向位置0的节点 [1]

# range(2-1) = range(1)，循环1次
for i in range(1):
    node = node.next  # node 从 [1] 移动到 [2]
    # 这个循环的主要作用就是通过循环次数不断使用node = node.next，最终获取到需要插入位置的前一个节点

# 循环结束，node 指向位置1的节点 [2]
# 现在可以在 node 后面插入新节点
node.next = Node(99, node.next)
```

### 为什么是 `index - 1`？

```
插入位置：2
前一个位置：2 - 1 = 1

head -> [1] -> [2] -> [3] -> None
              ↑
           要找的节点（位置1）

找到后，在 [2] 后面插入 [99]：
head -> [1] -> [2] -> [99] -> [3] -> None
```

### 不同 index 值的循环次数

| `index` | `range(index - 1)` | 循环次数 | 最终位置 |
| ------- | ------------------ | ---- | ---- |
| 0       | 头部插入，不走循环          | 0    | -    |
| 1       | `range(0)`         | 0    | 位置0  |
| 2       | `range(1)`         | 1    | 位置1  |
| 3       | `range(2)`         | 2    | 位置2  |

### 总结

```python
for i in range(index - 1):
    node = node.next
```

- **目的：** 从头节点开始，移动 `index-1` 次，到达目标位置的前一个节点
- **原理：** 链表无法随机访问，必须从头遍历
- **时间复杂度：** O(n)

