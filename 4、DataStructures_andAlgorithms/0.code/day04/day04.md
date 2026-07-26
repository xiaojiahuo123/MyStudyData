# Day04 - 排序算法

***

## 1. 冒泡排序（Bubble Sort）

### 概念

- **核心思想**：重复遍历数组，比较相邻元素，如果顺序错误就交换
- **特点**：每一轮将最大的元素"冒泡"到数组末尾
- **时间复杂度**：O(n²)
- **空间复杂度**：O(1)
- **稳定性**：稳定

### 代码实现

```python
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
```

### 算法原理

#### 外层循环

```python
for i in range(len(nums) - 1):
```

- 控制排序轮数，共需 `n-1` 轮
- 每轮确定一个元素的最终位置

#### 内层循环

```python
for j in range(len(nums) - 1 - i):
```

- 控制每轮比较次数
- 每轮结束后，末尾的 `i` 个元素已排好序，无需再比较
- 所以范围是 `len(nums) - 1 - i`

### 执行过程图解

```
原始数组：[3, 1, 5, 4, 2]

第1轮（i=0）：将最大值5冒泡到末尾
  比较 3,1 → 交换 → [1, 3, 5, 4, 2]
  比较 3,5 → 不换 → [1, 3, 5, 4, 2]
  比较 5,4 → 交换 → [1, 3, 4, 5, 2]
  比较 5,2 → 交换 → [1, 3, 4, 2, 5]  ← 5就位

第2轮（i=1）：将次大值4冒泡到倒数第二位
  比较 1,3 → 不换 → [1, 3, 4, 2, 5]
  比较 3,4 → 不换 → [1, 3, 4, 2, 5]
  比较 4,2 → 交换 → [1, 3, 2, 4, 5]  ← 4就位

第3轮（i=2）：将2冒泡到正确位置
  比较 1,3 → 不换 → [1, 3, 2, 4, 5]
  比较 3,2 → 交换 → [1, 2, 3, 4, 5]  ← 3就位

第4轮（i=3）：只剩1和2，已有序
  比较 1,2 → 不换 → [1, 2, 3, 4, 5]

结果：[1, 2, 3, 4, 5]
```

### 关键点总结

| 概念 | 说明 |
|------|------|
| **外层循环** | `range(len(nums) - 1)`：n-1轮 |
| **内层循环** | `range(len(nums) - 1 - i)`：每轮少比较一个 |
| **比较条件** | `nums[j] > nums[j + 1]`：相邻元素比较 |
| **交换操作** | 同时交换两个元素 |

***

## 2. 选择排序（Selection Sort）

### 概念

- **核心思想**：每轮从未排序部分选择最小元素，放到已排序部分的末尾
- **特点**：交换次数少，但比较次数多
- **时间复杂度**：O(n²)
- **空间复杂度**：O(1)
- **稳定性**：不稳定

### 代码实现

```python
def select_sort(nums):
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
```

### 算法原理

#### 外层循环

```python
for i in range(len(nums) - 1):
```

- 控制当前要填入最小值的位置
- 从索引0开始，到倒数第二个位置结束

#### 内层循环

```python
for j in range(i + 1, len(nums)):
```

- 从 `i+1` 开始遍历，寻找最小元素
- 与 `i` 位置及之后的元素比较

#### 交换操作

```python
nums[i], nums[min_index] = nums[min_index], nums[i]
```

- 将找到的最小元素与位置 `i` 的元素交换

### 执行过程图解

```
原始数组：[3, 1, 5, 4, 2]

第1轮（i=0）：找最小值，放到位置0
  遍历 [3, 1, 5, 4, 2]，最小值是1（索引1）
  交换 3 和 1 → [1, 3, 5, 4, 2]

第2轮（i=1）：找剩余最小值，放到位置1
  遍历 [3, 5, 4, 2]，最小值是2（索引4）
  交换 3 和 2 → [1, 2, 5, 4, 3]

第3轮（i=2）：找剩余最小值，放到位置2
  遍历 [5, 4, 3]，最小值是3（索引4）
  交换 5 和 3 → [1, 2, 3, 4, 5]

第4轮（i=3）：找剩余最小值，放到位置3
  遍历 [4, 5]，最小值是4（索引3）
  交换 4 和 4 → [1, 2, 3, 4, 5]

结果：[1, 2, 3, 4, 5]
```

