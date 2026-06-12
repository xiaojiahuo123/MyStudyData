"""
Day05 练习1 - 字符串、元组、集合、字典
由浅入深掌握 Python 核心数据结构

参考源码: Objects/unicodeobject.c  (字符串底层实现)
         Objects/tupleobject.c    (元组底层实现)
         Objects/setobject.c      (集合底层实现)
         Objects/dictobject.c     (字典底层实现)
版本: v1.1
最后更新: 2026-06-11
"""
import itertools
# ============================================================
#                      第一部分: 基础题
# ============================================================

from typing import Any


print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 字符串索引与切片 [必做] -----
# 知识点: 字符串索引、切片、步长
s = "Hello, Python!"

# 预测以下表达式的结果，然后运行验证
print(f"s[0]     = {s[0]}")       # ____H
print(f"s[-1]    = {s[-1]}")      # ____！
print(f"s[7:13]  = {s[7:13]}")    # ____Python!
print(f"s[::-1]  = {s[::-1]}")    # ____!nohtyP ,olleH
print(f"s[::2]   = {s[::2]}")     # ____Hlo yhn
# s[7:13] 'Python' 切片7到13（不包含13）
# s[::-1] '!nohtyP ,olleH' 步长-1，反转字符串
# s[::2] 'Hlo yhn' 步长2，每隔一个字符取一个

# ----- 题2: 字符串不可变性 [必做] -----
# 知识点: 字符串不可变、id 变化
s1 = "hello"
print(f"s1 的 id: {id(s1)}")
s1 = s1 + " world"
print(f"拼接后 s1 的 id: {id(s1)}")
# 问题: 为什么 id 变了？字符串不是不可变的吗？
# 答: ____因为字符串本身是不可变的，这里的S1实际上已经是指向了一个新的对象的指针了，所以得到的地址变了____________________________

# ----- 题3: 字符串常用方法 [必做] -----
# 知识点: strip, replace, split, count, startswith, find
text = "  Hello, World! Hello, Python!  "
print(text)
# TODO: 用字符串方法完成以下操作（每个只用一行）
# 1. 去除首尾空格
print(text.strip())

# 2. 将第一个 "Hello" 替换为 "Hi"
print(text.replace("Hello", "Hi", 1))

# 3. 按逗号分割成列表
print(text.strip().split(","))

# 4. 统计 "Hello" 出现的次数
print(text.count("Hello"))

# 5. 判断是否以两个空格开头
print(text.startswith("  "))

# 6. 找到 "Python" 的起始索引
print(text.find("Python"))

# ----- 题4: 元组基础 [必做] -----
# 知识点: 元组创建、单元素元组、type
# 预测以下代码的输出和类型
t1 = (1, 2, 3)
t2 = (1,)          # 单元素元组必须有逗号
t3 = ()            # 空元组
t4 = tuple([4, 5, 6])  # 从列表创建

print(f"t1 = {t1}, type = {type(t1)}")  #t1 = (1,2,3) tuple
print(f"t2 = {t2}, type = {type(t2)}")  #t2= (1,) tuple
print(f"t3 = {t3}, type = {type(t3)}")  #()  tuple
print(f"t4 = {t4}, type = {type(t4)}")  # ([4, 5, 6]) tuple

# 以下哪个会报错？
# a = (1)  都不会报错
# b = (1,)
# print(type(a))  # __int__
# print(type(b))  # ___tuple_

# ----- 题5: 元组不可变的特殊情况 [必做] -----
# 知识点: 元组不可变 vs 嵌套可变对象
t = (1, 2, 3, [4, 5])

# 以下操作哪些会报错？预测后运行验证
#t[0] = 10        # 会报错吗？____会
#t[3] = [6, 7]    # 会报错吗？____会
# t[3].append(6)   # 会报错吗？____
# print(t)         # 最终 t 是什么？___(1, 2, 3, [4, 5,6])_

# ----- 题6: 集合基础 [必做] -----
# 知识点: 集合创建、去重、空集合
# 预测以下代码的输出（注意集合是无序的）
s1 = {1, 2, 3, 2, 1}
print(f"s1 = {s1}")          # ____{1,2,3}

