# MyStudyData

这是我的个人学习仓库，记录了我在编程学习过程中的笔记、代码示例和项目实践。

## 📚 学习内容

### 1. Java 学习

| 章节 | 内容 |
|------|------|
| 1 | 位运算符和数组 |
| 2 | 方法 |
| 3 | 面向对象基础概念 |
| 4 | 面向对象构造器和封装 |
| 5 | 对象数组与继承 |
| 6 | 抽象类 |
| 7 | 接口、比较器接口 |
| 8 | 多态 |
| 9 | 关键字总结 |
| 10 | 内部类 |
| 11 | 特殊类、增强for循环、注解 |
| 12 | 异常 |
| 13 | 常用类（包装类、数学计算、日期、数据工具类） |
| 14 | 字符串 |
| 15 | 集合与泛型 |
| 16 | Collection和Map |
| 17 | ArrayList源码分析 |
| 18 | 双向链表 |
| 19 | 迭代器 |
| 20 | Lambda表达式 |
| 21 | Java多线程 |
| 22 | IO流和网络编程 |
| 23 | 反射 |

### 2. MySQL 学习

| 章节 | 内容 |
|------|------|
| day01 | SQL基础语法 |
| day02 | 函数、约束、分组查询、多表连接查询、排序分页 |

### 3. Python 学习

| 章节 | 内容 |
|------|------|
| **day01** | 变量、f-string格式化、Hello World |
| **day02** | 数字类型、进制转换、数据类型、类型转换、编码解码、输入输出、简单计算器、int()和float()实现原理 |
| **day03** | 运算符（算术、关系、逻辑、位运算）、条件语句（if/elif/else/match-case）、循环语句（while）、位运算加法实现 |
| **day04** | 序列（列表、元组、字符串）、for循环、range()函数、嵌套循环、break/continue、列表操作、enumerate()、循环中的变量作用域 |

#### Python 学习特色内容

- **源码分析**：包含 Python 3.13.13 源码阅读
- **实现原理**：深入理解 int()、float() 等内置函数的底层实现
- **练习题**：每个章节配有练习题巩固知识
- **数据类型**：掌握数字、字符串、列表等核心数据类型

## 📁 项目结构

```
MyStudyData/
├── 0.1、JAVA/                      # Java学习内容
│   ├── mian/                       # Java代码示例
│   │   ├── src/                    # 源代码目录
│   │   └── JAVA学习内容/            # 笔记文档
│   └── JAVA学习内容/                # Java学习笔记
│
├── 1.1、Mysql/                     # MySQL学习内容
│   ├── day01/                      # day01 SQL基础
│   └── day02/                      # day02 函数与查询
│
├── 1、MySql学习内容/               # MySQL笔记
│
└── 2、pythonStudy/                  # Python学习内容
    ├── 0.code/                     # Python代码示例
    │   ├── day01/                  # day01代码
    │   ├── day02/                  # day02代码
    │   │   ├── int_implementation.md   # int()实现原理
    │   │   └── float_implementation.md  # float()实现原理
    │   ├── day03/                  # day03代码
    │   ├── day04/                  # day04代码
    │   ├── exercises/               # 练习题
    │   │   ├── day01_ex/            # day01练习题
    │   │   ├── day02_ex/            # day02练习题
    │   │   └── day03_ex/            # day03练习题
    │   └── python3.13.13/           # Python源码阅读
    │       ├── Objects/             # 对象实现（listobject.c等）
    │       ├── Include/             # 头文件
    │       ├── Python/              # Python核心
    │       └── Lib/                 # 标准库
    │
    └── 1.doc/                      # Python学习文档
        ├── day01.md                 # day01文档
        └── day02.md                 # day02文档
```

## 🛠️ 技术栈

- **Java**: JDK 8+
- **Python**: Python 3.6+ / Python 3.13.13（源码阅读）
- **MySQL**: 8.0+

## 📝 学习目标

- ✅ 掌握 Java 面向对象编程
- ✅ 熟练使用 MySQL 数据库
- ✅ 掌握 Python 基础语法和常用库
- ✅ 深入理解 Python 底层实现（源码阅读）
- 🔄 持续学习，不断积累

## 📖 Python 源码学习方法

### 推荐阅读顺序

1. **数据类型**：`listobject.c`、`longobject.c`、`floatobject.c`
2. **字符串**：`unicodeobject.c`
3. **核心机制**：`object.c`、`typeobject.c`
4. **内存管理**：`gc.c`

### 学习资源

- 源码位置：`2、pythonStudy/0.code/python3.13.13/`
- 内置函数：`Python/bltinmodule.c`
- 对象定义：`Include/cpython/*.h`

---

*持续更新中...*
