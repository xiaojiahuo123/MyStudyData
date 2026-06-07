"""
Day04 练习2 - 列表深入
由浅入深掌握列表及其底层原理

参考源码: Objects/listobject.c  (列表的C实现)
         Objects/listsort.txt   (TimSort排序算法文档)
"""

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 列表创建 -----
# TODO: 用不同方式创建列表
# (1) 字面量创建: [1, 2, 3]
# (2) list() 构造: list("hello") -> ['h', 'e', 'l', 'l', 'o']
# (3) range() 转换: list(range(5)) -> [0, 1, 2, 3, 4]
# (4) 列表推导式: [i**2 for i in range(5)] -> [0, 1, 4, 9, 16]


# ----- 题2: 索引和切片 -----
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# TODO: 不运行代码，预测以下表达式的结果，然后验证
print(lst[0])        # ____
print(lst[-1])       # ____
print(lst[2:5])      # ____
print(lst[:3])       # ____
print(lst[7:])       # ____
print(lst[::2])      # ____
print(lst[::-1])     # ____
print(lst[8:2:-1])   # ____
print(lst[5:2])      # ____  注意: start > stop 且步长为正，返回空列表


# ----- 题3: 列表增删改 -----
nums = [10, 20, 30, 40, 50]
# TODO: 完成以下操作，每步打印结果
# 在索引2处插入 25
# 在末尾追加 60
# 删除值为 40 的元素
# 将索引0的元素改为 5
# 期望结果: [5, 20, 25, 30, 50, 60]


# ----- 题4: 列表遍历 -----
scores = [85, 92, 78, 96, 88]
# TODO: 用三种方式遍历:
# (1) 直接遍历元素
# (2) 用 range+下标 遍历
# (3) 用 enumerate 同时获取下标和元素


# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题5: 列表推导式 -----
# TODO: 用列表推导式完成以下任务

# (1) 生成 [1, 4, 9, 16, 25] (1-5的平方)

# (2) 从 [1,2,3,4,5,6,7,8,9,10] 中筛选偶数

# (3) 生成 1-20 中能被3整除但不能被5整除的数

# (4) 将 ["hello", "world", "python"] 转为 ["HELLO", "WORLD", "PYTHON"]

# (5) 生成一个 5x5 的单位矩阵 (对角线为1，其余为0)
# 提示: 嵌套列表推导式


# ----- 题6: 嵌套列表 -----
# 二维列表(矩阵)操作
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# TODO:
# (1) 打印矩阵 (每行一行)
# (2) 获取元素 5
# (3) 获取第二行 [4, 5, 6]
# (4) 获取第三列 [3, 6, 9]
# (5) 转置矩阵 (行变列，列变行)
# 期望: [[1,4,7], [2,5,8], [3,6,9]]


# ----- 题7: 列表排序 -----
import random
data = [random.randint(1, 100) for _ in range(10)]
print(f"原始数据: {data}")

# TODO:
# (1) sorted() 排序 (不修改原列表)
# (2) list.sort() 排序 (原地修改)
# (3) 降序排序
# (4) 自定义排序: 按绝对值排序 [-3, 1, -4, 1, 5, -9] -> [1, 1, -3, -4, 5, -9]


# ----- 题8: 列表方法对比 -----
lst = [1, 2, 3, 4, 5]
# 区分以下操作的返回值和副作用:
# lst.append(6)    # 返回 ___, lst 变为 ___
# lst.extend([7,8]) # 返回 ___, lst 变为 ___
# lst.insert(0, 0)  # 返回 ___, lst 变为 ___
# lst.pop()          # 返回 ___, lst 变为 ___
# lst.remove(3)      # 返回 ___, lst 变为 ___
# lst.clear()        # 返回 ___, lst 变为 ___

# 关键区别:
# append: 添加一个元素 (整体作为一个元素)
# extend: 逐个添加元素 (展开另一个列表)
# TODO: 验证 append 和 extend 的区别


# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题9: 列表的内存机制 -----
# 列表使用动态数组实现，当容量不足时会扩容
import sys