s2 = set([3, 4, 5, 3])
print(f"s2 = {s2}")          # ____{3,4,5}

# 空集合怎么创建？
# s3 = {}       # 这是 dict 还是 set？____dict
s3 = set()      # 这才是空 set
print(f"type({{}}) = {type({})}")
print(f"type(set()) = {type(s3)}")

# ----- 题7: 字典基础 [必做] -----
# 知识点: 字典访问、[] vs get、KeyError
# 预测以下代码的输出
d = {"name": "小明", "age": 18, "city": "北京"}

print(f"d['name']     = {d['name']}")       # ____小明
print(f"d.get('age')  = {d.get('age')}")    # ____18
print(f"d.get('score') = {d.get('score')}") # ____None
print(f"d.get('score', 0) = {d.get('score', 0)}")  # ____0，获取不存在的键，返回指定默认值0

# d['score'] 会怎样？____报错(KeyError)
# d.get('score') 会怎样？____返回None，不会创建key

# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题8: 字符串统计词频 [必做] -----
# 知识点: split、字典计数、sorted 排序
text = "the quick brown fox jumps over the lazy dog the fox"

# TODO: 统计每个单词出现的次数，按次数从高到低输出
# 提示: split() 分割 → 字典计数 → 排序
list1 = text.split(" ")  # 用 list 作为变量名会覆盖内置函数！
print(list1)
# 2. 统计每个单词出现的次数
word_count = {}  #空字典
for word in list1:
    if word in word_count:  # 最开始不存在字典中的返回flase
        word_count[word] += 1  # 以及存在的key,直接将值更新
    else:
        word_count[word] = 1  #  将列表中的元素添加为key,1作为value
# - 键不存在时， dict[key] = value 会 创建 新的键值对
# - 键存在时， dict[key] = value 会 修改 现有的值
# - dict.get(key, default) 安全获取值，键不存在返回默认值
print(f"统计结果: {word_count}")

# 3. 按次数从高到低排序
#sorted() 开始遍历word_count.items()这个列表，对每个元素调用 key 函数将列表中的每一个元素作为参数传给key函数
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)  # reverse=True，降序排列
# 字典的三个常用方法，items()、keys()、values()，keys()返回所有建，values()返回所有值
# items()返回所有键值对
# 普通函数
# def add_one(x):
#     return x + 1
# # lambda 匿名函数（等价）
# lambda x: x + 1
# # 使用
# print(add_one(5))      # 6
# print((lambda x: x + 1)(5))  # 6
print("\n按次数从高到低排序:")
for word, count in sorted_words:
    print(f"  {word}: {count}")

# ----- 题9: 字符串格式化表格 [必做] -----
# 知识点: f-string 对齐、元组解包
students = [
    ("张三", 85, 92, 78),
    ("李四", 90, 88, 95),
    ("王五", 76, 85, 80),
]

# TODO: 打印如下格式的表格（用 f-string 对齐）
# ┌──────┬──────┬──────┬──────┬──────┐
# │ 姓名 │ 语文 │ 数学 │ 英语 │ 总分 │
# ├──────┼──────┼──────┼──────┼──────┤
# │ 张三 │   85 │   92 │   78 │  255 │
# │ 李四 │   90 │   88 │   95 │  273 │
# │ 王五 │   76 │   85 │   80 │  241 │
# └──────┴──────┴──────┴──────┴──────┘
print("┌──────┬──────┬──────┬──────┬──────┐")
print("│ 姓名 │ 语文 │ 数学 │ 英语 │ 总分 │")
print("├──────┼──────┼──────┼──────┼──────┤")

for name, chinese, math, english in students:
    total = chinese + math + english
    print(f"│ {name:<4} │ {chinese:>4} │ {math:>4} │ {english:>4} │ {total:>4} │")
# # {name : <4} 左对齐，宽度4    {chinese : >4} 右对齐，宽度4 {name: ^4} 居中对齐，宽度4
# # 元组解包：将元组的每个元素分配给变量
# for name, chinese, math, english in students:
#     # name = 张三, chinese = 85, math = 92, english = 78
#     total = chinese + math + english

