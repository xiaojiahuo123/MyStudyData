"""
Day05 练习2 - 字符串深入与编码
由浅入深掌握字符串的高级操作和编码原理

参考源码: Objects/unicodeobject.c  (Unicode 字符串实现)
         Lib/codecs.py            (编解码器)
版本: v1.1
最后更新: 2026-06-11
"""

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 字符串判断方法 [必做] -----
# 知识点: isalpha, isdigit, isidentifier, isspace
s = "hello, WORLD, Hello, python, HELLO"

# TODO: 用字符串方法完成以下操作
# 1. 全部转小写
print(s.lower())

# 2. 全部转大写
print(s.upper())

# 3. 每个单词首字母大写
print(s.title())

# 4. 判断是否全是字母
print("hello".isalpha())       # ____
print("hello123".isalpha())    # ____

# 5. 判断是否全是数字
print("12345".isdigit())       # ____
print("123abc".isdigit())      # ____

# 6. 判断是否是合法的标识符（变量名规则）
print("hello_123".isidentifier())  # ____
print("123hello".isidentifier())   # ____
print("class".isidentifier())      # ____

# ----- 题2: 字符串对齐与填充 [必做] -----
# 知识点: center, ljust, rjust, zfill

# TODO: 用 center 打印等腰三角形
#     *
#    ***
#   *****
#  *******
# *********
for i in range(1, 10, 2):
    print(("*" * i).center(9))

# ----- 题3: find vs index [必做] -----
# 知识点: find, rfind, index, rindex 的区别
text = "Python is great. Python is powerful. I love Python."

# TODO: 完成以下操作
# 1. find 返回第一次出现的位置
print(f"find('Python'): {text.find('Python')}")

# 2. rfind 返回最后一次出现的位置
print(f"rfind('Python'): {text.rfind('Python')}")

# 3. find 找不到返回 -1，index 找不到会报错
print(f"find('Java'): {text.find('Java')}")
# print(text.index("Java"))  # 会怎样？____

# 4. replace 的第三个参数限制替换次数
print(text.replace("Python", "Java", 1))   # ____
print(text.replace("Python", "Java"))      # ____

# ----- 题4: split 和 join 的配合 [必做] -----
# 知识点: split 分割、join 合并、CSV 解析
csv_data = "张三,85,92,78\n李四,90,88,95\n王五,76,85,80"

# TODO: 解析 CSV 数据，计算每人总分并输出
# 提示: split("\n") 分行 → split(",") 分列 → int() 转数字

# ----- 题5: 元组解包 [必做] -----
# 知识点: 基础解包、星号解包、交换变量

# 基础解包
a, b, c = (1, 2, 3)
print(f"a={a}, b={b}, c={c}")

# 星号解包（Python 3.0+）
first, *rest = (1, 2, 3, 4, 5)
print(f"first={first}, rest={rest}")   # ____

*head, last = (1, 2, 3, 4, 5)
print(f"head={head}, last={last}")     # ____

first, *middle, last = (1, 2, 3, 4, 5)
print(f"first={first}, middle={middle}, last={last}")

# TODO: 用元组解包交换变量
a, b = 10, 20
# 交换 a 和 b

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题6: 字符串反转与回文判断 [必做] -----
# 知识点: 切片反转、reversed、回文判断
s = "Hello, World!"

# 方式1: 切片
print(s[::-1])

# 方式2: reversed + join
print("".join(reversed(s)))

# 方式3: 转列表后反转
lst = list(s)
lst.reverse()
print("".join(lst))

# TODO: 实现回文判断函数
def is_palindrome(s):
    pass  # 学生实现

# 验证:
# print(is_palindrome("racecar"))                         # 预期: True
# print(is_palindrome("hello"))                           # 预期: False
# print(is_palindrome("A man a plan a canal Panama"))     # 预期: True

# ----- 题7: 字符串编码 [必做] -----
# 知识点: encode/decode、UTF-8、GBK、字节
s = "你好世界"
print(f"字符串: {s}")
print(f"长度: {len(s)}")     # ____

# 编码为字节
b_utf8 = s.encode("utf-8")
b_gbk = s.encode("gbk")
print(f"UTF-8 编码: {b_utf8}")
print(f"GBK 编码: {b_gbk}")
print(f"UTF-8 字节数: {len(b_utf8)}")  # ____
print(f"GBK 字节数: {len(b_gbk)}")     # ____

# 从字节解码
print(f"UTF-8 解码: {b_utf8.decode('utf-8')}")
print(f"GBK 解码: {b_gbk.decode('gbk')}")

# TODO: 为什么 UTF-8 编码是 12 字节，GBK 是 8 字节？
# 答: ________________________________

# ----- 题8: ord 和 chr - 凯撒密码 [必做] -----
# 知识点: ord, chr, ASCII 码、字符运算

print(f"ord('A') = {ord('A')}")    # ____
print(f"ord('中') = {ord('中')}")  # ____
print(f"chr(65) = {chr(65)}")      # ____
print(f"chr(20013) = {chr(20013)}") # ____

