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
| **day05** | 字符串方法、元组、集合、字典、字典推导式、`dict.fromkeys()`保序去重、`max()`函数实现原理 |

#### Python 学习特色内容

- **源码分析**：包含 Python 3.13.13 源码阅读
- **实现原理**：深入理解 int()、float()、max() 等内置函数的底层实现
- **练习题**：每个章节配有练习题巩固知识
- **数据类型**：掌握数字、字符串、列表、元组、集合、字典等核心数据类型

## 📁 项目结构

```
MyStudyData/
├── 0.1、JAVA/                      # Java学习内容
│   ├── mian/                       # Java代码示例
│   │   ├── src/                    # 源代码目录
│   │   │   ├── algorithm/          # 算法练习
│   │   │   ├── cms/                # CMS系统练习
│   │   │   ├── day02-day_19/       # 每日练习代码
│   │   │   └── lib/                # 依赖库
│   │   └── JAVA学习内容/            # 笔记文档
│   └── .gitignore
│
├── 0、JAVA学习内容/                 # Java学习笔记（独立文档）
│   ├── images/                     # 配图资源
│   └── 1-23章节笔记.md             # 完整笔记系列
│
├── 1.1、Mysql/                     # MySQL学习内容
│   ├── day01/                      # day01 SQL基础
│   ├── day02/                      # day02 函数与查询
│   └── test/                       # 测试数据
│
├── 1、MySql学习内容/               # MySQL笔记
│   ├── image/                      # 配图资源
│   └── 学习文档.md
│
└── 2、pythonStudy/                  # Python学习内容
    ├── .idea/                      # IDE配置
    ├── 0.code/                     # Python代码示例
    │   ├── day01/                  # day01代码
    │   ├── day02/                  # day02代码
    │   │   ├── int_implementation.md   # int()实现原理
    │   │   └── float_implementation.md  # float()实现原理
    │   ├── day03/                  # day03代码
    │   ├── day04/                  # day04代码
    │   ├── day05/                  # day05代码
    │   │   └── max_implementation.md   # max()实现原理
    │   ├── exercises/              # 练习题
    │   └── python3.13.13/          # Python源码阅读
    │       ├── Objects/            # 对象实现（listobject.c等）
    │       ├── Include/            # 头文件
    │       ├── Python/             # Python核心
    │       └── Lib/                # 标准库
    │
    └── 1.doc/                      # Python学习文档
        ├── day01.md                # day01文档
        └── python3.13.13/          # 源码文档备份
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
- ✅ 掌握 Python 序列类型和字典操作
- 🔄 持续学习，不断积累

## 📖 Python 源码学习方法

### 推荐阅读顺序

1. **数据类型**：`listobject.c`、`longobject.c`、`floatobject.c`、`dictobject.c`
2. **字符串**：`unicodeobject.c`
3. **核心机制**：`object.c`、`typeobject.c`、`bltinmodule.c`
4. **内存管理**：`gc.c`

### 学习资源

- 源码位置：`2、pythonStudy/0.code/python3.13.13/`
- 内置函数：`Python/bltinmodule.c`
- 对象定义：`Include/cpython/*.h`
- 字典实现：`Objects/dictobject.c`

## 🎯 重点知识点

### Python 核心概念

| 概念 | 说明 |
|------|------|
| **字典保序** | Python 3.7+ 字典保持插入顺序，通过 `dk_entries` 数组实现 |
| **dict.fromkeys()** | 高效保序去重方法，利用字典键唯一性特性 |
| **max()/min()** | C 语言实现的内置函数，支持 key 参数和 default 参数 |
| **生成器表达式** | 惰性计算，节省内存，适合大数据处理 |
| **字典推导式** | 简洁创建字典的方式，支持过滤和转换 |

### Java 核心概念

| 概念 | 说明 |
|------|------|
| **面向对象** | 封装、继承、多态三大特性 |
| **集合框架** | List、Set、Map 的实现原理 |
| **ArrayList** | 动态数组实现，扩容机制 |
| **异常处理** | try-catch-finally、自定义异常 |
| **多线程** | Thread 类、Runnable 接口、线程同步 |

---

*持续更新中...*