print("└──────┴──────┴──────┴──────┴──────┘")



# ----- 题10: 集合运算实战 [必做] -----
# 知识点: 交集、并集、差集、对称差集
# 三个班级的学生选课情况
class_a = {"Python", "Java", "C++", "Go"}
class_b = {"Python", "JavaScript", "C++", "Rust"}
class_c = {"Python", "Java", "Rust", "Swift"}

# TODO: 用集合运算回答以下问题
# 1. 三个班都选的课程（交集）
# class_d = set(itertools.chain(class_a, class_b, class_c))
# class_d = class_a.intersection(class_b, class_c) 这才是正确的
class_d = class_a & class_b & class_c
print(f"三个班的交集是:{class_d}")
# 2. 只在 A 班开设的课程（A 有但 B 和 C 没有）
# [Claude修正] 注意：这里不能直接修改 class_a，否则后面第3、4问的并集和对称差集会用到被改过的 class_a
class_a_only = class_a - class_b - class_c
print(f"只在A班开设的课程:{class_a_only}")
# class_a = (class_a -class_c) - (class_a - class_b)  从数学上来说这是不对的，因为前者留下了c++和go，后者没有留下c++但有Go
# 3. 至少在一个班开设的所有课程（并集）
class_d = class_a | class_b | class_c
print(f"三个班的并集是:{class_d}")
# 4. 恰好在两个班开设的课程
#TODO: [Claude修正] 对称差集 ^ 运算基于"出现奇数次"，三个集合时不等于"恰好在两个班"
# 正确做法：(A∩B-C) ∪ (A∩C-B) ∪ (B∩C-A)
class_d = (class_a & class_b - class_c) | (class_a & class_c - class_b) | (class_b & class_c - class_a)
print(f"恰好在两个班开设的课程是:{class_d}")

# ----- 题11: 字典嵌套 - 学生成绩管理系统 [必做] -----
# 知识点: 嵌套字典、items() 遍历、max + key
students = {
    "张三": {"语文": 85, "数学": 92, "英语": 78},
    "李四": {"语文": 90, "数学": 88, "英语": 95},
    "王五": {"语文": 76, "数学": 85, "英语": 80},
}

# TODO: 完成以下操作
# 1. 计算每个学生的总分和平均分
for key, val in students.items():
    total = sum(val.values())  # 计算总分
    avg = total / len(val)     # 计算平均分
    print(f"学生{key}的总分{total},平均分为:{avg:.2f}")
# 2. 找出数学最高分的学生
match_socer_max = 0
match_socer_max_Stutdns_name = ""
for key, val in students.items():
    if val.get("数学") > match_socer_max:
        match_socer_max = val.get("数学")
        match_socer_max_Stutdns_name = key
print(f"{match_socer_max_Stutdns_name}的数学分数最高，为{match_socer_max}")
# 使用匿名函数
max_student = max(students.items(), key=lambda x: x[1]["数学"])
print(f"{max_student[0]}的数学分数最高，为{max_student[1]['数学']}")
# 3. 计算每科的平均分
subjects = list(list(students.values())[0].keys())
print(subjects)
for subject in subjects:
    avg = sum(s[subject] for s in students.values()) / len(students)
# [x for x in iterable] 列表推导式
# (x for x in iterable) 生成器表达导式
    print(f"{subject}平均分: {avg:.1f}")


# ----- 题12: 字典推导式 [必做] -----
# 知识点: 字典推导式、zip、反转键值对
# TODO: 用字典推导式完成以下任务

# 1. 创建 {1: 1, 2: 4, 3: 9, ..., 10: 100}（数字到平方的映射）
squares = {x: x**2 for x in range(1, 101)}
print(squares)

# 2. 反转字典的键值对 {"a": 1, "b": 2, "c": 3} → {1: "a", 2: "b", 3: "c"}
squares1 = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in squares1.items()}
print(reversed_dict)

