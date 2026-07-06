# MyStudyData

这是我的个人学习仓库，记录了我在编程学习和网络安全学习过程中的笔记、代码示例和项目实践。

## 学习内容

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
| day01 | 变量、f-string格式化、Hello World |
| day02 | 数字类型、进制转换、数据类型、类型转换、编码解码、输入输出、int()/float()实现原理 |
| day03 | 运算符（算术、关系、逻辑、位运算）、条件语句、循环语句 |
| day04 | 序列（列表、元组、字符串）、for循环、range()函数、嵌套循环 |
| day05 | 字符串方法、元组、集合、字典、字典推导式、max()函数实现原理 |
| day06 | 函数定义与调用、函数参数、浅拷贝与深拷贝 |
| day07 | 递归、嵌套函数、作用域（LEGB规则）、闭包、匿名函数、文件操作 |
| day08 | 面向对象基础（类定义、`__init__`、`self`）、实例方法/类方法/静态方法 |
| day09 | 封装（私有属性、`@property`）、继承（单继承、多继承、`super()`）、多态 |
| day10 | 异常处理（try/except/else/finally）、自定义异常、with语句 |
| day11 | 模块与包（`import`、`__all__`、包的结构）、面向对象综合练习 |

### 4. 网络安全 学习

| 章节 | 内容 |
|------|------|
| Day1 | 网络与通信安全（HTTP/HTTPS、FTP、DNS、SSH、TCP/UDP攻击防护、VLAN、ACL、Wireshark） |
| Day2 | 操作系统安全配置（Linux用户安全检测、文件权限、密码复杂度、Ubuntu用户管理） |
| Day3 | 物理和环境安全 |
| Day4 | 竞赛与攻防基础 |
| Day5 | Web安全基础2-3 |
| Day6 | MISC安全基础与隐写 |
| Day7 | Misc综合安全与考核 |

#### 网络安全补充知识

| 文档 | 内容 |
|------|------|
| HTTP协议详解 | HTTP报文结构、请求方法、状态码、连接管理、HTTPS、安全头 |
| Ubuntu22.04 syslog日志 | Ubuntu系统日志配置与分析 |

#### 网络安全实操内容

- SSH实验（路由器SSH登录配置、抓包分析）
- TCP-SYN防护实验（防火墙SYN Cookie配置）
- Telnet实验（抓包分析）
- 三层交换机VLAN路由实验（VLAN划分、三层路由）
- 基本ACL/高级ACL配置实验
- UDP Flood防护实验
- HTTP协议实验（报文构造、本地HTTP服务器/客户端、抓包分析）
- Session攻防实验（Session概念、Session劫持演示、Session存储机制）

## 项目结构

```
MyStudyData/
├── 0.1、JAVA/                      # Java代码示例和笔记
│   ├── mian/
│   │   ├── src/                    # 源代码目录
│   │   │   ├── algorithm/          # 算法练习
│   │   │   ├── cms/                # CMS系统练习
│   │   │   ├── day02-day_19/       # 每日练习代码
│   │   │   └── lib/                # 依赖库（lombok、jsoup、junit）
│   │   └── JAVA学习内容/            # 笔记文档
│   └── .gitignore
│
├── 0、JAVA学习内容/                 # Java学习笔记（独立文档）
│   ├── images/                     # 配图资源
│   └── 1-23章笔记.md               # 完整笔记系列
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
├── 2、pythonStudy/                  # Python学习内容
│   ├── 0.code/                     # Python代码示例
│   │   ├── day01/                  # day01 变量与格式化
│   │   ├── day02/                  # day02 数字类型、类型转换、编码解码
│   │   ├── day03/                  # day03 运算符、条件语句、循环语句
│   │   ├── day04/                  # day04 序列（列表、元组、字符串）
│   │   ├── day05/                  # day05 字符串方法、集合、字典
│   │   ├── day06/                  # day06 函数、参数、深浅拷贝
│   │   ├── day07/                  # day07 递归、闭包、匿名函数、文件操作
│   │   ├── day08/                  # day08 面向对象基础（类、self、方法）
│   │   ├── day09/                  # day09 封装、继承、多态
│   │   ├── day10/                  # day10 异常处理、自定义异常、with语句
│   │   ├── day11/                  # day11 模块与包（import、包结构、__all__）
│   │   ├── exercises/              # 练习题（day01-day11，含答案）
│   │   └── python3.13.13/          # Python 3.13.13源码阅读
│   │       ├── Objects/            # 对象实现（listobject.c、dictobject.c等）
│   │       ├── Include/            # 头文件
│   │       ├── Python/             # Python核心
│   │       ├── Lib/                # 标准库
│   │       └── Misc/               # 其他文件
│   │
│   └── 1.doc/                      # Python学习文档
│       ├── day01-day08.md          # 各章节文档（day04含列表推导式）
│       ├── max函数实现原理.md       # max()源码分析
│       └── python3.13.13/          # 源码文档备份
│
└── 3、网络安全/                     # 网络安全学习内容
    ├── 知识点/                      # 知识点笔记
    │   ├── Day1_网络与通信安全.md
    │   ├── Day2_操作系统安全配置.md
    │   ├── Day3_物理和环境安全.md
    │   ├── Day4_竞赛与攻防基础.md
    │   ├── Day5_Web安全基础2-3.md
    │   ├── Day6_MISC安全基础与隐写.md
    │   ├── Day7_Misc综合安全与考核.md
    │   ├── HTTP协议详解.md          # HTTP协议专题
    │   └── Ubuntu22_04_syslog日志.md # Ubuntu日志系统
    │
    └── 实操/                        # 实操和实验
        ├── 0706/                   # HTTP协议与Session实验
        │   ├── http/               # HTTP报文构造、本地服务器/客户端、抓包
        │   └── session/            # Session概念、劫持演示、存储机制
        ├── day01/                  # 基本ACL、高级ACL实验
        ├── 6月29日上午上课实验/      # SSH、TCP-SYN、VLAN、Telnet实验
        ├── 第1题网络拓扑/            # 交换机拓扑
        └── 第2题网络拓扑/            # 路由器拓扑
```

## 技术栈

- **Java**: JDK 8+
- **Python**: Python 3.6+ / Python 3.13.13（源码阅读）
- **MySQL**: 8.0+
- **网络安全**: eNSP仿真、Wireshark抓包、华为交换机/路由器/防火墙配置

## 学习目标

### 编程学习
- 掌握 Java 面向对象编程
- 熟练使用 MySQL 数据库
- 掌握 Python 基础语法和面向对象编程
- 深入理解 Python 底层实现（源码阅读）

### 网络安全学习
- 掌握常见应用层协议的工作原理（HTTP/HTTPS、FTP、DNS、SSH）
- 深入理解HTTP协议（报文结构、请求方法、状态码、连接管理、安全机制）
- 学会使用SSH安全连接网络设备
- 理解TCP/UDP攻击原理及防护方法（SYN Flood、UDP Flood）
- 掌握三层交换机VLAN配置和ACL访问控制
- 学会使用Wireshark进行流量分析
- 掌握Linux系统安全检测和加固方法
- 理解Session机制与常见攻击手法

## Python 源码学习方法

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

---

*持续更新中...*