### 关键点总结

| 概念 | 说明 |
|------|------|
| **外层循环** | `range(len(nums) - 1)`：n-1轮 |
| **内层循环** | `range(i + 1, len(nums))`：从i+1开始找最小值 |
| **最小值索引** | `min_index` 记录当前最小值位置 |
| **交换次数** | 最多n-1次，比冒泡少 |

***

## 3. 插入排序（Insertion Sort）

### 概念

- **核心思想**：将未排序元素插入到已排序部分的正确位置
- **特点**：类似整理扑克牌，逐张插入
- **时间复杂度**：O(n²)，最好O(n)
- **空间复杂度**：O(1)
- **稳定性**：稳定

### 代码实现

```python
def insert_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] >= nums[j - 1]:
                break
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
```

### 算法原理

#### 外层循环

```python
for i in range(1, len(nums)):
```

- 从索引1开始，将每个元素视为待插入元素
- `i` 左侧是已排序部分，右侧是未排序部分

#### 内层循环

```python
for j in range(i, 0, -1):
```

- 从 `i` 开始向前遍历
- 将当前元素与前面的元素比较，找到正确位置

#### 交换条件

```python
if nums[j] >= nums[j - 1]:
    break
```

- 如果当前元素大于等于前一个元素，说明已找到正确位置
- 否则交换，继续向前比较

### 执行过程图解

```
原始数组：[3, 1, 5, 4, 2]

第1轮（i=1）：插入1
  比较 1,3 → 1<3，交换 → [1, 3, 5, 4, 2]

第2轮（i=2）：插入5
  比较 5,3 → 5>3，停止 → [1, 3, 5, 4, 2]

第3轮（i=3）：插入4
  比较 4,5 → 4<5，交换 → [1, 3, 4, 5, 2]
  比较 4,3 → 4>3，停止 → [1, 3, 4, 5, 2]

第4轮（i=4）：插入2
  比较 2,5 → 2<5，交换 → [1, 3, 4, 2, 5]
  比较 2,4 → 2<4，交换 → [1, 3, 2, 4, 5]
  比较 2,3 → 2<3，交换 → [1, 2, 3, 4, 5]
  比较 2,1 → 2>1，停止 → [1, 2, 3, 4, 5]

结果：[1, 2, 3, 4, 5]
```

### 关键点总结

| 概念 | 说明 |
|------|------|
| **外层循环** | `range(1, len(nums))`：从1开始 |
| **内层循环** | `range(i, 0, -1)`：从i向前遍历 |
| **停止条件** | `nums[j] >= nums[j-1]`：找到正确位置 |
| **最佳情况** | 数组已有序，只需O(n)比较 |

***

## 4. 归并排序（Merge Sort）

### 概念

- **核心思想**：分治法，将数组拆分为子数组，分别排序后合并
- **特点**：稳定的O(n log n)排序算法
- **时间复杂度**：O(n log n)
- **空间复杂度**：O(n)
- **稳定性**：稳定

### 代码实现

```python
def merge(left, right):
    """合并两个已排序的数组"""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(arr):
    """归并排序"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

### 算法原理

#### 分割阶段

```python
mid = len(arr) // 2
left = merge_sort(arr[:mid])
right = merge_sort(arr[mid:])
```

- 递归地将数组对半分割
- 直到子数组长度为1（基本情况）

#### 合并阶段

```python
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
```

- 比较两个子数组的元素
- 按顺序放入新数组
- 处理剩余元素

### 执行过程图解

```
原始数组：[3, 1, 4, 2]

分割阶段：
[3, 1, 4, 2]
    /    \
