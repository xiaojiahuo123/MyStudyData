# MyStudyData

这是我的个人学习仓库，系统记录了我在**编程开发**（Java、Python、MySQL、数据结构与算法、Linux/Shell）和**网络安全**（CTF、渗透测试、协议分析）两大方向上的学习笔记、示例代码、实验实操与考核解题过程。

仓库特点：

- **体系化学习**：以"天"为单位组织内容，每个主题都配有知识点文档（`1、doc`）和练习代码（`0、code`）
- **源码深读**：收录 Python 3.13.13 与 PHP 8.6 完整源码，配合底层原理笔记（`max()`/`int()`/`float()` 实现原理、引用计数、魔术方法等）
- **项目实战**：Java 客户管理系统（CMS）、Python 客户管理系统等练手项目
- **竞赛与考核**：网络安全 CTF 实操（隐写、流量分析、SQL 注入、反序列化、WebShell 后门）、结课考核解题 Writeup
- **海量刷题**：LeetCode Hot 100 题解 120+ 题（Python 实现）
- **配套资料**：尚硅谷大模型技术系列课程 PDF、JDK API 文档（1.6/1.8/17）、阿里 Java 开发手册等

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
| day01 | DDL/DML 基础（数据库与表的创建/删除/查询、数据插入与查询）、运算符汇总、模糊匹配（`LIKE`/`%`/`_`）、数据导入导出（`source`/`mysqldump`）、Navicat 可视化操作、MySQL 密码重置 |

- 课程资料：《尚硅谷大模型技术之MySQL1.0》（PDF/DOCX）
- 配套数据：`演示数据.sql`、`练习数据.sql`
- 实操练习：`题目/` 目录含 day01 全量练习与 LIKE 模糊匹配专项（均带答案版）

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
| day12 | 浅拷贝与深拷贝、迭代器（Iterable/Iterator）、生成器（yield/send）、作用域（LEGB）、闭包、装饰器 |
| day13 | 并发与并行、多进程（Process/Pool/Queue通信）、多线程（Thread/ThreadPoolExecutor/线程安全/Lock） |
| day14 | 线程安全与锁（Lock/RLock/Condition）、网络编程（UDP/TCP Socket、HTTP请求、Web服务） |
| day15 | 正则表达式（re模块、匹配规则、分组、替换）、客户管理系统（CMS）项目 |

### 4. 数据结构与算法学习

| 章节 | 内容 |
|------|------|
| day01 | 时间复杂度（Big O）、数组、链表 |
| day02 | 栈（后进先出）、队列（先进先出）、哈希表（数组+链表、哈希函数、负载因子、扩容机制） |
| day03 | 二叉搜索树（BST）实现与操作 |
| day04 | 排序算法（冒泡、选择、插入、归并、快速、堆排序）、汉诺塔 |
| day05 | 分治算法（Karatsuba算法）、动态规划（爬楼梯、子数组和、背包问题、全排列） |
| 刷题 | LeetCode Hot 100 题解（Python实现，约120题） |

#### LeetCode 题目列表

