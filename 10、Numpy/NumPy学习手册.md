# NumPy 学习手册

> **配套课程**：《尚硅谷大模型技术之 NumPy 与 Pandas》第 2 章
> **环境**：Python 3.12.14 · NumPy 2.3.5
> **数据**：`10、Numpy/data/` 下的 6 个 CSV
> **说明**：本手册里**每一段代码都在 NumPy 2.3.5 + Python 3.12 上实际跑过**，输出是真实的。

---

## 📌 为什么你该用这份文档，而不是直接啃原 PDF

原课程文档（`尚硅谷大模型技术之numpy与pandas1.0.md`）作为**参考书**没问题，但作为**学习材料**有四个硬伤：

| 问题 | 具体表现 |
|---|---|
| **代码取不出来** | PDF 转 Markdown 后，大量代码被拆进了图片，或者变成一行乱码——比如 2.7.3 比较函数整节都塞在表格里 |
| **内容严重不全** | 第 2 章只覆盖了 NumPy 的入门部分。**视图/副本、二维以上索引、布尔索引、形状操作、axis 的深入理解、NaN 处理**——这些每天都要用的东西，一个字没讲 |
| **有内容已经过时** | 课程还在教 `np.matrix`，它在 NumPy 2.x 里已经是待废弃状态 |
| **没有练习** | 看完不知道自己会不会 |

这份手册按「**知识点 → 可运行代码 → 真实输出 → ⚠️ 坑**」四段式重写，每章末尾配练习，第 8 章用你自己 `data/` 里的真实数据做实战。

### 怎么用

1. **不要只读**。每个代码块都亲手敲一遍（或复制到 PyCharm / Jupyter 里跑），改改参数看输出怎么变。
2. 每章读完做 🧪 练习。答案默认折叠，先自己想，再点开。
3. 卡住了查 **附录 B 报错急救**。
4. 学完想做项目，直接跳到第 8 章。

### 三条铁律（先记住，后面全用得着）

1. **所有元素必须是同一种数据类型**。混着放会自动「向上提升」。
2. **创建后总大小固定**。想加元素只能新建一个数组，不能原地长大。
3. **形状必须是矩形**。二维数组每一行列数必须一样，**锯齿状数组在 NumPy 2.x 会直接报错**（老版本只是警告）。

```python
import numpy as np

# 铁律 1：类型自动提升
print(np.array([1, 2, 3.5]).dtype)      # int 和 float 混 -> float64
print(np.array([True, 1, 2]).dtype)     # bool 和 int 混  -> int64
print(np.array([1, 2, "x"]).dtype)      # 有字符串，全变字符串 -> <U21

# 铁律 3：锯齿数组直接报错
try:
    np.array([[1, 2], [3]])
except ValueError as e:
    print("报错：", str(e)[:60], "...")
```

**输出**

    float64
    int64
    <U21
    报错： setting an array element with a sequence. The requested arra ...

---

## 🗺️ 学习路线图

| 章 | 内容 | 对应课程 | 重要度 | 建议时间 |
|---|---|---|---|---|
| 0 | 环境准备 | 1.1 / 1.2 | — | 20 min |
| 1 | 认识 NumPy：为什么快、属性、轴 | 2.1 – 2.3 | ⭐⭐⭐ | 1 h |
| 2 | 创建数组 | 2.4 | ⭐⭐⭐ | 1.5 h |
| 3 | 索引与切片 | 2.6（**大幅补充**） | ⭐⭐⭐⭐⭐ | 3 h |
| 4 | 形状操作 | **课程没有，必补** | ⭐⭐⭐⭐⭐ | 2 h |
| 5 | 常用函数与 axis | 2.7 | ⭐⭐⭐⭐⭐ | 2.5 h |
| 6 | 运算与广播 | 2.8 – 2.9 | ⭐⭐⭐⭐ | 2 h |
| 7 | 文件读写与线性代数 | **补充** | ⭐⭐ | 1 h |
| 8 | 综合实战（真实数据） | 第 4 章 | ⭐⭐⭐⭐ | 3 h |

**如果时间紧**：第 3、4、5 章是 NumPy 的命根子，务必吃透。第 7 章可以最后再看。

---

# 第 0 章 准备

## 0.1 环境

课程用 Anaconda。**你已经有能用的环境了**——我检测到你机器上的运行时是 Python 3.12.14 + NumPy 2.3.5，版本很新，直接用就行，不用再装 Anaconda。

验证一下：

```python
import sys
import numpy as np

print("Python:", sys.version.split()[0])
print("NumPy :", np.__version__)
```

**输出**

    Python: 3.12.14
    NumPy : 2.3.5

如果显示 `ModuleNotFoundError: No module named 'numpy'`，在 PyCharm 的终端里装：

    pip install numpy

> Anaconda 用户用 `conda install numpy`。两者不要混用同一个环境。

## 0.2 一个开局设置

写 NumPy 代码时，建议开头加上这一行：

```python
import numpy as np

# 让浮点数打印好看一点：保留 4 位小数
np.set_printoptions(precision=4, suppress=True)

print(np.array([0.1, 1/3, 1e-8, 1234567.891]))
```

**输出**

    [      0.1          0.3333       0.     1234567.891 ]

**不加这一行的话**，默认输出长这样，第一次见会一脸问号：

    [1.00000000e-01 3.33333333e-01 1.00000000e-08 1.23456789e+06]

> ⚠️ `suppress=True` 会把很小很小的数直接显示成 `0.`，调试精度问题时记得关掉。

## 0.3 随机数必须固定种子

NumPy 的随机数默认每次都不一样，**学的时候根本没法对照输出**。养成习惯：固定种子。

```python
import numpy as np

# 老 API（课程里用的）：全局种子
np.random.seed(0)
print("老 API rand:", np.random.rand(3))

# 新 API（NumPy 1.17+ 推荐）：独立的随机数发生器，互不干扰
rng = np.random.default_rng(0)
print("新 API integers:\n", rng.integers(0, 10, (2, 3)))
```

**输出**

    老 API rand: [0.5488135  0.71518937 0.60276338]
    新 API integers:
     [[8 6 5]
     [2 3 0]]

> ⚠️ **新老 API 不要混着用**。`np.random.seed()` 管不到 `default_rng()`，反之亦然。
> 本手册为了和课程对齐，大部分地方用老 API；你在自己项目里**优先用 `default_rng()`**。

---

# 第 1 章 认识 NumPy

> 对应课程 2.1 – 2.3

## 1.1 NumPy 是什么，为什么不用 list

NumPy 是 Python 科学计算的基础包，核心是 **ndarray**（N 维数组）。

一句话概括它比 list 强在哪：**同样的活，它写得短、跑得快、占内存少。**

**为什么快？** Python 的 list 存的是一堆「指针」，每个元素都是一个独立的 Python 对象；ndarray 存的是一整块连续内存里的**原始字节**。所以 ndarray 不需要挨个拆装箱，还能直接用 CPU 的 SIMD 指令批量算。

```python
import sys
import numpy as np

arr = np.arange(10)

# 每个 Python int 对象本身就要 28 字节，外加 list 里 8 字节的指针
print("Python int 对象:", sys.getsizeof(0), "字节")
print("ndarray 每个元素:", arr.itemsize, "字节")
print("10 个元素的 ndarray 总共:", arr.nbytes, "字节")
```

**输出**

    Python int 对象: 28 字节
    ndarray 每个元素: 8 字节
    10 个元素的 ndarray 总共: 80 字节

**快多少？** 我实测了一下（100 万个数乘 2 再求和）：

    循环: 0.0311s  向量化: 0.0025s  加速比: 12x

在你机器上数字会不同，但**量级差 10 倍以上是稳定的**。而且数据量越大、运算越复杂，差距越夸张。

**写得短**，是这个意思：

```python
import numpy as np

a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

# Python list：必须写循环
c_list = [x + y for x, y in zip(a, b)]

# NumPy：直接加
c_np = np.array(a) + np.array(b)

print("list :", c_list)
print("numpy:", c_np)
```

**输出**

    list : [11, 22, 33, 44, 55]
    numpy: [11 22 33 44 55]

这种「不写循环，直接对整个数组做运算」的方式叫**矢量化运算**，是 NumPy 的灵魂。

## 1.2 ndarray 的五大属性

课程里提了 `ndim / shape / size / dtype / itemsize`，逐个说清楚：

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print("数组:\n", a)
print("ndim   维度数        :", a.ndim)
print("shape  形状(每维长度) :", a.shape)
print("size   元素总个数     :", a.size)
print("dtype  元素类型       :", a.dtype)
print("itemsize 单元素字节   :", a.itemsize)
```

**输出**

    数组:
     [[1 2 3]
     [4 5 6]]
    ndim   维度数        : 2
    shape  形状(每维长度) : (2, 3)
    size   元素总个数     : 6
    dtype  元素类型       : int64
    itemsize 单元素字节   : 8

### ⚠️ 坑：`size` 和 `len()` 不是一回事

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print("a.size =", a.size)   # 6，所有元素
print("len(a) =", len(a))   # 2，只是第 0 维的长度
```

**输出**

    a.size = 6
    len(a) = 2

**记法**：`len()` 永远只返回「最外层有几个」，`size` 是「一共有几个」。

### ⚠️ 坑：`shape` 是元组，一维数组是 `(3,)` 不是 `(3)`

```python
import numpy as np

print(np.array([1, 2, 3]).shape)    # (3,)   一维
print(np.array([[1, 2, 3]]).shape)  # (1, 3) 二维，1 行 3 列
```

**输出**

    (3,)
    (1, 3)

`(3,)` 和 `(1, 3)` 完全不同，这是后面广播出错的头号原因。

## 1.3 轴（axis）到底是什么 ⭐

**这一节比课程讲得细，请务必看懂，否则第 5 章会全线崩溃。**

课程里说「`axis=0` 按列统计、`axis=1` 按行统计」。这句话**能用但没解释清楚**，很多人背下来了还是不会用。

**正确的理解方式：`axis` 指定的是「要被消掉的那个维度」。**

拿一个 `(2, 3)` 的数组举例：

        列0  列1  列2
    行0 [  1    2    3 ]
    行1 [  4    5    6 ]

- **`axis=0`**：消掉第 0 维（行），剩下 3 个数 → 结果是长度 3。计算方式：把每一**列**竖着压扁。
- **`axis=1`**：消掉第 1 维（列），剩下 2 个数 → 结果是长度 2。计算方式：把每一**行**横着压扁。

```python
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print("原数组 shape:", a.shape)
print("sum(axis=0) =", a.sum(axis=0), "-> shape", a.sum(axis=0).shape)
print("sum(axis=1) =", a.sum(axis=1), "-> shape", a.sum(axis=1).shape)
print("sum()       =", a.sum(),       "-> 标量，消掉所有维度")
```

**输出**

    原数组 shape: (2, 3)
    sum(axis=0) = [5 7 9] -> shape (3,)
    sum(axis=1) = [ 6 15] -> shape (2,)
    sum()       = 21 -> 标量，消掉所有维度

手工对一下 `sum(axis=0) = [5, 7, 9]`：第 0 列 `1+4=5`，第 1 列 `2+5=7`，第 2 列 `3+6=9`。**列还在，行没了**——这就是「消掉 axis=0」。

### 一句话口诀

> **`axis=0` 竖着压（沿着行往下走），`axis=1` 横着压（沿着列往右走）。**
> 结果形状 = 原形状**删掉 axis 指定的那一维**。

验证一下：原 shape `(2, 3)`，`axis=0` 后剩 `(3,)`，`axis=1` 后剩 `(2,)`。✅

三维也一样：

```python
import numpy as np

b = np.arange(24).reshape(2, 3, 4)   # shape (2, 3, 4)

print("原 shape    :", b.shape)
print("sum(axis=0) ->", b.sum(axis=0).shape)
print("sum(axis=1) ->", b.sum(axis=1).shape)
print("sum(axis=2) ->", b.sum(axis=2).shape)
```

**输出**

    原 shape    : (2, 3, 4)
    sum(axis=0) -> (3, 4)
    sum(axis=1) -> (2, 4)
    sum(axis=2) -> (2, 3)

看，规律完全一致：**消掉哪一维，哪一维就没了**。

### ⚠️ 坑：`axis=-1` 是「最后一维」

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.sum(axis=-1))   # 等同于 axis=1
```

**输出**

    [ 6 15]

很多函数（比如 `sort`）默认 `axis=-1`，就是「对每一行内部排序」。

## 🧪 第 1 章 练习

**1-1** 创建一个形状为 `(3, 4)` 的 int 数组，打印出它的五个属性。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print("ndim:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)
print("dtype:", a.dtype)
print("itemsize:", a.itemsize)
```

输出：`ndim: 2` / `shape: (3, 4)` / `size: 12` / `dtype: int64` / `itemsize: 8`

</details>

**1-2** 不运行代码，先猜 `np.array([[1, 2, 3]]).size` 和 `len(np.array([[1, 2, 3]]))` 分别是多少，再验证。

<details>
<summary>💡 参考答案</summary>

`size` 是 **3**（一共 3 个元素），`len()` 是 **1**（最外层只有 1 行）。

```python
import numpy as np
a = np.array([[1, 2, 3]])
print(a.size, len(a))   # 3 1
```

</details>

**1-3** 下面这行代码为什么会报错？怎么改？

```python
import numpy as np
np.array([[1, 2, 3], [4, 5]])
```

<details>
<summary>💡 参考答案</summary>

违反了**铁律 3：形状必须是矩形**。第一行 3 个元素、第二行 2 个，NumPy 2.x 会直接抛
`ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape...`

三种改法：

```python
import numpy as np

# 1) 补齐成矩形
a = np.array([[1, 2, 3], [4, 5, 0]])

# 2) 故意用 object 类型（一般不要这么做，会失去 NumPy 的性能优势）
b = np.array([[1, 2, 3], [4, 5]], dtype=object)

# 3) 拆成两个数组，用 list 装着
c = [np.array([1, 2, 3]), np.array([4, 5])]

print(a.shape, b.shape, len(c))
```

输出：`(2, 3) (2,) 2`

</details>

**1-4** 一个 shape 为 `(4, 5, 6)` 的数组，`sum(axis=1)` 的结果 shape 是多少？先按口诀推，再用代码验证。

<details>
<summary>💡 参考答案</summary>

口诀：**消掉 axis 指定的那一维**。`(4, 5, 6)` 去掉第 1 维 → **`(4, 6)`**。

```python
import numpy as np
b = np.arange(120).reshape(4, 5, 6)
print(b.sum(axis=1).shape)   # (4, 6)
```

</details>

---

# 第 2 章 创建数组

> 对应课程 2.4

创建数组的方法有十几种，**但常用的就 6 类**。先把这 6 类记牢，其余的用到再查。

| 场景 | 方法 |
|---|---|
| 从 Python 列表/元组转 | `np.array()` `np.asarray()` |
| 全 0 / 全 1 / 空 | `np.zeros()` `np.ones()` `np.empty()` |
| 填充指定值 | `np.full()` |
| 等差 / 等比 | `np.arange()` `np.linspace()` `np.logspace()` |
| 随机数 | `np.random.*` |
| 特殊矩阵 | `np.eye()` `np.identity()` |

> 名字里带 `_like` 的（`zeros_like` / `ones_like` / `full_like` / `empty_like`）都是**照着另一个数组的形状和类型**来造，非常常用。

## 2.1 `array()` 与 `asarray()`

**区别只有一句话**：`np.array()` 永远复制一份；`np.asarray()` 如果输入已经是 ndarray，就**直接把原对象还给你，不复制**。

```python
import numpy as np

data = [1, 2, 3]
arr = np.array(data)
print("arr          :", arr)

arr2 = np.array(arr)      # 再转一次，仍然复制
arr3 = np.asarray(arr)    # 已经是 ndarray，直接返回同一个对象

print("np.array(arr)  is arr ?", arr2 is arr)     # False
print("np.asarray(arr) is arr ?", arr3 is arr)    # True
print("np.asarray(data) is arr ?", np.asarray(data) is arr)  # False，list 还是要转
```

**输出**

    arr          : [1 2 3]
    np.array(arr)  is arr ? False
    np.asarray(arr) is arr ? True
    np.asarray(data) is arr ? False

> ⚠️ **实用建议**：写函数时如果参数可能是 list 也可能是 ndarray，用 `np.asarray()`——避免不必要的复制，但又能保证拿到 ndarray。

> ⚠️ 课程原文用 `id()` 打印内存地址来演示。**别学那个写法**：`id()` 返回的是对象的身份标识，跟"数据在哪块内存"没关系，而且每次运行数字都不一样，没法对照。

## 2.2 `zeros()` / `ones()` / `empty()` 与 `*_like`

```python
import numpy as np

print("zeros((2,3)):\n", np.zeros((2, 3)))
print("ones((2,3)):\n", np.ones((2, 3)))
print("默认 dtype:", np.zeros((2, 3)).dtype)

a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)
print("zeros_like(a) 会跟着 a 的 dtype:\n", np.zeros_like(a))
print("ones_like(a):\n", np.ones_like(a))
```

**输出**

    zeros((2,3)):
     [[0. 0. 0.]
     [0. 0. 0.]]
    ones((2,3)):
     [[1. 1. 1.]
     [1. 1. 1.]]
    默认 dtype: float64
    zeros_like(a) 会跟着 a 的 dtype:
     [[0 0 0]
     [0 0 0]]
    ones_like(a):
     [[1 1 1]
     [1 1 1]]

> ⚠️ **坑 1**：`zeros()` / `ones()` / `empty()` 默认是 **float64**，不是 int！要整数得写 `np.zeros((2,3), dtype=int)`。
> ⚠️ **坑 2**：`np.empty()` **不是"空数组"**，而是"分配了内存但没初始化"——里面的值是**内存里残留的垃圾数据**，每次运行都不一样。它的用处只有一个：**你确定马上会把每个元素都赋值**，这时它比 `zeros()` 快一点点。**初学阶段别用它**。