# TODO: 实现凯撒密码（每个字母后移3位）
def caesar_encrypt(text, shift=3):
    pass  # 学生实现

# 验证:
# print(caesar_encrypt("Hello"))      # 预期: Khoor
# print(caesar_encrypt("Khoor", -3))  # 预期: Hello

# ----- 题9: 集合的哈希原理 [选做] -----
# 知识点: hashable、frozenset、可变 vs 不可变

# 可以放入集合的类型（不可变/可哈希）
valid_set = {1, "hello", (1, 2, 3), frozenset([1, 2])}
print(f"可哈希的元素: {valid_set}")

# 不能放入集合的类型
# {[1, 2]}          # TypeError: unhashable type: 'list'
# {{"a": 1}}        # TypeError: unhashable type: 'dict'

# frozenset: 不可变的集合，可以放入另一个集合
fs = frozenset([1, 2, 3])
print(f"frozenset: {fs}")

# ----- 题10: setdefault vs get [必做] -----
# 知识点: setdefault, get, 默认值处理
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# 用 get 简化（最常用）
count1 = {}
for word in words:
    count1[word] = count1.get(word, 0) + 1
print(f"get方式: {count1}")

# 用 setdefault 简化
count2 = {}
for word in words:
    count2.setdefault(word, 0)
    count2[word] += 1
print(f"setdefault: {count2}")

# TODO: get 和 setdefault 的区别是什么？
# 答: ________________________________

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题11: 字符串拼接的性能 [选做] -----
# 知识点: += 拼接 vs join、时间复杂度 O(n²) vs O(n)
import time

# 方式1: += 拼接（慢！每次创建新字符串）
start = time.time()
s = ""
for i in range(100000):
    s += str(i)
t1 = time.time() - start

# 方式2: join 拼接（快！一次性拼接）
start = time.time()
s = "".join(str(i) for i in range(100000))
t2 = time.time() - start

print(f"+= 拼接: {t1:.4f}秒")
print(f"join 拼接: {t2:.4f}秒")
print(f"join 比 += 快 {t1/t2:.1f} 倍")
# 为什么 join 更快？
# 答: ________________________________

# ----- 题12: 字典 vs 列表的查找效率 [选做] -----
# 知识点: 哈希表 O(1) vs 线性查找 O(n)
import time

big_list = list(range(100000))
big_set = set(big_list)
big_dict = {i: True for i in big_list}

target = 99999

# 列表查找
start = time.time()
for _ in range(1000):
    target in big_list
t_list = time.time() - start

# 集合查找
start = time.time()
for _ in range(1000):
    target in big_set
t_set = time.time() - start

# 字典查找
start = time.time()
for _ in range(1000):
    target in big_dict
t_dict = time.time() - start

print(f"列表查找: {t_list:.4f}秒")
print(f"集合查找: {t_set:.4f}秒")
print(f"字典查找: {t_dict:.4f}秒")
print(f"集合比列表快 {t_list/t_set:.0f} 倍")

# ----- 题13: 综合实战 - 文本分析器 [选做] -----
# 知识点: 综合运用字符串方法、字典、排序

def analyze_text(text):
    """分析文本的基本统计信息"""
    # TODO: 实现以下功能
    # 1. 统计总字符数和非空字符数
    # 2. 统计单词数和句子数
    # 3. 统计词频，找出最常见的5个词
    pass

sample = """Python is a programming language. Python is easy to learn.
Python is powerful and flexible. Many developers love Python."""

# result = analyze_text(sample)
# print(result)

# ----- 题14: 调试修复 - 找出以下代码中的 3 个 BUG [选做] -----
# 知识点: 常见编码和字符串错误

# BUG: 编码 - 用错误的编码解码会怎样？
data = "你好".encode("utf-8")
result = data.decode("gbk")  # 编码不匹配

# BUG: 逻辑 - split 默认按空白分割，不只是空格
text = "hello  world"  # 中间有两个空格
parts = text.split(" ")  # 想按单个空格分
print(f"分割结果: {parts}")  # 会有空字符串

# BUG: 类型 - join 要求元素全是字符串
nums = [1, 2, 3, 4, 5]
result = "-".join(nums)  # 数字不能直接 join

# ----- 题15: 数据结构转换总结 [选做] -----
# 知识点: 各数据结构之间的相互转换

# 转换速查:
# 列表 → 元组: tuple([1,2,3])
# 列表 → 集合: set([1,2,3])
# 列表 → 字符串: ",".join(["a","b","c"])
# 元组 → 列表: list((1,2,3))
# 集合 → 列表: list({1,2,3})
# 字符串 → 列表: list("abc") 或 "a,b,c".split(",")
# 字典 → 列表: list(d.keys()) / list(d.values()) / list(d.items())
# 列表 → 字典: dict([("a",1),("b",2)])

# TODO: 完成以下转换
# 1. 将字符串 "hello" 转为字符列表
# 2. 将列表 [1, 2, 2, 3, 3, 3] 去重并排序
# 3. 将两个列表 [1,2,3] 和 ["a","b","c"] 转为字典