已刷题目包括但不限于：
- 数组与双指针：两数之和、盛最多水的容器、三数之和、删除有序数组中的重复项、移除元素、接雨水、合并两个有序数组
- 链表：两数相加、合并两个有序链表、合并K个升序链表、K个一组翻转链表、删除链表的倒数第N个结点、旋转链表、删除排序链表中的重复元素II、分隔链表、反转链表II、随机链表的复制、环形链表、LRU缓存
- 栈与队列：有效的括号、最长有效括号、简化路径、逆波兰表达式求值、最小栈、滑动窗口最大值
- 哈希表：字母异位词分组、最长连续序列、快乐数、同构字符串、有效的字母异位词、单词规律、赎金信
- 二叉树：二叉树的中序遍历、对称二叉树、二叉树的层序遍历、二叉树的锯齿形层序遍历、二叉树的最大深度、二叉树中的最大路径和、二叉树的右视图、翻转二叉树、二叉搜索树中第K小的元素、二叉树的最近公共祖先、二叉树的直径、二叉树的层平均值、验证二叉搜索树
- 图论：被围绕的区域、克隆图、岛屿数量、课程表、课程表II、除法求值、冗余连接
- 动态规划：最长回文子串、不同路径、最小路径和、爬楼梯、编辑距离、交错字符串、不同的子序列、单词拆分、乘积最大子数组、打家劫舍、最大正方形、最长递增子序列、零钱兑换、分割等和子集、最长公共子序列
- 贪心算法：跳跃游戏II、跳跃游戏、加油站、分发糖果、H指数
- 回溯：电话号码的字母组合、括号生成、组合总和、全排列、N皇后II、子集、单词搜索、分割回文串
- 二分查找：寻找两个正序数组的中位数、搜索旋转排序数组、在排序数组中查找元素的第一个和最后一个位置、搜索插入位置、搜索二维矩阵、寻找旋转排序数组中的最小值、寻找重复数
- 滑动窗口/子串：无重复字符的最长子串、串联所有单词的子串、最小覆盖子串、长度最小的子数组
- 堆/优先队列：数组中的第K个最大元素、数据流的中位数、查找和最小的K对数字、IPO
- Trie/前缀树：实现Trie(前缀树)、添加与搜索单词
- 矩阵：有效的数独、旋转图像、螺旋矩阵、矩阵置零、颜色分类
- 股票系列：买卖股票的最佳时机、买卖股票的最佳时机II、买卖股票的最佳时机IV
- 其他：整数反转、Pow(x,n)、二进制求和、x的平方根、只出现一次的数字、直线上最多的点数、分数到小数、多数元素、轮转数组、除自身以外数组的乘积、生命游戏

### 5. 网络安全 学习

| 章节 | 内容 |
|------|------|
| Day1 | 网络与通信安全（HTTP/HTTPS、FTP、DNS、SSH、TCP/UDP攻击防护、VLAN、ACL、Wireshark） |
| Day2 | 操作系统安全配置（Linux用户安全检测、文件权限、密码复杂度、Ubuntu用户管理） |
| Day3 | 物理和环境安全 |
| Day4 | 竞赛与攻防基础 |
| Day5 | Web安全基础2-3（SQL联合注入/报错注入/盲注、反序列化漏洞、PHP魔术方法） |
| Day6 | MISC安全基础与隐写（摩斯编码、Whitespace隐写、LSB隐写、CRC32碰撞爆破） |
| Day7 | Misc综合安全与考核 |
| Day8 | PHP序列化/反序列化深入、命令注入绕过、文件过滤绕过、空格/读取过滤绕过 |

#### 网络安全补充知识

| 文档 | 内容 |
|------|------|
| HTTP协议详解 | HTTP报文结构、请求方法、状态码、连接管理、HTTPS、安全头（X-Forwarded-For/Referer） |
| SQL注入 | 联合注入、报错注入、布尔盲注、自动化爆破脚本 |
| 反序列化漏洞 | PHP序列化格式、魔术方法（`__construct/destruct/wakeup/sleep`）、POP链 |
| 命令注入绕过 | 空格过滤（$IFS等）、文件过滤（通配符/Base64）、读取过滤（tac/head替代cat） |
| Ubuntu22.04 syslog日志 | Ubuntu系统日志配置与分析 |
| 7月7日内容 | 命令注入绕过（空格/文件/读取过滤） |
| 7月8日内容 | SQL注入、反序列化、PHP魔术方法 |
| 7月9日内容 | MISC隐写（摩斯密码、Whitespace隐写、LSB隐写）、ZIP破解（CRC32碰撞爆破、已知明文攻击、伪加密） |
| 7月10日内容 | 流量分析（Wireshark数据提取、协议分析）、WebShell后门分析（蚁剑WebShell、open_basedir绕过、Shellshock漏洞利用） |

#### 网络安全实操内容

**协议与网络实验：**
- SSH实验（路由器SSH登录配置、抓包分析）
- TCP-SYN防护实验（防火墙SYN Cookie配置）
- Telnet实验（抓包分析）
- 三层交换机VLAN路由实验（VLAN划分、三层路由）
- 基本ACL/高级ACL配置实验
- UDP Flood防护实验
- HTTP协议实验（报文构造、本地HTTP服务器/客户端、抓包分析）