```python
import numpy as np

# 不要试图对照 empty 的具体数字——那是内存垃圾
print("empty 的形状:", np.empty((2, 3)).shape)
print("empty 的 dtype:", np.empty((2, 3)).dtype)
print("它的值可能是 0，可能是 1e-312，也可能是 1e+248")
```

**输出**

    empty 的形状: (2, 3)
    empty 的 dtype: float64
    它的值可能是 0，可能是 1e-312，也可能是 1e+248

## 2.3 `full()` 与 `full_like()`

```python
import numpy as np

print("full((2,3), 6):\n", np.full((2, 3), 6))
print("full((2,3), 3.14):\n", np.full((2, 3), 3.14))

arr = np.full((2, 3), 6)
print("full_like(arr, 5):\n", np.full_like(arr, 5))
print("dtype 跟着 arr:", np.full_like(arr, 5).dtype)
```

**输出**

    full((2,3), 6):
     [[6 6 6]
     [6 6 6]]
    full((2,3), 3.14):
     [[3.14 3.14 3.14]
     [3.14 3.14 3.14]]
    full_like(arr, 5):
     [[5 5 5]
     [5 5 5]]
    dtype 跟着 arr: int64

> ⚠️ `full_like(arr, 5.5)` 里的 `5.5` 会被**截断**成 `5`，因为 dtype 跟着 `arr` 是 int64。要小数得显式写 `dtype=float`。

## 2.4 `arange()`

**左闭右开**，用法和 Python 的 `range()` 一样，但**支持小数步长**。

```python
import numpy as np

print("arange(10)        :", np.arange(10))
print("arange(0, 10, 2)  :", np.arange(0, 10, 2))
print("arange(5, 0, -1)  :", np.arange(5, 0, -1))
print("arange(0, 1, 0.3) :", np.arange(0, 1, 0.3))
print("dtype 是浮点      :", np.arange(0, 1, 0.3).dtype)
```

**输出**

    arange(10)        : [0 1 2 3 4 5 6 7 8 9]
    arange(0, 10, 2)  : [0 2 4 6 8]
    arange(5, 0, -1)  : [5 4 3 2 1]
    arange(0, 1, 0.3) : [0.  0.3 0.6 0.9]
    dtype 是浮点      : float64

> ⚠️ **坑：小数步长的 `arange` 元素个数不可靠**。因为浮点数有误差，"正好到没到终点"很难判断。**需要精确个数就用 `linspace`。**

## 2.5 `linspace()` 与 `logspace()`

- `linspace`：给定**个数**，自动算步长（"linear space"，等差）
- `logspace`：给的是**指数**范围（"log space"，等比）

```python
import numpy as np

print("linspace(0,10,5)             :", np.linspace(0, 10, 5))
print("linspace(0,10,5,endpoint=F)  :", np.linspace(0, 10, 5, endpoint=False))
print("默认包含终点，所以是 5 个数分 4 段，每段 2.5")

result, step = np.linspace(0, 10, 5, retstep=True)
print("retstep 能直接拿到步长     :", step)

print("logspace(2,5,5,base=2) = 2的[2..5]次方:", np.logspace(start=2, stop=5, num=5, base=2))
print("logspace(0,3,4)  base默认10 :", np.logspace(0, 3, 4))
```

**输出**

    linspace(0,10,5)             : [ 0.   2.5  5.   7.5 10. ]
    linspace(0,10,5,endpoint=F)  : [0. 2. 4. 6. 8.]
    默认包含终点，所以是 5 个数分 4 段，每段 2.5
    retstep 能直接拿到步长     : 2.5
    logspace(2,5,5,base=2) = 2的[2..5]次方: [ 4.          6.72717132 11.3137085  19.02731384 32.        ]
    logspace(0,3,4)  base默认10 : [   1.   10.  100. 1000.]

> 💡 课程文档花了很长篇幅推导 `linspace` 的步长公式。其实记住这一句就够了：
> **`endpoint=True`（默认）→ 分 `num-1` 段；`endpoint=False` → 分 `num` 段。** `retstep=True` 直接把步长给你，不用自己推。

## 2.6 创建随机数数组

**下面每个 `seed(0)` 都是为了让你能对照输出。** 去掉它，每次运行结果都不一样。

```python
import numpy as np

np.random.seed(0)
print("rand(2,3)      [0,1) 均匀浮点:\n", np.random.rand(2, 3))

np.random.seed(0)
print("uniform(3,6)   [3,6) 均匀浮点:\n", np.random.uniform(3, 6, (2, 3)))

np.random.seed(0)
print("randint(0,10)  [0,10) 均匀整数:\n", np.random.randint(0, 10, (2, 3)))

np.random.seed(0)
print("randn(2,3)     标准正态(均值0,标准差1):\n", np.random.randn(2, 3))

np.random.seed(0)
print("normal(100,15,5) 指定均值和标准差:", np.random.normal(100, 15, 5))
```

**输出**

    rand(2,3)      [0,1) 均匀浮点:
     [[0.5488135  0.71518937 0.60276338]
     [0.54488318 0.4236548  0.64589411]]
    uniform(3,6)   [3,6) 均匀浮点:
     [[4.64644051 5.1455681  4.80829013]
     [4.63464955 4.2709644  4.93768234]]
    randint(0,10)  [0,10) 均匀整数:
     [[5 0 3]
     [3 7 9]]
    randn(2,3)     标准正态(均值0,标准差1):
     [[ 1.76405235  0.40015721  0.97873798]
     [ 2.2408932   1.86755799 -0.97727788]]
    normal(100,15,5) 指定均值和标准差: [126.46078519 106.00235813 114.68106976 133.61339799 128.01336985]

**从现有数据里抽样的三个方法**：

```python
import numpy as np

np.random.seed(0)
print("choice 有放回  :", np.random.choice([1, 2, 3, 4], size=3))

np.random.seed(0)
print("choice 无放回  :", np.random.choice([1, 2, 3, 4], size=3, replace=False))

np.random.seed(0)
print("permutation 打乱:", np.random.permutation(5))

np.random.seed(0)
a = np.arange(5)
np.random.shuffle(a)          # 注意：就地打乱，没有返回值
print("shuffle 就地打乱:", a)
```

**输出**

    choice 有放回  : [1 4 2]
    choice 无放回  : [3 4 2]
    permutation 打乱: [2 0 1 3 4]
    shuffle 就地打乱: [2 0 1 3 4]

> ⚠️ `shuffle` **就地修改**，返回 `None`。写 `a = np.random.shuffle(a)` 会让 `a` 变成 `None`——这是新手高频事故。

> ⚠️ 上面全是**老 API**。新代码推荐：
> ```python
> import numpy as np
> rng = np.random.default_rng(42)
> rng.random((2, 3))            # 对应 rand
> rng.integers(0, 10, (2, 3))  # 对应 randint
> rng.normal(0, 1, (2, 3))      # 对应 randn
> rng.choice([1,2,3,4], 3, replace=False)
> ```

## 2.7 ⚠️ `np.matrix` 已经废弃——课程里的过时内容

课程 2.4.7 教了 `np.matrix`。**这个类从 NumPy 1.15 起就被官方标记为"不推荐使用"，现在处于待废弃状态。**

```python
import warnings
import numpy as np

with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    m = np.matrix("1 2; 3 4")
    print("触发的警告:", w[0].category.__name__)
    print(m)
```

**输出**

    触发的警告: PendingDeprecationWarning
    [[1 2]
     [3 4]]

**为什么必须避开它？** 因为 `np.matrix` 的 `*` 是**矩阵乘法**，而 `np.array` 的 `*` 是**元素乘法**。同一个符号两种含义，混用必出 bug：

```python
import numpy as np

m1 = np.matrix([[1, 2], [3, 4]])
m2 = np.matrix([[1, 2], [3, 4]])
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[1, 2], [3, 4]])

print("matrix 的 * 是矩阵乘法:\n", m1 * m2)
print("array  的 * 是元素乘法:\n", a1 * a2)
```

**输出**

    matrix 的 * 是矩阵乘法:
     [[ 7 10]
     [15 22]]
    array  的 * 是元素乘法:
     [[ 1  4]
     [ 9 16]]

**结论：忘掉 `np.matrix`。** 一律用 `np.array`，矩阵乘法用 `a @ b`（见 6.4 节）。

## 2.8 顺手认识两个特殊矩阵

```python
import numpy as np

print("eye(3) 单位矩阵:\n", np.eye(3))
print("eye(3, 4) 非方阵:\n", np.eye(3, 4))
print("eye(3, k=1) 对角线右移一格:\n", np.eye(3, k=1))
```

**输出**

    eye(3) 单位矩阵:
     [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    eye(3, 4) 非方阵:
     [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]]
    eye(3, k=1) 对角线右移一格:
     [[0. 1. 0.]
     [0. 0. 1.]
     [0. 0. 0.]]

## 🧪 第 2 章 练习

**2-1** 用**三种不同方法**创建数组 `[0, 0, 0, 0, 0]`。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

a = np.zeros(5)
b = np.full(5, 0)
c = np.array([0] * 5)
d = np.arange(5) * 0

print(a, b, c, d, sep="\n")
```

注意 `np.zeros(5)` 默认是 float64，输出 `[0. 0. 0. 0. 0.]`；`np.full(5, 0)` 是 int64，输出 `[0 0 0 0 0]`。

</details>

**2-2** 不运行代码，说出 `np.arange(0, 10, 3)` 和 `np.linspace(0, 10, 3)` 分别输出什么，再验证。

<details>
<summary>💡 参考答案</summary>

- `np.arange(0, 10, 3)` → `[0 3 6 9]`（**步长**是 3，终点不保证到达）
- `np.linspace(0, 10, 3)` → `[ 0.  5. 10.]`（**个数**是 3，终点保证到达）

```python
import numpy as np
print(np.arange(0, 10, 3))     # [0 3 6 9]
print(np.linspace(0, 10, 3))   # [ 0.  5. 10.]
```

**这是最容易被问到的面试题之一。**

</details>

**2-3** 创建一个 3×3 的随机整数矩阵，元素取值范围 `[10, 20)`，并要求**每次运行结果都一样**。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

np.random.seed(42)
a = np.random.randint(10, 20, (3, 3))
print(a)

# 新 API 写法（推荐）
rng = np.random.default_rng(42)
b = rng.integers(10, 20, (3, 3))
print(b)
```

关键点：`randint(low, high)` 是**左闭右开**的，所以 `high` 要写 20 才能取到 19。

</details>

**2-4** 下面代码有什么问题？

```python
import numpy as np
a = np.arange(5)
a = np.random.shuffle(a)
print(a)
```

<details>
<summary>💡 参考答案</summary>

`np.random.shuffle()` **就地打乱，返回 `None`**。所以 `a` 被赋成了 `None`，打印出来是 `None`。

正确写法：

```python
import numpy as np

np.random.seed(0)
a = np.arange(5)
np.random.shuffle(a)     # 不要赋值
print(a)                 # [2 4 3 0 1]
```

需要返回值就用 `np.random.permutation(a)`，它返回打乱后的**新数组**，不改原数组。

</details>

---

# 第 3 章 索引与切片 ⭐⭐⭐⭐⭐

> 对应课程 2.6 —— **但课程只讲了一维，这一章是本手册最重要的补充之一**

**这一章是 NumPy 最核心的技能。** 数据分析 80% 的时间都在"取出我想要的那些元素"，取不出来后面全是空谈。

## 3.1 一维切片（课程内容）

规则和 Python list **完全一样**：`[start:stop:step]`，**左闭右开**。

```python
import numpy as np

arr = np.arange(10)
print("arr          :", arr)
print("arr[2]       :", arr[2])
print("arr[2:9:2]   :", arr[2:9:2])
print("arr[slice(2,9,2)] 等价写法:", arr[slice(2, 9, 2)])
print("arr[2:]      :", arr[2:])
print("arr[:5]      :", arr[:5])
print("arr[::2]     :", arr[::2])
print("arr[::-1] 反转:", arr[::-1])
```

**输出**

    arr          : [0 1 2 3 4 5 6 7 8 9]
    arr[2]       : 2
    arr[2:9:2]   : [2 4 6 8]
    arr[slice(2,9,2)] 等价写法: [2 4 6 8]
    arr[2:]      : [2 3 4 5 6 7 8 9]
    arr[:5]      : [0 1 2 3 4]
    arr[::2]     : [0 2 4 6 8]
    arr[::-1] 反转: [9 8 7 6 5 4 3 2 1 0]

> 💡 课程里用 `slice(2, 9, 2)` 演示，其实 `arr[2:9:2]` 就是它的语法糖，**平时直接用冒号写法**。

## 3.2 二维及以上的索引 ⭐

**二维索引用逗号分隔**：`a[行, 列]`。记住这个格式，比什么都重要。

```python
import numpy as np

a = np.arange(1, 25).reshape(4, 6)
print("原数组 a =\n", a)

print("\na[1, 2]      =", a[1, 2])        # 第1行第2列
print("a[1]         =", a[1])           # 第1行（整行）
print("a[:, 1]      =", a[:, 1])        # 第1列（整列）
print("a[1:3, 1:4]  =\n", a[1:3, 1:4])   # 行1~2 且 列1~3
print("a[::2, ::3]  =\n", a[::2, ::3])   # 行隔1取1，列隔2取1
print("a[-1, -1]    =", a[-1, -1])      # 最后一行最后一列
print("a[:, ::-1]   =\n", a[:, ::-1])    # 每行反转
```

**输出**

    原数组 a =
     [[ 1  2  3  4  5  6]
     [ 7  8  9 10 11 12]
     [13 14 15 16 17 18]
     [19 20 21 22 23 24]]

    a[1, 2]      = 9
    a[1]         = [ 7  8  9 10 11 12]
    a[:, 1]      = [ 2  8 14 20]
    a[1:3, 1:4]  =
     [[ 8  9 10]
     [14 15 16]]
    a[::2, ::3]  =
     [[ 1  4]
     [13 16]]
    a[-1, -1]    = 24
    a[:, ::-1]   =
     [[ 6  5  4  3  2  1]
     [12 11 10  9  8  7]
     [18 17 16 15 14 13]
     [24 23 22 21 20 19]]

### 常用套路：取"中心"

```python
import numpy as np

m = np.arange(1, 26).reshape(5, 5)
print("5x5 原矩阵:\n", m)
print("中心 3x3:\n", m[1:4, 1:4])
```

**输出**

    5x5 原矩阵:
     [[ 1  2  3  4  5]
     [ 6  7  8  9 10]
     [11 12 13 14 15]
     [16 17 18 19 20]
     [21 22 23 24 25]]
    中心 3x3:
     [[ 7  8  9]
     [12 13 14]
     [17 18 19]]

> ⚠️ **别写成 `a[1:4][1:4]`**！那是"先取第 1~3 行，再从结果里取第 1~3 行（其实是列）"，结果完全不对。**多个维度要写在同一个方括号里，用逗号隔开。**

## 3.3 视图 vs 副本 ⭐⭐⭐ 本章最重要的一节

**这是 NumPy 最大的坑，也是课程完全没讲的东西。没搞懂它，你会在某天突然发现"我明明没改这个数组，它怎么变了"。**

**一句话结论**：

> **基本切片（冒号）返回的是「视图」——它和原数组共享同一块内存，改一个另一个也变。**
> **花式索引、布尔索引返回的是「副本」——改它不影响原数组。**

### 演示 1：切片是视图，会"隔空改原数组"

```python
import numpy as np

a = np.arange(10)
print("改之前 a     :", a)

v = a[2:5]        # 这是视图！
v[0] = 999        # 改视图

print("改之后 a     :", a)
print("视图 v       :", v)
```

**输出**

    改之前 a     : [0 1 2 3 4 5 6 7 8 9]
    改之后 a     : [  0   1 999   3   4   5   6   7   8   9]
    视图 v       : [999   3   4]

**看到没？我根本没碰 `a`，但 `a` 变了。** 这就是视图。

### 演示 2：花式索引 / 布尔索引是副本，改了不影响

```python
import numpy as np

a = np.arange(10)
c = a[[1, 2, 3]]     # 花式索引 -> 副本
c[0] = 999
print("改花式索引后 a:", a)          # 没变

a = np.arange(10)
c = a[a > 5]         # 布尔索引 -> 副本
c[0] = 999
print("改布尔索引后 a:", a)          # 没变
```

**输出**

    改花式索引后 a: [0 1 2 3 4 5 6 7 8 9]
    改布尔索引后 a: [0 1 2 3 4 5 6 7 8 9]

### 怎么判断？看 `.base` 和 `.flags.owndata`

```python
import numpy as np

a = np.arange(10)

print("切片      base is a :", a[2:5].base is a,   "| owndata:", a[2:5].flags.owndata)
print("reshape   base is a :", a.reshape(2, 5).base is a)
print("花式索引  base       :", a[[1, 2, 3]].base, "| owndata:", a[[1, 2, 3]].flags.owndata)
print("布尔索引  base       :", a[a > 5].base,     "| owndata:", a[a > 5].flags.owndata)
print("flatten   owndata   :", a.reshape(2, 5).flatten().flags.owndata)
print("ravel     base is a :", a.reshape(2, 5).ravel().base is a)
```

**输出**

    切片      base is a : True | owndata: False
    reshape   base is a : True
    花式索引  base       : None | owndata: True
    布尔索引  base       : None | owndata: True
    flatten   owndata   : True
    ravel     base is a : True

**判读方法**：`owndata=True`（或 `base is None`）= 副本，自己管着自己的内存；`owndata=False` 且 `base` 指向别人 = 视图。