# 3. 从列表 ["a", "b", "a", "c", "b", "a", "d"] 中统计每个元素出现的次数
lst = ["a", "b", "a", "c", "b", "a", "d"]
freq = {x: lst.count(x) for x in lst}
print(freq)

# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题13: 字符串驻留（Interning） [选做] -----
# 知识点: 字符串驻留机制、is vs ==
# Python 会缓存一些字符串，使相同内容的字符串指向同一对象
a = "hello"
b = "hello"
print(f"a is b: {a is b}")       # [Claude修正] ____True（Python对短字符串自动驻留，"hello"只含字母，会被缓存为同一对象）

a = "hello world!"
b = "hello world!"
print(f"a is b: {a is b}")       # ___true_

a = "hello123"
b = "hello123"
print(f"a is b: {a is b}")       # ____true

# 规则: 只包含字母、数字、下划线的字符串会被自动驻留
# 永远用 == 比较字符串值，不要用 is

# ----- 题14: 元组 vs 列表的性能 [选做] -----
# 知识点: 不可变对象的性能优势
import time

# 创建速度对比
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
# 为什么元组更快？
# 答: ________________元组是在创建的时候一次性分配固定内存，列表会预留空间，并且小元组有缓存，列表没有，我觉得是这个原因________________

# ----- 题15: 集合的去重与顺序 [选做] -----
# 知识点: set 无序、dict.fromkeys() 保序去重
original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
deduplicated = list(set(original))
print(f"原列表: {original}")
print(f"set去重: {deduplicated}")  # 顺序不确定！

# 如果需要保持顺序去重，可以用 dict.fromkeys()
deduplicated_ordered = list(dict.fromkeys(original))
print(f"保序去重: {deduplicated_ordered}")

# 为什么 dict.fromkeys() 能保序？
# 答: ________________________________

# ----- 题16: 字典的键必须是不可变类型 [选做] -----
# 知识点: hashable、可变 vs 不可变
# 以下哪些能作为字典的键？预测后运行验证

d = {}
d[1] = "整数"           # 可以吗？____可以
d["hello"] = "字符串"    # 可以吗？____可以
d[(1, 2)] = "元组"      # [Claude修正] 可以吗？____可以（元组是不可变的，可以作为字典键）
# d[[1, 2]] = "列表"     # 可以吗？____不可以
# d[{"a": 1}] = "字典"   # 可以吗？____不可以

print(d)

# 核心规则: 能作为字典键的类型必须是 hashable（可哈希的）
# hashable = 不可变（数字、字符串、元组等）
# 可变对象（列表、字典、集合）不能作为键

# ----- 题17: 调试修复 - 找出以下代码中的 3 个 BUG [选做] -----
# 知识点: 常见错误类型

# BUG: 逻辑 - 空集合的创建方式
# my_set = {}
my_set = set()  # 这才是创建空集合的方式
print(f"我想创建集合，但实际类型是: {type(my_set)}")

# BUG: 类型 - 列表不能作为字典的键
# data = {[1, 2, 3]: "坐标"}  # 列表是可变的，不能够作为字典

# BUG: 运行时 - 元组不可变，不能直接赋值
point = (10, 20)
# point[0] = 30

# ----- 题18: 数据结构选择 [选做] -----
# 知识点: 根据场景选择合适的数据结构
# 以下场景应该用什么数据结构？说明理由

# 场景1: 存储一个班级所有学生的学号（不能重复，需要快速判断某个学号是否存在）
# 答: ____________set

# 场景2: 存储一本书的目录（章节名 -> 页码）
# 答: ____________dict

# 场景3: 存储一个 GPS 坐标 (经度, 纬度)
# 答: ____________tuple（坐标是固定的两个值，不需要修改，用元组最合适）  # [Claude补充]

# 场景4: 存储一个网页的所有超链接（可能有重复，需要按出现顺序）
# 答: ____________list

# 参考答案（运行后查看）:
print("\n--- 数据结构选择参考答案 ---")
print("场景1: set     - 去重 + O(1) 查找")
print("场景2: dict    - 键值对映射")
print("场景3: tuple   - 不可变的固定结构数据")
print("场景4: list    - 有序 + 允许重复")