**Web安全实验：**
- Session攻防实验（Session概念、Session劫持演示、Session存储机制）
- SQL注入实战（联合注入、报错注入、布尔盲注自动化）
- PHP反序列化漏洞利用（POP链构造）
- WebShell后门分析（蚁剑WebShell结构、open_basedir绕过、多策略命令执行）

**MISC安全实验：**
- Misc隐写实战（摩斯密码、Whitespace隐写、LSB隐写、图片分离）
- ZIP破解（CRC32碰撞爆破、已知明文攻击、伪加密）
- 流量分析实战（Wireshark数据提取、协议分析、FTP流量分析）

### 6. Linux与Shell 学习

| 文档 | 内容 |
|------|------|
| Linux.md | Linux系统基础 |
| shell.md | Shell脚本编程 |

### 7. NumPy 与 Pandas（规划中）

| 章节 | 内容 |
|------|------|
| - | 目录已预留（`6、numpyAndPandas/`），学习内容待补充 |

## 项目结构

```
MyStudyData/
├── 0.1、JAVA/                              # Java代码示例和笔记
│   └── mian/
│       ├── README.md / 值得一学的代码.md / SSH配置指南.md   # 项目说明文档
│       ├── src/                            # 源代码目录
│       │   ├── day02/                      # day02 基础语法练习
│       │   ├── day03/                      # day03 位运算与条件语句
│       │   ├── day04/                      # day04 循环与switch
│       │   ├── day05_teacher_code/         # day05 数组练习
│       │   ├── day06_teacher_code/         # day06 数组算法
│       │   ├── day07_teacher_code/         # day07 方法
│       │   ├── day_08/                     # day08 面向对象基础
│       │   ├── day_09/                     # day09 封装与继承
│       │   ├── day_10/                     # day10 抽象类与接口
│       │   ├── day_11/                     # day11 多态与作业
│       │   ├── day_12/ - day_19/           # day12-19 练习（异常、集合、多线程、IO、反射等）
│       │   ├── algorithm/                  # 算法实现（数组、二分查找）
│       │   └── cms/                        # 客户管理系统项目
│       ├── JAVA学习内容/                    # 笔记文档（21-23章）
│       └── lib/                            # 依赖库（JUnit4、jsoup、Lombok）
│
├── 0、JAVA学习内容/                         # Java学习笔记（独立文档）
│   └── 1-23章笔记.md                       # 完整笔记系列
│
├── 1、Mysql/                                # MySQL学习内容
│   ├── 0、code/
│   │   └── day01/                          # day01 SQL练习、MySQL密码重置方法
│   ├── 1、doc/
│       ├── day01.md                        # DDL/DML基础、运算符、模糊匹配、数据导入导出、Navicat使用
│       ├── 演示数据.sql / 练习数据.sql      # 配套练习数据
│       ├── 尚硅谷大模型技术之MySQL1.0.docx / .pdf
│       └── images/                         # 学习截图
│   └── 题目/                                 # 实操练习题（含答案）
│       ├── day01-实操练习题.md                  # day01 全量练习
│       ├── day01-实操练习题-答案.md               # 对应答案
│       ├── day01-模糊匹配练习题.md                # LIKE 模糊匹配专项
│       └── day01-模糊匹配练习题-答案.md             # 对应答案
│
├── 2、pythonStudy/                          # Python学习内容
│   ├── 0.code/                             # Python代码示例
│   │   ├── day01/                          # day01 基础语法（变量、f-string）
│   │   ├── day02/                          # day02 数据类型与转换
│   │   ├── day03/                          # day03 运算符与条件语句
│   │   ├── day04/                          # day04 循环与列表
│   │   ├── day05/                          # day05 字符串、元组、集合、字典
│   │   ├── day06/                          # day06 函数基础
│   │   ├── day07/                          # day07 作用域与高阶函数
│   │   ├── day08/                          # day08 面向对象基础
│   │   ├── day09/                          # day09 封装、继承、多态
│   │   ├── day10/                          # day10 异常处理
│   │   ├── day11/                          # day11 模块与包
│   │   ├── day12/                          # day12 迭代器、生成器、装饰器
│   │   ├── day13/                          # day13 多进程与多线程
│   │   ├── day14/                          # day14 网络编程
│   │   ├── day15/                          # day15 正则表达式与CMS项目
│   │   ├── exercises/                      # 练习题（含答案）
│   │   └── python3.13.13/                  # Python 3.13.13源码阅读
│   │       ├── Include/                    # 头文件
│   │       ├── Lib/                        # 标准库
│   │       ├── Modules/                    # C扩展模块
│   │       ├── Objects/                    # 对象实现
│   │       ├── Parser/                     # 解析器
│   │       └── Python/                     # Python核心
│   │
│   └── 1.doc/                              # Python学习文档
│       ├── day01_f-string详解.md           # day01学习笔记
│       ├── day02_进制基础与数据类型.md      # day02学习笔记
│       ├── day03_运算符与位运算.md          # day03学习笔记
│       ├── day04_序列与列表.md             # day04学习笔记
│       ├── day05_字符串方法与字典.md        # day05学习笔记
│       ├── day06_浅深拷贝与引用计数.md      # day06学习笔记
│       ├── day07_作用域与高阶函数.md        # day07学习笔记
│       ├── day08_类与面向对象.md           # day08学习笔记
│       ├── day09_封装继承与多态.md          # day09学习笔记
│       ├── day10_异常处理与上下文管理器.md   # day10学习笔记
│       ├── day12_迭代器生成器与装饰器.md    # day12学习笔记
│       ├── day13_多进程多线程与并发.md      # day13学习笔记
│       ├── day14.md                        # day14学习笔记
│       ├── day12_练习.md / day13练习.md     # day12/day13配套练习
│       ├── Process详解.md                  # 多进程详解
│       ├── Queue实现进程间通信原理.md       # 进程间通信原理
│       ├── max函数实现原理.md              # max函数实现原理
│       ├── __call__以及__init__解释.md     # 魔术方法解析
│       ├── 尚硅谷大模型技术之Python1.0.pdf  # 配套课程资料
│       ├── python3.13.13/                  # 源码文档备份
│       └── images/                         # 学习截图
│
├── 3、网络安全/                             # 网络安全学习内容
│   ├── php源码/                            # PHP 8.6 源码（Zend引擎、扩展、SAPI）
│   │   ├── Zend/                           # Zend引擎核心
│   │   ├── ext/                            # PHP扩展模块
│   │   ├── main/                           # PHP核心主程序
│   │   ├── sapi/                           # 服务器API（CGI/CLI/FPM）
│   │   └── win32/                          # Windows平台支持
│   │
│   ├── 知识点/                             # 知识点笔记
│   │   ├── Day1_网络与通信安全.md           # HTTP/HTTPS、FTP、DNS、SSH、TCP/UDP攻击防护
│   │   ├── Day2_操作系统安全配置.md         # Linux用户安全检测、文件权限、密码复杂度
│   │   ├── Day3_物理和环境安全.md           # 物理和环境安全
│   │   ├── Day4_竞赛与攻防基础.md           # 竞赛与攻防基础
│   │   ├── Day5_Web安全基础2-3.md           # SQL联合注入/报错注入/盲注、反序列化漏洞
│   │   ├── Day6_MISC安全基础与隐写.md       # 摩斯编码、Whitespace隐写、LSB隐写
│   │   ├── Day7_Misc综合安全与考核.md       # Misc综合安全与考核
│   │   ├── HTTP协议详解.md                 # HTTP报文、HTTPS、安全头
│   │   ├── Ubuntu22_04_syslog日志.md       # Ubuntu系统日志配置与分析
│   │   ├── 7月7日内容.md                   # 命令注入绕过
│   │   ├── 7月8日.md                       # SQL注入、反序列化
│   │   ├── 7月9日内容.md                   # MISC隐写、ZIP破解
│   │   ├── 7月10日.md                      # 流量分析、WebShell后门分析
│   │   ├── 总结.md                         # CTF综合总结（网络迷踪、手动构造请求、源码查阅、防盗链、后台扫描、Linux绕过等）
│   │   ├── SQL注入绕过空格过滤获取flag.md    # SQL注入绕过技巧
│   │   ├── 手动构造HTTP请求获取flag.md      # HTTP请求构造
│   │   ├── 盲注爆破.py / base64_decoder.py / Acsll.py   # 配套工具脚本
│   │   └── test.php / 0708zuoye.php 等      # 课程练习脚本
│   │
│   └── 实操/                               # 实操和实验
│       ├── 6月29日上午上课实验/             # eNSP网络实验（SSH实验、TCP-SYN防护、Telnet实验、三层交换机VLAN路由实验）
│       ├── day01/                          # 基本ACL、高级ACL实验（含eNSP拓扑）
│       ├── 第1题网络拓扑/ 第2题网络拓扑/     # 网络拓扑练习题（交换机/路由器.topo）
│       ├── dirsearch-master/               # 后台目录扫描工具
│       ├── 0706/                           # HTTP协议与Session实验
│       ├── 0709/                           # Misc综合实操（隐写、ZIP破解、编码）
│       │   ├── LSB/                        # LSB隐写术练习
│       │   ├── ZIPbaopo.py                 # ZIP爆破脚本
│       │   └── 多个压缩包文件              # 各种CTF练习题
│       ├── 0710/                           # 流量分析与WebShell实操
│       ├── 7月8日/                         # PHP反序列化实操
│       ├── 01.流量分析教学示例包.pcap       # 流量分析教学示例
│       └── 其他实验文件/                    # 各种实验数据包和工具
│
├── 4、DataStructures_andAlgorithms/         # 数据结构与算法
│   ├── 0.code/                             # 代码示例
│   │   ├── day01/                          # day01 时间复杂度、数组、链表
│   │   ├── day02/                          # day02 栈、队列、哈希表
│   │   ├── day03/                          # day03 二叉搜索树
│   │   ├── day04/                          # day04 排序算法（冒泡、选择、插入、归并、快速、堆排序、汉诺塔）
│   │   ├── day05/                          # day05 分治算法（Karatsuba）、动态规划（爬楼梯、背包、全排列）
│   │   └── Loocode/                        # LeetCode Hot 100 题解（约120题，Python实现）
│   │
│   └── 1.doc/                              # 学习文档
│       ├── day01_数组与链表基础.md          # 数组与链表学习笔记
│       ├── day02_栈、队列与哈希表.md        # day02 学习笔记
│       ├── day03_二叉搜索树.md             # day03 学习笔记
│       ├── day04.md                        # day04 学习笔记
│       ├── 二叉搜索树的简易实现.md         # BST实现文档
│       ├── 栈的简易实现.md                 # 栈的实现详解
│       ├── 哈希表的简易实现.md             # 哈希表的实现详解
│       ├── 单向链表简易实现.md             # 链表的实现详解
│       ├── 自定义数组简易实现.md           # 数组的实现详解
│       ├── 刷题.md                         # 刷题记录
│       ├── images/                         # 学习截图
│       ├── 尚硅谷大模型技术之数据结构与算法1.0.docx
│       └── 尚硅谷大模型技术之数据结构与算法1.0.pdf
│
├── 5、LiunxAndShell/                        # Linux与Shell学习
│   ├── 0、code/                            # 代码目录（预留）
│   └── 1、doc/
│       ├── Linux.md                        # Linux系统基础
│       ├── shell.md                        # Shell脚本编程
│       ├── 尚硅谷大模型技术之Linux（Ubuntu）1.0.pdf
│       └── 尚硅谷大模型技术之Shell1.0.pdf
│
├── 6、numpyAndPandas/                       # NumPy与Pandas学习（规划中，目录已预留）
│   ├── 0、code/
│   └── 1、doc/
│
├── scroe/                                   # 结课考核（CTF真题）
│   └── 1/考核/
│       ├── 题目列表.txt                     # 考核题目（8道Web + 2道附件Misc，每题10分共100分）
│       ├── 谭跃_解题.docx                   # 考核解题Writeup
│       ├── EzMisc1/                        # EzMisc1附件与解题过程（flag.jpg、audit.txt）
│       └── EzMisc2/                        # EzMisc2附件与解题过程（flag.jpg、wp.txt）
│
├── secret_file/                             # CTF题目附件（flag.zip、logo.zip、logo.png等）
├── test/                                    # 临时测试目录
├── tools/                                   # 工具目录（预留）
└── 资料/                                    # 参考资料
    ├── 0、python/                          # Python学习资料（day01-14笔记副本、《尚硅谷大模型技术之Python1.0.pdf》）
    └── JDK_api（文档）/                     # Java API文档与规范
        ├── JDK_API_1.6_zh_中文.CHM          # JDK 1.6 中文API
        ├── JAVA_API_1.8_CHS.CHM             # JDK 1.8 中文API
        ├── jdk-17.0.5-api/                  # JDK 17 官方HTML API文档
        ├── JavaSE常用API文档.md             # 常用API速查笔记
        └── 阿里Java开发手册黄山版2022.02.03V1.7.1.pdf
```

