"""
Day02 练习1 - 数据类型深入理解
由浅入深理解 Python 的数据类型系统

参考源码: Objects/longobject.c   (int)
         Objects/floatobject.c  (float)
         Objects/boolobject.c   (bool)
         Objects/unicodeobject.c (str)
         Objects/complexobject.c (complex)
         Lib/decimal.py         (Decimal)
"""

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 类型识别 -----
# 遍历以下值，打印每个值、它的类型、以及它是否是 int/float/bool/str
values = [42, 3.14, True, "hello", 0, "", 3+4j, None, False, "0"]
for v in values:
    # TODO: 打印格式: "值=42, 类型=<class 'int'>, 是int? True"
    print(f"值={v} ,类型={type(v)}")
    print(type(v) == int)


# ----- 题2: 类型转换 -----
# 完成以下转换，观察结果
print("--- int() ---")
print(int("123"))        # 字符串转整数: ___123
print(int("12", 16))    # 十六进制字符串转整数: ____18
print(int(3.99))         # 浮点数转整数: ____3 (注意截断方式)
print(int(-3.99))        # 负浮点数转整数: ____-3
print(int(True))         # 布尔转整数: ____1

print("--- float() ---")
print(float("3.14"))     # ____3.14
print(float("inf"))      # ____inf
print(float("-inf"))     # ____-inf
print(float("nan"))      # ____nan
print(float(True))       # ____1.0

print("--- str() ---")
print(str(123))          # ____123
print(str(3.14))         # ____3.14
print(str(True))         # ____true
print(str(None))         # ____None

print("--- bool() ---")
print(bool(0))           # ____flase
print(bool(1))           # ____true
print(bool(-1))          # ____ true
print(bool(""))          # ____flase
print(bool("0"))         # ____  注意! "0" 是非空字符串 true
print(bool([]))          # ____ flase
print(bool([0]))         # ____  注意! [0] 是非空列表 true
print(bool(None))        # ____flase

# 总结: bool() 中哪些值是 False？
# 记忆口诀: "零空None" — 数值0、空容器、None


# ----- 题3: 整数不同进制表示 -----
# 用不同进制表示十进制数 42，验证它们相等
dec = 42
binary = 0b101010
octal = 0o52
hexa = 0x2A
# TODO: 验证这四个值相等
if bin(dec) == binary :
    print("dec 和 binary相等")
else:print("NO")
if oct(dec) == octal :
    print("dec 和 octal")
else:print("NO")
if hex(dec) == hexa :
    print("dec 和 hexa")
else:print("NO")
# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题4: 整数没有上限 -----
# Python 的 int 没有溢出限制，可以表示任意大的整数
# 计算 100 的阶乘 (100!)
import math
result = math.factorial(100)
print(f"100! = {result}")
print(f"100! 的位数: {len(str(result))}")
# 思考: C语言中的 int 最大值是多少？Python 为什么没有这个限制？
# 参考源码: Objects/longobject.c
# Python 的 int 使用可变长度的数组存储，按需扩展


# ----- 题5: 浮点数精度深入 -----
# IEEE 754 双精度浮点数: 1位符号 + 11位指数 + 52位尾数
# 精度约为 15-17 位有效数字
print(f"sys.float_info = {__import__('sys').float_info}")
print()

# 以下哪些比较会出问题？
print(f"0.1 + 0.2 == 0.3:        {0.1 + 0.2 == 0.3}")         # ____flase
print(f"0.1 + 0.2 - 0.3 == 0.0:  {0.1 + 0.2 - 0.3 == 0.0}")  # ____flase

# 正确的浮点数比较方式
import math
print(f"math.isclose(0.1+0.2, 0.3): {math.isclose(0.1+0.2, 0.3)}")

# Decimal 精确计算
from decimal import Decimal
a = Decimal("0.1")
b = Decimal("0.2")
print(f"Decimal('0.1') + Decimal('0.2') = {a + b}")
# 注意: Decimal("0.1") vs Decimal(0.1) 的区别！
print(f"Decimal(0.1) = {Decimal(0.1)}")       # 为什么不精确？
print(f"Decimal('0.1') = {Decimal('0.1')}")   # 为什么精确？
# Decimal(0.1) = 0.1000000000000000055511151231257827021181583404541015625
# Decimal('0.1') = 0.1
# 第一步：Python 解释器解析 0.1
# 0.1 在 Python 中首先被解释为 float 类型，#第二步：float 0.1 本身就是不精确的
# 第三步：Decimal(0.1) 接收的是这个已经不精确的值
# 它只能精确表示这个不精确的 float 值


