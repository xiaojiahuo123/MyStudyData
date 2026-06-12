"""
Day05 练习1 - 字符串、元组、集合、字典（答案版）
版本: v1.1
最后更新: 2026-06-11
"""

# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 字符串索引与切片 [必做] -----
s = "Hello, Python!"

print(f"s[0]     = {s[0]}")       # ____  ✅ 答案: H
print(f"s[-1]    = {s[-1]}")      # ____  ✅ 答案: !
print(f"s[7:13]  = {s[7:13]}")    # ____  ✅ 答案: Python
print(f"s[::-1]  = {s[::-1]}")    # ____  ✅ 答案: !nohtyP ,olleH
print(f"s[::2]   = {s[::2]}")     # ____  ✅ 答案: Hlo yhn

# ----- 题2: 字符串不可变性 [必做] -----
s1 = "hello"
print(f"s1 的 id: {id(s1)}")
s1 = s1 + " world"
print(f"拼接后 s1 的 id: {id(s1)}")
# ✅ 答案: 字符串是不可变的，拼接操作会创建一个新的字符串对象，s1 变量指向了新对象，所以 id 变了。
# 原来的 "hello" 对象并没有被修改，它仍然存在于内存中（直到被回收）。

# ----- 题3: 字符串常用方法 [必做] -----
text = "  Hello, World! Hello, Python!  "

print(text.strip())                    # ✅ 答案: "Hello, World! Hello, Python!"
print(text.replace("Hello", "Hi", 1)) # ✅ 答案: "  Hi, World! Hello, Python!  "
print(text.strip().split(","))         # ✅ 答案: ['Hello', ' World! Hello', ' Python!']
print(text.count("Hello"))             # ✅ 答案: 2
print(text.startswith("  "))           # ✅ 答案: True
print(text.find("Python"))             # ✅ 答案: 27

# ----- 题4: 元组基础 [必做] -----
t1 = (1, 2, 3)
t2 = (1,)
t3 = ()
t4 = tuple([4, 5, 6])

print(f"t1 = {t1}, type = {type(t1)}")  # ✅ 答案: <class 'tuple'>
print(f"t2 = {t2}, type = {type(t2)}")  # ✅ 答案: <class 'tuple'>
print(f"t3 = {t3}, type = {type(t3)}")  # ✅ 答案: <class 'tuple'>
print(f"t4 = {t4}, type = {type(t4)}")  # ✅ 答案: <class 'tuple'>

# ✅ 答案:
# a = (1)   → type 是 int（括号被当作运算符，不是元组）
# b = (1,)  → type 是 tuple（逗号才是创建元组的关键）

# ----- 题5: 元组不可变的特殊情况 [必做] -----
t = (1, 2, 3, [4, 5])

# ✅ 答案:
# t[0] = 10        → 会报错 TypeError（元组元素不可变）
# t[3] = [6, 7]    → 会报错 TypeError（元组元素不可变）
# t[3].append(6)   → 不会报错（列表本身可变，元组只是持有列表的引用）
# print(t)         → (1, 2, 3, [4, 5, 6])

# ----- 题6: 集合基础 [必做] -----
s1 = {1, 2, 3, 2, 1}
print(f"s1 = {s1}")          # ____  ✅ 答案: {1, 2, 3}（去重）

s2 = set([3, 4, 5, 3])
print(f"s2 = {s2}")          # ____  ✅ 答案: {3, 4, 5}（去重）

# ✅ 答案: s3 = {} 创建的是 dict，不是 set
s3 = set()
print(f"type({{}}) = {type({})}")      # ✅ 答案: <class 'dict'>
print(f"type(set()) = {type(s3)}")     # ✅ 答案: <class 'set'>

# ----- 题7: 字典基础 [必做] -----
d = {"name": "小明", "age": 18, "city": "北京"}

print(f"d['name']     = {d['name']}")       # ____  ✅ 答案: 小明
print(f"d.get('age')  = {d.get('age')}")    # ____  ✅ 答案: 18
print(f"d.get('score') = {d.get('score')}") # ____  ✅ 答案: None
print(f"d.get('score', 0) = {d.get('score', 0)}")  # ____  ✅ 答案: 0

# ✅ 答案:
# d['score']      → 报错 KeyError
# d.get('score')  → 返回 None

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题8: 字符串统计词频 [必做] -----
text = "the quick brown fox jumps over the lazy dog the fox"

# 参考实现:
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(f"  {word}: {count}")

# ----- 题9: 字符串格式化表格 [必做] -----
students = [
    ("张三", 85, 92, 78),
    ("李四", 90, 88, 95),
    ("王五", 76, 85, 80),
]

# 参考实现:
print("┌──────┬──────┬──────┬──────┬──────┐")
print("│ 姓名 │ 语文 │ 数学 │ 英语 │ 总分 │")
print("├──────┼──────┼──────┼──────┼──────┤")
for name, c, m, e in students:
    total = c + m + e
    print(f"│ {name} │ {c:4d} │ {m:4d} │ {e:4d} │ {total:4d} │")
print("└──────┴──────┴──────┴──────┴──────┘")