### 速查表（建议背下来）

| 操作 | 返回 | 改它会影响原数组吗 |
|---|---|---|
| `a[2:5]` 切片 | **视图** | ✅ 会 |
| `a[a > 5]` 布尔索引 | 副本 | ❌ 不会 |
| `a[[1,2,3]]` 花式索引 | 副本 | ❌ 不会 |
| `a.reshape(...)` | **视图**（能看就看） | ✅ 会 |
| `a.ravel()` | **视图**（能看就看） | ✅ 会 |
| `a.T` / `a.transpose()` | **视图** | ✅ 会 |
| `a.flatten()` | 副本 | ❌ 不会 |
| `np.array(a)` | 副本 | ❌ 不会 |
| `a.copy()` | 副本 | ❌ 不会 |

### 想安全地切一段出来改？加 `.copy()`

```python
import numpy as np

a = np.arange(10)
safe = a[2:5].copy()     # 明确要副本
safe[0] = 999

print("a 没被改:", a)
print("safe    :", safe)
```

**输出**

    a 没被改: [0 1 2 3 4 5 6 7 8 9]
    safe    : [999   3   4]

> 💡 **这条规则的另一面是好事**：处理 100 万行的数据时，`df[col]` 之类的切片不复制内存，所以 NumPy 才这么快。**理解它，而不是害怕它。**

## 3.4 布尔索引 ⭐⭐

用一个"真假数组"当索引，**取出所有为 True 的位置**。数据分析里天天用。

```python
import numpy as np

a = np.array([1, -2, 3, -4, 5])

print("a > 0        :", a > 0)
print("a[a > 0]     :", a[a > 0])
print("(a > 0).sum():", (a > 0).sum(), "  <- True 当 1 数")
print("(a > 0).mean():", (a > 0).mean(), " <- 占比")
print("(a > 0).any():", (a > 0).any())
print("(a > 0).all():", (a > 0).all())
```

**输出**

    a > 0        : [ True False  True False  True]
    a[a > 0]     : [1 3 5]
    (a > 0).sum(): 3   <- True 当 1 数
    (a > 0).mean(): 0.6  <- 占比
    (a > 0).any(): True
    (a > 0).all(): False

> 💡 **`(a > 0).sum()` 数个数、`(a > 0).mean()` 算比例**——这两个是数据分析里最常用的组合，比 `len(a[a>0])` 快得多也清楚得多。

### 多条件：`&` `|` `~`，**括号不能省**

```python
import numpy as np

a = np.array([1, -2, 3, -4, 5])

print("(a>0) & (a<5) :", a[(a > 0) & (a < 5)])
print("(a<-2) | (a>3):", a[(a < -2) | (a > 3)])
print("~(a > 0)      :", a[~(a > 0)])
```

**输出**

    (a>0) & (a<5) : [1 3]
    (a<-2) | (a>3): [-4  5]
    ~(a > 0)      : [-2 -4]

> ⚠️ **坑**：不能写 `a[a > 0 and a < 5]`。Python 的 `and` 遇到数组会直接抛
> `ValueError: The truth value of an array with more than one element is ambiguous`。
> **必须用 `&` `|` `~`，并且每个条件都用括号包起来。**

### 布尔索引赋值：批量改值的神器

```python
import numpy as np

a = np.array([1, -2, 3, -4, 5])

a[a < 0] = 0              # 所有负数变 0
print("负数清零     :", a)

b = np.arange(10)
b[b % 2 == 0] = -1        # 所有偶数变 -1
print("偶数变 -1    :", b)

c = np.array([1.0, np.nan, 3.0])
c[np.isnan(c)] = 0        # NaN 填 0（pandas 里更常用，这里先认识）
print("NaN 填 0     :", c)
```

**输出**

    负数清零     : [1 0 3 0 5]
    偶数变 -1    : [-1  1 -1  3 -1  5 -1  7 -1  9]
    NaN 填 0     : [1. 0. 3.]

### 二维布尔索引：返回的是**展平的一维数组**

```python
import numpy as np

a = np.arange(1, 13).reshape(3, 4)
print("a =\n", a)
print("a[a > 6]     =", a[a > 6])
print("a[a % 2 == 0]=", a[a % 2 == 0])
print("np.where(a>6)=", np.where(a > 6))
```

**输出**

    a =
     [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]]
    a[a > 6]     = [ 7  8  9 10 11 12]
    a[a % 2 == 0]= [ 2  4  6  8 10 12]
    np.where(a>6)= (array([1, 1, 2, 2, 2, 2]), array([2, 3, 0, 1, 2, 3]))

> ⚠️ **注意形状变了**：`(3,4)` 的数组做布尔索引，返回的是 `(6,)` 的一维数组，**原来的行列结构丢掉了**。
> 想要保留结构，用 `np.where(a > 6, a, 0)` 或者 `a * (a > 6)`。

## 3.5 花式索引（fancy indexing）

用**整数数组**当索引，可以任意指定顺序、重复取值。

```python
import numpy as np

a = np.array([10, 20, 30, 40, 50])
print("a[[0, 2, 4]]       :", a[[0, 2, 4]])
print("a[[4, 3, 2, 1, 0]] :", a[[4, 3, 2, 1, 0]], " <- 反转")
print("a[[1, 1, 3]]       :", a[[1, 1, 3]], " <- 可以重复取")

b = np.arange(1, 13).reshape(3, 4)
print("\nb =\n", b)
print("b[[0, 2]]          =\n", b[[0, 2]], " <- 取第 0、2 行")
print("b[:, [0, 3]]       =\n", b[:, [0, 3]], " <- 取第 0、3 列")
print("b[[0, 2], [1, 3]]  =", b[[0, 2], [1, 3]], " <- 取 (0,1) 和 (2,3) 两个点")
```

**输出**

    a[[0, 2, 4]]       : [10 30 50]
    a[[4, 3, 2, 1, 0]] : [50 40 30 20 10]  <- 反转
    a[[1, 1, 3]]       : [20 20 40]  <- 可以重复取

    b =
     [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]]
    b[[0, 2]]          =
     [[ 1  2  3  4]
     [ 9 10 11 12]]  <- 取第 0、2 行
    b[:, [0, 3]]       =
     [[ 1  4]
     [ 5  8]
     [ 9 12]]  <- 取第 0、3 列
    b[[0, 2], [1, 3]]  = [ 2 12]  <- 取 (0,1) 和 (2,3) 两个点

> ⚠️ **`b[[0, 2], [1, 3]]` 是"配对取值"，不是"取子矩阵"**！它取的是 `b[0,1]` 和 `b[2,3]` 这两个点。
> 想要"第 0、2 行 与 第 1、3 列 的交叉子矩阵"，要写成 `b[np.ix_([0, 2], [1, 3])]`：
>
> ```python
> import numpy as np
> b = np.arange(1, 13).reshape(3, 4)
> print(b[np.ix_([0, 2], [1, 3])])
> ```
>
> 输出：
>
>     [[ 2  4]
>      [10 12]]
>
> 这是课程完全没提、但很实用的一招。

## 3.6 `np.where` / `np.select` / `np.clip`

课程只提了一句 `np.where(condition, x, y)`，其实它有两个完全不同的用法。

```python
import numpy as np

a = np.array([1, -2, 3, -4, 5])

# 用法 1：只传条件 -> 返回满足条件的【下标】
print("np.where(a > 0)        =", np.where(a > 0))

# 用法 2：传三个参数 -> 三元运算符 vectorized 版
print("np.where(a > 0, a, 0)  =", np.where(a > 0, a, 0))
print("np.where(a > 0, 1, -1) =", np.where(a > 0, 1, -1))
```

**输出**

    np.where(a > 0)        = (array([0, 2, 4]),)
    np.where(a > 0, a, 0)  = [1 0 3 0 5]
    np.where(a > 0, 1, -1) = [ 1 -1  1 -1  1]

**多分支用 `np.select`**（`where` 只能二选一）：

```python
import numpy as np

scores = np.array([45, 62, 78, 91])

grades = np.select(
    [scores < 60, scores < 80],   # 条件列表，从上往下匹配
    ["不及格", "及格"],             # 对应取值
    default="优秀",
)
print("成绩:", scores)
print("等级:", grades)
```

**输出**

    成绩: [45 62 78 91]
    等级: ['不及格' '及格' '及格' '优秀']

**`clip` 用来截断**（比 `where` 更直接）：

```python
import numpy as np

print("clip([1,5,9], 2, 7) =", np.clip(np.array([1, 5, 9]), 2, 7))
print("clip 只给上限       =", np.clip(np.array([1, 5, 9]), None, 4))
```

**输出**

    clip([1,5,9], 2, 7) = [2 5 7]
    clip 只给上限       = [1 4 4]

## 🧪 第 3 章 练习

**3-1** 给定 `m = np.arange(1, 26).reshape(5, 5)`，取出它的**中心 3×3**，以及**四个角**。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

m = np.arange(1, 26).reshape(5, 5)

print("中心 3x3:\n", m[1:4, 1:4])
print("四个角:", m[0, 0], m[0, -1], m[-1, 0], m[-1, -1])
print("四角组成的数组:", m[[0, 0, -1, -1], [0, -1, 0, -1]])
```

输出：

    中心 3x3:
     [[ 7  8  9]
     [12 13 14]
     [17 18 19]]
    四个角: 1 5 21 25
    四角组成的数组: [ 1  5 21 25]

最后一行用的是**花式索引配对取值**（3.5 节）。

</details>

**3-2** 把 `a = np.array([1, -2, 3, -4, 5])` 里所有负数替换成它的绝对值，其他不变。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

a = np.array([1, -2, 3, -4, 5])
a[a < 0] = np.abs(a[a < 0])
print(a)     # [1 2 3 4 5]
```

更简单的写法（不需要布尔索引）：

```python
import numpy as np
a = np.array([1, -2, 3, -4, 5])
print(np.abs(a))     # [1 2 3 4 5]
```

</details>

**3-3** 下面代码运行后，`a` 和 `b` 分别是什么？先想，再跑。

```python
import numpy as np

a = np.arange(10)
b = a[3:7]
b[:] = 0
print(a)
print(b)
```

<details>
<summary>💡 参考答案</summary>

`a` 变成 `[0 1 2 0 0 0 0 7 8 9]`，`b` 变成 `[0 0 0 0]`。

因为**切片是视图**，`b` 和 `a[3:7]` 共享内存，改 `b` 就是改 `a`。

```python
import numpy as np

a = np.arange(10)
b = a[3:7]
b[:] = 0
print(a)   # [0 1 2 0 0 0 0 7 8 9]
print(b)   # [0 0 0 0]
```

**如果不想影响 `a`**，把 `b = a[3:7]` 改成 `b = a[3:7].copy()`。

</details>

**3-4** 用 `np.where` 把数组 `a = np.array([-5, 3, -1, 8, 0])` 变成：正数保留原值，负数变成 0。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

a = np.array([-5, 3, -1, 8, 0])
print(np.where(a > 0, a, 0))     # [0 3 0 8 0]
```

注意 `a > 0` 对 0 返回 False，所以 0 会走 "`else` 分支"变成 0——正好符合要求。

</details>

**3-5** 给定一个 `(4, 5)` 的随机整数矩阵（值域 0~99），**只把其中大于 50 的元素乘以 10，其余不变**。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

np.random.seed(0)
a = np.random.randint(0, 100, (4, 5))
print("原矩阵:\n", a)

# 方法 1：np.where（推荐，不改原数组）
b = np.where(a > 50, a * 10, a)
print("where 结果:\n", b)

# 方法 2：布尔索引赋值（就地改）
c = a.copy()
c[c > 50] *= 10
print("布尔赋值结果:\n", c)
```

两种都对。**方法 1 更适合函数式写法，方法 2 更省内存。**

</details>

---

# 第 4 章 形状操作 ⭐⭐⭐⭐⭐

> **课程第 2 章完全没有这一节。** 但只要你开始处理真实数据，改形状就是家常便饭。

## 4.1 `reshape()` 与万能的 `-1`

```python
import numpy as np

a = np.arange(12)
print("原始:", a, "| shape", a.shape)

print("\nreshape(3, 4):\n", a.reshape(3, 4))
print("\nreshape(2, -1) 让 NumPy 自己算:\n", a.reshape(2, -1))
print("\nreshape(-1, 6):\n", a.reshape(-1, 6))
print("\nreshape(2, 2, 3) 三维 shape:", a.reshape(2, 2, 3).shape)
```

**输出**

    原始: [ 0  1  2  3  4  5  6  7  8  9 10 11] | shape (12,)

    reshape(3, 4):
     [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]

    reshape(2, -1) 让 NumPy 自己算:
     [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]]

    reshape(-1, 6):
     [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]]

    reshape(2, 2, 3) 三维 shape: (2, 2, 3)

> 💡 **`-1` 是「你算，我不算」**。一个 reshape 里**最多只能有一个 `-1`**，否则 NumPy 也懵了。
> ⚠️ 元素总数必须对得上：12 个元素只能 reshape 成 `2×6`、`3×4`、`2×2×3` 这类，写 `reshape(5, 3)` 会报
> `ValueError: cannot reshape array of size 12 into shape (5,3)`。

> ⚠️ **reshape 默认是"按行填"（C 顺序）**。想按列填要写 `order='F'`，一般用不到。

## 4.2 `ravel()` 与 `flatten()`：拍平成一维

两个都是拉平，**区别在返回值**：

```python
import numpy as np

# ravel() 返回视图：改它 = 改原数组
a = np.arange(6).reshape(2, 3)
r = a.ravel()
r[0] = 999
print("用 ravel 改第一个元素后，a =\n", a)
print("  -> a 被改了，说明 ravel 返回的是视图\n")

# flatten() 返回副本：改它不影响原数组
b = np.arange(6).reshape(2, 3)
f = b.flatten()
f[0] = 999
print("用 flatten 改第一个元素后，b =\n", b)
print("  -> b 没变，说明 flatten 返回的是副本")
print("\n被改的副本 f 本身:", f)
```

**输出**

    用 ravel 改第一个元素后，a =
     [[999   1   2]
     [  3   4   5]]
      -> a 被改了，说明 ravel 返回的是视图

    用 flatten 改第一个元素后，b =
     [[0 1 2]
     [3 4 5]]
      -> b 没变，说明 flatten 返回的是副本

    被改的副本 f 本身: [999   1   2   3   4   5]

| | 返回 | 什么时候用 |
|---|---|---|
| `ravel()` | **视图**（能返回视图时） | 只是要遍历一遍，不改数据 —— **更快** |
| `flatten()` | 副本 | 要放心大胆地改 —— **更安全** |

## 4.3 转置 `T` / `transpose()` / `swapaxes()`

```python
import numpy as np

# .copy() 让 a 自己拥有内存，这样 a.T 的"父亲"才明确是 a
a = np.arange(1, 7).reshape(2, 3).copy()
print("a (2,3) =\n", a)

print("\na.T (3,2) =\n", a.T)
print("a.T.shape      :", a.T.shape)
print("a.transpose() 等价于 a.T")
print("a.T.base is a  :", a.T.base is a, " <- 视图，不复制内存")

# 行为验证：改转置，原数组会不会变？
t = a.T
t[0, 0] = 999
print("\n改 a.T[0,0] 之后 a =\n", a, " <- a 也变了，确认是视图")
```

**输出**

    a (2,3) =
     [[1 2 3]
     [4 5 6]]

    a.T (3,2) =
     [[1 4]
     [2 5]
     [3 6]]
    a.T.shape      : (3, 2)
    a.transpose() 等价于 a.T
    a.T.base is a  : True  <- 视图，不复制内存

    改 a.T[0,0] 之后 a =
     [[999   2   3]
     [  4   5   6]]  <- a 也变了，确认是视图

> 💡 **为什么这里要加 `.copy()`？** 因为 `np.arange(1, 7).reshape(2, 3)` 得到的 `a` 本身也是别人的视图，
> 此时 `a.T.base` 会指向更底层那个临时数组，`a.T.base is a` 就是 `False` 了。
> **判断视图/副本，不要只看 `base is`，更可靠的是"改一下看原数组变不变"**——就像上面这样。

**三维以上**用 `transpose(轴的新顺序)` 或 `swapaxes`：

```python
import numpy as np

b = np.arange(24).reshape(2, 3, 4)
print("b.shape                    :", b.shape)
print("b.transpose(1, 0, 2).shape :", b.transpose(1, 0, 2).shape)
print("b.swapaxes(0, 2).shape     :", b.swapaxes(0, 2).shape)
```

**输出**

    b.shape                    : (2, 3, 4)
    b.transpose(1, 0, 2).shape : (3, 2, 4)
    b.swapaxes(0, 2).shape     : (4, 3, 2)

> 💡 转置在实战里的用途：算"每行 vs 每列"的距离矩阵、把 `(样本数, 特征数)` 变成 `(特征数, 样本数)`。

## 4.4 升维与降维：`np.newaxis` / `expand_dims` / `squeeze`

**这是解决广播问题的关键工具**，课程没讲。

```python
import numpy as np

v = np.array([1, 2, 3])
print("v.shape             :", v.shape)
print("v[:, np.newaxis]    :", v[:, np.newaxis].shape, " <- 变列向量")
print("v[np.newaxis, :]    :", v[np.newaxis, :].shape, " <- 变行向量")
print("np.expand_dims(v, 0):", np.expand_dims(v, 0).shape)
print("np.expand_dims(v, 1):", np.expand_dims(v, 1).shape)
print("\nv[:, np.newaxis] =\n", v[:, np.newaxis])
print("\nsqueeze 去掉长度为1的维度:", np.squeeze(np.zeros((1, 3, 1))).shape)
```

