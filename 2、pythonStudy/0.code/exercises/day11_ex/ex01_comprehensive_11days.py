"""
Day11 练习1 - 11天综合练习
综合复习 day01-day11: 基础语法、容器、函数、闭包、文件、面向对象、异常、模块与包

参考源码: python3.13.13/Objects/listobject.c      (列表对象)
         python3.13.13/Objects/dictobject.c      (字典对象)
         python3.13.13/Objects/typeobject.c      (类与实例)
         python3.13.13/Lib/importlib/__init__.py (模块导入)
版本: v1.0
最后更新: 2026-07-04
"""

import copy
import json
from functools import reduce
from pathlib import Path


# ============================================================
#                      第一部分: 基础题
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 变量、类型与 f-string 格式化 [必做] -----
# 知识点: 变量绑定、type、f-string、格式控制
# 预测以下代码的输出结果

name = "Python"
day = 11
progress = day / 30

print(f"name={name}, type={type(name).__name__}")  # 此处的__name__就是只取类型名称    # ____Python，str,
print(f"day={day:03d}")                                # ____011
print(f"progress={progress:.2%}")                       # ____36.67%
print(f"{{course}} = {name}")                           # ____{course} = Python
print()

# ----- 题2: 类型转换与编码解码 [必做] -----
# 知识点: int、float、bool、encode、decode、ord、chr
# 预测以下代码的输出结果

num_text = "101"
print(int(num_text, 2))   # int(x, base=10),base是的进制格式，此处代表X是二进制，将其转换为十进制          # ____5
print(float("3.5") + 2)             # ____5.5
print(bool("False"), bool(""))      # ____false,true
print("中".encode("utf-8"))         # ____
print(chr(ord("A") + 2))            # ____

print()

# ----- 题3: 运算符、短路与控制流 [必做] -----
# 知识点: 算术运算、逻辑短路、比较链、match-case
# 预测以下代码的输出结果