lst = []
prev_size = sys.getsizeof(lst)
for i in range(32):
    lst.append(i)
    curr_size = sys.getsizeof(lst)
    if curr_size != prev_size:
        print(f"添加元素 {i}: 容量变化 {prev_size} -> {curr_size} 字节")
        prev_size = curr_size

# 思考:
# 1. 列表扩容策略是什么？(大约是 1.125 倍)
# 2. append 的平均时间复杂度是多少？(摊还 O(1))
# 3. insert(0, x) 的时间复杂度是多少？(O(n)，需要移动所有元素)
# 参考源码: Objects/listobject.c 中 list_resize 函数


# ----- 题10: 列表的浅拷贝与深拷贝 -----
import copy

# 浅拷贝: 只复制第一层
original = [[1, 2], [3, 4], [5, 6]]
shallow = original.copy()  # 等价于 original[:]
shallow[0][0] = 999
print(f"original: {original}")  # original 也被修改了！
print(f"shallow:  {shallow}")

# 深拷贝: 递归复制所有层
original = [[1, 2], [3, 4], [5, 6]]
deep = copy.deepcopy(original)
deep[0][0] = 999
print(f"original: {original}")  # original 不受影响
print(f"deep:     {deep}")

# 为什么浅拷贝会影响原列表？
# 因为浅拷贝只复制了外层列表的引用，内部的子列表还是同一个对象
# 参考源码: Objects/listobject.c 中 list___copy___ 函数


# ----- 题11: 列表 vs 其他数据结构 -----
import time

# 对比: 列表查找 vs 集合查找
data_list = list(range(100000))
data_set = set(range(100000))
target = 99999

start = time.time()
for _ in range(100):
    target in data_list
t_list = time.time() - start

start = time.time()
for _ in range(100):
    target in data_set
t_set = time.time() - start

print(f"列表查找: {t_list:.4f}秒")
print(f"集合查找: {t_set:.4f}秒")
print(f"集合比列表快 {t_list/t_set:.0f} 倍")

# 为什么集合快这么多？
# 列表: O(n) 线性扫描
# 集合: O(1) 哈希查找
# 如果需要频繁判断元素是否存在，用 set 或 dict


# ----- 题12: 列表的 sort() vs sorted() -----
# sort(): 原地排序，返回 None，不创建新列表
# sorted(): 返回新列表，不修改原列表

data = [3, 1, 4, 1, 5, 9, 2, 6]
result = data.sort()
print(f"data.sort() 返回值: {result}")  # ____
print(f"排序后 data: {data}")

data = [3, 1, 4, 1, 5, 9, 2, 6]
result = sorted(data)
print(f"sorted(data) 返回值: {result}")
print(f"原 data 不变: {data}")

# sort() 使用的是 TimSort 算法 (Python 自创，Java 也用)
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)
# 参考: Objects/listsort.txt (TimSort 的设计文档)


# ----- 题13: 列表作为栈和队列 -----
# 栈: 后进先出 (LIFO) - 用 append + pop
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(f"栈: {stack}")
print(f"弹出: {stack.pop()}")
print(f"弹出: {stack.pop()}")

# 队列: 先进先出 (FIFO) - 用 append + pop(0) (不推荐，O(n))
# 推荐: from collections import deque
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(f"队列: {queue}")
print(f"弹出: {queue.popleft()}")
print(f"弹出: {queue.popleft()}")

# 为什么 deque 的 popleft 是 O(1) 而 list 的 pop(0) 是 O(n)?
# deque 使用双向链表实现，list 使用数组实现
# 参考源码: Modules/_collectionsmodule.c


# ----- 题14: 实战 - 成绩管理系统 -----
# 综合运用列表知识
students = ["小明", "小红", "小刚", "小丽", "小华", "小李", "小张", "小王"]
scores =   [85,     92,     78,     96,     88,     55,     63,     91]

# TODO: 完成以下功能
# (1) 计算平均分

# (2) 找出最高分和对应学生

# (3) 找出最低分和对应学生

# (4) 统计各等级人数 (A/B/C/D/E)

# (5) 按成绩从高到低排序，输出排名

# (6) 找出所有不及格的学生

# (7) 用 zip 将 students 和 scores 配对，创建字典 (选做)