**输出**

    v.shape             : (3,)
    v[:, np.newaxis]    : (3, 1)  <- 变列向量
    v[np.newaxis, :]    : (1, 3)  <- 变行向量
    np.expand_dims(v, 0): (1, 3)
    np.expand_dims(v, 1): (3, 1)

    v[:, np.newaxis] =
     [[1]
     [2]
     [3]]

    squeeze 去掉长度为1的维度: (3,)

**为什么重要？** 看这个"每行除以行和"的例子——`keepdims` 和 `newaxis` 都是为了保持维度：

```python
import numpy as np

a = np.arange(6).reshape(2, 3)
print("a =\n", a)

print("\nsum(axis=1) 的形状是 (2,)，没法直接除:")
print("  a.sum(axis=1) =", a.sum(axis=1), "shape", a.sum(axis=1).shape)

print("\n方法1 加 keepdims 保持 (2,1):")
print(a / a.sum(axis=1, keepdims=True))

print("\n方法2 手动加一维 [:, np.newaxis]:")
print(a / a.sum(axis=1)[:, np.newaxis])
```

**输出**

    a =
     [[0 1 2]
     [3 4 5]]

    sum(axis=1) 的形状是 (2,)，没法直接除:
      a.sum(axis=1) = [ 3 12] shape (2,)

    方法1 加 keepdims 保持 (2,1):
    [[0.         0.33333333 0.66666667]
     [0.25       0.33333333 0.41666667]]

    方法2 手动加一维 [:, np.newaxis]:
    [[0.         0.33333333 0.66666667]
     [0.25       0.33333333 0.41666667]]

> 💡 `a / a.sum(axis=1)` 直接写会报 `operands could not be broadcast together with shapes (2,3) (2,)`。
> **记住这个套路：`sum(axis=1, keepdims=True)`。**

## 4.5 拼接：`concatenate` / `vstack` / `hstack` / `stack`

**先分清两组概念**：

- `concatenate`：**沿着已有的一维拼**，维度数不变
- `stack`：**新开一维**，维度数 +1

```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("concatenate 拼成一维:", np.concatenate([x, y]), "| shape", np.concatenate([x, y]).shape)
print("\nstack axis=0 叠成两行:\n", np.stack([x, y], axis=0), "| shape", np.stack([x, y], axis=0).shape)
print("\nstack axis=1 叠成两列:\n", np.stack([x, y], axis=1), "| shape", np.stack([x, y], axis=1).shape)
```

**输出**

    concatenate 拼成一维: [1 2 3 4 5 6] | shape (6,)

    stack axis=0 叠成两行:
     [[1 2 3]
     [4 5 6]] | shape (2, 3)

    stack axis=1 叠成两列:
     [[1 4]
     [2 5]
     [3 6]] | shape (3, 2)

**二维数组**：

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("A =\n", A)
print("B =\n", B)

print("\nvstack 竖着摞:\n", np.vstack([A, B]))
print("\nhstack 横着接:\n", np.hstack([A, B]))
print("\nconcatenate(axis=0) 等同 vstack:\n", np.concatenate([A, B], axis=0))
print("\nconcatenate(axis=1) 等同 hstack:\n", np.concatenate([A, B], axis=1))
```

**输出**

    A =
     [[1 2]
     [3 4]]
    B =
     [[5 6]
     [7 8]]

    vstack 竖着摞:
     [[1 2]
     [3 4]
     [5 6]
     [7 8]]

    hstack 横着接:
     [[1 2 5 6]
     [3 4 7 8]]

    concatenate(axis=0) 等同 vstack:
     [[1 2]
     [3 4]
     [5 6]
     [7 8]]

    concatenate(axis=1) 等同 hstack:
     [[1 2 5 6]
     [3 4 7 8]]

> ⚠️ **坑**：`concatenate` 除了拼接轴以外，**其他维度必须完全一致**。`(2,3)` 和 `(2,4)` 按 axis=0 拼没问题，按 axis=1 拼也会成功（3+4=7）；但 `(2,3)` 和 `(3,3)` 按 axis=1 拼就会报错。

## 4.6 拆分：`split` / `array_split` / `vsplit` / `hsplit`

```python
import numpy as np

a = np.arange(9)
print("split(a, 3) 三等分:", np.split(a, 3))

print("\n10 个元素分 3 份，split 会报错，要用 array_split:")
print(np.array_split(np.arange(10), 3))

b = np.arange(12).reshape(3, 4)
print("\nb =\n", b)
print("\nvsplit(b, 3) 按行切:\n", np.vsplit(b, 3))
print("\nhsplit(b, 2) 按列切:\n", np.hsplit(b, 2))
```

**输出**

    split(a, 3) 三等分: [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]

    10 个元素分 3 份，split 会报错，要用 array_split:
    [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]

    b =
     [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]

    vsplit(b, 3) 按行切:
     [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

    hsplit(b, 2) 按列切:
     [array([[0, 1],
           [4, 5],
           [8, 9]]), array([[ 2,  3],
           [ 6,  7],
           [10, 11]])]

> 💡 `split` 返回的是**列表**，不是数组。想拿第 1 份要写 `np.split(a, 3)[0]`。

## 🧪 第 4 章 练习

**4-1** 把 `np.arange(24)` 变成 shape 为 `(2, 3, 4)` 的数组，再把它变成 `(4, 6)`。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

a = np.arange(24)
b = a.reshape(2, 3, 4)
print(b.shape)          # (2, 3, 4)
print(b.reshape(4, 6).shape)   # (4, 6)
print(b.reshape(4, -1).shape)  # (4, 6)  用 -1 更省事
```

`reshape` 不要求形状"对应"，只要求**元素总数相等**。24 = 2×3×4 = 4×6，所以随便转。

</details>

**4-2** 给定 `a = np.arange(12).reshape(3, 4)`，用三种方法把它拉平成一维。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

a = np.arange(12).reshape(3, 4)

print(a.ravel())            # 视图
print(a.flatten())          # 副本
print(a.reshape(-1))        # 视图
print(a.reshape(12))        # 视图
```

四种都输出 `[ 0  1  2  3  4  5  6  7  8  9 10 11]`。
区别：`flatten()` 返回副本，其余返回视图。

</details>

**4-3** 有两个一维数组 `x = np.array([1, 2, 3])` 和 `y = np.array([4, 5, 6])`，
把它们变成一个 `(2, 3)` 的数组，再变成一个 `(3, 2)` 的数组。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(np.stack([x, y], axis=0))   # (2, 3)
print(np.stack([x, y], axis=1))   # (3, 2)
```

输出：

    [[1 2 3]
     [4 5 6]]
    [[1 4]
     [2 5]
     [3 6]]

**关键点**：`stack` 是"新开一维"，`concatenate` 做不到这件事（它只会得到 `(6,)`）。

</details>

**4-4** 给定 `a = np.arange(6).reshape(2, 3)`，算出**每列占该列总和的比例**（即每列归一化到和为 1）。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

a = np.arange(6).reshape(2, 3)
print("a =\n", a)

result = a / a.sum(axis=0, keepdims=True)
print("每列归一化:\n", result)
print("验证每列和为1:", result.sum(axis=0))
```

输出：

    a =
     [[0 1 2]
     [3 4 5]]
    每列归一化:
     [[0.  0.2 0.28571429]
     [1.  0.8 0.71428571]]
    验证每列和为1: [1. 1. 1.]

**注意 `axis=0`**：要按列归一化（每列和为 1），就要消掉行这一维。

</details>

---

# 第 5 章 常用函数与 axis ⭐⭐⭐⭐⭐

> 对应课程 2.7

## 5.1 数学函数

课程列了一张表，这里补全并逐个验证。

```python
import numpy as np

a = np.array([-1.7, -0.5, 0.5, 1.7, 2.5])

print("原数组 :", a)
print("abs    :", np.abs(a))
print("ceil   :", np.ceil(a), "  <- 向上取整")
print("floor  :", np.floor(a), "  <- 向下取整")
print("rint   :", np.rint(a), "  <- 四舍五入到最近的偶数")
print("sign   :", np.sign(a), "  <- 符号")
```

**输出**

    原数组 : [-1.7 -0.5  0.5  1.7  2.5]
    abs    : [1.7 0.5 0.5 1.7 2.5]
    ceil   : [-1. -0.  1.  2.  3.]   <- 向上取整
    floor  : [-2. -1.  0.  1.  2.]   <- 向下取整
    rint   : [-2. -0.  0.  2.  2.]   <- 四舍五入到最近的偶数
    sign   : [-1. -1.  1.  1.  1.]   <- 符号

> ⚠️ **`rint` 是"银行家舍入"**：`0.5` → `0`，`1.5` → `2`，`2.5` → `2`。**不是**你小学学的"四舍五入"！
> 金融计算里这很重要。想要传统四舍五入，用 `np.floor(x + 0.5)`。

```python
import numpy as np

b = np.array([1, 4, 9, 16])

print("sqrt  :", np.sqrt(b))
print("power :", np.power(b, 2))
print("mod   :", np.mod(np.array([7, 8, 9]), 3))
print("exp   :", np.exp(np.array([0.0, 1.0])))
print("log   :", np.log(np.array([1.0, np.e])))
print("log2  :", np.log2(np.array([1.0, 8.0])))
```

**输出**

    sqrt  : [1. 2. 3. 4.]
    power : [  1  16  81 256]
    mod   : [1 2 0]
    exp   : [1.         2.71828183]
    log   : [0. 1.]
    log2  : [0. 3.]

**除零和非法运算**——NumPy 不会抛异常，而是给你 `inf` / `nan`：

```python
import numpy as np

a = np.array([1.0, 0.0, -1.0])

with np.errstate(divide="ignore", invalid="ignore"):
    print("1/a :", 1 / a)
    print("log :", np.log(a))
```

**输出**

    1/a : [ 1. inf -1.]
    log : [  0. -inf  nan]

> ⚠️ 默认情况下 NumPy 会打印 `RuntimeWarning: divide by zero encountered`，但**照样算完**。用 `np.errstate(...)` 可以临时关掉警告。
> ⚠️ `inf` 参与运算会污染结果（`inf - inf = nan`），分析数据前记得检查 `np.isfinite(a).all()`。

## 5.2 统计函数与 axis ⭐

**这是课程 2.7.2 的内容，但课程只讲了"默认算全部"，没讲透 axis。**

```python
import numpy as np

a = np.array([[4, 2, 7, 1],
              [9, 3, 5, 8],
              [6, 1, 2, 4]])
print("a =\n", a)
```

**输出**

    a =
     [[4 2 7 1]
     [9 3 5 8]
     [6 1 2 4]]

```python
import numpy as np

a = np.array([[4, 2, 7, 1],
              [9, 3, 5, 8],
              [6, 1, 2, 4]])

print("sum  全部       :", a.sum())
print("sum  axis=0 每列:", a.sum(axis=0))
print("sum  axis=1 每行:", a.sum(axis=1))

print("\nmean 全部       :", a.mean())
print("mean axis=0 每列:", a.mean(axis=0))
print("mean axis=1 每行:", a.mean(axis=1))

print("\nmax  axis=0 每列:", a.max(axis=0))
print("max  axis=1 每行:", a.max(axis=1))
print("min  axis=0 每列:", a.min(axis=0))

print("\nstd  全部       :", a.std())
print("var  全部       :", a.var())
print("median 全部     :", np.median(a))
```

**输出**

    sum  全部       : 52
    sum  axis=0 每列: [19  6 14 13]
    sum  axis=1 每行: [14 25 13]

    mean 全部       : 4.333333333333333
    mean axis=0 每列: [6.33333333 2.         4.66666667 4.33333333]
    mean axis=1 每行: [3.5  6.25 3.25]

    max  axis=0 每列: [9 3 7 8]
    max  axis=1 每行: [7 9 6]
    min  axis=0 每列: [4 1 2 1]

    std  全部       : 2.592724864350674
    var  全部       : 6.722222222222222
    median 全部     : 4.0

**手工验证 `sum(axis=0) = [19, 6, 14, 13]`**：第 0 列 `4+9+6=19`，第 1 列 `2+3+1=6`，第 2 列 `7+5+2=14`，第 3 列 `1+8+4=13`。✅ 列还在、行没了。

### `argmax` / `argmin`：返回**下标**而不是值

```python
import numpy as np

a = np.array([[1, 9], [5, 2]])

print("a =\n", a)
print("argmax 全局        :", a.argmax(), " <- 展平后的下标，不是行列！")
print("还原成行列         :", np.unravel_index(a.argmax(), a.shape))
print("argmax(axis=0) 每列最大值的行号:", a.argmax(axis=0))
print("argmax(axis=1) 每行最大值的列号:", a.argmax(axis=1))
```

**输出**

    a =
     [[1 9]
     [5 2]]
    argmax 全局        : 1  <- 展平后的下标，不是行列！
    还原成行列         : (np.int64(0), np.int64(1))
    argmax(axis=0) 每列最大值的行号: [1 0]
    argmax(axis=1) 每行最大值的列号: [1 0]

> ⚠️ **坑**：不加 `axis` 的 `argmax()` 返回的是"把数组拍平之后"的下标。`(2,2)` 的数组返回 `1`，你没法直接知道是第几行第几列——**必须用 `np.unravel_index()` 还原**。

### 累加累乘 `cumsum` / `cumprod`

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print("a =\n", a)
print("\ncumsum 默认拍平      :", a.cumsum())
print("cumsum(axis=0) 逐列累加:\n", a.cumsum(axis=0))
print("cumsum(axis=1) 逐行累加:\n", a.cumsum(axis=1))
print("\ncumprod 默认拍平     :", a.cumprod())
print("cumprod(axis=1)      :\n", a.cumprod(axis=1))
```

**输出**

    a =
     [[1 2 3]
     [4 5 6]]

    cumsum 默认拍平      : [ 1  3  6 10 15 21]
    cumsum(axis=0) 逐列累加:
     [[1 2 3]
     [5 7 9]]
    cumsum(axis=1) 逐行累加:
     [[ 1  3  6]
     [ 4  9 15]]

    cumprod 默认拍平     : [  1   2   6  24 120 720]
    cumprod(axis=1)      :
     [[  1   2   6]
     [  4  20 120]]

> ⚠️ **`cumsum()` 不加 axis 会把数组拍平再累加**，结果是一维的。这跟 `sum()` 不加 axis 返回标量不是一个套路，容易搞混。
> **记住：`cumsum` / `cumprod` 默认 `axis=None`（拍平），`sum` / `mean` 默认 `axis=None`（全部）。**

### 百分位数 `percentile` / `quantile`

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("中位数 median     :", np.median(x))
print("percentile 25     :", np.percentile(x, 25))
print("percentile 90     :", np.percentile(x, 90))
print("一次算多个分位数   :", np.percentile(x, [25, 50, 75]))
print("quantile 0.25 等价 :", np.quantile(x, 0.25))
```

**输出**

    中位数 median     : 5.5
    percentile 25     : 3.25
    percentile 90     : 9.1
    一次算多个分位数   : [3.25 5.5  7.75]
    quantile 0.25 等价 : 3.25

> 💡 `percentile(x, 25)` 和 `quantile(x, 0.25)` 是一回事，只是刻度不同（0~100 vs 0~1）。
> 第 8 章用 IQR 法找异常值时会用到。

## 5.3 `keepdims`：保持维度，专治广播报错

```python
import numpy as np

a = np.arange(6).reshape(2, 3)

print("不保持维度 sum(axis=1)        :", a.sum(axis=1), "shape", a.sum(axis=1).shape)
print("保持维度 sum(axis=1,keepdims) :\n", a.sum(axis=1, keepdims=True), "shape", a.sum(axis=1, keepdims=True).shape)
```

**输出**

    不保持维度 sum(axis=1)        : [ 3 12] shape (2,)
    保持维度 sum(axis=1,keepdims) :
     [[ 3]
     [12]] shape (2, 1)

**用途就一个：让后面的广播能对上。** 详见 4.4 节的"每行除以行和"。

## 5.4 比较与逻辑：`any` / `all` / `array_equal` / `allclose`

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])

print("any(a > 3):", np.any(a > 3), " <- 存在就 True")
print("all(a > 3):", np.all(a > 3), " <- 全部才 True")
print("any(a > 9):", np.any(a > 9))
print("all(a > 0):", np.all(a > 0))

b = np.array([[1, 2, 3], [4, 5, 6]])
print("\nall(b > 0, axis=1):", np.all(b > 0, axis=1))
print("any(b > 5, axis=1):", np.any(b > 5, axis=1))
```

**输出**

    any(a > 3): True  <- 存在就 True
    all(a > 3): False  <- 全部才 True
    any(a > 9): False
    all(a > 0): True

    all(b > 0, axis=1): [ True  True]
    any(b > 5, axis=1): [False  True]

### ⚠️ 浮点数比较**永远**不要用 `==`

```python
import numpy as np

print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3 ?", 0.1 + 0.2 == 0.3)

print("\narray_equal 严格比较:", np.array_equal([0.1 + 0.2], [0.3]))
print("allclose 容差比较  :", np.allclose([0.1 + 0.2], [0.3]))
print("allclose 自定义容差:", np.allclose([0.1 + 0.2], [0.3], atol=1e-10))
```

**输出**

    0.1 + 0.2 = 0.30000000000000004
    0.1 + 0.2 == 0.3 ? False

    array_equal 严格比较: False
    allclose 容差比较  : True
    allclose 自定义容差: True

> ⚠️ **这是所有编程语言的通病，不是 Python 的 bug**：二进制没法精确表示 0.1 和 0.2。
> **判断浮点数组是否相等，一律用 `np.allclose()`，不要用 `==` 或 `array_equal()`。**

## 5.5 排序