[3, 1]  [4, 2]
  / \     / \
[3] [1] [4] [2]

合并阶段：
[3] [1] → [1, 3]
[4] [2] → [2, 4]
[1, 3] [2, 4] → [1, 2, 3, 4]

结果：[1, 2, 3, 4]
```

### 关键点总结

| 概念 | 说明 |
|------|------|
| **分割** | `arr[:mid]` 和 `arr[mid:]` 对半分 |
| **基本情况** | `len(arr) <= 1` 时返回 |
| **合并** | 双指针比较，按序放入新数组 |
| **空间** | 需要O(n)额外空间存储合并结果 |

***

## 5. 快速排序（Quick Sort）

### 概念

- **核心思想**：选择基准元素，将数组分为小于和大于基准的两部分，递归排序
- **特点**：平均性能最好，但最坏情况O(n²)
- **时间复杂度**：平均O(n log n)，最坏O(n²)
- **空间复杂度**：O(log n)
- **稳定性**：不稳定

### 代码实现

```python
def partition(nums, left, right):
    """选择基准并按基准划分"""
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left

def quick_sort(nums, left, right):
    """快速排序"""
    if left < right:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid + 1, right)
```

### 算法原理

#### partition函数

```python
def partition(nums, left, right):
    pivot = nums[left]  # 选择最左元素作为基准
    while left < right:
        # 右指针左移，找小于基准的元素
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        # 左指针右移，找大于基准的元素
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot  # 基准放到正确位置
    return left
```

#### 递归排序

```python
def quick_sort(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)  # 左半部分
        quick_sort(nums, mid + 1, right) # 右半部分
```

### 执行过程图解

```
原始数组：[3, 1, 5, 4, 2]

第1次partition：pivot=3
  right左移找<3的元素：2
  left右移找>3的元素：5
  交换后：[2, 1, 3, 4, 5]
  基准3就位，返回索引2

递归左半部分：[2, 1]
  pivot=2
  right左移找<2的元素：1
  left右移找>2的元素：无
  交换后：[1, 2]
  基准2就位

递归右半部分：[4, 5]
  pivot=4
  right左移找<4的元素：无
  left右移找>4的元素：5
  交换后：[4, 5]
  基准4就位