# 第一步：Python 解释器解析字符串 "0.1"
# 字符串是精确的文本表示
# 第二步：Decimal('0.1') 直接解析字符串
# 它不需要经过 float 转换，可以精确表示十进制 0.1


# ----- 题6: 布尔是整数的子类 -----
# bool 继承自 int，True 就是 1，False 就是 0
print(f"isinstance(True, int): {isinstance(True, int)}")
print(f"True + True: {True + True}")         # ____2
print(f"True * 10: {True * 10}")              # ____10
print(f"False + 100: {False + 100}")          # ____100
print(f"True > False: {True > False}")        # ____true

# 实际应用: 统计列表中满足条件的元素个数
nums = [1, 0, 3, 0, 5, 0, 7]
# TODO: 用一行代码统计非零元素个数 (提示: sum + bool转换)
count = sum(num != 0 for num in nums)  # 替换为你的代码
print(f"非零元素个数: {count}")  # 期望: 4


# ----- 题7: 字符串编码深入 -----
# Python 3 的字符串是 Unicode 字符串
s = "你好Python"
print(f"字符串: {s}")
print(f"长度(字符数): {len(s)}")

# 编码为字节
utf8_bytes = s.encode("utf-8")
gbk_bytes = s.encode("gbk")
print(f"UTF-8 编码: {utf8_bytes}")
print(f"UTF-8 字节数: {len(utf8_bytes)}")
print(f"GBK 编码: {gbk_bytes}")
print(f"GBK 字节数: {len(gbk_bytes)}")

# 为什么 UTF-8 和 GBK 的字节数不同？
# UTF-8: 中文3字节, ASCII 1字节
# GBK:   中文2字节, ASCII 1字节
# TODO: 验证这个规律
# 这怎么验证，你在上面已经验证了


# 编码解码必须使用相同的字符集
# TODO: 尝试用 UTF-8 解码 GBK 编码的字节，观察会发生什么
str = "用来编码"
UtfTest = str.encode("GBK")
print(UtfTest)
str1 = UtfTest.decode("GBK")
print(str1)
# 报错：'utf-8' codec can't decode byte 0xd3 in position 0: invalid continuation byte

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题8: type() vs isinstance() -----
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(f"type(d) == Dog:     {type(d) == Dog}")         # ____true
print(f"type(d) == Animal:  {type(d) == Animal}")      # ____flase
print(f"isinstance(d, Dog):    {isinstance(d, Dog)}")  # ____true
print(f"isinstance(d, Animal): {isinstance(d, Animal)}") # ____true

# 总结: type() 严格匹配类型，isinstance() 考虑继承关系
# 什么时候用哪个？  我的理解是type()是只考虑需要判断的对象属于什么类型，当需要判断属于哪个类或者类型的时候使用isinstance()


# ----- 题9: 对象的三要素 -----
# Python 中每个对象都有: id(身份)、type(类型)、value(值)
# 不可变对象: id 可能变，type 不变，value 不变(int/str/tuple)
# 可变对象:   id 不变，type 不变，value 可变(list/dict/set)

# 验证整数是不可变的
a = 23100
print(f"修改前: id={id(a)}, type={type(a)}, value={a}")
a = a + 1
print(f"修改后: id={id(a)}, type={type(a)}, value={a}")
# id 变了吗？说明什么？
# id了，a = a + 1实际上是让a指向了新的对象即23101，而原本的地址23100没有变化，这恰恰说明了整数的不可变

# 验证列表是可变的
lst = [1, 2, 3]
print(f"修改前: id={id(lst)}, type={type(lst)}, value={lst}")
lst.append(4)
print(f"修改后: id={id(lst)}, type={type(lst)}, value={lst}")
# id 变了吗？说明什么？
# 地址没有变化，说明是直接对原本的对象进行的修改，也就证明了列表是可变的

# 参考源码:
# Objects/longobject.c - int 是不可变的，每次运算创建新对象
# Objects/listobject.c - list 是可变的，append 直接修改内部数组


# ----- 题10: eval() 和 exec() -----
# eval() 执行表达式并返回结果
# exec() 执行代码块，返回 None
print(f"eval('2 + 3'): {eval('2 + 3')}")
print(f"eval('2 ** 10'): {eval('2 ** 10')}")

# 注意: eval/exec 只能用于学习，生产环境有安全风险！
# 思考: 为什么 eval() 不安全？