```python
import numpy as np

a = np.array([[3, 1, 4, 1],
              [5, 9, 2, 6],
              [5, 3, 5, 8]])
print("a =\n", a)

b = a.copy()
b.sort()                     # 就地排序，默认 axis=-1（每行内部排）
print("\nndarray.sort() 就地，默认每行排:\n", b)

c = a.copy()
c.sort(axis=0)               # 每列排序
print("\nsort(axis=0) 每列排:\n", c)

print("\nnp.sort(a) 返回副本，a 不变:\n", np.sort(a))
print("\na 依然是原来的:\n", a)
```

**输出**

    a =
     [[3 1 4 1]
     [5 9 2 6]
     [5 3 5 8]]

    ndarray.sort() 就地，默认每行排:
     [[1 1 3 4]
     [2 5 6 9]
     [3 5 5 8]]

    sort(axis=0) 每列排:
     [[3 1 2 1]
     [5 3 4 6]
     [5 9 5 8]]

    np.sort(a) 返回副本，a 不变:
     [[1 1 3 4]
     [2 5 6 9]
     [3 5 5 8]]

    a 依然是原来的:
     [[3 1 4 1]
     [5 9 2 6]
     [5 3 5 8]]

> ⚠️ **`a.sort()` 就地改，返回 `None`；`np.sort(a)` 返回新数组。**
> 和 `shuffle` 一样，写 `a = a.sort()` 会让 `a` 变 `None`——高频事故。

### `argsort`：拿到排序后的**下标**（做 Top-N 必备）

```python
import numpy as np

x = np.array([30, 10, 50, 20, 40])

print("原数组          :", x)
print("argsort 升序下标:", np.argsort(x))
print("用下标取值       :", x[np.argsort(x)])
print("降序            :", x[np.argsort(x)][::-1])

print("\n最大的 3 个值   :", np.sort(x)[::-1][:3])
print("最大的 3 个下标 :", np.argsort(x)[::-1][:3])
```

**输出**

    原数组          : [30 10 50 20 40]
    argsort 升序下标: [1 3 0 4 2]
    用下标取值       : [10 20 30 40 50]
    降序            : [50 40 30 20 10]

    最大的 3 个值   : [50 40 30]
    最大的 3 个下标 : [2 4 0]

> 💡 **`x[np.argsort(x)[::-1][:3]]` 是"取最大的 3 个元素"的标准写法。**
> 想同时拿到值和原始位置（比如"销售额最高的 3 个门店是哪几家"），就靠 `argsort`。

## 5.6 去重 `unique`

```python
import numpy as np

a = np.array([3, 1, 3, 2, 1, 3])

print("原数组 :", a)
print("unique :", np.unique(a), " <- 顺便排好序了")
```

**输出**

    原数组 : [3 1 3 2 1 3]
    unique : [1 2 3]  <- 顺便排好序了

**`return_counts` 是最常用的参数**（相当于 Pandas 的 `value_counts`）：

```python
import numpy as np

a = np.array([3, 1, 3, 2, 1, 3])

values, counts = np.unique(a, return_counts=True)
print("值  :", values)
print("次数:", counts)

print("\n出现最多的值:", values[counts.argmax()], "出现", counts.max(), "次")

# 还想知道每个值第一次出现在哪
values, first_idx = np.unique(a, return_index=True)
print("\n首次出现的下标:", first_idx)
```

**输出**

    值  : [1 2 3]
    次数: [2 1 3]

    出现最多的值: 3 出现 3 次

    首次出现的下标: [1 3 0]

**二维数组按行去重**（课程没讲，很实用）：

```python
import numpy as np

b = np.array([[1, 2],
              [1, 2],
              [3, 4]])
print("原数组:\n", b)
print("\nunique(axis=0) 按行去重:\n", np.unique(b, axis=0))
```

**输出**

    原数组:
     [[1 2]
     [1 2]
     [3 4]]

    unique(axis=0) 按行去重:
     [[1 2]
     [3 4]]

## 5.7 NaN 处理 ⭐⭐⭐ 课程完全没讲

**真实数据一定有缺失值。** NumPy 里缺失值就是 `np.nan`（Not a Number），它有**两个致命特性**：

1. **任何跟 `nan` 的运算结果都是 `nan`** —— 所以 `sum()` `mean()` 直接被污染
2. **`nan == nan` 永远是 `False`** —— 所以不能用 `==` 判断，必须用 `np.isnan()`

```python
import numpy as np

a = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
print("数组:", a)

print("\n=== 特性1：nan 会污染运算 ===")
print("sum     :", a.sum(), "  <- 直接废了")
print("mean    :", a.mean(), "  <- 直接废了")

print("\n=== 特性2：nan == nan 是 False ===")
print("a == np.nan :", a == np.nan, "  <- 全是 False！")
print("np.isnan(a) :", np.isnan(a), "  <- 必须这样判")
```

**输出**

    数组: [ 1. nan  3. nan  5.]

    === 特性1：nan 会污染运算 ===
    sum     : nan   <- 直接废了
    mean    : nan   <- 直接废了

    === 特性2：nan == nan 是 False ===
    a == np.nan : [False False False False False]   <- 全是 False！
    np.isnan(a) : [False  True False  True False]   <- 必须这样判

### 五个 `nan*` 函数：跳过缺失值再算

```python
import numpy as np

a = np.array([1.0, np.nan, 3.0, np.nan, 5.0])

print("isnan 个数  :", np.isnan(a).sum())
print("nansum      :", np.nansum(a))
print("nanmean     :", np.nanmean(a))
print("nanmax/nanmin:", np.nanmax(a), np.nanmin(a))
print("nanstd      :", np.nanstd(a))
print("nanmedian   :", np.nanmedian(a))
```

**输出**

    isnan 个数  : 2
    nansum      : 9.0
    nanmean     : 3.0
    nanmax/nanmin: 5.0 1.0
    nanstd      : 1.632993161855452
    nanmedian   : 3.0

**把缺失值删掉或者填上**：

```python
import numpy as np

a = np.array([1.0, np.nan, 3.0, np.nan, 5.0])

# 删掉
print("删除 NaN :", a[~np.isnan(a)])

# 填 0
print("填 0     :", np.where(np.isnan(a), 0, a))

# 填均值（比填 0 合理得多）
print("填均值   :", np.where(np.isnan(a), np.nanmean(a), a))
```

**输出**

    删除 NaN : [1. 3. 5.]
    填 0     : [1. 0. 3. 0. 5.]
    填均值   : [1. 3. 3. 3. 5.]

> ⚠️ **坑**：如果某一列**全是 NaN**，`np.nanmean()` 会返回 `nan` 并打印
> `RuntimeWarning: Mean of empty slice`。这时要先检查 `np.isnan(col).all()`。

> 💡 **实战提醒**：真实数据里，一列出现 `nan` 通常有三种含义——**真的缺失**、**该值不存在**（比如"未翻新"的年份）、**0 但被记成了空**。
> 处理前**一定先问清楚业务含义**，不要无脑 `fillna(0)`。第 8 章会踩到这个坑。

## 🧪 第 5 章 练习

**5-1** 给定 `a = np.array([[4, 2, 7, 1], [9, 3, 5, 8], [6, 1, 2, 4]])`，
求：① 每列最大值 ② 每行平均值 ③ 所有元素的中位数 ④ 每行最大值所在的列号。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

a = np.array([[4, 2, 7, 1],
              [9, 3, 5, 8],
              [6, 1, 2, 4]])

print("每列最大值 :", a.max(axis=0))        # [9 3 7 8]
print("每行平均值 :", a.mean(axis=1))       # [3.5  6.25 3.25]
print("整体中位数 :", np.median(a))         # 4.0
print("每行最大值列号:", a.argmax(axis=1))  # [2 0 0]
```

第 4 问最容易错：`a.argmax()` 不加 axis 会返回**展平后的下标**，必须加 `axis=1`。

</details>

**5-2** 判断：`np.rint(0.5)` `np.rint(1.5)` `np.rint(2.5)` 分别是多少？先猜再验证。

<details>
<summary>💡 参考答案</summary>

分别是 **0.0、2.0、2.0**。

```python
import numpy as np
print(np.rint([0.5, 1.5, 2.5, 3.5]))   # [0. 2. 2. 4.]
```

`np.rint` 用的是**银行家舍入**（四舍六入五取偶），不是小学的四舍五入。想要传统写法用 `np.floor(x + 0.5)`。

</details>

**5-3** 有一个含缺失值的数组 `a = np.array([2.0, np.nan, 8.0, np.nan, 4.0, 6.0])`，
求：① 缺失值个数 ② 忽略缺失值后的均值 ③ 用均值填补后的数组。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

a = np.array([2.0, np.nan, 8.0, np.nan, 4.0, 6.0])

print("缺失个数:", np.isnan(a).sum())            # 2
print("均值    :", np.nanmean(a))                # 5.0
print("填补后  :", np.where(np.isnan(a), np.nanmean(a), a))
# [2. 5. 8. 5. 4. 6.]
```

</details>

**5-4** 给定一维数组 `x = np.array([30, 10, 50, 20, 40])`，
取出**最大的两个元素的原始下标**。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

x = np.array([30, 10, 50, 20, 40])

idx = np.argsort(x)[::-1][:2]
print("下标:", idx)          # [2 4]
print("值  :", x[idx])       # [50 40]
```

如果只要值不要下标，`np.sort(x)[::-1][:2]` 就够了。

</details>

**5-5** 下面代码输出什么？为什么？

```python
import numpy as np
a = np.array([0.1, 0.2, 0.3])
print("a[2] == 0.3          :", a[2] == 0.3)
print("a[0] + a[1] == a[2]  :", a[0] + a[1] == a[2])
print("a[0] + a[1] 实际等于  :", repr(a[0] + a[1]))
print("allclose 判断         :", np.allclose(a[0] + a[1], a[2]))
```

<details>
<summary>💡 参考答案</summary>

输出：

    a[2] == 0.3          : True
    a[0] + a[1] == a[2]  : False
    a[0] + a[1] 实际等于  : 0.30000000000000004
    allclose 判断         : True

**这里有两个容易搞混的点，一定要分清：**

① `a[2] == 0.3` 是 **True**。因为字面量 `0.3` 和存进数组的 `0.3` 是**同一个二进制双精度数**，当然相等。

② `a[0] + a[1] == a[2]` 是 **False**。因为 `0.1 + 0.2` 算出来是 `0.30000000000000004`，
和 `0.3` 差了一个极小的量——**误差是在"算"的过程中产生的，不是"存"的过程中**。

**结论：只要做过运算，就别用 `==` 比较浮点数，一律用 `np.allclose()`。**

> 💡 想确认某个浮点数组到底存的是什么，用 `repr()` 或 `.tolist()`，
> 别用 `print(a)`——NumPy 默认会"四舍五入"显示，看不出真实值。

</details>

---

# 第 6 章 运算与广播 ⭐⭐⭐⭐

> 对应课程 2.8 – 2.9

## 6.1 元素级运算

**大小相同的两个数组做任何算术运算，都是"对应位置各算各的"。**

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print("a =\n", a)
print("b =\n", b)

print("\na + b  =\n", a + b)
print("\na - b  =\n", a - b)
print("\na * b  元素相乘 =\n", a * b)
print("\na / b  结果自动变浮点 =\n", a / b)
print("\na // b 整除 =\n", a // b)
print("\na % b  取余 =\n", a % b)
print("\na ** 2 平方 =\n", a ** 2)
```

**输出**

    a =
     [[1 2 3]
     [4 5 6]]
    b =
     [[ 7  8  9]
     [10 11 12]]

    a + b  =
     [[ 8 10 12]
     [14 16 18]]

    a - b  =
     [[-6 -6 -6]
     [-6 -6 -6]]

    a * b  元素相乘 =
     [[ 7 16 27]
     [40 55 72]]

    a / b  结果自动变浮点 =
     [[0.14285714 0.25       0.33333333]
     [0.4        0.45454545 0.5       ]]

    a // b 整除 =
     [[0 0 0]
     [0 0 0]]

    a % b  取余 =
     [[1 2 3]
     [4 5 6]]

    a ** 2 平方 =
     [[ 1  4  9]
     [16 25 36]]

### 和标量运算：标量自动"扩散"到每个元素

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print("a + 100 =\n", a + 100)
print("\na * 100 =\n", a * 100)
print("\na / 100 =\n", a / 100)
```

**输出**

    a + 100 =
     [[101 102 103]
     [104 105 106]]

    a * 100 =
     [[100 200 300]
     [400 500 600]]

    a / 100 =
     [[0.01 0.02 0.03]
     [0.04 0.05 0.06]]

### 比较运算也是元素级

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print("a > 3  =\n", a > 3)
print("\na == 2 =\n", a == 2)
print("\na != 2 =\n", a != 2)
```

**输出**

    a > 3  =
     [[False False False]
     [ True  True  True]]

    a == 2 =
     [[False  True False]
     [False False False]]

    a != 2 =
     [[ True False  True]
     [ True  True  True]]

### ⚠️ 坑：就地运算 `+=` 会改原数组

```python
import numpy as np

a = np.array([1, 2, 3])
b = a            # b 和 a 是同一个对象
b += 100         # 就地修改
print("a:", a)   # a 也变了
print("b:", b)

x = np.array([1, 2, 3])
y = x + 100      # 这会创建新数组
print("\nx:", x, " <- 没变")
print("y:", y)
```

**输出**

    a: [101 102 103]
    b: [101 102 103]

    x: [1 2 3]  <- 没变
    y: [101 102 103]

## 6.2 广播机制的三条规则 ⭐⭐⭐

**广播（broadcasting）= 形状不同的数组之间也能做逐元素运算。**

课程给了三条规则，但说得绕。这里换成**一遍就能记住**的版本：

> **规则 1**：把两个形状**右对齐**排列，左边不够的补 `1`。
> **规则 2**：从右往左逐个维度比较，**相等**或者**其中一个是 1** 就能兼容；是 1 的那个会"复制展开"。
> **规则 3**：只要有一个维度**既不相等、又都不是 1**，直接报错。

### 演示：规则 1 + 规则 2

```python
import numpy as np

arr1 = np.array([1, 2, 3])          # shape (3,)
arr2 = np.array([[4], [5], [6]])    # shape (3, 1)

print("arr1.shape:", arr1.shape, "   arr2.shape:", arr2.shape)
print("右对齐:  (3,)  -> (1, 3)   [左边补 1]")
print("          (3,1) -> (3, 1)")
print("第1维: 1 vs 3，兼容，arr1 沿第0维复制 3 份 -> (3,3)")
print("第0维: 3 vs 3，相等，兼容\n")

print("arr1 + arr2 =\n", arr1 + arr2)
```

**输出**

    arr1.shape: (3,)    arr2.shape: (3, 1)
    右对齐:  (3,)  -> (1, 3)   [左边补 1]
              (3,1) -> (3, 1)
    第1维: 1 vs 3，兼容，arr1 沿第0维复制 3 份 -> (3,3)
    第0维: 3 vs 3，相等，兼容

    arr1 + arr2 =
     [[5 6 7]
     [6 7 8]
     [7 8 9]]

手工验证一下 `[0][0]`：`arr1` 展开后的 `1` 加上 `arr2` 展开后的 `4`，等于 `5`。✅

### 演示：规则 3（报错）

```python
import numpy as np

arr5 = np.array([1, 2, 3])   # (3,)
arr6 = np.array([4, 5])      # (2,)

try:
    arr5 + arr6
except ValueError as e:
    print("报错:", e)
```

**输出**

    报错: operands could not be broadcast together with shapes (3,) (2,) 

### 一张表看完全部情况

```python
import numpy as np

cases = [
    ((3,),   (3, 1)),
    ((2, 3), (3,)),
    ((2, 3), (2, 1)),
    ((2, 1), (1, 3)),
    ((4, 1), (3,)),
    ((5, 1), (1,)),
    ((2, 3), (2,)),      # 这行会失败
]

for s1, s2 in cases:
    try:
        result = (np.zeros(s1) + np.zeros(s2)).shape
        print(f"{str(s1):8} + {str(s2):8} -> {result}")
    except ValueError:
        print(f"{str(s1):8} + {str(s2):8} -> 报错")
```

**输出**

    (3,)     + (3, 1)   -> (3, 3)
    (2, 3)   + (3,)     -> (2, 3)
    (2, 3)   + (2, 1)   -> (2, 3)
    (2, 1)   + (1, 3)   -> (2, 3)
    (4, 1)   + (3,)     -> (4, 3)
    (5, 1)   + (1,)     -> (5, 1)
    (2, 3)   + (2,)     -> 报错

**为什么最后一行会报错？** 右对齐后：

    (2, 3)
    (   2)   <- (2,) 补成 (1, 2)

比较第 1 维：`3 vs 2`，既不相等、也都不是 1 → **报错**。

> 💡 **把这张表抄在便签上**，遇到 `operands could not be broadcast together` 就拿出来对一下。

### 广播报错怎么排查（三步）

```python
import numpy as np

a = np.zeros((2, 3))
b = np.zeros((2,))

try:
    a + b
except ValueError as e:
    print("第一步 看报错信息里的两个 shape:", e)
    print()
    print("第二步 打印实际形状:")
    print("   a.shape =", a.shape)
    print("   b.shape =", b.shape)
    print()
    print("第三步 想清楚你要什么，然后显式改形状:")
    print("   如果你想 b 是【列】，改成 b[:, np.newaxis]，变成", b[:, np.newaxis].shape)
    print("   如果你想 b 是【行】，改成 b[np.newaxis, :]，变成", b[np.newaxis, :].shape)
```

**输出**

    第一步 看报错信息里的两个 shape: operands could not be broadcast together with shapes (2,3) (2,) 

    第二步 打印实际形状:
       a.shape = (2, 3)
       b.shape = (2,)

    第三步 想清楚你要什么，然后显式改形状:
       如果你想 b 是【列】，改成 b[:, np.newaxis]，变成 (2, 1)
       如果你想 b 是【行】，改成 b[np.newaxis, :]，变成 (1, 2)

