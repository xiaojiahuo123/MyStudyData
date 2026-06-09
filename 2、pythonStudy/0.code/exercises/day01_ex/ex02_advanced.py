"""
Day01 练习2 - 进阶挑战
综合运用变量、f-string、进制知识

参考源码: Objects/floatobject.c (浮点数对象)
         Objects/boolobject.c  (布尔对象)
"""

# ============================================================
#                    综合挑战题
# ============================================================

# ----- 题1: 进制计算器 -----
# 编写一个进制转换工具:
# 输入一个十进制数，输出它的二进制、八进制、十六进制
# 要求用 f-string 格式化输出，对齐显示
# 示例输出:
# 十进制: 255
# 二进制: 0b11111111
# 八进制: 0o377
# 十六进制: 0xff
# num = int(input("请输入一个十进制数: "))
# # TODO:
# print(f"十进制:{num}")
# print(f"二进制:{bin(num)}") # 或者 {num:08b}
# print(f"八进制:{oct(num)}") # 或者 {num:03b}
# print(f"十六进制:{hex(num)}") # 或者 {num:02x}

# ----- 题2: 二进制加法 -----
# 不使用 + 运算符，用位运算实现两个正整数的加法
# 提示: 异或(^) 得到不进位的和，与(&)<<1 得到进位
# 循环直到没有进位
a, b = 15, 29
# TODO: 用位运算计算 a + b
# ----- 题2: 二进制加法 -----
# 不使用 + 运算符，用位运算实现两个正整数的加法
# 提示: 异或(^) 得到不进位的和，与(&)<<1 得到进位
# 循环直到没有进位

a, b = 15, 29

# 用位运算计算 a + b
def add_by_bit(a, b):
    while b != 0:
        # 异或得到不进位的和
        sum_without_carry = a ^ b
        # 与运算后左移得到进位
        carry = (a & b) << 1
        # 将进位赋值给 b，无进位时循环结束
        a = sum_without_carry
        b = carry
    return a

result = add_by_bit(a, b)
print(f"{a} + {b} = {result}")
print(f"验证: {a} + {b} = {a + b}")

# ----- 题3: 类型探索 -----
# 不运行代码，预测以下每个 type() 的结果
# 然后运行验证，说明原因
print(type(1))          # ____INT
print(type(1.0))        # ____FLOAT
print(type(True))       # ____BOOL
print(type("True"))     # ____String
print(type(1+2j))       # ____complex
print(type(None))       # ____NoneType

# 思考: bool 为什么是 int 的子类？
# 参考源码: Objects/boolobject.c
# PyBool_Type 继承自 PyLong_Type


# ----- 题4: 浮点数陷阱 -----
# 预测输出并解释原因
print(0.1 + 0.2 == 0.3)           # 预测: ____
print(0.1 + 0.2)                   # 输出: ____
print(f"{0.1 + 0.2:.20f}")        # 用20位小数看看实际值

# 如何正确比较两个浮点数？
# 提示: 使用 math.isclose() 或 abs(a-b) < epsilon
# 参考源码: Objects/floatobject.c
# 浮点数使用 IEEE 754 双精度格式，0.1 无法精确表示


# ----- 题5: 字符串本质 -----
# Python 字符串是不可变的 Unicode 字符序列
s = "Python"
# 以下操作哪些会报错？为什么？
# s[0] = "J"          # 会报错吗？为什么？  会，是直接堆s进行更改，但是实际上s是String，不可更改
# s2 = "J" + s[1:]    # 这行能执行吗？ 可以，这是创建一个新的String变量
s2 ="j" + "Python" + s
print(id(s))
print(id(s2))

# 尝试用 id() 验证字符串的不可变性
# TODO: 证明每次"修改"字符串都会创建新对象


# ----- 题6: 赋值的多种方式 -----
# Python 支持多种赋值方式，写出以下赋值的等价形式
# 海象运算符 (Python 3.8+)
import random
# 传统写法
# n = random.randint(1, 100)
# if n > 50:
#     print(f"{n} 大于 50")
if (n := random.randint(1, 100)) > 50:
    print(f"{n} 大于 50")
# 海象运算符写法 (用 := 在表达式中赋值)
# TODO: 用海象运算符改写上面的代码


# ----- 题7: f-string 调试技巧 -----
# Python 3.8+ 支持 f-string 调试语法 {expr=}
x = 10
y = 3
# TODO: 用 {x=} 和 {y=} 打印变量名和值
# 期望输出类似: x=10, y=3
print(f"{x=}, {y=}")  
# TODO: 用 f-string 调试语法打印 x//y 和 x%y 的结果
print(f"{x//y=}, {x%y=}")
# // 是取整运算