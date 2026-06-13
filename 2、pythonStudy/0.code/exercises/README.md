# Python 练习题

根据每日学习内容生成的配套练习，由浅入深，结合 CPython 源码深入理解。

## 目录结构

```
exercises/
├── day01_ex/
│   ├── ex01_variables.py      # 变量、f-string、进制转换、内存模型
│   └── ex02_advanced.py       # 位运算加法、类型系统、浮点陷阱
│
├── day02_ex/
│   ├── ex01_datatype.py       # 数据类型、类型转换、编码、可变/不可变
│   └── ex02_io.py             # 输入输出、格式化、print高级用法
│
├── day03_ex/
│   ├── ex01_operators.py      # 算术/逻辑/位/成员运算符、短路、优先级
│   └── ex02_control_flow.py   # if/match-case/while/for、递归、迭代器
│
├── day04_ex/
│   ├── ex01_loop.py           # range深入、嵌套循环、图形打印、质数
│   └── ex02_list.py           # 列表操作、推导式、内存机制、排序、深浅拷贝
│
├── day05_ex/
│   ├── ex01_collections.py    # 字典嵌套、max()/min()、lambda、集合运算、f-string表格
│   ├── ex01_collections_answer.py  # day05 练习答案
│   ├── ex02_strings_deep.py   # 字符串切片、方法、不可变性、编码
│   └── ex02_strings_deep_answer.py # 字符串练习答案
│
├── AI_EXERCISE_GUIDE.md       # AI 练习生成指南
└── README.md                  # 练习说明
```

## 难度分级

每个文件分三部分，逐级递进：

| 级别 | 说明 |
|------|------|
| **第一部分: 基础题** | 巩固基本语法，能独立完成 |
| **第二部分: 进阶题** | 综合运用，理解细节差异 |
| **第三部分: 深入理解题** | 探究底层原理，结合 CPython 源码 |

## 使用方式

1. 打开对应的练习文件
2. 找到 `# TODO` 标记，在下方编写代码
3. 运行文件查看结果
4. 部分题目有预测题(____)，先思考再运行验证
5. 每个文件顶部标注了相关 CPython 源码路径

## CPython 源码参考

`python3.13.13/` 目录包含 CPython v3.13.3 源码：

| 文件 | 内容 |
|------|------|
| `Objects/longobject.c` | 整数对象实现 (任意精度、小整数池) |
| `Objects/floatobject.c` | 浮点数对象 (IEEE 754) |
| `Objects/boolobject.c` | 布尔对象 (int子类) |
| `Objects/unicodeobject.c` | 字符串对象 (Unicode、驻留) |
| `Objects/listobject.c` | 列表对象 (动态数组、TimSort) |
| `Objects/rangeobject.c` | range对象 (惰性序列) |
| `Modules/_collectionsmodule.c` | deque 双端队列 |
| `Python/ceval.c` | 字节码执行引擎 |
| `Lib/` | 标准库纯Python源码 |