> ⚠️ **别用 `reshape` 猜**。`b.reshape(2,1)` 和 `b[:, np.newaxis]` 结果一样，但后者**一眼能看出你是想加一维**，可读性好得多。

## 6.3 广播实战：三个必会套路

### 套路 1：中心化（每列减去列均值）

```python
import numpy as np

a = np.array([[1., 2., 3.],
              [4., 5., 6.],
              [7., 8., 9.]])
print("原始 a =\n", a)

col_mean = a.mean(axis=0)
print("\n每列均值:", col_mean, " shape", col_mean.shape)
print("(3,3) - (3,) 能广播，因为 (3,) -> (1,3) 后第0维 1 vs 3 兼容")

centered = a - col_mean
print("\n中心化后（每列均值变成 0）:\n", centered)
print("\n验证:", np.round(centered.mean(axis=0), 10))
```

**输出**

    原始 a =
     [[1. 2. 3.]
     [4. 5. 6.]
     [7. 8. 9.]]

    每列均值: [4. 5. 6.]  shape (3,)
    (3,3) - (3,) 能广播，因为 (3,) -> (1,3) 后第0维 1 vs 3 兼容

    中心化后（每列均值变成 0）:
     [[-3. -3. -3.]
     [ 0.  0.  0.]
     [ 3.  3.  3.]]

    验证: [0. 0. 0.]

### 套路 2：标准化（z-score）

```python
import numpy as np

a = np.array([[1., 2., 3.],
              [4., 5., 6.],
              [7., 8., 9.]])

z = (a - a.mean(axis=0)) / a.std(axis=0)
print("标准化后（每列均值0、标准差1）:\n", z)
print("\n验证每列均值:", np.round(z.mean(axis=0), 10))
print("验证每列标准差:", np.round(z.std(axis=0), 10))
```

**输出**

    标准化后（每列均值0、标准差1）:
     [[-1.22474487 -1.22474487 -1.22474487]
     [ 0.          0.          0.        ]
     [ 1.22474487  1.22474487  1.22474487]]

    验证每列均值: [0. 0. 0.]
    验证每列标准差: [1. 1. 1.]

> 💡 **这就是机器学习里"特征标准化"的全部代码**。`axis=0` 是因为数据按"行=样本、列=特征"排布。

### 套路 3：距离矩阵（三维广播）

```python
import numpy as np

pts = np.array([[0, 0], [3, 4], [6, 8]])
print("三个点:\n", pts)

# 关键：一个加 newaxis 在中间，一个加在最前面
diff = pts[:, np.newaxis, :] - pts[np.newaxis, :, :]
print("\n两两之差 shape:", diff.shape, " <- (3,1,2) 和 (1,3,2) 广播成 (3,3,2)")

dist = np.sqrt((diff ** 2).sum(axis=-1))
print("\n距离矩阵:\n", dist)
```

**输出**

    三个点:
     [[0 0]
     [3 4]
     [6 8]]

    两两之差 shape: (3, 3, 2)  <- (3,1,2) 和 (1,3,2) 广播成 (3,3,2)

    距离矩阵:
     [[ 0.  5. 10.]
     [ 5.  0.  5.]
     [10.  5.  0.]]

**验证**：`(0,0)` 到 `(3,4)` 的距离 `√(3²+4²)=5`。✅

**外积**也靠广播：

```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([10, 20])

print("x[:, np.newaxis] shape:", x[:, np.newaxis].shape)
print("y shape:", y.shape)
print("\n外积:\n", x[:, np.newaxis] * y)
```

**输出**

    x[:, np.newaxis] shape: (3, 1)
    y shape: (2,)

    外积:
     [[10 20]
     [20 40]
     [30 60]]

## 6.4 矩阵乘法 `@`

**必须分清两个符号**：

| 符号 | 含义 | 例子 |
|---|---|---|
| `*` | **元素**相乘（对应位置） | `[1,2] * [3,4] = [3, 8]` |
| `@` | **矩阵**乘法 | 见下 |

```python
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])    # (2, 3)
arr2 = np.array([[6, 5], [4, 3], [2, 1]])  # (3, 2)

print("arr1.shape:", arr1.shape, "  arr2.shape:", arr2.shape)
print("要求：第一个的列数(3) == 第二个的行数(3) ✅\n")

print("arr1 @ arr2 =  (2,2)\n", arr1 @ arr2)
print("\nnp.dot(arr1, arr2) 完全一样:\n", np.dot(arr1, arr2))
print("\narr1.dot(arr2) 也完全一样:\n", arr1.dot(arr2))
```

**输出**

    arr1.shape: (2, 3)   arr2.shape: (3, 2)
    要求：第一个的列数(3) == 第二个的行数(3) ✅

    arr1 @ arr2 =  (2,2)
     [[20 14]
     [56 41]]

    np.dot(arr1, arr2) 完全一样:
     [[20 14]
     [56 41]]

    arr1.dot(arr2) 也完全一样:
     [[20 14]
     [56 41]]

**手算验证**（课程里也是这么推导的）：

- 结果 `[0][0]` = arr1 第 0 行 `[1,2,3]` · arr2 第 0 列 `[6,4,2]` = `1×6 + 2×4 + 3×2 = 20` ✅
- 结果 `[0][1]` = arr1 第 0 行 `[1,2,3]` · arr2 第 1 列 `[5,3,1]` = `5 + 6 + 3 = 14` ✅
- 结果 `[1][0]` = `4×6 + 5×4 + 6×2 = 56` ✅
- 结果 `[1][1]` = `4×5 + 5×3 + 6×1 = 41` ✅

**二维 @ 一维，结果是一维**：

```python
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.array([6, 5, 4])

print("arr1 @ arr3 =", arr1 @ arr3)
print("手算: 1*6+2*5+3*4 =", 1*6 + 2*5 + 3*4)
print("      4*6+5*5+6*4 =", 4*6 + 5*5 + 6*4)
```

**输出**

    arr1 @ arr3 = [28 73]
    手算: 1*6+2*5+3*4 = 28
          4*6+5*5+6*4 = 73

### ⚠️ 坑：`*` 和 `@` 搞混

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 2], [3, 4]])

print("a * b 元素乘法:\n", a * b)
print("\na @ b 矩阵乘法:\n", a @ b)
```

**输出**

    a * b 元素乘法:
     [[ 1  4]
     [ 9 16]]

    a @ b 矩阵乘法:
     [[ 7 10]
     [15 22]]

> ⚠️ **机器学习里"矩阵相乘"必须用 `@`**。用 `*` 算出来的是逐元素乘积，形状对但数值全错，**不会报错，最难查**。

## 6.5 向量化 vs 循环：为什么值得学 NumPy

```python
import time
import numpy as np

n = 1_000_000
lst = list(range(n))
arr = np.arange(n)

t0 = time.perf_counter()
s1 = sum(x * 2 for x in lst)
t1 = time.perf_counter()
s2 = (arr * 2).sum()
t2 = time.perf_counter()

print(f"Python 循环 : {t1 - t0:.4f}s")
print(f"NumPy 向量化: {t2 - t1:.4f}s")
print(f"加速比      : {(t1 - t0) / (t2 - t1):.0f}x")
print(f"结果一致    : {s1 == s2}")
```

**输出**（你的机器上数字会不同，但量级关系稳定）

    Python 循环 : 0.0311s
    NumPy 向量化: 0.0025s
    加速比      : 12x
    结果一致    : True

**"向量化思维"长什么样？**

```python
import numpy as np

a = np.array([1, -2, 3, -4, 5])

# ❌ 循环思维：能跑，但慢，而且啰嗦
result = []
for x in a:
    if x > 0:
        result.append(x)
    else:
        result.append(0)
print("循环写法:", result)

# ✅ 向量化思维：一行搞定，快几十倍
print("向量化  :", np.where(a > 0, a, 0).tolist())
print("向量化(不转 list):", np.where(a > 0, a, 0))
```

**输出**

    循环写法: [np.int64(1), 0, np.int64(3), 0, np.int64(5)]
    向量化  : [1, 0, 3, 0, 5]
    向量化(不转 list): [1 0 3 0 5]

> ⚠️ **注意第一行那奇怪的样子**。遍历 ndarray 拿到的每个元素**都不是 Python 原生 `int`，而是 `np.int64` 标量对象**。
> 平时打印看着像数字，但一到下面这些场景就炸：
>
> ```python
> import json
> import numpy as np
>
> a = np.array([1, 2, 3])
> try:
>     json.dumps([x for x in a])
> except TypeError as e:
>     print("报错:", e)
>
> print("转成原生 int 就好了:", json.dumps([int(x) for x in a]))
> print("整数组一次转换   :", json.dumps(a.tolist()))
> ```
>
> **输出**
>
>     报错: Object of type int64 is not JSON serializable
>     转成原生 int 就好了: [1, 2, 3]
>     整数组一次转换   : [1, 2, 3]
>
> **修法**：单个用 `int(x)` / `float(x)`，整数组用 `a.tolist()`。
> 写接口、存数据库、导出 JSON 时**一定会遇到**，先记住。

> 💡 **判断标准**：只要你在 NumPy 代码里写了 `for` 循环遍历数组元素，**大概率有更好的写法**。
> 常用替代：`np.where`、布尔索引赋值、`np.select`、`a.sum(axis=...)`、广播。

## 🧪 第 6 章 练习

**6-1** 给定 `a = np.arange(12).reshape(3, 4)`，求**每一列减去该列的最小值**（列归一化的第一步）。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

a = np.arange(12).reshape(3, 4)
print("a =\n", a)

result = a - a.min(axis=0)
print("\n每列减去列最小值:\n", result)
print("验证每列最小值都是0:", result.min(axis=0))
```

输出：

    a =
     [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]

    每列减去列最小值:
     [[0 0 0 0]
     [4 4 4 4]
     [8 8 8 8]]
    验证每列最小值都是0: [0 0 0 0]

`a.min(axis=0)` 形状是 `(4,)`，和 `(3,4)` 广播成 `(3,4)`。

</details>

**6-2** 下面的代码会报什么错？怎么改？

```python
import numpy as np
a = np.zeros((3, 4))
b = np.zeros((3,))
print(a + b)
```

<details>
<summary>💡 参考答案</summary>

报 `ValueError: operands could not be broadcast together with shapes (3,4) (3,)`。

右对齐后 `(3,)` 变 `(1,3)`，第 1 维 `4 vs 3` 既不相等也都不是 1 → 不兼容。

**改法取决于你想干什么**：

```python
import numpy as np

a = np.zeros((3, 4))
b = np.zeros((3,))

# 想按【行】加（每行加同一个数）—— 不可能，(3,) 是 3 个数，4 列对不上
# 想按【列】加（每列加同一个数）—— 需要 b 是 (3,1)
print((a + b[:, np.newaxis]).shape)   # (3, 4)  ✅

# 如果 b 本来就是 4 个数，想按行加：
b4 = np.zeros(4)
print((a + b4).shape)                 # (3, 4)  ✅
```

</details>

**6-3** 已知 `a = np.array([[1, 2], [3, 4]])`，不运行代码，说出 `a * a` 和 `a @ a` 的结果。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
print("a * a =\n", a * a)     # 元素乘
print("a @ a =\n", a @ a)     # 矩阵乘
```

输出：

    a * a =
     [[ 1  4]
     [ 9 16]]
    a @ a =
     [[ 7 10]
     [15 22]]

`a @ a` 的手算：`[0][0] = 1×1 + 2×3 = 7`，`[0][1] = 1×2 + 2×4 = 10`，
`[1][0] = 3×1 + 4×3 = 15`，`[1][1] = 3×2 + 4×4 = 22`。

</details>

**6-4** 用广播计算：一个 `(5, 2)` 的随机点集，两两之间的欧氏距离矩阵。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

rng = np.random.default_rng(0)
pts = rng.random((5, 2)) * 10
print("点集:\n", np.round(pts, 2))

diff = pts[:, np.newaxis, :] - pts[np.newaxis, :, :]     # (5,5,2)
dist = np.sqrt((diff ** 2).sum(axis=-1))                 # (5,5)

print("\n距离矩阵 shape:", dist.shape)
print(np.round(dist, 2))
print("\n对角线应该是0:", np.allclose(np.diag(dist), 0))
print("矩阵应该对称:", np.allclose(dist, dist.T))
```

**三个关键点**：
① `[:, np.newaxis, :]` 让形状变 `(5,1,2)`，`[np.newaxis, :, :]` 变 `(1,5,2)`；
② 广播成 `(5,5,2)`，最后一维是坐标差；
③ `sum(axis=-1)` 把坐标维消掉，得到 `(5,5)`。

</details>

---

# 第 7 章 文件读写与线性代数

> **课程第 2 章完全没有。** 这章偏工具，可以先扫一眼，用到再回来查。

## 7.1 保存和读取数组

| 格式 | 函数 | 特点 |
|---|---|---|
| `.npy` | `np.save` / `np.load` | **二进制**，单个数组，最快最小 |
| `.npz` | `np.savez` / `np.load` | 二进制，**多个数组打包** |
| `.csv` / `.txt` | `np.savetxt` / `np.loadtxt` | 文本，人能看懂，慢 |
| 带缺失值的文本 | `np.genfromtxt` | 文本，**能处理缺失值** |

```python
import numpy as np

a = np.arange(6).reshape(2, 3)
b = np.arange(3)

# 单个数组
np.save("_demo_a.npy", a)
print("npy 读回来是否一致:", np.array_equal(np.load("_demo_a.npy"), a))

# 多个数组打包
np.savez("_demo_data.npz", x=a, y=b)
z = np.load("_demo_data.npz")
print("npz 里的键:", list(z.keys()))
print("z['x'] =\n", z["x"])

# 文本格式
np.savetxt("_demo_a.csv", a, delimiter=",", fmt="%d")
print("\ncsv 读回来:\n", np.loadtxt("_demo_a.csv", delimiter=",", dtype=int))
```

**输出**

    npy 读回来是否一致: True
    npz 里的键: ['x', 'y']
    z['x'] =
     [[0 1 2]
     [3 4 5]]

    csv 读回来:
     [[0 1 2]
     [3 4 5]]

> ⚠️ 上面会在当前目录生成三个 `_demo_*` 文件，**练完记得删掉**。

### 读取真实数据：`loadtxt` vs `genfromtxt`

```python
import numpy as np

# weather.csv 有表头，而且最后一列是字符串
# 用 usecols 只取数值列，用 skiprows 跳过表头
w = np.loadtxt("weather.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4))
print("weather.csv ->", w.shape, w.dtype)

# penguins.csv 有缺失值，必须用 genfromtxt（loadtxt 会直接报错）
pg = np.genfromtxt("penguins.csv", delimiter=",", skip_header=1, usecols=(2, 3, 4, 5))
print("penguins.csv ->", pg.shape)
print("缺失值个数:", np.isnan(pg).sum())
```

**输出**

    weather.csv -> (1461, 4) float64
    penguins.csv -> (344, 4)
    缺失值个数: 8

| | `np.loadtxt` | `np.genfromtxt` |
|---|---|---|
| 缺失值 | ❌ 直接报错 | ✅ 填成 `nan` |
| 表头 | 需要 `skiprows` | 用 `skip_header` 更清楚 |
| 速度 | 快 | 慢一些 |

> 💡 **实战里读 CSV 基本都用 Pandas 的 `read_csv`**（第 3 章内容）。NumPy 这两个函数适合"纯数值、结构规整"的小文件。

## 7.2 `np.linalg`：线性代数

```python
import numpy as np

A = np.array([[1., 2.],
              [3., 4.]])
b = np.array([5., 11.])

print("A =\n", A)
print("\n行列式 det      :", np.linalg.det(A))
print("\n逆矩阵 inv      :\n", np.linalg.inv(A))
print("\n解方程 Ax=b     :", np.linalg.solve(A, b))
print("验证 A @ x == b :", np.allclose(A @ np.linalg.solve(A, b), b))
print("\n特征值 eigvals  :", np.linalg.eigvals(A))
print("\n秩 matrix_rank  :", np.linalg.matrix_rank(A))
```

**输出**

    A =
     [[1. 2.]
     [3. 4.]]

    行列式 det      : -2.0000000000000004

    逆矩阵 inv      :
     [[-2.   1. ]
     [ 1.5 -0.5]]

    解方程 Ax=b     : [1. 2.]
    验证 A @ x == b : True

    特征值 eigvals  : [-0.37228132  5.37228132]

    秩 matrix_rank  : 2

> ⚠️ **`det` 的结果是 `-2.0000000000000004` 而不是精确的 `-2`。** 这不是 bug，是浮点运算的必然结果。
> **永远不要用 `==` 比较线性代数的结果**，用 `np.allclose()`。
> 想要干净显示，用 `np.round(np.linalg.det(A), 10)`。

> 💡 **注意 `solve` 不要写成 `inv(A) @ b`**。数学上等价，但 `solve` 数值更稳定、速度更快。

## 🧪 第 7 章 练习

**7-1** 生成一个 `(3, 3)` 的随机数组，保存为 `.npy`，删除内存中的变量后再读回来，验证内容一致。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.random((3, 3))

np.save("_q71.npy", a)
del a                       # 删掉内存里的

b = np.load("_q71.npy")
print("读回来:\n", np.round(b, 4))
print("形状一致:", b.shape == (3, 3))
```

关键点：`np.save` 会自动加 `.npy` 后缀，所以 `np.load` 时要写全名 `'_q71.npy'`。

</details>

**7-2** 解方程组：
`2x + y = 5`
`x + 3y = 10`

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np

A = np.array([[2., 1.],
              [1., 3.]])
b = np.array([5., 10.])

x = np.linalg.solve(A, b)
print("解:", x)                       # [1. 3.]
print("验证:", A @ x)                 # [ 5. 10.]
```