x = 0
y = 10
print(y // 3, y % 3, 2 ** 3)        # ____3,1,8
print(x and (10 / x))               # ____0
print(3 < y < 20)                   # ____true

status = 2
match status:
    case 1:
        result = "待开始"
    case 2:
        result = "学习中"
    case 3:
        result = "已完成"
    case _:
        result = "未知"
print(result)                       # ____学习中

print()

# ----- 题4: 列表、切片与推导式 [必做] -----
# 知识点: 列表索引、切片、append、推导式、排序
# TODO: 根据 scores 完成以下任务
# 1. 取出前三个成绩
# 2. 取出最后两个成绩
# 3. 生成所有及格成绩(>=60)的新列表
# 4. 将成绩从高到低排序，不修改原列表

scores = [88, 59, 92, 76, 45, 100, 67]

top_three = None       # TODO
top_three = scores[:3]
last_two = None        # TODO
last_two = scores[5::1]
# last_two = scores[-2:]
passed = None          # TODO
passed = [s for s in scores if s >=60]
sorted_scores = None   # TODO
sorted_scores = copy.deepcopy(scores)
sorted_scores.sort(reverse=True)

# 验证:
print(top_three)      # 预期: [88, 59, 92]
print(last_two)       # 预期: [100, 67]
print(passed)         # 预期: [88, 92, 76, 100, 67]
print(sorted_scores)  # 预期: [100, 92, 88, 76, 67, 59, 45]
print(scores)         # 原列表不变

print("题4: 请完成列表处理")
print()

# ----- 题5: 字符串、元组、集合、字典综合 [必做] -----
# 知识点: split、strip、tuple、set、dict、get
# TODO: 统计文本中的单词次数，忽略大小写和首尾空格
# 要求:
# 1. 返回字典 {"python": 3, "java": 1, ...}
# 2. 返回去重后的单词集合
# 3. 返回按出现顺序保存的单词元组

text = " Python, java, PYTHON, go, python "


def analyze_words(raw_text):
    # TODO: 完成这里
    
    pass


# 验证:
# counts, unique_words, words_tuple = analyze_words(text)
# print(counts)        # 预期: {'python': 3, 'java': 1, 'go': 1}
# print(unique_words)  # 预期: {'python', 'java', 'go'}
# print(words_tuple)   # 预期: ('python', 'java', 'python', 'go', 'python')

print("题5: 请完成单词统计")
print()


# ============================================================
#                    第二部分: 进阶题
# ============================================================

print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题6: 学习记录解析器 [必做] -----
# 知识点: 字符串处理、列表、字典、异常处理
# TODO: 将原始记录解析为字典列表
# 输入格式: "姓名,day编号,分数,标签1|标签2"
# 要求:
# 1. day 转为 int，score 转为 int
# 2. tags 转为列表
# 3. 空行跳过
# 4. 字段数量不等于 4 时抛出 ValueError

raw_records = [
    "张三,1,88,变量|f-string",
    "李四,2,91,类型转换|输入输出",
    "",
    "张三,3,79,运算符|控制流",
    "王五,5,95,字符串|字典|集合",
]


def parse_records(lines):
    # TODO: 完成这里
    pass


# 验证:
# records = parse_records(raw_records)
# print(records[0])
# 预期: {'name': '张三', 'day': 1, 'score': 88, 'tags': ['变量', 'f-string']}

print("题6: 请完成记录解析")
print()

# ----- 题7: 按学生汇总成绩 [必做] -----
# 知识点: 嵌套字典、setdefault、max/min/sum、sorted
# TODO: 根据 records 统计每个学生的学习情况
# 返回格式:
# {
#   "张三": {"days": [1, 3], "avg": 83.5, "max": 88, "tags": {"变量", ...}},
#   ...
# }
# 要求: days 按升序排列，avg 保留 1 位小数


def summarize_by_student(records):
    # TODO: 完成这里
    pass


# 验证:
# summary = summarize_by_student(parse_records(raw_records))
# print(summary["张三"])
# 预期: {'days': [1, 3], 'avg': 83.5, 'max': 88, 'tags': {'变量', 'f-string', '运算符', '控制流'}}

print("题7: 请完成学生汇总")
print()

# ----- 题8: 函数参数与解包传参 [必做] -----
# 知识点: 默认参数、关键字参数、*args、**kwargs、解包
# TODO: 实现 make_report(title, *items, author="AI", **meta)
# 要求:
# 1. 返回一个字典
# 2. title 保存标题
# 3. items 保存为列表
# 4. author 保存作者
# 5. meta 保存额外信息


def make_report(title, *items, author="AI", **meta):
    # TODO: 完成这里
    pass


# 验证:
# args = ("day01", "day02", "day03")
# kwargs = {"author": "student", "version": "v1.0", "passed": True}
# report = make_report("阶段复习", *args, **kwargs)
# print(report)
# 预期:
# {
#   'title': '阶段复习',
#   'items': ['day01', 'day02', 'day03'],
#   'author': 'student',
#   'meta': {'version': 'v1.0', 'passed': True}
# }

print("题8: 请完成报告函数")
print()

# ----- 题9: 浅拷贝与深拷贝辨析 [必做] -----
# 知识点: copy.copy、copy.deepcopy、可变对象引用
# 预测以下代码的输出结果

plan = {"days": [1, 2, 3], "owner": "张三"}
shallow = copy.copy(plan)
deep = copy.deepcopy(plan)

shallow["days"].append(4)
deep["days"].append(5)

print(plan["days"])       # ____
print(shallow["days"])    # ____
print(deep["days"])       # ____
print(plan is shallow)    # ____
print(plan["days"] is shallow["days"])  # ____

print()

# ----- 题10: 闭包实现计分器 [必做] -----
# 知识点: 函数嵌套、闭包、nonlocal
# TODO: 实现 make_score_counter(start=0)
# 要求:
# 1. 返回 add_score(score)、get_total() 两个函数
# 2. add_score 每次累加分数并返回当前总分
# 3. get_total 返回当前总分


def make_score_counter(start=0):
    # TODO: 完成这里
    pass


# 验证:
# add_score, get_total = make_score_counter(10)
# print(add_score(5))    # 预期: 15
# print(add_score(20))   # 预期: 35
# print(get_total())     # 预期: 35
# print(add_score.__closure__)  # 能看到闭包 cell

print("题10: 请完成闭包计分器")
print()

# ----- 题11: lambda、map、filter、reduce 综合 [必做] -----
# 知识点: 匿名函数、高阶函数、迭代器、reduce
# TODO: 从 nums 中筛选偶数，平方后求和
# 要求: 必须至少使用 map、filter、reduce 中的两个

nums = [1, 2, 3, 4, 5, 6]


def even_square_sum(nums):
    # TODO: 完成这里
    pass


# 验证:
# print(even_square_sum(nums))  # 预期: 56，因为 2**2 + 4**2 + 6**2 = 56

print("题11: 请完成高阶函数练习")
print()


# ============================================================
#                    第三部分: 深入理解题
# ============================================================

print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题12: 面向对象综合 - 课程与学生 [选做] -----
# 知识点: class、__init__、实例属性、类属性、property、__str__
# TODO: 实现 Student 类
# 要求:
# 1. 类属性 school = "Python训练营"
# 2. __init__(name) 初始化 name 和空成绩列表 _scores
# 3. add_score(score) 添加成绩，score 必须在 0-100，否则抛出 ValueError
# 4. avg 属性使用 @property，返回平均分，没成绩返回 0
# 5. __str__ 返回 "张三: 83.5"


class Student:
    # TODO: 完成这里
    pass


# 验证:
# stu = Student("张三")
# stu.add_score(88)
# stu.add_score(79)
# print(stu.school)  # 预期: Python训练营
# print(stu.avg)     # 预期: 83.5
# print(stu)         # 预期: 张三: 83.5

print("题12: 请完成 Student 类")
print()

# ----- 题13: 继承、多态与鸭子类型 [选做] -----
# 知识点: 继承、方法重写、super、多态、鸭子类型
# TODO:
# 1. 实现 Exercise 基类，包含 title 属性和 run() 方法
# 2. 实现 PredictExercise、TodoExercise 两个子类，重写 run()
# 3. 实现 run_all(exercises)，调用每个对象的 run()
# 4. run_all 不检查类型，只要求对象有 run 方法


class Exercise:
    # TODO: 完成这里
    pass


class PredictExercise(Exercise):
    # TODO: 完成这里
    pass


class TodoExercise(Exercise):
    # TODO: 完成这里
    pass


def run_all(exercises):
    # TODO: 完成这里
    pass


# 验证:
# items = [PredictExercise("预测输出"), TodoExercise("实现函数")]
# print(run_all(items))
# 预期: ['预测题: 预测输出', 'TODO题: 实现函数']

print("题13: 请完成继承与多态练习")
print()

# ----- 题14: 异常、自定义异常与 with 文件操作 [选做] -----
# 知识点: try-except-else-finally、raise、自定义异常、with、json
# TODO: 实现 save_summary(summary, file_path)
# 要求:
# 1. summary 必须是非空字典，否则抛出 EmptySummaryError
# 2. 使用 with 打开文件并写入 JSON
# 3. 返回写入的文件路径字符串
# 4. 捕获 TypeError 并重新抛出 ValueError("summary 中存在无法 JSON 序列化的对象")


class EmptySummaryError(Exception):
    """汇总结果为空时抛出。"""


def save_summary(summary, file_path):
    # TODO: 完成这里
    pass


# 验证:
# summary = {"张三": {"days": [1, 3], "avg": 83.5, "max": 88}}
# path = Path("summary_demo.json")
# print(save_summary(summary, path))
# print(path.read_text(encoding="utf-8"))

print("题14: 请完成异常与文件写入")
print()

# ----- 题15: 模块、包与 __name__ 辨析 [选做] -----
# 知识点: import、from import、__all__、__name__、dir
# 回答以下问题，写在注释下方:
# 1. 为什么模块中的测试代码要放进 if __name__ == "__main__": 下面？
# TODO:
#
# 2. from module import * 会导入哪些名字？__all__ 起什么作用？
# TODO:
#
# 3. import package.module as m 与 from package import module 有什么调用差异？
# TODO:
#

print("题15: 请完成模块与包辨析")
print()

# ----- 题16: 调试修复 - 找出以下代码中的 5 个 BUG [选做] -----
# 知识点: 可变默认参数、属性封装、异常、继承、导入保护
# 要求: 不要直接运行错误代码，阅读并说明如何修复

# BUG: 逻辑 - 可变默认参数会在多次调用之间共享
def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags


# BUG: 逻辑 - property setter 没有做边界校验
class Score:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


# BUG: 运行时 - finally 中 return 会覆盖 try/except 中的 return 或异常
def risky_divide(a, b):
    try:
        return a / b
    finally:
        return 0


# BUG: 逻辑 - 子类 __init__ 没有调用父类 __init__
class BaseUser:
    def __init__(self, name):
        self.name = name


class AdminUser(BaseUser):
    def __init__(self, name, level):
        self.level = level


# BUG: 设计 - 模块被 import 时测试代码会立即执行
print("这里假设是模块测试代码，应该放到 __name__ 判断下面")

print("题16: 请修复 5 个 BUG")


# 修改记录:
# v1.0 (2026-07-04): 初始版本，覆盖 day01-day11 综合知识点