# ----- 题10: 集合运算实战 [必做] -----
class_a = {"Python", "Java", "C++", "Go"}
class_b = {"Python", "JavaScript", "C++", "Rust"}
class_c = {"Python", "Java", "Rust", "Swift"}

# 参考实现:
# 1. 三个班都选的课程
all_three = class_a & class_b & class_c
print(f"三个班都选的: {all_three}")  # ✅ 答案: {'Python'}

# 2. 只在 A 班开设的课程
only_a = class_a - class_b - class_c
print(f"只在 A 班: {only_a}")  # ✅ 答案: {'Go'}

# 3. 至少在一个班开设的所有课程
all_courses = class_a | class_b | class_c
print(f"所有课程: {all_courses}")

# 4. 恰好在两个班开设的课程
two_classes = set()
for course in all_courses:
    count = (course in class_a) + (course in class_b) + (course in class_c)
    if count == 2:
        two_classes.add(course)
print(f"恰好两个班: {two_classes}")  # ✅ 答案: {'Java', 'C++', 'Rust'}

# ----- 题11: 字典嵌套 - 学生成绩管理系统 [必做] -----
students = {
    "张三": {"语文": 85, "数学": 92, "英语": 78},
    "李四": {"语文": 90, "数学": 88, "英语": 95},
    "王五": {"语文": 76, "数学": 85, "英语": 80},
}

# 参考实现:
# 1. 计算每个学生的总分和平均分
for name, scores in students.items():
    total = sum(scores.values())
    avg = total / len(scores)
    print(f"{name}: 总分={total}, 平均分={avg:.1f}")

# 2. 找出数学最高分的学生
best_math = max(students.items(), key=lambda x: x[1]["数学"])
print(f"数学最高: {best_math[0]} ({best_math[1]['数学']}分)")

# 3. 计算每科的平均分
subjects = list(list(students.values())[0].keys())
for subject in subjects:
    avg = sum(s[subject] for s in students.values()) / len(students)
    print(f"{subject}平均分: {avg:.1f}")

# ----- 题12: 字典推导式 [必做] -----

# 参考实现:
# 1. 平方字典
squares = {i: i**2 for i in range(1, 11)}
print(f"平方字典: {squares}")

# 2. 反转键值对
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(f"反转: {reversed_dict}")

# 3. 统计元素出现次数
chars = ["a", "b", "a", "c", "b", "a", "d"]
char_count = {c: chars.count(c) for c in set(chars)}
print(f"字符计数: {char_count}")

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题13: 字符串驻留（Interning） [选做] -----
a = "hello"
b = "hello"
print(f"a is b: {a is b}")       # ____  ✅ 答案: True

a = "hello world!"
b = "hello world!"
print(f"a is b: {a is b}")       # ____  ✅ 答案: 可能 False（含空格和标点）

a = "hello123"
b = "hello123"
print(f"a is b: {a is b}")       # ____  ✅ 答案: 可能 True（标识符规则字符串）

# ----- 题14: 元组 vs 列表的性能 [选做] -----
import time

start = time.time()
for _ in range(1000000):
    lst = [1, 2, 3, 4, 5]
t_list = time.time() - start

start = time.time()
for _ in range(1000000):
    tup = (1, 2, 3, 4, 5)
t_tuple = time.time() - start

print(f"创建列表: {t_list:.4f}秒")
print(f"创建元组: {t_tuple:.4f}秒")
print(f"元组比列表快 {t_list/t_tuple:.1f} 倍")
# ✅ 答案: 元组是不可变的，Python 可以对其进行缓存和优化，创建时不需要分配可变的内存空间。

# ----- 题15: 集合的去重与顺序 [选做] -----
original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
deduplicated = list(set(original))
print(f"原列表: {original}")
print(f"set去重: {deduplicated}")  # ✅ 答案: 顺序不确定

deduplicated_ordered = list(dict.fromkeys(original))
print(f"保序去重: {deduplicated_ordered}")
# ✅ 答案: Python 3.7+ 的字典保持插入顺序，dict.fromkeys() 按插入顺序去重。

# ----- 题16: 字典的键必须是不可变类型 [选做] -----
d = {}
d[1] = "整数"           # ✅ 可以
d["hello"] = "字符串"    # ✅ 可以
d[(1, 2)] = "元组"      # ✅ 可以
# d[[1, 2]] = "列表"     # ❌ 不可以，列表不可哈希
# d[{"a": 1}] = "字典"   # ❌ 不可以，字典不可哈希
print(d)

# ----- 题17: 调试修复 [选做] -----
# ✅ 修复:
my_set = set()  # 修复: 用 set() 创建空集合，不是 {}
print(f"类型: {type(my_set)}")

data = {(1, 2, 3): "坐标"}  # 修复: 用元组代替列表作为键

point = (10, 20)
point = (30, point[1])  # 修复: 创建新元组，不能直接赋值 point[0] = 30

# ----- 题18: 数据结构选择 [选做] -----
print("\n--- 数据结构选择参考答案 ---")
print("场景1: set     - 去重 + O(1) 查找")
print("场景2: dict    - 键值对映射")
print("场景3: tuple   - 不可变的固定结构数据")
print("场景4: list    - 有序 + 允许重复")