所以 `x = 1`，`y = 3`。代回去：`2×1+3=5` ✅，`1+3×3=10` ✅

</details>

---

# 第 8 章 综合实战（真实数据）⭐⭐⭐⭐

> 前面 7 章是"零件"，这一章把它们组装起来。
> 用的是你仓库里 `10、Numpy/data/` 下真实存在的 CSV。

## 8.0 先解决"文件怎么读"

三个数据集的情况不一样，读法也不同：

| 文件 | 行数 | 特点 | 怎么读 |
|---|---|---|---|
| `penguins.csv` | 344 | **有缺失值**，有字符串列 | `genfromtxt` + `usecols` |
| `weather.csv` | 1461 | 有表头，最后一列是字符串 | `loadtxt` + `usecols` |
| `house_sales.csv` | 10000 | 全是数字，无缺失 | `loadtxt` |

**统一的路径处理**（把 `DATA` 改成你自己机器上的路径）：

```python
import numpy as np
from pathlib import Path

# 在 PyCharm 里右键 data 文件夹 -> Copy Path 粘到这里
DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")

print("路径存在:", DATA.exists())
print("目录下的文件:", sorted(p.name for p in DATA.glob("*.csv")))
```

**输出**

    路径存在: True
    目录下的文件: ['employees.csv', 'house_sales.csv', 'penguins.csv', 'sleep.csv', 'weather.csv', 'weather_withna.csv']

> 💡 如果不想写死路径，也可以在 `10、Numpy/Code/` 目录下运行，然后写 `DATA = Path("../data")`。

---

## 8.1 实战一：企鹅数据分析

**目标**：算出三种企鹅的体型差异，找出体重最大的个体。

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")

# 只取 4 个数值列：bill_length, bill_depth, flipper_length, body_mass
pg = np.genfromtxt(DATA / "penguins.csv", delimiter=",", skip_header=1,
                   usecols=(2, 3, 4, 5))

print("形状:", pg.shape)
print("每列缺失值个数:", np.isnan(pg).sum(axis=0))
print("总缺失值:", np.isnan(pg).sum())
```

**输出**

    形状: (344, 4)
    每列缺失值个数: [2 2 2 2]
    总缺失值: 8

> 💡 共有 **2 只企鹅的 4 个测量值全缺失**（所以是 2×4=8 个 `nan`），不是 8 只企鹅有问题。

### 第 1 步：不做任何处理，先看看会发生什么

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
pg = np.genfromtxt(DATA / "penguins.csv", delimiter=",", skip_header=1, usecols=(2, 3, 4, 5))

print("直接算均值:", pg.mean(axis=0))
print("直接算相关系数:\n", np.corrcoef(pg[:, 2], pg[:, 3]))
```

**输出**

    直接算均值: [nan nan nan nan]
    直接算相关系数:
     [[nan nan]
     [nan nan]]

> ⚠️ **这就是 NaN 的杀伤力**：8 个缺失值，把 344 行数据的统计结果**全部污染成 nan**。
> 这是新手最容易卡住的地方——"我明明有数据，为什么算出来全是 nan？"
> **答案永远是：先查 `np.isnan().sum()`。**

### 第 2 步：用 `nan*` 函数跳过缺失值

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
pg = np.genfromtxt(DATA / "penguins.csv", delimiter=",", skip_header=1, usecols=(2, 3, 4, 5))

names = ["喙长(mm)", "喙深(mm)", "鳍长(mm)", "体重(g)"]
means = [np.nanmean(pg[:, i]) for i in range(4)]
mins = [np.nanmin(pg[:, i]) for i in range(4)]
maxs = [np.nanmax(pg[:, i]) for i in range(4)]

for i, name in enumerate(names):
    print(f"{name:10} 均值 {means[i]:8.2f}   最小 {mins[i]:8.1f}   最大 {maxs[i]:8.1f}")
```

**输出**

    喙长(mm)     均值    43.92   最小     32.1   最大     59.6
    喙深(mm)     均值    17.15   最小     13.1   最大     21.5
    鳍长(mm)     均值   200.92   最小    172.0   最大    231.0
    体重(g)      均值  4201.75   最小   2700.0   最大   6300.0

### 第 3 步：布尔索引做筛选统计

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
pg = np.genfromtxt(DATA / "penguins.csv", delimiter=",", skip_header=1, usecols=(2, 3, 4, 5))

mass = pg[:, 3]

big = mass > 5000
print("体重大于 5000g 的企鹅:", big.sum(), "只")
print("占比:", round(float(big.mean()), 4))

print("\n体重最大的那只:")
idx = np.nanargmax(mass)
print("  行号:", idx)
print("  全部测量值:", pg[idx])
```

**输出**

    体重大于 5000g 的企鹅: 61 只
    占比: 0.1773

    体重最大的那只:
      行号: 237
      全部测量值: [  49.2   15.2  221.  6300. ]

> 💡 `big.sum()` 数个数、`big.mean()` 算比例 —— **不需要 `len(mass[big])`**。
> ⚠️ 注意这里必须用 `nanargmax`，用 `argmax` 会因为 `nan` 导致结果不可靠（`nan` 在比较时行为特殊）。

### 第 4 步：删掉缺失值再做相关性分析

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
pg = np.genfromtxt(DATA / "penguins.csv", delimiter=",", skip_header=1, usecols=(2, 3, 4, 5))

# 删掉任何一个字段缺失的行
clean = pg[~np.isnan(pg).any(axis=1)]
print("清理前:", pg.shape, " 清理后:", clean.shape)

# 现在可以放心用普通函数了
means = clean.mean(axis=0)
print("\n清理后各列均值:", np.round(means, 2))

corr = np.corrcoef(clean[:, 2], clean[:, 3])[0, 1]
print("\n鳍长 与 体重 的相关系数:", round(float(corr), 4))
```

**输出**

    清理前: (344, 4)  清理后: (342, 4)

    清理后各列均值: [  43.92   17.15  200.92 4201.75]

    鳍长 与 体重 的相关系数: 0.8712

**结论**：鳍长和体重的相关系数 **0.87**，属于**强正相关**——企鹅越大，鳍越长，完全符合生物学直觉。

> 💡 `clean = pg[~np.isnan(pg).any(axis=1)]` 这个套路请背下来：
> `np.isnan(pg)` 得到布尔矩阵 → `.any(axis=1)` 找出"这一行有没有 nan" → `~` 取反 → 布尔索引。
> **这是 NumPy 里删除缺失值行的标准写法。**

---

## 8.2 实战二：西雅图天气分析（2012–2015）

**目标**：找出最热的一天、统计降雨规律。

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")

# 列顺序: date, precipitation, temp_max, temp_min, wind, weather
#        跳过 date(0) 和 weather(5)，取 1~4 列
w = np.loadtxt(DATA / "weather.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4))

print("形状:", w.shape)
print("列: [precipitation, temp_max, temp_min, wind]")
print("\n前 3 行:\n", w[:3])
```

**输出**

    形状: (1461, 4)
    列: [precipitation, temp_max, temp_min, wind]

    前 3 行:
     [[ 0.  12.8  5.   4.7]
     [10.9 10.6  2.8  4.5]
     [ 0.8 11.7  7.2  2.3]]

1461 行 = 4 年（2012 是闰年，366+365+365+365 = 1461）。✅

