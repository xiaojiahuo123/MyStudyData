"""
Day04 练习1 - 循环与range深入
由浅入深掌握循环的各种用法

参考源码: Objects/rangeobject.c (range对象)
         Lib/itertools.py     (迭代器工具)
"""

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: range 三种用法 -----
# range(stop)
# range(start, stop)
# range(start, stop, step)

# TODO: 用 range 生成并打印以下序列:
# [0, 1, 2, 3, 4]
# range() 返回的是一个 range 对象，不是列表，直接打印不会显示元素。
# - ange 对象 ：节省内存，按需生成元素（懒加载）
# - 列表 ：立即生成所有元素，占用完整内存
nums = list(range(0, 5))
print(nums)

# [5, 6, 7, 8, 9]
nums = list(range(5, 10))
print(nums)

# [2, 4, 6, 8, 10]
nums = list(range(2, 11,2))
print(nums)

# [10, 8, 6, 4, 2]
nums = list(range(10, 1,-2))
print(nums)

# ----- 题2: 求和 -----
# TODO: 计算 1+2+3+...+100 (用 for 循环)
nums = range(1, 101)
count = 0
for i in nums:
    count += i
print(count)

# TODO: 计算 1-100 中所有奇数的和
nums = range(1, 101)
count = 0
for i in nums:
    if i & 1 != 0 :
        count += i
print(count)

# TODO: 计算 1-100 中所有能被3整除但不能被5整除的数的和
nums = range(1, 101)
count = 0
for i in nums:
    if i % 3 == 0 and i % 5 != 0 :
        count += i
print(count)

# ----- 题3: 计数 -----
# TODO: 统计 1-1000 中有多少个质数
# 质数（素数） ：大于1的自然数，除了1和它本身外，不能被其他自然数整除。
count = 0
for num in range(2, 1001):
    if num == 2:
        count += 1
    elif num % 2 == 0:
        continue
    else:
        is_prime = True
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
print(f"1-1000 中有 {count} 个质数")

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题4: 嵌套循环 - 图形打印 -----
# TODO: 打印以下图形:

# (1) 直角三角形 (右下)
# *
# **
# ***
# ****
# *****
nums = range(1, 6)
for i in nums:
    for j in range(1, i+1):
        print("*", end="")
    print()

# (2) 倒直角三角形 (右上)
# *****
# ****
# ***
# **
# *
for i in range(5, 0, -1):
    print("*" * i)


# (3) 等腰三角形
#     *
#    ***
#   *****
#  *******
# *********
# nums = range(1, 10,2)
# for i in nums:
#     for j in range(1, i+1):
#         print("*", end="")
#     print()
for i in range(1, 10, 2):
    # 打印空格
    print(" " * ((9 - i) // 2), end="")
    # 打印星号
    print("*" * i)


# (4) 菱形 (选做)
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# 上半部分：1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(" " * ((9 - i) // 2), end="")
    print("*" * i)

# 下半部分：7, 5, 3, 1
for i in range(7, 0, -2):
    print(" " * ((9 - i) // 2), end="")
    print("*" * i)



# ----- 题5: 质数相关 -----
# TODO: 打印 1-100 所有质数，每行10个


# TODO: 打印前20个质数


# ----- 题6: 水仙花数 -----
# 水仙花数: 每位数字的立方和等于该数本身
# 例如: 153 = 1^3 + 5^3 + 3^3
# TODO: 打印所有三位数的水仙花数


# 扩展: 打印所有四位数的"四叶草数" (每位数字的四次方之和等于该数)


# ----- 题7: 完数 -----
# 完数: 一个数等于它的因子之和 (不含自身)
# 例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
# TODO: 打印 1-1000 中所有完数


# ----- 题8: continue 和 break 练习 -----
# TODO: 找出 1-100 中第一个能同时被 3 和 7 整除的数


# TODO: 打印 1-50，跳过所有包含数字 7 的数 (如 7, 17, 27, 37, 47)


# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题9: range 的本质 -----
# range 是一个不可变的序列对象，不是列表
r = range(0, 10, 2)
print(f"type(r): {type(r)}")
print(f"r: {r}")
print(f"r[2]: {r[2]}")         # 支持索引
print(f"2 in r: {2 in r}")     # 支持成员检测 (O(1)！)
print(f"11 in r: {11 in r}")
print(f"len(r): {len(r)}")

# range 的 in 操作为什么是 O(1)？
# 因为 range 只需要检查: start <= x < stop 且 (x-start) % step == 0
# 参考源码: Objects/rangeobject.c 中 range_contains 函数


# ----- 题10: enumerate 和 zip -----
# enumerate 同时获取索引和值
fruits = ["apple", "banana", "cherry"]
# TODO: 用 enumerate 打印 "0: apple", "1: banana", "2: cherry"
for i,value in enumerate(fruits):
    print(i, value)

# zip 同时遍历多个序列
names = ["小明", "小红", "小刚"]
scores = [85, 92, 78]
# TODO: 用 zip 打印 "小明: 85分", "小红: 92分", "小刚: 78分"
list1 = zip(names, scores)
for name, score in list1:
    print(f"{name} : {score}")

# zip 的长度以最短的为准
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]
print(f"zip 长度不同: {list(zip(a, b))}")  # 以 b 的长度为准

# itertools.zip_longest 以最长的为准
from itertools import zip_longest, count  # 以 a 为准

print(f"zip_longest: {list(zip_longest(a, b, fillvalue='?'))}")


# ----- 题11: 循环中的变量作用域 -----
# Python 的 for 循环变量会泄漏到外部作用域！
for i in range(5):
    pass
print(f"循环结束后 i = {i}")  # i 的值是 4

# 对比: 在函数中，for 循环变量不会泄漏
def test():
    for i in range(5):
        pass
    return i  # 函数内可以访问

print(f"函数中 i = {test()}")
# 这和很多其他语言不同！


# ----- 题12: 性能对比 -----
import time

# 对比: range 循环 vs while 循环的性能
start = time.time()
s = 0
for i in range(1000000):
    s += i
t1 = time.time() - start

start = time.time()
s = 0
i = 0
while i < 1000000:
    s += i
    i += 1
t2 = time.time() - start

print(f"for 循环: {t1:.4f}秒")
print(f"while 循环: {t2:.4f}秒")
print(f"for 比 while 快 {t2/t1:.1f} 倍")
# 为什么 for 循环更快？
# 因为 for 循环的迭代在 C 层面执行，while 循环每次都要在 Python 层面判断条件
