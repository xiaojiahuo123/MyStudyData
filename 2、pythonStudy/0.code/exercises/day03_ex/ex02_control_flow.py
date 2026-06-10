"""
Day03 练习2 - 条件判断与循环
由浅入深掌握控制流

参考源码: Python/ceval.c (字节码执行引擎，包含 if/while 的底层实现)
         Lib/random.py  (随机数模块)
"""

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 成绩等级判断 -----
# 输入0-100的分数，输出等级: A(90-100), B(80-89), C(70-79), D(60-69), E(0-59)
# 处理非法输入(超出范围)
# score = int(input("请输入分数(0-100): "))
# TODO:
while True:
    try:
        score = int(input("请输入分数(0-100): "))
        if 0 <= score <= 100:
            break
        print("分数必须在0-100之间")
    except ValueError:
        print("请输入有效的整数")

# 使用 match 语句判断等级
match score:
    case score if score >= 90:
        print("等级: A")
    case score if score >= 80:
        print("等级: B")
    case score if score >= 70:
        print("等级: C")
    case score if score >= 60:
        print("等级: D")
    case _:
        print("等级: E")

# ----- 题2: 闰年判断 -----
# 闰年规则: 能被4整除但不能被100整除，或者能被400整除
# year = int(input("请输入年份: "))
# TODO:

#我写的
# while True :
#     year = int(input("请输入年份: "))
#     try:
#       if year < 0 :
#           print("请输出正确的年份！")
#     except:
#         print("请输入正确的整数!")
#     break  #  break（第55行）在 try/except 外面，循环只会执行一次，没有起到输入验证的作用
# if year == 0 :
#     print("不是闰年")
# elif year > 0 and year % 4 == 0 and year % 100 != 0 :  #  闰年规则漏了 year % 400 == 0 的情况（如 2000 年是闰年）
#  year == 0 的判断没必要单独处理
#     print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")
# TODO ：AI 更正
while True:
      try:
          year = int(input("请输入年份: "))
          break
      except ValueError:
          print("请输入正确的整数!")
      if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year}是闰年")
      else:
        print(f"{year}不是闰年")

# ----- 题3: while 循环基础 -----
# 用 while 循环计算 1+2+3+...+100
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(f"加起来的值为：{total}")



# ----- 题4: for 循环基础 -----

# 用 for 循环打印 1-20 中所有能被3整除的数
# TODO:
for i in range(1, 21):
    if i % 3 == 0:
        print(i)

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题5: match-case (Python 3.10+) -----
# 用 match-case 实现一个简单的计算器
# 输入两个数字和运算符(+,-,*,/)，输出结果
# 处理除零错误
num1 = float(input("输入第一个数: "))
op = input("输入运算符(+,-,*,/): ")
num2 = float(input("输入第二个数: "))
# # TODO
match op:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        if num2 == 0:
            print("错误：除数不能为零")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print(f"错误：未知运算符 '{op}'")


# ----- 题6: match-case 匹配复杂模式 -----
# match-case 不仅能匹配值，还能匹配结构
# 给定一个坐标点，判断它在哪个象限
point = (3, -2)
match point:
    case (0, 0):
        print("原点")
    case (x, 0):
        print(f"X轴上, x={x}")
    case (0, y):
        print(f"Y轴上, y={y}")
    case (x, y) if x > 0 and y > 0:
        print(f"第一象限: ({x}, {y})")
    # TODO: 补充其他三个象限的判断
    case (x, y) if x > 0 and y < 0:
        print(f"第四象限: ({x}, {y})")
    case (x, y) if x < 0 and y > 0:
        print(f"第二象限: ({x}, {y})")
    case (x, y) if x < 0 and y < 0:
        print(f"第三象限: ({x}, {y})")
    case _:
        print("错误")

# ----- 题7: 猜数字游戏 -----
# 程序随机生成1-100的数字，用户猜测
# 提示"大了"或"小了"，7次内猜对算赢
from random import randint
target = randint(1, 100)
max_attempts = 7
count = 0
# TODO : 实现猜数字逻辑
while count < max_attempts:
    count += 1
    CaiCe = input("请输入你猜测的数字~")

    # 1. 处理退出命令
    if CaiCe == 'exit':
        print("游戏退出")
        break

    # 2. 尝试转换为整数
    try:
        num = int(CaiCe)
    except ValueError:
        print("请输入有效的数字")
        count -= 1  # 输入错误不消耗次数
        continue

    # 3. 判断大小
    if num > target:
        print("大了")
    elif num < target:
        print("小了")
    else:
        print(f"恭喜你猜对了！用了 {count} 次")
        break