## 技术栈

- **Java**: JDK 8+、JUnit4、Lombok、jsoup、IntelliJ IDEA
- **Python**: Python 3.6+ / Python 3.13.13（源码阅读）、PyCharm
- **MySQL**: MySQL 8.0、Navicat（DDL/DML、数据导入导出）
- **PHP**: PHP 8.6（源码分析、反序列化漏洞研究）
- **数据结构与算法**: LeetCode Hot 100（Python实现，约120题）、尚硅谷数据结构与算法课程
- **网络安全**: eNSP仿真、Wireshark抓包、Burp Suite、dirsearch、华为交换机/路由器/防火墙配置、CTF竞赛
- **Linux**: Ubuntu 22.04、Shell脚本
- **NumPy/Pandas**: 规划中（目录已预留）

## 学习目标

### 编程学习
- 掌握 Java 面向对象编程（封装、继承、多态、抽象类、接口）
- 掌握 MySQL 数据库基础操作（DDL/DML、数据导入导出、Navicat 使用）
- 掌握 Python 基础语法和面向对象编程
- 掌握 Python 多进程与多线程编程（Process/Thread/Pool/线程安全/Lock）
- 掌握 Python 网络编程（UDP/TCP Socket、HTTP请求、Web服务）
- 掌握 Python 正则表达式（re模块、匹配规则、分组、替换）
- 深入理解 Python 底层实现（源码阅读）
- 掌握常见数据结构与算法（数组、链表、栈、队列、哈希表、二叉树、排序算法、动态规划）
- 掌握 LeetCode 刷题技巧（已完成约120题，覆盖主要算法类型）
- 掌握 Linux 系统基础和 Shell 脚本编程
- 计划学习 NumPy 与 Pandas 数据分析库（目录已预留）

### 网络安全学习
- 掌握常见应用层协议的工作原理（HTTP/HTTPS、FTP、DNS、SSH）
- 深入理解HTTP协议（报文结构、请求方法、状态码、连接管理、安全机制）
- 学会使用SSH安全连接网络设备
- 理解TCP/UDP攻击原理及防护方法（SYN Flood、UDP Flood）
- 掌握三层交换机VLAN配置和ACL访问控制
- 学会使用Wireshark进行流量分析
- 掌握Linux系统安全检测和加固方法
- 理解Session机制与常见攻击手法
- 掌握SQL注入原理与实战（联合注入、报错注入、布尔盲注、自动化爆破）
- 理解PHP反序列化漏洞原理（魔术方法、POP链构造）
- 掌握MISC常见题型（隐写、编码、ZIP破解、流量分析）
- 理解WebShell后门原理（open_basedir绕过、多策略命令执行、Shellshock漏洞利用）
- 掌握命令注入绕过技巧（空格过滤、文件过滤、读取过滤）
- 理解PHP源码结构（Zend引擎、扩展、SAPI）

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
