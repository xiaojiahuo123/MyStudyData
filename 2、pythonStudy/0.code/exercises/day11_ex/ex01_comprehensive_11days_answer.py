"""
Day11 练习1 - 11天综合练习（答案版）
版本: v1.0
最后更新: 2026-07-04
"""

import copy
import json
from functools import reduce
from pathlib import Path


print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 变量、类型与 f-string 格式化 -----
name = "Python"
day = 11
progress = day / 30

print(f"name={name}, type={type(name).__name__}")      # ____ 答案: name=Python, type=str
print(f"day={day:03d}")                                # ____ 答案: day=011
print(f"progress={progress:.2%}")                       # ____ 答案: progress=36.67%
print(f"{{course}} = {name}")                           # ____ 答案: {course} = Python

print()

# ----- 题2: 类型转换与编码解码 -----
num_text = "101"
print(int(num_text, 2))             # ____ 答案: 5
print(float("3.5") + 2)             # ____ 答案: 5.5
print(bool("False"), bool(""))      # ____ 答案: True False
print("中".encode("utf-8"))         # ____ 答案: b'\xe4\xb8\xad'
print(chr(ord("A") + 2))            # ____ 答案: C

print()

# ----- 题3: 运算符、短路与控制流 -----
x = 0
y = 10
print(y // 3, y % 3, 2 ** 3)        # ____ 答案: 3 1 8
print(x and (10 / x))               # ____ 答案: 0
print(3 < y < 20)                   # ____ 答案: True

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
print(result)                       # ____ 答案: 学习中

print()

# ----- 题4: 列表、切片与推导式 -----
scores = [88, 59, 92, 76, 45, 100, 67]

top_three = scores[:3]
last_two = scores[-2:]
passed = [score for score in scores if score >= 60]
sorted_scores = sorted(scores, reverse=True)

print(top_three)
print(last_two)
print(passed)
print(sorted_scores)
print(scores)

print()

# ----- 题5: 字符串、元组、集合、字典综合 -----
text = " Python, java, PYTHON, go, python "


def analyze_words(raw_text):
    words = tuple(part.strip().lower() for part in raw_text.split(",") if part.strip())
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    unique_words = set(words)
    return counts, unique_words, words


counts, unique_words, words_tuple = analyze_words(text)
print(counts)
print(unique_words)
print(words_tuple)


print("\n" + "=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题6: 学习记录解析器 -----
raw_records = [
    "张三,1,88,变量|f-string",
    "李四,2,91,类型转换|输入输出",
    "",
    "张三,3,79,运算符|控制流",
    "王五,5,95,字符串|字典|集合",
]


def parse_records(lines):
    records = []
    for line in lines:
        if not line.strip():
            continue

        parts = [part.strip() for part in line.split(",")]
        if len(parts) != 4:
            raise ValueError(f"记录字段数量错误: {line}")

        name, day, score, tags = parts
        records.append({
            "name": name,
            "day": int(day),
            "score": int(score),
            "tags": [tag.strip() for tag in tags.split("|") if tag.strip()],
        })
    return records


records = parse_records(raw_records)
print(records[0])

print()

# ----- 题7: 按学生汇总成绩 -----
def summarize_by_student(records):
    summary = {}

    for record in records:
        item = summary.setdefault(record["name"], {
            "days": [],
            "scores": [],
            "tags": set(),
        })
        item["days"].append(record["day"])
        item["scores"].append(record["score"])
        item["tags"].update(record["tags"])

    result = {}
    for name, item in summary.items():
        result[name] = {
            "days": sorted(item["days"]),
            "avg": round(sum(item["scores"]) / len(item["scores"]), 1),
            "max": max(item["scores"]),
            "tags": item["tags"],
        }
    return result


summary = summarize_by_student(records)
print(summary["张三"])

print()

# ----- 题8: 函数参数与解包传参 -----
def make_report(title, *items, author="AI", **meta):
    return {
        "title": title,
        "items": list(items),
        "author": author,
        "meta": meta,
    }


args = ("day01", "day02", "day03")
kwargs = {"author": "student", "version": "v1.0", "passed": True}
report = make_report("阶段复习", *args, **kwargs)
print(report)

print()

# ----- 题9: 浅拷贝与深拷贝辨析 -----
plan = {"days": [1, 2, 3], "owner": "张三"}
shallow = copy.copy(plan)
deep = copy.deepcopy(plan)

shallow["days"].append(4)
deep["days"].append(5)

print(plan["days"])       # ____ 答案: [1, 2, 3, 4]
print(shallow["days"])    # ____ 答案: [1, 2, 3, 4]
print(deep["days"])       # ____ 答案: [1, 2, 3, 5]
print(plan is shallow)    # ____ 答案: False
print(plan["days"] is shallow["days"])  # ____ 答案: True

print()

# ----- 题10: 闭包实现计分器 -----
def make_score_counter(start=0):
    total = start

    def add_score(score):
        nonlocal total
        total += score
        return total

    def get_total():
        return total

    return add_score, get_total


add_score, get_total = make_score_counter(10)
print(add_score(5))
print(add_score(20))
print(get_total())
print(add_score.__closure__)

print()

# ----- 题11: lambda、map、filter、reduce 综合 -----
nums = [1, 2, 3, 4, 5, 6]


def even_square_sum(nums):
    even_nums = filter(lambda x: x % 2 == 0, nums)
    squares = map(lambda x: x ** 2, even_nums)
    return reduce(lambda total, x: total + x, squares, 0)


print(even_square_sum(nums))


print("\n" + "=" * 50)
print("第三部分: 深入理解题")
print("=" * 50)

# ----- 题12: 面向对象综合 - 课程与学生 -----
class Student:
    school = "Python训练营"

    def __init__(self, name):
        self.name = name
        self._scores = []

    def add_score(self, score):
        if not 0 <= score <= 100:
            raise ValueError("score 必须在 0-100 之间")
        self._scores.append(score)

    @property
    def avg(self):
        if not self._scores:
            return 0
        return round(sum(self._scores) / len(self._scores), 1)

    def __str__(self):
        return f"{self.name}: {self.avg}"


stu = Student("张三")
stu.add_score(88)
stu.add_score(79)
print(stu.school)
print(stu.avg)
print(stu)

print()

# ----- 题13: 继承、多态与鸭子类型 -----
class Exercise:
    def __init__(self, title):
        self.title = title

    def run(self):
        return f"练习: {self.title}"


class PredictExercise(Exercise):
    def run(self):
        return f"预测题: {self.title}"


class TodoExercise(Exercise):
    def run(self):
        return f"TODO题: {self.title}"


def run_all(exercises):
    return [exercise.run() for exercise in exercises]


items = [PredictExercise("预测输出"), TodoExercise("实现函数")]
print(run_all(items))

print()

# ----- 题14: 异常、自定义异常与 with 文件操作 -----
class EmptySummaryError(Exception):
    """汇总结果为空时抛出。"""


def save_summary(summary, file_path):
    if not isinstance(summary, dict) or not summary:
        raise EmptySummaryError("summary 必须是非空字典")

    path = Path(file_path)
    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(summary, file, ensure_ascii=False, indent=2)
    except TypeError as exc:
        raise ValueError("summary 中存在无法 JSON 序列化的对象") from exc

    return str(path)


demo_summary = {"张三": {"days": [1, 3], "avg": 83.5, "max": 88}}
demo_path = Path(r"C:\tmp\summary_demo.json")
try:
    print(save_summary(demo_summary, demo_path))
    print(demo_path.read_text(encoding="utf-8"))
except PermissionError as exc:
    print(f"当前环境不允许 Python 写入演示文件: {exc}")

print()

# ----- 题15: 模块、包与 __name__ 辨析 -----
# 1. 模块被 import 时会执行顶层代码。测试代码放进
#    if __name__ == "__main__": 下面，可以保证只有直接运行该文件时才执行测试。
#
# 2. from module import * 默认导入模块中不以下划线开头的名字。
#    如果模块定义了 __all__，则只导入 __all__ 列表中的名字。
#
# 3. import package.module as m 之后通过 m.xxx 调用。
#    from package import module 之后通过 module.xxx 调用。
#    两者通常都拿到模块对象，但绑定到当前文件中的名字不同。

print("题15答案见源码注释")

print()

# ----- 题16: 调试修复 -----
def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


class Score:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not 0 <= value <= 100:
            raise ValueError("value 必须在 0-100 之间")
        self._value = value


def risky_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        print("计算结束")


class BaseUser:
    def __init__(self, name):
        self.name = name


class AdminUser(BaseUser):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level


def _demo():
    print(add_tag("python"))
    score = Score(95)
    print(score.value)
    print(risky_divide(10, 2))
    admin = AdminUser("root", 10)
    print(admin.name, admin.level)


if __name__ == "__main__":
    _demo()


# 修改记录:
# v1.0 (2026-07-04): 初始版本，覆盖 day01-day11 综合知识点