结果：[1, 2, 3, 4, 5]
```

### 关键点总结

| 概念 | 说明 |
|------|------|
| **基准选择** | 通常选最左或最右元素 |
| **双指针** | left和right从两端向中间扫描 |
| **原地排序** | 不需要额外数组空间 |
| **最坏情况** | 数组已有序，退化为O(n²) |

***

## 6. 堆排序（Heap Sort）

### 概念

- **核心思想**：利用堆数据结构，先建大顶堆，再依次取堆顶放到末尾
- **特点**：不稳定，但空间效率高
- **时间复杂度**：O(n log n)
- **空间复杂度**：O(1)
- **稳定性**：不稳定

### 代码实现

```python
def heapify(arr, n, i):
    """堆化：维护大顶堆性质"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """堆排序"""
    n = len(arr)
    # 构建大顶堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # 依次将堆顶元素放在末尾
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
```

### 算法原理

#### 堆化函数

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1      # 左子节点索引
    right = 2 * i + 2     # 右子节点索引
    # 找最大节点
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    # 如果最大节点不是父节点，交换并递归
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

#### 建堆

```python
for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)
```

- 从最后一个非叶子节点开始堆化
- 确保每个子树都满足大顶堆性质

#### 排序

```python
for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]  # 堆顶放到末尾
    heapify(arr, i, 0)               # 重新堆化
```

### 执行过程图解

```
原始数组：[3, 1, 5, 4, 2]

构建大顶堆：
        3              5
       / \            / \
      1   5    →     4   3
     / \            / \
    4   2          1   2

排序过程：
堆顶5与末尾2交换：[2, 4, 3, 1, 5]
堆化：[4, 2, 3, 1, 5]

堆顶4与末尾1交换：[1, 2, 3, 4, 5]
堆化：[3, 2, 1, 4, 5]

堆顶3与末尾1交换：[1, 2, 3, 4, 5]
堆化：[2, 1, 3, 4, 5]

堆顶2与末尾1交换：[1, 2, 3, 4, 5]

结果：[1, 2, 3, 4, 5]
```

### 关键点总结

| 概念 | 说明 |
|------|------|
| **堆性质** | 父节点大于子节点（大顶堆） |
| **索引计算** | 左子节点 `2i+1`，右子节点 `2i+2` |
| **建堆** | 从最后一个非叶子节点开始 |
| **排序** | 堆顶与末尾交换，重新堆化 |

***

## 7. 汉诺塔（Tower of Hanoi）

### 概念

- **核心思想**：递归将n个盘子从源柱子移动到目标柱子
- **规则**：每次只能移动一个盘子，大盘子不能放在小盘子上面
- **时间复杂度**：O(2ⁿ)
- **空间复杂度**：O(n)

### 代码实现

```python
def hanota(n, source, target, buffer):
    # 基本情况：只有一个盘子
    if n == 1:
        item = source.pop()
        target.append(item)
        return

    # 1. 将n-1个盘子从源移到缓冲
    hanota(n - 1, source, buffer, target)
    # 2. 将第n个盘子从源移到目标
    hanota(1, source, target, buffer)
    # 3. 将n-1个盘子从缓冲移到目标
    hanota(n - 1, buffer, target, source)
```

### 算法原理

#### 递归三步

```
1. 将 n-1 个盘子从 source 移到 buffer（借助 target）
2. 将第 n 个盘子从 source 移到 target
3. 将 n-1 个盘子从 buffer 移到 target（借助 source）
```

#### 基本情况

```python
if n == 1:
    item = source.pop()
    target.append(item)
    return
```

- 只有一个盘子时，直接移动

### 执行过程图解

```
初始状态：a=[3,2,1], b=[], c=[]

移动3个盘子的过程：

步骤1：将2个盘子从a移到b（借助c）
  - 将1个盘子从a移到c：a=[3,2], b=[], c=[1]
  - 将1个盘子从a移到b：a=[3], b=[2], c=[1]
  - 将1个盘子从c移到b：a=[3], b=[2,1], c=[]

步骤2：将第3个盘子从a移到c
  - a=[], b=[2,1], c=[3]

步骤3：将2个盘子从b移到c（借助a）
  - 将1个盘子从b移到a：a=[1], b=[2], c=[3]
  - 将1个盘子从b移到c：a=[1], b=[], c=[3,2]
  - 将1个盘子从a移到c：a=[], b=[], c=[3,2,1]

结果：所有盘子移到c柱
```

### 关键点总结

| 概念 | 说明 |
|------|------|
| **递归结构** | 三步：移动n-1、移动第n个、移动n-1 |
| **参数变化** | source、target、buffer 角色轮换 |
| **基本情况** | n=1时直接移动 |
| **复杂度** | 移动次数 = 2ⁿ - 1 |

***

## 总结：排序算法对比

| 算法 | 时间复杂度（平均） | 时间复杂度（最坏） | 空间复杂度 | 稳定性 | 特点 |
|------|-----------------|-----------------|-----------|--------|------|
| 冒泡排序 | O(n²) | O(n²) | O(1) | 稳定 | 简单，交换频繁 |
| 选择排序 | O(n²) | O(n²) | O(1) | 不稳定 | 交换次数少 |
| 插入排序 | O(n²) | O(n²) | O(1) | 稳定 | 适合小规模或基本有序 |
| 归并排序 | O(n log n) | O(n log n) | O(n) | 稳定 | 稳定的O(n log n) |
| 快速排序 | O(n log n) | O(n²) | O(log n) | 不稳定 | 平均性能最好 |
| 堆排序 | O(n log n) | O(n log n) | O(1) | 不稳定 | 空间效率高 |

***

*持续更新中...*