else:
    print(f"游戏结束，正确答案是 {target}")



# ----- 题8: 九九乘法表 -----
# 用嵌套循环打印九九乘法表
# 提示: print(f"{i}x{j}={i*j}", end="\t")
# TODO:


# ----- 题9: break 和 continue -----
# break: 跳出整个循环
# continue: 跳过本次循环，进入下一次

# 用 for 循环找出 1-100 中第一个能被 17 整除的数
# TODO: 用 break
from random import randint
nums = range(1, 101)
for num in nums:
    if num % 17 == 0:
        print(num)
        break
# 用 for 循环打印 1-20 中所有奇数 (用 continue 跳过偶数)
# TODO:
nums1 = range(1, 21)
for num in nums1:
    if num & 1 != 0:
        print(num)

# ----- 题10: while-else -----
# while-else: 循环正常结束(没有被 break 中断)时执行 else
# 找一个数的最小因子(除了1)
n = 91
factor = 2
while factor < n:
    if n % factor == 0:
        print(f"{n} 的最小因子是 {factor}")
        break
    factor += 1
else:
    print(f"{n} 是质数")


# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题11: for 循环的本质 -----
# for 循环实际上是对迭代器(iterator)的调用
# 等价于:
# it = iter(iterable)
# while True:
#     try:
#         value = next(it)
#         # 循环体
#     except StopIteration:
#         break

# 验证: 手动实现 for 循环
lst = [10, 20, 30, 40, 50]
# TODO: 用 iter() 和 next() 手动遍历列表
# 提示: 用 try...except StopIteration 捕获结束
#我还没有学迭代器


# ----- 题12: range() 的惰性求值 -----
# range() 不会立即生成所有数，而是按需生成
import sys
r = range(1000000)
print(f"range(1000000) 占用内存: {sys.getsizeof(r)} 字节")
lst = list(r)
print(f"list(range(1000000)) 占用内存: {sys.getsizeof(lst)} 字节")
# 为什么 range 比 list 省这么多内存？
# 因为 range 只存储 start, stop, step 三个值，不存储所有元素


# ----- 题13: 条件表达式(三元运算符) -----
# Python 的三元运算符: x if condition else y
age = 20
# TODO: 用三元运算符判断是否成年
status = None  # 替换为你的代码
print(f"年龄{age}, {status}")

# 嵌套三元运算符 (不推荐过度嵌套)
score = 85
# TODO: 用嵌套三元运算符判断等级 (A/B/C/D/E)
grade = None  # 替换为你的代码
print(f"分数{score}, 等级{grade}")


# ----- 题14: 循环中的 else -----
# for-else 和 while-else 是 Python 独有的特性
# else 在循环正常结束时执行，被 break 中断时不执行

# 找质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        # 循环正常结束，说明没有找到因子
        return True

# TODO: 打印 1-50 中所有质数


# ----- 题15: 递归 vs 循环 -----
# 很多循环可以用递归实现，但要注意递归深度限制
n = 10
# 用递归计算阶乘
def factorial_recursive(n):
    # TODO: 递归实现
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
print(f"递归结果: {factorial_recursive(n)}")  # 调用函数


# 用循环计算阶乘
def factorial_loop(n):
    if n == 0 or n == 1:
        return 1
    result = 1  # ✅ 初始化为1
    for i in range(2, n + 1):  # ✅ 正确迭代
        result *= i
    return result  # ✅ 返回结果

print(f"循环结果: {factorial_loop(n)}")

# 测试
print(f"递归: 10! = {factorial_recursive(10)}")
print(f"循环: 10! = {factorial_loop(10)}")

# 查看递归深度限制
import sys
print(f"默认递归深度限制: {sys.getrecursionlimit()}")
# 可以用 sys.setrecursionlimit() 修改，但不推荐设置太大