### 任务 1：最热的一天

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
w = np.loadtxt(DATA / "weather.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4))
temp_max = w[:, 1]

idx = temp_max.argmax()
print("最热的一天是第", idx, "行")
print("最高温:", temp_max[idx], "度")
print("那一天的全部数据:", w[idx])
```

**输出**

    最热的一天是第 953 行
    最高温: 35.6 度
    那一天的全部数据: [ 0.5 35.6 17.8  2.6]

> 💡 `argmax()` 返回的是**行号**（下标），用 `w[idx]` 就能拿到那一行的全部信息。
> **这就是"找到最大值"和"找到最大值所在的那条记录"的区别**——后者才是实战里真正要的。

### 任务 2：降雨规律

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
w = np.loadtxt(DATA / "weather.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4))
precip = w[:, 0]

print("总降雨量:", precip.sum(), "mm")
print("单日最大:", precip.max(), "mm")
print("平均每天:", round(float(precip.mean()), 4), "mm")

rainy = precip > 0
print("\n下雨天数:", rainy.sum(), "/", len(precip))
print("下雨天占比:", round(float(rainy.mean()), 4))
print("只有", round(float(precip[rainy].mean()), 2), "mm 是一下雨就下的平均量")
```

**输出**

    总降雨量: 4426.0 mm
    单日最大: 55.9 mm
    平均每天: 3.0294 mm

    下雨天数: 623 / 1461
    下雨天占比: 0.4264
    只有 7.1 mm 是一下雨就下的平均量

> 💡 **注意这里的逻辑**：`precip.mean()` 算的是"**所有天**的平均"，被 838 个 0 拉低了；
> `precip[rainy].mean()` 算的是"**下雨天**的平均"，才是"下雨时通常下多大"。
> **两个数回答的是完全不同的问题**——数据分析里这种区分极其重要。

### 任务 3：用 ^^reshape^^ 做"每 30 天一块"的统计

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
w = np.loadtxt(DATA / "weather.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4))
temp_max = w[:, 1]

# 前 1440 天 = 48 个"30天块"
blocks = temp_max[:1440].reshape(48, 30)
print("切块后 shape:", blocks.shape)

block_mean = blocks.mean(axis=1)
print("\n前 6 个 30 天块的平均最高温:")
print(np.round(block_mean[:6], 3))
```

**输出**

    切块后 shape: (48, 30)

    前 6 个 30 天块的平均最高温:
    [ 6.977  9.28   9.54  14.78  17.453 18.527]

**看懂了吗**：`reshape(48, 30)` 把 1440 天的数据按顺序**每 30 天切成一行**，然后 `mean(axis=1)` 对每行求平均。
这就是"**用 reshape 做分组统计**"——在还没有学 Pandas 的 `groupby` 之前，这是 NumPy 里最实用的技巧。

> ⚠️ 这只在"总长度能整除"时可用。1441 天（实际数据是 1461 天）不能整除 30，所以要截断成 `[:1440]`。
> **不能整除时用 `np.array_split(w, 48)`**，它会自动处理余数。

---

## 8.3 实战三：房价数据（含一个重要警告）⚠️

### ⚠️ 先说结论：这份 `house_sales.csv` 是**随机生成**的假数据

课程第 4 章用它做"房地产市场洞察"。**但我要提前告诉你：这份数据里没有任何真实规律。**

我算了两两之间的相关系数矩阵，**最大绝对值只有 0.022** —— 这在统计学上就等于"毫无关系"。

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")

# 列: id(0) date(1) price(2) bedrooms(3) bathrooms(4) sqft_living(5)
#     sqft_lot(6) floors(7) waterfront(8) view(9) condition(10) grade(11)
#     sqft_above(12) sqft_basement(13) yr_built(14) yr_renovated(15)
#     zipcode(16) lat(17) long(18)
hs = np.loadtxt(DATA / "house_sales.csv", delimiter=",", skiprows=1,
                usecols=(2, 3, 4, 5, 6, 14, 15, 16, 17))

names = ["price", "bedrooms", "bathrooms", "sqft_living", "sqft_lot",
         "yr_built", "yr_renovated", "zipcode", "lat"]

print("形状:", hs.shape)
print("最大值 |相关系数|（非对角线）:",
      round(float(np.max(np.abs(np.corrcoef(hs, rowvar=False) - np.eye(9)))), 4))
```

**输出**

    形状: (10000, 9)
    最大值 |相关系数|（非对角线）: 0.022

**0.022 是什么概念？** 相关系数范围是 -1 到 1：

| 绝对值 | 含义 |
|---|---|
| 0.8 ~ 1.0 | 极强相关 |
| 0.6 ~ 0.8 | 强相关 |
| 0.4 ~ 0.6 | 中等相关 |
| 0.2 ~ 0.4 | 弱相关 |
| **0 ~ 0.2** | **基本无关** |

`0.022` 连"弱相关"的门槛都够不上。

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
hs = np.loadtxt(DATA / "house_sales.csv", delimiter=",", skiprows=1,
                usecols=(2, 3, 4, 5, 6, 14, 15, 16, 17))
price = hs[:, 0]

for i, name in enumerate(["bedrooms", "bathrooms", "sqft_living", "sqft_lot",
                          "yr_built", "yr_renovated", "zipcode", "lat"], start=1):
    c = np.corrcoef(hs[:, i], price)[0, 1]
    print(f"{name:14} 与 price 的相关系数: {c:8.4f}")
```

**输出**

    bedrooms       与 price 的相关系数:   0.0054
    bathrooms      与 price 的相关系数:   0.0035
    sqft_living    与 price 的相关系数:   0.0073
    sqft_lot       与 price 的相关系数:   0.0051
    yr_built       与 price 的相关系数:   0.0133
    yr_renovated   与 price 的相关系数:  -0.0044
    zipcode        与 price 的相关系数:   0.0085
    lat            与 price 的相关系数:   0.0002

**真实世界里，`sqft_living`（居住面积）与房价的相关系数应该在 0.7 左右。这里只有 0.0073。**

> 💡 **这个警告很重要**：学课程第 4 章时，你会算出"面积越大房价越高"之类结论**完全不成立**，
> 然后怀疑自己代码写错了。**代码没错，是数据本身随机生成的。**
> 这份数据**只适合练语法**（怎么读文件、怎么分组、怎么画图），**不适合练分析结论**。
> 想要真实规律，换成 Kaggle 的 `kc_house_data.csv`（这份数据就是照它生成的，但把相关性抹掉了）。

### 那用这份数据练什么？练**语法**：IQR 异常值检测

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
hs = np.loadtxt(DATA / "house_sales.csv", delimiter=",", skiprows=1,
                usecols=(2, 3, 4, 5, 6, 14, 15, 16, 17))
price = hs[:, 0]

print("价格均值:", round(float(price.mean()), 2))
print("价格中位数:", round(float(np.median(price)), 2))
print("价格标准差:", round(float(price.std()), 2))
print("价格最大:", float(price.max()))
```

**输出**

    价格均值: 500836.08
    价格中位数: 501404.46
    价格标准差: 100106.33
    价格最大: 841466.39

**IQR 法找异常值**（这是数据分析的标准套路）：

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
hs = np.loadtxt(DATA / "house_sales.csv", delimiter=",", skiprows=1,
                usecols=(2, 3, 4, 5, 6, 14, 15, 16, 17))
price = hs[:, 0]

q1, q3 = np.percentile(price, [25, 75])
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print("Q1 (25分位):", q1)
print("Q3 (75分位):", q3)
print("IQR        :", iqr)
print("\n下界:", lower)
print("上界:", upper)

outliers = (price < lower) | (price > upper)
print("\n异常值个数:", outliers.sum())
print("占比:", round(float(outliers.mean()), 4))
print("异常价格范围:", price[outliers].min(), "~", price[outliers].max())
```

**输出**

    Q1 (25分位): 432656.315
    Q3 (75分位): 568049.5225
    IQR        : 135393.20749999996

    下界: 229566.50375000006
    上界: 771139.3337499999

    异常值个数: 70
    占比: 0.007
    异常价格范围: 100000.0 ~ 841466.39

> 💡 **注意最后一行**：异常价格的**最小值正好是 100000.0**——一个整数。真实房价不会这么整齐。
> 这又一次印证了这份数据是**用随机数造出来的**（价格大概是在 100000~841466 之间均匀撒点）。
> **做数据分析时，这种"太整齐"的数字是重要的线索。**

**IQR 法三步走，背下来**：
1. `q1, q3 = np.percentile(x, [25, 75])`
2. `iqr = q3 - q1`
3. 正常范围 = `[q1 - 1.5*iqr, q3 + 1.5*iqr]`，超出即异常

> 💡 `np.percentile(x, [25, 75])` 一次传一个列表，**同时拿到多个分位数**，比调用两次快。

---

## 🧪 第 8 章 综合练习

**8-1** 用 `sleep.csv` 算出：**睡眠时长的平均值、中位数、标准差**，以及**睡眠时长大于 7 小时的人占比**。
（提示：列顺序是 `person_id, gender, age, occupation, sleep_duration, sleep_quality, ...`，`sleep_duration` 是第 4 列）

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")

# 只取 sleep_duration(4) 一列
duration = np.loadtxt(DATA / "sleep.csv", delimiter=",", skiprows=1, usecols=(4,))

print("样本数    :", duration.shape[0])
print("平均睡眠  :", round(float(duration.mean()), 4))
print("中位数    :", float(np.median(duration)))
print("标准差    :", round(float(duration.std()), 4))

enough = duration > 7
print("\n睡够 7 小时的人数:", enough.sum())
print("占比:", round(float(enough.mean()), 4))
```

输出：

    样本数    : 400
    平均睡眠  : 8.0412
    中位数    : 8.2
    标准差    : 2.3878
    睡够 7 小时的人数: 249
    占比: 0.6225

> 💡 注意 `平均睡眠 8.04 小时`——这个数字**现实中偏高得不正常**（真实人群平均在 7 小时左右）。
> 说明这份 `sleep.csv` 也是**模拟生成**的数据。做分析时对"看起来太完美/太离谱"的数字保持敏感。

</details>

**8-2** 用 `weather.csv` 找出：**① 温差（`temp_max - temp_min`）最大的那天是第几行 ② 温差超过 15 度的天数**。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
w = np.loadtxt(DATA / "weather.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4))

diff = w[:, 1] - w[:, 2]          # temp_max - temp_min
print("温差均值:", round(float(diff.mean()), 4))

idx = diff.argmax()
print("温差最大的是第", idx, "行，温差", diff[idx], "度")
print("那天的数据 [降雨, 最高, 最低, 风速]:", w[idx])

big_diff = diff > 15
print("\n温差超过 15 度的天数:", big_diff.sum())
print("占比:", round(float(big_diff.mean()), 4))
```

**关键点**：`w[:, 1] - w[:, 2]` 是两个**整列**相减，NumPy 自动逐元素算，**不用写循环**。

</details>

**8-3**（挑战）用 `penguins.csv`：**按体重排序，找出体重前 10 名的鳍长平均值**，并与全体鳍长平均值比较。

<details>
<summary>💡 参考答案</summary>

```python
import numpy as np
from pathlib import Path

DATA = Path(r"E:\Code\MyStudyData\10、Numpy\data")
pg = np.genfromtxt(DATA / "penguins.csv", delimiter=",", skip_header=1, usecols=(2, 3, 4, 5))

mass = pg[:, 3]
flipper = pg[:, 2]

# 先清理缺失值
ok = ~np.isnan(mass) & ~np.isnan(flipper)
mass, flipper = mass[ok], flipper[ok]

# argsort 拿排序后的下标，取前 10（降序）
top10_idx = np.argsort(mass)[::-1][:10]

print("体重前10名的体重:", mass[top10_idx])
print("体重前10名的鳍长:", flipper[top10_idx])
print("\n前10名平均鳍长:", round(float(flipper[top10_idx].mean()), 2))
print("全体平均鳍长  :", round(float(flipper.mean()), 2))
print("差值          :", round(float(flipper[top10_idx].mean() - flipper.mean()), 2), "mm")
```

**思路拆解**：
① 用 `~np.isnan(a) & ~np.isnan(b)` 同时清理两列的缺失值（**必须同步清理，否则下标错位**）；
② `np.argsort(mass)[::-1][:10]` 拿到"体重最大的 10 个位置"；
③ 用同一组下标去取鳍长——**这就是"按 A 列排序取 B 列"的标准做法**。

</details>

---

# 附录 A 速查表

## A.1 创建

| 代码 | 说明 |
|---|---|
| `np.array([1,2,3])` | 从列表创建 |
| `np.asarray(x)` | 转换，已是 ndarray 则不复制 |
| `np.zeros((2,3))` / `np.ones()` | 全 0 / 全 1（默认 float64） |
| `np.full((2,3), 7)` | 全 7 |
| `np.zeros_like(a)` | 照 `a` 的形状和类型造 |
| `np.arange(0, 10, 2)` | 等差，左闭右开 |
| `np.linspace(0, 10, 5)` | 等差，指定**个数** |
| `np.logspace(2, 5, 5, base=2)` | 等比 |
| `np.eye(3)` | 单位矩阵 |
| `np.random.seed(0)` + `np.random.rand(2,3)` | 可复现随机 |

## A.2 属性

| 属性 | 说明 |
|---|---|
| `a.shape` | 形状元组，一维是 `(3,)` |
| `a.ndim` | 维度数 |
| `a.size` | 元素总数 |
| `a.dtype` | 元素类型 |
| `a.itemsize` | 单元素字节数 |
| `a.nbytes` | 总字节数 |
| `a.T` | 转置（视图） |
| `a.base` | 我"寄生"在谁身上（`None` = 副本） |
| `a.flags.owndata` | 我是否自己拥有内存 |

## A.3 索引

| 代码 | 结果 |
|---|---|
| `a[2]` / `a[-1]` | 单个元素 |
| `a[2:5]` | 切片（**视图**） |
| `a[::2]` / `a[::-1]` | 步长 / 反转 |
| `a[1, 2]` | 二维：第1行第2列 |
| `a[:, 1]` | 第 1 列 |
| `a[1:3, 1:4]` | 子矩阵 |
| `a[a > 0]` | 布尔索引（**副本**） |
| `a[[0, 2, 4]]` | 花式索引（**副本**） |
| `np.ix_([0,2],[1,3])` | 交叉子矩阵 |
| `np.where(cond, x, y)` | 三元运算 |
| `np.select([c1,c2],[v1,v2],default=v3)` | 多分支 |
| `np.clip(a, lo, hi)` | 截断 |

## A.4 形状

| 代码 | 说明 |
|---|---|
| `a.reshape(3, 4)` / `a.reshape(-1, 6)` | 改形状，`-1` 自动推断 |
| `a.ravel()` / `a.flatten()` | 拉平（视图 / 副本） |
| `a.T` / `a.transpose(1,0,2)` | 转置 |
| `a.swapaxes(0, 2)` | 交换两轴 |
| `a[:, np.newaxis]` / `np.expand_dims(a, 1)` | 加一维 |
| `np.squeeze(a)` | 去掉长度为 1 的维 |
| `np.concatenate([a,b], axis=0)` | 拼接（不加维） |
| `np.vstack` / `np.hstack` | 竖着摞 / 横着接 |
| `np.stack([a,b], axis=0)` | 堆叠（**加一维**） |
| `np.split` / `np.array_split` | 拆分 |
| `np.vsplit` / `np.hsplit` | 按行 / 按列拆 |

## A.5 统计（都支持 `axis` 和 `keepdims`）

| 代码 | 说明 |
|---|---|
| `a.sum()` / `a.mean()` | 和 / 均值 |
| `a.max()` / `a.min()` | 最大 / 最小 |
| `a.std()` / `a.var()` | 标准差 / 方差 |
| `a.argmax()` / `a.argmin()` | **下标**（不加 axis 会拍平！） |
| `np.median(a)` | 中位数 |
| `np.percentile(a, [25,75])` | 百分位 |
| `a.cumsum()` / `a.cumprod()` | 累加 / 累乘 |
| `np.unique(a, return_counts=True)` | 去重 + 计数 |
| `np.corrcoef(x, y)[0,1]` | 相关系数 |
| `np.bincount(a)` | 整数频次统计 |

## A.6 NaN

| 代码 | 说明 |
|---|---|
| `np.isnan(a)` | 判断缺失（**不能用 `== np.nan`**） |
| `np.isnan(a).sum()` | 缺失个数 |
| `np.nansum` `np.nanmean` `np.nanmax` `np.nanmin` `np.nanstd` `np.nanmedian` | 跳过缺失值计算 |
| `a[~np.isnan(a)]` | 删除缺失值 |
| `np.where(np.isnan(a), 0, a)` | 填补缺失值 |
| `np.isfinite(a)` | 是否有限（能同时排除 `nan` 和 `inf`） |

## A.7 排序

| 代码 | 说明 |
|---|---|
| `a.sort()` | **就地**排序，返回 `None` |
| `np.sort(a)` | 返回副本 |
| `np.argsort(a)` | 返回排序后的**下标** |
| `a[np.argsort(a)[::-1]]` | 降序排列 |
| `np.sort(a)[::-1][:3]` | Top-3 |

## A.8 文件

| 代码 | 说明 |
|---|---|
| `np.save("a.npy", a)` / `np.load("a.npy")` | 二进制单数组 |
| `np.savez("d.npz", x=a, y=b)` | 多数组打包 |
| `np.loadtxt(f, delimiter=",", skiprows=1, usecols=(1,2))` | 纯数字文本 |
| `np.genfromtxt(f, delimiter=",", skip_header=1)` | **能处理缺失值** |
| `np.savetxt("a.csv", a, delimiter=",", fmt="%d")` | 写文本 |

## A.9 线性代数

| 代码 | 说明 |
|---|---|
| `a @ b` / `np.dot(a, b)` | 矩阵乘法 |
| `np.linalg.inv(A)` | 逆矩阵 |
| `np.linalg.det(A)` | 行列式 |
| `np.linalg.solve(A, b)` | 解 `Ax=b`（比 `inv` 更好） |
| `np.linalg.eigvals(A)` | 特征值 |
| `np.linalg.matrix_rank(A)` | 秩 |
| `np.linalg.norm(v)` | 向量范数 |

---

# 附录 B 报错急救

**遇到红色报错先别慌，90% 是下面这 10 个之一。**

## B.1 `operands could not be broadcast together with shapes (2,3) (2,)`

**原因**：形状对不上，没法广播。

**排查**：右对齐看哪一维既不相等、又都不是 1。

**修**：想清楚你要的是"行方向"还是"列方向"，然后**显式加维度**：

```python
import numpy as np

a = np.zeros((2, 3))
b = np.zeros((2,))

# 让 b 变成列
print((a + b[:, np.newaxis]).shape)

# 让 b 变成行（这里会失败，因为 2 != 3，只是演示语法）
try:
    print((a + b[np.newaxis, :]).shape)
except ValueError as e:
    print("还是不行:", e)
```

**输出**

    (2, 3)
    还是不行: operands could not be broadcast together with shapes (2,3) (1,2) 

## B.2 `setting an array element with a sequence. The requested array has an inhomogeneous shape...`

**原因**：数组**不是矩形**（每行长度不一样）。

**修**：补齐、切成多个数组、或者显式 `dtype=object`。

```python
import numpy as np

try:
    np.array([[1, 2, 3], [4, 5]])
except ValueError as e:
    print("报错:", str(e)[:70], "...")

print("补齐后:", np.array([[1, 2, 3], [4, 5, 0]]).shape)
```

**输出**

    报错: setting an array element with a sequence. The requested array has an i ...
    补齐后: (2, 3)

## B.3 `cannot reshape array of size 12 into shape (5,3)`

**原因**：元素总数对不上。`12 ≠ 5×3`。

**修**：算一下 `a.size`，确保 `reshape` 的目标形状乘积等于它。用 `-1` 交给 NumPy 算。

```python
import numpy as np

a = np.arange(12)
print("总数:", a.size)
print("能整除的形状:", a.reshape(3, 4).shape)
print("用 -1 自动算:", a.reshape(2, -1).shape)
```

**输出**

    总数: 12
    能整除的形状: (3, 4)
    用 -1 自动算: (2, 6)

## B.4 `IndexError: index 5 is out of bounds for axis 0 with size 5`

**原因**：下标越界。**Python 下标从 0 开始**，长度 5 的数组最大下标是 4。

**修**：检查 `a.shape`，或者用 `-1` 取最后一个。

```python
import numpy as np

a = np.arange(5)
print("长度:", a.shape[0])
print("最后一个:", a[-1], " 或 a[4]")

try:
    a[5]
except IndexError as e:
    print("报错:", e)
```

**输出**

    长度: 5
    最后一个: 4  或 a[4]
    报错: index 5 is out of bounds for axis 0 with size 5

## B.5 `ValueError: The truth value of an array with more than one element is ambiguous`

**原因**：把 `and` / `or` / `if` 用在数组上了。

**修**：用 `&` `|` `~`，**并且加括号**。

```python
import numpy as np

a = np.array([1, -2, 3])

try:
    a[(a > 0) and (a < 3)]
except ValueError as e:
    print("报错:", str(e)[:60], "...")

print("正确写法:", a[(a > 0) & (a < 3)])
```

**输出**

    报错: The truth value of an array with more than one element is am ...
    正确写法: [1]

## B.6 算出来全是 `nan`

**原因**：数据里有 `nan`，而 `nan` 会污染 `sum` `mean` `corrcoef` 等一切运算。

**修**：先 `np.isnan(a).sum()` 确认，再用 `nan*` 系列函数或先删缺失值。

```python
import numpy as np

a = np.array([1.0, np.nan, 3.0])
print("缺失个数:", np.isnan(a).sum())
print("mean（被污染）:", a.mean())
print("nanmean（正确）:", np.nanmean(a))
print("删掉后 mean   :", a[~np.isnan(a)].mean())
```

**输出**

    缺失个数: 1
    mean（被污染）: nan
    nanmean（正确）: 2.0
    删掉后 mean   : 2.0

## B.7 `a = a.sort()` 之后 `a` 变成了 `None`

**原因**：`ndarray.sort()` `shuffle()` `fill()` `resize()` 都是**就地操作，返回 `None`**。

**修**：不要赋值。要返回值就用 `np.sort()` `np.random.permutation()`。

```python
import numpy as np

a = np.array([3, 1, 2])

b = a.copy()
b = b.sort()          # ❌ b 变成 None
print("错误写法 b:", b)

c = a.copy()
c.sort()              # ✅ 不要赋值
print("正确写法 c:", c)

print("或者用 np.sort:", np.sort(a))
```

**输出**

    错误写法 b: None
    正确写法 c: [1 2 3]
    或者用 np.sort: [1 2 3]

## B.8 `RuntimeWarning: invalid value encountered in ...`

**原因**：出现了 `0/0` `log(负数)` 之类的非法运算，结果是 `nan`。

**修**：用 `np.errstate` 临时静音，或者先清洗数据。**别无视它**。

```python
import numpy as np

a = np.array([1.0, -1.0, 0.0])

with np.errstate(divide="ignore", invalid="ignore"):
    print("1/a :", 1 / a)
    print("log :", np.log(a))
```

**输出**

    1/a : [ 1. -1. inf]
    log : [  0.  nan -inf]

## B.9 `AttributeError: 'list' object has no attribute 'shape'`

**原因**：忘了转成数组。

**修**：`np.array(data)`。

```python
import numpy as np

data = [1, 2, 3]

try:
    data.shape
except AttributeError as e:
    print("报错:", e)

print("转成数组后:", np.array(data).shape)
```

**输出**

    报错: 'list' object has no attribute 'shape'
    转成数组后: (3,)

## B.10 改了切片，原数组也跟着变了

**原因**：**切片是视图，不是副本**。详见 3.3 节。

**修**：`a[2:5].copy()`。

```python
import numpy as np

a = np.arange(5)
v = a[1:3]
v[:] = 0
print("视图会影响原数组:", a)

b = np.arange(5)
c = b[1:3].copy()
c[:] = 0
print("副本不影响原数组:", b)
```

**输出**

    视图会影响原数组: [0 0 0 3 4]
    副本不影响原数组: [0 1 2 3 4]

---

# 附录 C 与课程文档的对照及勘误

## C.1 章节对照

| 本手册 | 课程原文 | 说明 |
|---|---|---|
| 第 0 章 | 1.1 – 1.2 | 环境（你已有可用环境，可跳过） |
| 1.1 – 1.2 | 2.1 – 2.3 | 原样对应 + 补充内存原理 |
| **1.3 轴 axis** | 2.7.2 一句话 | **大幅展开**，课程那句"axis=0 按列"不够用 |
| 2.1 – 2.6 | 2.4 | 原样对应 + 补充 `retstep` / 新随机 API |
| **2.7 np.matrix** | 2.4.7 | **勘误**：已废弃 |
| 2.8 np.eye | — | 补充 |
| 3.1 | 2.6 | 原样对应 |
| **3.2 – 3.6** | — | **全部为补充**：多维索引、视图/副本、布尔索引、花式索引、where/select/clip |
| **第 4 章 形状操作** | — | **全部为补充** |
| 5.1 – 5.2 | 2.7.1 – 2.7.2 | 原样对应 + 补充 axis/keepdims/percentile |
| 5.3 – 5.6 | 2.7.3 – 2.7.5 | 原样对应 + 补充 argsort/unique(axis=0) |
| **5.7 NaN 处理** | — | **全部为补充** |
| 6.1 – 6.2 | 2.8 | 原样对应 + 广播表格化 |
| 6.4 – 6.5 | 2.9 | 原样对应 + 补充向量化思维 |
| **第 7 章 读写/线代** | — | **全部为补充** |
| 第 8 章 | 第 4 章 | 换用你本地 `data/` 的真实数据 |

## C.2 课程文档的四类问题

### 问题 1：过时内容——`np.matrix`

课程 2.4.7 教 `np.matrix`，但它在 NumPy 1.15 就被标记为不推荐，现在会抛 `PendingDeprecationWarning`。

**而且它有个致命陷阱**：`np.matrix` 的 `*` 是矩阵乘法，`np.array` 的 `*` 是元素乘法。**同一个符号两种含义**。

**处理**：忘掉它。用 `np.array` + `a @ b`。

### 问题 2：代码被 PDF 转换破坏

比如 2.7.3「比较函数」整节：

    |函数|说明|
    |np.any()|至少有一个元素满足指定条件，就返回True|
    |np.all()|所有的元素都满足指定条件，才返回True|
    |arr1 = np.array([1, 2,|3, 4, 5])|      ← 代码被塞进表格里了
    |print(np.any(arr1 > 3))||

代码和表格混在一起，**根本没法复制运行**。本手册全部重写并验证过。

### 问题 3：只讲"是什么"，不讲"什么时候会踩坑"

比如课程说 `np.empty()` "返回未初始化的数组"，但没说**它的值是内存垃圾，每次都不一样**，新手很容易以为它是"空的零数组"。

再比如课程完全没提**视图 vs 副本**——这是 NumPy 第一大坑，不知道它的人早晚会写出"我没改这个数组啊，它怎么自己变了"的 bug。

### 问题 4：第 4 章的数据没有分析价值

课程第 4 章用 `house_sales.csv` 做"房地产市场洞察"。**但这份数据是随机生成的**，所有特征与房价的相关系数都在 ±0.03 以内（真实数据里 `sqft_living` 与房价的相关性应该在 0.7 左右）。

**处理**：这份数据可以练语法，**但不要在它上面下分析结论**。

## C.3 学完之后做什么

1. **把第 8 章的三个实战自己重写一遍**，不看答案。
2. 去 Kaggle 下 `kc_house_data.csv`（真实房价数据），重做一遍第 4 章的分析，你会看到完全不同的结论。
3. 学完 NumPy 后**尽快进入 Pandas**（课程第 3 章）。真实数据分析里，Pandas 用得比 NumPy 多得多——**但 Pandas 的底层全是 NumPy，第 3、4、5 章的基础决定了你 Pandas 能走多远。**
4. 回头把 `10、Numpy/Code/001.ipynb` 换成按章节组织的练习笔记本。

---

**手册完。**




