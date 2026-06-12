"""
Day05 练习2 - 字符串深入与编码（答案版）
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
s = "hello, WORLD, Hello, python, HELLO"

print(s.lower())           # ✅ 答案: "hello, world, hello, python, hello"
print(s.upper())           # ✅ 答案: "HELLO, WORLD, HELLO, PYTHON, HELLO"
print(s.title())           # ✅ 答案: "Hello, World, Hello, Python, Hello"
print("hello".isalpha())       # ____  ✅ 答案: True
print("hello123".isalpha())    # ____  ✅ 答案: False
print("12345".isdigit())       # ____  ✅ 答案: True
print("123abc".isdigit())      # ____  ✅ 答案: False
print("hello_123".isidentifier())  # ____  ✅ 答案: True
print("123hello".isidentifier())   # ____  ✅ 答案: False（数字开头）
print("class".isidentifier())      # ____  ✅ 答案: True（是关键字，但符合标识符规则）

# ----- 题2: 字符串对齐与填充 [必做] -----
for i in range(1, 10, 2):
    print(("*" * i).center(9))

# ----- 题3: find vs index [必做] -----
text = "Python is great. Python is powerful. I love Python."

print(f"find('Python'): {text.find('Python')}")   # ✅ 答案: 0
print(f"rfind('Python'): {text.rfind('Python')}") # ✅ 答案: 42
print(f"find('Java'): {text.find('Java')}")       # ✅ 答案: -1
# print(text.index("Java"))  # ✅ 答案: 会报错 ValueError

print(text.replace("Python", "Java", 1))   # ✅ 答案: "Java is great. Python is powerful. I love Python."
print(text.replace("Python", "Java"))      # ✅ 答案: 全部替换

# ----- 题4: split 和 join 的配合 [必做] -----
csv_data = "张三,85,92,78\n李四,90,88,95\n王五,76,85,80"

# 参考实现:
lines = csv_data.split("\n")
for line in lines:
    parts = line.split(",")
    name = parts[0]
    scores = [int(s) for s in parts[1:]]
    total = sum(scores)
    print(f"{name}: 各科={scores}, 总分={total}")

# ----- 题5: 元组解包 [必做] -----
a, b, c = (1, 2, 3)
print(f"a={a}, b={b}, c={c}")

first, *rest = (1, 2, 3, 4, 5)
print(f"first={first}, rest={rest}")   # ____  ✅ 答案: first=1, rest=[2, 3, 4, 5]

*head, last = (1, 2, 3, 4, 5)
print(f"head={head}, last={last}")     # ____  ✅ 答案: head=[1, 2, 3, 4], last=5

first, *middle, last = (1, 2, 3, 4, 5)
print(f"first={first}, middle={middle}, last={last}")
# ✅ 答案: first=1, middle=[2, 3, 4], last=5

# 参考实现: 交换变量
a, b = 10, 20
a, b = b, a
print(f"交换后: a={a}, b={b}")  # ✅ 答案: a=20, b=10

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题6: 字符串反转与回文判断 [必做] -----
s = "Hello, World!"
print(s[::-1])                    # ✅ 答案: !dlroW ,olleH
print("".join(reversed(s)))       # ✅ 答案: !dlroW ,olleH

lst = list(s)
lst.reverse()
print("".join(lst))               # ✅ 答案: !dlroW ,olleH

# 参考实现:
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(f"'racecar' 是回文: {is_palindrome('racecar')}")                         # ✅ True
print(f"'hello' 是回文: {is_palindrome('hello')}")                             # ✅ False
print(f"'A man a plan a canal Panama' 是回文: {is_palindrome('A man a plan a canal Panama')}")  # ✅ True

# ----- 题7: 字符串编码 [必做] -----
s = "你好世界"
print(f"字符串: {s}")
print(f"长度: {len(s)}")     # ____  ✅ 答案: 4（字符数）

b_utf8 = s.encode("utf-8")
b_gbk = s.encode("gbk")
print(f"UTF-8 编码: {b_utf8}")
print(f"GBK 编码: {b_gbk}")
print(f"UTF-8 字节数: {len(b_utf8)}")  # ____  ✅ 答案: 12（每个中文3字节）
print(f"GBK 字节数: {len(b_gbk)}")     # ____  ✅ 答案: 8（每个中文2字节）

print(f"UTF-8 解码: {b_utf8.decode('utf-8')}")
print(f"GBK 解码: {b_gbk.decode('gbk')}")

# ✅ 答案: UTF-8 中文占3字节，4个字=12字节；GBK 中文占2字节，4个字=8字节

# ----- 题8: ord 和 chr - 凯撒密码 [必做] -----
print(f"ord('A') = {ord('A')}")    # ____  ✅ 答案: 65
print(f"ord('中') = {ord('中')}")  # ____  ✅ 答案: 20013
print(f"chr(65) = {chr(65)}")      # ____  ✅ 答案: A
print(f"chr(20013) = {chr(20013)}") # ____  ✅ 答案: 中

# 参考实现:
def caesar_encrypt(text, shift=3):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)

print(f"凯撒加密 'Hello': {caesar_encrypt('Hello')}")      # ✅ 答案: Khoor
print(f"凯撒解密 'Khoor': {caesar_encrypt('Khoor', -3)}")  # ✅ 答案: Hello

# ----- 题9: 集合的哈希原理 [选做] -----
valid_set = {1, "hello", (1, 2, 3), frozenset([1, 2])}
print(f"可哈希的元素: {valid_set}")

fs = frozenset([1, 2, 3])
print(f"frozenset: {fs}")

# ----- 题10: setdefault vs get [必做] -----
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

count1 = {}
for word in words:
    count1[word] = count1.get(word, 0) + 1
print(f"get方式: {count1}")

count2 = {}
for word in words:
    count2.setdefault(word, 0)
    count2[word] += 1
print(f"setdefault: {count2}")

# ✅ 答案: get 只读取默认值，不修改字典；setdefault 会在 key 不存在时插入默认值。
# 计数场景两者效果一样，但 setdefault 会多一次插入操作。

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题11: 字符串拼接的性能 [选做] -----
import time

start = time.time()
s = ""
for i in range(100000):
    s += str(i)
t1 = time.time() - start

start = time.time()
s = "".join(str(i) for i in range(100000))
t2 = time.time() - start

print(f"+= 拼接: {t1:.4f}秒")
print(f"join 拼接: {t2:.4f}秒")
print(f"join 比 += 快 {t1/t2:.1f} 倍")
# ✅ 答案: += 每次创建新字符串对象并复制内容，时间复杂度 O(n²)；
# join 先计算总长度，一次性分配内存，时间复杂度 O(n)。

# ----- 题12: 字典 vs 列表的查找效率 [选做] -----
big_list = list(range(100000))
big_set = set(big_list)
big_dict = {i: True for i in big_list}

target = 99999

start = time.time()
for _ in range(1000):
    target in big_list
t_list = time.time() - start

start = time.time()
for _ in range(1000):
    target in big_set
t_set = time.time() - start

start = time.time()
for _ in range(1000):
    target in big_dict
t_dict = time.time() - start

print(f"列表查找: {t_list:.4f}秒")
print(f"集合查找: {t_set:.4f}秒")
print(f"字典查找: {t_dict:.4f}秒")
print(f"集合比列表快 {t_list/t_set:.0f} 倍")
# ✅ 答案: 列表是 O(n) 线性查找，集合和字典是 O(1) 哈希查找。

# ----- 题13: 综合实战 - 文本分析器 [选做] -----
def analyze_text(text):
    """分析文本的基本统计信息"""
    total_chars = len(text)
    chars_no_space = len(text.replace(" ", ""))
    words = text.split()
    total_words = len(words)
    sentences = text.count(".") + text.count("!") + text.count("?")

    word_freq = {}
    for word in words:
        word = word.lower().strip(".,!?;:")
        word_freq[word] = word_freq.get(word, 0) + 1

    top5 = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        "总字符数": total_chars,
        "非空字符数": chars_no_space,
        "单词数": total_words,
        "句子数": sentences,
        "最常见词": top5,
    }

sample = """Python is a programming language. Python is easy to learn.
Python is powerful and flexible. Many developers love Python."""

result = analyze_text(sample)
print("\n--- 文本分析结果 ---")
for key, value in result.items():
    print(f"  {key}: {value}")

# ----- 题14: 调试修复 [选做] -----
# ✅ 修复:
data = "你好".encode("utf-8")
result = data.decode("utf-8")  # 修复: 编码和解码要用相同的编码格式

text = "hello  world"
parts = text.split()  # 修复: 不传参数按任意空白分割，自动忽略多余空格
print(f"分割结果: {parts}")

nums = [1, 2, 3, 4, 5]
result = "-".join(str(n) for n in nums)  # 修复: 先转为字符串再 join
print(f"结果: {result}")

# ----- 题15: 数据结构转换总结 [选做] -----
print(list("hello"))                              # ✅ ['h', 'e', 'l', 'l', 'o']
print(sorted(set([1, 2, 2, 3, 3, 3])))           # ✅ [1, 2, 3]
print(dict(zip([1, 2, 3], ["a", "b", "c"])))     # ✅ {1: 'a', 2: 'b', 3: 'c'}
