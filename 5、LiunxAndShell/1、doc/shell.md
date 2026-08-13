# Shell 脚本学习笔记

***

## 1. 脚本的执行方式与权限

### Shebang（#!）—— 脚本开头

```bash
#!/bin/bash
```

`#!/bin/bash` **不是必须的**，但**强烈建议加上**。

| 情况                      | 说明                                  |
| ----------------------- | ----------------------------------- |
| 有 `#!/bin/bash`         | 系统用 `/bin/bash` 解释执行                |
| 有 `#!/bin/sh`           | 系统用 `/bin/sh` 解释执行（可能是 dash）        |
| 有 `#!/usr/bin/env bash` | 从环境变量中查找 bash                       |
| 没有 shebang              | 由**当前使用的 Shell** 解释执行（不确定用哪个 Shell） |

**为什么建议加上 shebang**：

- 明确指定用哪个 Shell 解释器
- 避免不同 Shell 语法不兼容的问题
- 直接执行时系统才知道用哪个解释器

### 执行 Shell 脚本的三种方式

假设有一个脚本 `test.sh`：

```bash
#!/bin/bash
echo "Hello, World!"
```

#### 方式一：`sh 脚本路径`（不需要执行权限）

```bash
sh test.sh
sh /home/ty/test.sh
```

- 用 `sh` 解释器执行，**不需要文件有执行权限**
- 会**忽略** shebang 行，强制用 `sh` 解释

#### 方式二：`bash 脚本路径`（不需要执行权限）

```bash
bash test.sh
bash /home/ty/test.sh
```

- 用 `bash` 解释器执行，**不需要文件有执行权限**
- 会**忽略** shebang 行，强制用 `bash` 解释

#### 方式三：`./脚本路径`（需要执行权限）

```bash
./test.sh
/home/ty/test.sh
```

- 直接执行，**需要文件有执行权限**
- 系统根据 shebang 行决定用哪个解释器
- 报错 `Permission denied` 表示没有执行权限

### 三种方式对比

| 方式             | 需要执行权限 | 使用 shebang | 说明               |
| -------------- | ------ | ---------- | ---------------- |
| `sh test.sh`   | 不需要    | 忽略         | 强制用 sh 解释        |
| `bash test.sh` | 不需要    | 忽略         | 强制用 bash 解释      |
| `./test.sh`    | **需要** | 使用         | 根据 shebang 决定解释器 |

### 给脚本添加执行权限

```bash
# 查看文件权限
ls -la test.sh
# -rw-r--r-- 1 ty ty 30 Jul 21 10:00 test.sh
# ↑ 没有 x（执行）权限

# 添加执行权限
chmod +x test.sh

# 再次查看
ls -la test.sh
# -rwxr-xr-x 1 ty ty 30 Jul 21 10:00 test.sh
# ↑ 有 x 权限了

# 现在可以直接执行
./test.sh
```

### 为什么新建的脚本没有执行权限

Linux 中新建文件的默认权限由 `umask` 决定，通常为 `644`（`rw-r--r--`），**不包含执行权限**。

这是出于安全考虑：防止意外执行恶意文件。

```bash
# 查看当前 umask
umask
# 0022

# 默认权限 = 666 - 022 = 644（文件）
# 目录默认权限 = 777 - 022 = 755
```

### 完整流程演示

```bash
# 1. 创建脚本
cat > hello.sh << 'EOF'
#!/bin/bash
echo "Hello from shell script!"
echo "当前用户: $(whoami)"
echo "当前时间: $(date)"
EOF

# 2. 查看权限（没有执行权限）
ls -la hello.sh
# -rw-r--r-- 1 ty ty ... hello.sh

# 3. 方式一：用 sh 执行（不需要权限）
sh hello.sh
# Hello from shell script!

# 4. 方式二：用 bash 执行（不需要权限）
bash hello.sh
# Hello from shell script!

# 5. 方式三：直接执行（会失败）
./hello.sh
# -bash: ./hello.sh: Permission denied

# 6. 添加执行权限
chmod +x hello.sh

# 7. 直接执行（成功）
./hello.sh
# Hello from shell script!
```

### 常见问题

| 问题                  | 原因           | 解决方案                         |
| ------------------- | ------------ | ---------------------------- |
| `Permission denied` | 文件没有执行权限     | `chmod +x script.sh`         |
| `command not found` | 路径不对或没有 `./` | 使用 `./script.sh` 或完整路径       |
| `bad interpreter`   | shebang 路径错误 | 检查 `#!/bin/bash` 路径是否正确      |
| Windows 编辑的脚本报错     | 换行符是 `\r\n`  | `sed -i 's/\r$//' script.sh` |

### Shell 缩进规则

**Shell 没有缩进要求**，缩进只是为了**可读性**，不影响程序执行。

#### Shell vs Python 缩进对比

| 语言         | 缩进要求 | 说明             |
| ---------- | ---- | -------------- |
| **Shell**  | 不强制  | 缩进不影响执行，只影响可读性 |
| **Python** | 强制   | 缩进是语法的一部分，必须正确 |

#### Shell 中这三种写法都正确

**写法1：有缩进（推荐，易读）**

```bash
for file in /var/log/*.log; do
    if [ -f "$file" ]; then
        size=$(stat -c %s "$file")
        total=$(( total + size ))
    fi
done
```

**写法2：无缩进（也能执行）**

```bash
# 即使是数字，也是字符串
num=100
echo $num        # 输出: 100
echo "num is $num"  # 输出: num is 100

# 需要数学运算时，用 $(()) 或 let
result=$((num + 1))
let result=num+1
```

**写法3：乱七八糟的缩进（也能执行）**

```bash
for file in /var/log/*.log; do
if [ -f "$file" ]; then
            size=$(stat -c %s "$file")
total=$(( total + size ))
fi
          done
```

**三种写法执行结果完全相同！**

#### Python 的缩进是语法要求

```python
# Python 正确写法
for i in range(5):
    print(i)        # 必须缩进

# Python 错误写法（会报错）
for i in range(5):
print(i)            # IndentationError: expected an indented block
```

#### Shell 的语法边界靠关键字

| 结构   | 开始            | 结束     |
| ---- | ------------- | ------ |
| 条件判断 | `if ... then` | `fi`   |
| 循环   | `for ... do`  | `done` |
| 函数   | `{`           | `}`    |

#### 建议

虽然 Shell 不强制缩进，但**建议保持良好的缩进习惯**：

```bash
# 好的风格（清晰易读）
if [ -f "$file" ]; then
    if [ -r "$file" ]; then
        cat "$file"
    fi
fi

# 不好的风格（难以阅读）
if [ -f "$file" ]; then
if [ -r "$file" ]; then
cat "$file"
fi
fi
```

***

## 2. Shell 变量

### 变量定义

```bash
# 等号两边不能有空格！
name="hello"
age=18
path=/home/ty
```

| 正确             | 错误               |
| -------------- | ---------------- |
| `name="hello"` | `name = "hello"` |
| `age=18`       | `age= 18`        |

### 变量使用

```bash
# 使用变量：加 $ 前缀
echo $name
echo ${name}     # 推荐用花括号，明确边界

# 花括号的必要性
echo "My name is ${name}abc"   # 正确：helloabc
echo "My name is $nameabc"     # 错误：变量名变成 nameabc，为空
```

### 变量类型

Shell 中变量**不需要声明类型**，所有变量默认都是**字符串**。

```bash
# 即使是数字，也是字符串
num=100
echo $num        # 输出: 100
echo "num is $num"  # 输出: num is 100

# 需要数学运算时，用 $(()) 或 let
result=$((num + 1))
let result=num+1
```

### 变量赋值方式

```bash
# 1. 直接赋值
name="ty"

# 2. 命令替换：将命令输出赋值给变量
date_now=$(date)
files=$(ls /home)
kernel=$(uname -r)

# 3. 交互式赋值：从用户输入读取
read -p "请输入用户名: " username
read -s -p "请输入密码: " password    # -s 不显示输入
```

### 命令替换 $() 的执行时机

使用 `变量=$(命令)` 赋值时，命令在**赋值那一刻就执行了**，变量中存储的是命令输出的**纯文本**。

```bash
# 赋值时就执行了 ls -la，输出结果存为字符串
files=$(ls -la)

# echo 只是打印存储的文本，不会再次执行 ls -la
echo $files
```

**核心理解**：

| 阶段                | 发生了什么                 |
| ----------------- | --------------------- |
| `files=$(ls -la)` | 执行 `ls -la`，输出结果存为字符串 |
| `echo $files`     | 把那个字符串打印出来，**不再执行命令** |

> **注意**：`echo` 本身不会执行变量中的命令，它只是打印文本。

### 变量作用域

| 类型   | 说明               | 用法                              |
| ---- | ---------------- | ------------------------------- |
| 局部变量 | 仅在当前 Shell 进程中有效 | 直接赋值                            |
| 全局变量 | 子进程也可访问          | `export 变量名`                    |
| 环境变量 | 系统级全局变量          | 写入 `/etc/profile` 或 `~/.bashrc` |

```bash
# 局部变量
local_var="only here"

# 全局变量（子进程可访问）
export global_var="everywhere"

# 查看所有环境变量
env
printenv

# 查看所有变量（含局部）
set

# 删除变量
unset local_var
```

### 系统预定义变量

| 变量          | 含义                 |
| ----------- | ------------------ |
| `$HOME`     | 当前用户家目录            |
| `$USER`     | 当前用户名              |
| `$PWD`      | 当前工作目录             |
| `$SHELL`    | 当前 Shell 路径        |
| `$PATH`     | 命令搜索路径             |
| `$HOSTNAME` | 主机名                |
| `$RANDOM`   | 随机数（0-32767）       |
| `$?`        | 上一个命令的退出状态码（0表示成功） |
| `$$`        | 当前 Shell 进程的 PID   |
| `$0`        | 脚本名称               |
| `$1-$9`     | 脚本参数（第1-9个）        |
| `$#`        | 脚本参数个数             |
| `$@`        | 所有参数（独立字符串）        |
| `$*`        | 所有参数（单个字符串）        |

### 特殊变量示例

```bash
#!/bin/bash
echo "脚本名称: $0"
echo "第一个参数: $1"
echo "第二个参数: $2"
echo "参数个数: $#"
echo "所有参数: $@"
echo "上一条命令状态: $?"
echo "当前进程 PID: $$"
```

```bash
# 执行
bash test.sh arg1 arg2
# 脚本名称: test.sh
# 第一个参数: arg1
# 第二个参数: arg2
# 参数个数: 2
# 所有参数: arg1 arg2
# 上一条命令状态: 0
# 当前进程 PID: 12345
```

### $? 退出状态码详解

`$?` 保存**上一条命令**的退出状态码，每次执行新命令都会被覆盖。

| 状态码     | 含义          | 常见原因       |
| ------- | ----------- | ---------- |
| **0**   | 成功          | 命令正常执行     |
| **1**   | 一般错误        | 通用错误       |
| **2**   | 误用 Shell 命令 | 语法错误       |
| **126** | 权限不够        | 文件没有执行权限   |
| **127** | 命令未找到       | 命令拼写错误或未安装 |
| **130** | Ctrl+C 终止   | 用户手动中断     |

```bash
# 命令正常执行 → 0
ls
echo $?    # 0

# 命令未找到 → 127
lsaa
# lsaa: command not found
echo $?    # 127

# 文件没有执行权限 → 126
./test.sh
# Permission denied
echo $?    # 126
```

> **注意**：`$?` 只保存上一条命令的退出状态码，执行 `echo $?` 后 `$?` 会变成 `echo` 的状态码（0）。

### 字符串操作

```bash
str="Hello World"

# 字符串长度
echo ${#str}          # 11

# 截取子串
echo ${str:0:5}       # Hello（从位置0取5个字符）
echo ${str:6}         # World（从位置6取到末尾）

# 替换
echo ${str/World/Linux}  # Hello Linux（替换第一个匹配）
echo ${str//l/L}         # HeLLo WorLd（替换所有匹配）

# 删除
echo ${str#Hello }    # World（从左删除最短匹配）
echo ${str##*o}       # rld（从左删除最长匹配）
echo ${str%orld}      # Hello W（从右删除最短匹配）
echo ${str%%*o}       # Hell（从右删除最长匹配）

# 默认值
echo ${var:-"默认值"}  # 如果 var 未定义或为空，返回 "默认值"
echo ${var:="默认值"}  # 如果 var 未定义或为空，赋值并返回
```

### 数组

```bash
# 定义数组
arr=(apple banana cherry)

# 访问元素
echo ${arr[0]}       # apple
echo ${arr[1]}       # banana
echo ${arr[@]}       # 所有元素
echo ${#arr[@]}      # 数组长度：3

# 添加元素
arr+=(date)

# 遍历数组
for item in ${arr[@]}; do
    echo $item
done

# 关联数组（类似字典）
declare -A map
map[name]="ty"
map[age]=18
echo ${map[name]}    # ty
echo ${map[@]}       # 所有值
echo ${!map[@]}      # 所有键
```

***

## 3. read 命令 —— 用户输入

### 基本用法

```bash
read 变量名
```

从标准输入读取一行内容，赋值给指定变量。

```bash
# 基本用法
read name
echo "你输入的名字是: $name"

# 带提示信息
read -p "请输入用户名: " username
echo "用户名: $username"
```

### 常用选项

| 选项 | 说明 | 示例 |
|------|------|------|
| `-p` | 显示提示信息 | `read -p "请输入: " var` |
| `-s` | 静默模式（不显示输入） | `read -s -p "密码: " pass` |
| `-t` | 设置超时时间（秒） | `read -t 5 -p "5秒内输入: " var` |
| `-n` | 限制输入字符数 | `read -n 1 -p "按任意键: " var` |
| `-r` | 禁止反斜杠转义 | `read -r line` |
| `-a` | 读入数组 | `read -a arr` |
| `-d` | 指定结束符 | `read -d ":" var` |

### 基本示例

```bash
#!/bin/bash

# 示例1：基本输入
read -p "请输入你的名字: " name
echo "你好, $name!"

# 示例2：多个变量
read -p "请输入姓名和年龄: " name age
echo "姓名: $name, 年龄: $age"

# 示例3：密码输入（不显示）
read -s -p "请输入密码: " password
echo ""
echo "密码已设置"
```

### 超时处理

```bash
#!/bin/bash

# 设置5秒超时
if read -t 5 -p "请在5秒内输入 (超时将使用默认值): " input; then
    echo "你输入了: $input"
else
    echo ""
    echo "超时，使用默认值"
    input="default"
fi
```

### 单字符输入

```bash
#!/bin/bash

# 只读取一个字符
read -n 1 -p "确认继续? (y/n): " confirm
echo ""

if [ "$confirm" = "y" ]; then
    echo "继续执行..."
else
    echo "已取消"
fi
```

### 读取数组

```bash
#!/bin/bash

# 将输入读入数组
read -a fruits -p "请输入水果 (空格分隔): "

echo "你输入的水果:"
for fruit in "${fruits[@]}"; do
    echo "- $fruit"
done
```

### 读取多行

```bash
#!/bin/bash

# 方式1：使用 while read 循环
echo "请输入多行内容 (输入空行结束):"
while read -r line; do
    [ -z "$line" ] && break
    echo "读取: $line"
done

# 方式2：从文件读取
while IFS= read -r line; do
    echo "行: $line"
done < /etc/hosts
```

### 管道与重定向

```bash
#!/bin/bash

# 从管道读取
echo "hello" | read var
# 注意：管道中的 read 在子 Shell 中执行，变量不会传递到父 Shell

# 正确方式：使用进程替换
read var < <(echo "hello")
echo $var  # hello

# 从文件读取
read line < /etc/hostname
echo "主机名: $line"
```

### IFS 分隔符

```bash
#!/bin/bash

# 默认分隔符是空格/制表符/换行符
read -p "输入姓名 年龄 城市: " name age city
echo "$name, $age岁, $city"

# 自定义分隔符
IFS=':' read -p "输入 user:pass: " user pass
echo "用户: $user, 密码: $pass"

# 从 /etc/passwd 读取
IFS=':' read username _ uid gid _ home shell < /etc/passwd
echo "用户名: $username, UID: $uid, Shell: $shell"
```

### 实用示例

#### 确认提示

```bash
#!/bin/bash

confirm() {
    read -p "$1 (y/n): " -n 1 -r
    echo ""
    [[ $REPLY =~ ^[Yy]$ ]]
}

if confirm "确定要删除文件吗?"; then
    echo "删除文件..."
else
    echo "已取消"
fi
```

#### 菜单选择

```bash
#!/bin/bash

echo "请选择操作:"
echo "1) 查看文件"
echo "2) 创建文件"
echo "3) 删除文件"
echo "4) 退出"

read -p "请输入选项 (1-4): " choice

case $choice in
    1) echo "查看文件" ;;
    2) echo "创建文件" ;;
    3) echo "删除文件" ;;
    4) echo "退出" ;;
    *) echo "无效选项" ;;
esac
```

#### 密码验证

```bash
#!/bin/bash

max_attempts=3
attempt=0

while [ $attempt -lt $max_attempts ]; do
    read -s -p "请输入密码: " password
    echo ""

    if [ "$password" = "secret" ]; then
        echo "登录成功!"
        break
    else
        attempt=$((attempt + 1))
        echo "密码错误，还剩 $((max_attempts - attempt)) 次机会"
    fi
done

if [ $attempt -eq $max_attempts ]; then
    echo "登录失败，账户已锁定"
    exit 1
fi
```

#### 读取配置文件

```bash
#!/bin/bash

# 读取 key=value 格式的配置文件
while IFS='=' read -r key value; do
    # 跳过注释和空行
    [[ $key =~ ^#.*$ || -z $key ]] && continue

    # 去除空格
    key=$(echo $key | xargs)
    value=$(echo $value | xargs)

    echo "配置: $key = $value"
    # 可以用 declare 或 export 设置变量
    declare "$key=$value"
done < config.conf
```

### 常见错误

| 错误写法 | 正确写法 | 原因 |
|----------|----------|------|
| `echo "输入" \| read var` | `read var < <(echo "输入")` | 管道中 read 在子 Shell |
| `read -p "提示" var1 var2` | 用空格分隔输入 | 多个变量用空格分隔输入 |
| `read $var` | `read var` | read 后不加 $ |
| `read -t 0` | `read -t 1` | 超时不能为 0 |

### 注意事项

```bash
# 1. 管道中的 read 在子 Shell 执行
echo "test" | read var
echo $var  # 空！变量在子 Shell 中

# 解决方案：使用进程替换
read var < <(echo "test")
echo $var  # test

# 2. read 默认会去除行尾换行符
read line < file.txt
echo "$line"  # 没有尾部换行

# 3. -r 选项防止反斜杠转义
read -r line  # 输入 a\tb 会保留为 a\tb
read line     # 输入 a\tb 会转义为 a(tab)b

# 4. 空输入
read -p "输入: " var
if [ -z "$var" ]; then
    echo "输入为空"
fi
```

***

## 4. Shell 算术运算符

### 算术运算方式

Shell 中进行数学运算有多种方式：

| 方式       | 语法                           | 说明                |
| -------- | ---------------------------- | ----------------- |
| `$(( ))` | `$(( expression ))`          | **推荐**，最常用，支持整数运算 |
| `let`    | `let expression`             | 内置命令，等号两边不能有空格    |
| `expr`   | `expr expression`            | 外部命令，操作符两边必须有空格   |
| `bc`     | `echo "scale=2; 10/3" \| bc` | 支持浮点数运算           |

### 基本算术运算符

| 运算符  | 说明     | 示例              | 结果 |
| ---- | ------ | --------------- | -- |
| `+`  | 加法     | `$(( 10 + 3 ))` | 13 |
| `-`  | 减法     | `$(( 10 - 3 ))` | 7  |
| `*`  | 乘法     | `$(( 10 * 3 ))` | 30 |
| `/`  | 整除（取商） | `$(( 10 / 3 ))` | 3  |
| `%`  | 取模（取余） | `$(( 10 % 3 ))` | 1  |
| `**` | 幂运算    | `$(( 2 ** 3 ))` | 8  |

```bash
# 使用 $(( )) 进行运算
a=10
b=3

echo $(( a + b ))    # 13
echo $(( a - b ))    # 7
echo $(( a * b ))    # 30
echo $(( a / b ))    # 3（整除）
echo $(( a % b ))    # 1
echo $(( a ** 2 ))   # 100

# 赋值写法
result=$(( a + b ))
echo $result         # 13
```

### 复合赋值运算符

| 运算符  | 说明 | 等价写法             |
| ---- | -- | ---------------- |
| `+=` | 加等 | `a=$(( a + b ))` |
| `-=` | 减等 | `a=$(( a - b ))` |
| `*=` | 乘等 | `a=$(( a * b ))` |
| `/=` | 除等 | `a=$(( a / b ))` |
| `%=` | 模等 | `a=$(( a % b ))` |

```bash
a=10

(( a += 5 ))    # a = a + 5 = 15
echo $a         # 15

(( a -= 3 ))    # a = a - 3 = 12
echo $a         # 12

(( a *= 2 ))    # a = a * 2 = 24
echo $a         # 24

(( a /= 4 ))    # a = a / 4 = 6
echo $a         # 6

(( a %= 4 ))    # a = a % 4 = 2
echo $a         # 2
```

### 自增自减运算符

| 运算符   | 说明   | 示例                     |
| ----- | ---- | ---------------------- |
| `++`  | 自增1  | `(( a++ ))` 后置，先返回值再加1 |
| `--`  | 自减1  | `(( a-- ))` 后置，先返回值再减1 |
| `++a` | 前置自增 | `(( ++a ))` 先加1再返回值    |
| `--a` | 前置自减 | `(( --a ))` 先减1再返回值    |

```bash
a=5

# 后置自增：先使用当前值，再加1
echo $(( a++ ))    # 输出 5，然后 a 变成 6
echo $a            # 6

# 前置自增：先加1，再使用新值
echo $(( ++a ))    # a 先变成 7，输出 7
echo $a            # 7

# 后置自减
echo $(( a-- ))    # 输出 7，然后 a 变成 6
echo $a            # 6

# 前置自减
echo $(( --a ))    # a 先变成 5，输出 5
echo $a            # 5
```

### 比较运算符（用于条件判断）

| 运算符  | 说明   | 示例             |
| ---- | ---- | -------------- |
| `==` | 等于   | `(( a == b ))` |
| `!=` | 不等于  | `(( a != b ))` |
| `>`  | 大于   | `(( a > b ))`  |
| `<`  | 小于   | `(( a < b ))`  |
| `>=` | 大于等于 | `(( a >= b ))` |
| `<=` | 小于等于 | `(( a <= b ))` |

```bash
a=10
b=20

# 在条件判断中使用
if (( a > b )); then
    echo "$a 大于 $b"
else
    echo "$a 小于等于 $b"
fi
# 输出: 10 小于等于 20

# 三元运算符
max=$(( a > b ? a : b ))
echo "较大值是: $max"    # 20
```

### 逻辑运算符

| 运算符    | 说明  | 示例                        |
| ------ | --- | ------------------------- |
| `&&`   | 逻辑与 | `(( a > 5 && b < 30 ))`   |
| `\|\|` | 逻辑或 | `(( a > 5 \|\| b < 10 ))` |
| `!`    | 逻辑非 | `(( !0 ))` 结果为 1          |

```bash
a=10
b=20

# 逻辑与
if (( a > 5 && b < 30 )); then
    echo "条件成立"    # 输出
fi

# 逻辑或
if (( a > 15 || b < 30 )); then
    echo "至少一个条件成立"    # 输出
fi

# 逻辑非
(( !0 ))    # 结果为 1（真）
(( !1 ))    # 结果为 0（假）
```

### 位运算符

| 运算符  | 说明   | 示例              | 结果 |
| ---- | ---- | --------------- | -- |
| `&`  | 按位与  | `$(( 5 & 3 ))`  | 1  |
| `\|` | 按位或  | `$(( 5 \| 3 ))` | 7  |
| `^`  | 按位异或 | `$(( 5 ^ 3 ))`  | 6  |
| `~`  | 按位取反 | `$(( ~5 ))`     | -6 |
| `<<` | 左移   | `$(( 5 << 1 ))` | 10 |
| `>>` | 右移   | `$(( 5 >> 1 ))` | 2  |

```bash
# 5 的二进制: 101
# 3 的二进制: 011

echo $(( 5 & 3 ))    # 1  (001)
echo $(( 5 | 3 ))    # 7  (111)
echo $(( 5 ^ 3 ))    # 6  (110)
echo $(( ~5 ))       # -6 (补码)
echo $(( 5 << 1 ))   # 10 (1010)
echo $(( 5 >> 1 ))   # 2  (10)
```

**按位取反** **`~`** **的计算公式**：`~x = -(x + 1)`

```bash
~5 = -(5 + 1) = -6
~(-6) = -(-6 + 1) = -(-5) = 5
```

### 不同运算方式的对比

#### $(( )) 方式（推荐）

```bash
a=10
b=3

# 直接运算
echo $(( a + b ))    # 13

# 变量赋值
result=$(( a + b ))

# 可以省略 $ 符号（在 (( )) 内）
(( result = a + b ))

# 支持复合语句
(( a++, b-- ))
```

#### let 方式

```bash
let result=10+3
echo $result    # 13

let a=5
let a=a+1
echo $a         # 6

# 等号两边不能有空格
let a = a + 1   # 错误！
let a=a+1       # 正确

# 可以省略引号
let "a = a + 1"  # 也可以
```

#### expr 方式（较旧）

```bash
# 操作符两边必须有空格
result=$(expr 10 + 3)
echo $result    # 13

# 乘法需要转义
result=$(expr 10 \* 3)
echo $result    # 30

# 比较操作
expr 10 \> 3    # 输出 1（真）
expr 10 \< 3    # 输出 0（假）
```

#### bc 方式（支持浮点数）

```bash
# 基本浮点运算
echo "10 / 3" | bc              # 3（整数）
echo "scale=2; 10 / 3" | bc     # 3.33

# 设置精度
echo "scale=4; 22 / 7" | bc     # 3.1428

# 复杂运算
echo "scale=2; (10 + 3) * 2" | bc    # 26.00

# 平方根
echo "scale=4; sqrt(2)" | bc    # 1.4142

# 变量使用
a=10
b=3
result=$(echo "scale=2; $a / $b" | bc)
echo $result    # 3.33
```

### 实用示例

#### 计算文件大小总和

```bash
#!/bin/bash
total=0

for file in /var/log/*.log; do
    if [ -f "$file" ]; then
    #-f 是 文件测试运算符 ，用于判断路径是否为 普通文件，检查 $file 是否是一个普通文件
    #每个file都是/var/log目录下后缀为.log的文件
        size=$(stat -c %s "$file")
        #stat获取文件状态信息 -c指定输出格式  %s格式化选项，这个%s是stat的参数，还有其他的

        total=$(( total + size ))
    fi  # fi 是 if 语句的结束标志 ，表示 if 代码块的结束
done

echo "日志文件总大小: $(( total / 1024 )) KB"

#shell中for 循环结构
for 变量 in 列表; do
    命令
done
```

**stat 常用格式选项**：

| 格式   | 说明         | 示例输出                  |
| ---- | ---------- | --------------------- |
| `%s` | 文件大小（字节）   | `1048576`             |
| `%n` | 文件名        | `syslog`              |
| `%U` | 所有者用户名     | `root`                |
| `%G` | 所有者组名      | `adm`                 |
| `%a` | 访问权限（八进制）  | `644`                 |
| `%A` | 访问权限（可读格式） | `-rw-r--r--`          |
| `%y` | 最后修改时间     | `2024-01-15 10:30:00` |

```bash
# 示例用法
stat -c %s /var/log/syslog      # 获取文件大小
stat -c %U /var/log/syslog      # 获取文件所有者
stat -c %A /var/log/syslog      # 获取权限格式
```

#### 简易计算器

```bash
#!/bin/bash
read -p "请输入第一个数: " num1
read -p "请输入运算符 (+ - * /): " op
read -p "请输入第二个数: " num2

case $op in
    +) result=$(( num1 + num2 )) ;;
    -) result=$(( num1 - num2 )) ;;
    \*) result=$(( num1 * num2 )) ;;
    /) 
        if [ $num2 -eq 0 ]; then
            echo "错误: 除数不能为0"
            exit 1
        fi
        result=$(( num1 / num2 ))
        ;;
    *)
        echo "错误: 不支持的运算符"
        exit 1
        ;;
esac

echo "$num1 $op $num2 = $result"
```

#### 循环中的计数器

```bash
#!/bin/bash
sum=0

for i in $(seq 1 100); do
    (( sum += i ))
done

echo "1到100的和: $sum"    # 5050
```

#### 进制转换

```bash
# 十进制转其他进制
echo "obase=2; 255" | bc     # 11111111 (二进制)
echo "obase=8; 255" | bc     # 377 (八进制)
echo "obase=16; 255" | bc    # FF (十六进制)

# 其他进制转十进制
echo $(( 2#11111111 ))       # 255 (二进制转十进制)
echo $(( 8#377 ))            # 255 (八进制转十进制)
echo $(( 16#FF ))            # 255 (十六进制转十进制)
```

### 常见错误

| 错误写法            | 正确写法           | 原因            |
| --------------- | -------------- | ------------- |
| `$a + $b`       | `$(( a + b ))` | 直接写会当成字符串     |
| `expr 10*3`     | `expr 10 \* 3` | 乘法需要转义        |
| `let a = 1`     | `let a=1`      | let 等号两边不能有空格 |
| `$(( 10 / 0 ))` | 需要先判断除数        | 除以0会报错        |

***

## 5. Shell 条件判断

### 条件判断概述

Shell 中的条件判断用于根据不同条件执行不同的代码逻辑，是脚本编程的核心功能之一。

**主要语法形式**：

- `test` 命令
- `[ ]` 单括号（推荐）
- `[[ ]]` 双括号（Bash 扩展，功能更强）

### test 命令

`test` 是 Shell 内置命令，用于检查条件是否成立。

```bash
# 基本语法
test expression

# 示例
test -f /etc/passwd && echo "文件存在" || echo "文件不存在"
# 输出: 文件存在

test 10 -gt 5 && echo "10 大于 5" || echo "10 不大于 5"
# 输出: 10 大于 5
```

### \[ ] 单括号（推荐使用）

`[ ]` 是 `test` 命令的简写形式，**注意方括号内部必须有空格**。

```bash
# 基本语法
[ expression ]

# 正确写法
[ -f /etc/passwd ] && echo "文件存在"

# 错误写法（缺少空格）
[-f /etc/passwd]  # 报错

# 变量最好加引号，防止空变量导致语法错误
[ -f "$file" ] && echo "文件存在"
```

### \[\[ ]] 双括号（Bash 扩展）

`[[ ]]` 是 Bash 的扩展语法，比 `[ ]` 更强大，**推荐在 Bash 中使用**。

```bash
# 支持正则表达式
[[ "hello" =~ ^h ]] && echo "以 h 开头"

# 支持模式匹配
[[ "file.txt" == *.txt ]] && echo "是文本文件"

# 不需要对变量加引号（但仍建议加）
[[ -f $file ]] && echo "文件存在"

# 支持逻辑运算符 && || 直接使用
[[ -f "file1" && -f "file2" ]] && echo "两个文件都存在"
```

**\[ ] 与 \[\[ ]] 对比**：

| 特性    | `[ ]`        | `[[ ]]`         |
| ----- | ------------ | --------------- |
| 兼容性   | 所有 Shell     | 仅 Bash/Zsh      |
| 变量引用  | 必须加引号        | 可省略引号           |
| 正则表达式 | 不支持          | 支持 `=~`         |
| 模式匹配  | 不支持          | 支持 `==` 通配符     |
| 逻辑运算  | 需要 `-a` `-o` | 直接用 `&&` `\|\|` |

### 文件测试运算符

| 运算符  | 说明      | 示例               |
| ---- | ------- | ---------------- |
| `-f` | 是否为普通文件 | `[ -f "$file" ]` |
| `-d` | 是否为目录   | `[ -d "$dir" ]`  |
| `-e` | 是否存在    | `[ -e "$path" ]` |
| `-r` | 是否可读    | `[ -r "$file" ]` |
| `-w` | 是否可写    | `[ -w "$file" ]` |
| `-x` | 是否可执行   | `[ -x "$file" ]` |
| `-s` | 文件是否非空  | `[ -s "$file" ]` |
| `-L` | 是否为符号链接 | `[ -L "$file" ]` |
| `-b` | 是否为块设备  | `[ -b "$file" ]` |
| `-c` | 是否为字符设备 | `[ -c "$file" ]` |

```bash
#!/bin/bash

file="/etc/passwd"

if [ -f "$file" ]; then
    echo "$file 是普通文件"
fi

if [ -r "$file" ]; then
    echo "$file 可读"
fi

if [ -w "$file" ]; then
    echo "$file 可写"
fi

# 组合检查
if [ -f "$file" ] && [ -r "$file" ]; then
    echo "$file 是可读的普通文件"
fi
```

### 字符串比较运算符

| 运算符        | 说明         | 示例                       |
| ---------- | ---------- | ------------------------ |
| `=` 或 `==` | 字符串相等      | `[ "$str1" = "$str2" ]`  |
| `!=`       | 字符串不等      | `[ "$str1" != "$str2" ]` |
| `-z`       | 字符串为空      | `[ -z "$str" ]`          |
| `-n`       | 字符串非空      | `[ -n "$str" ]`          |
| `<`        | 字典序小于（需转义） | `[ "$str1" \< "$str2" ]` |
| `>`        | 字典序大于（需转义） | `[ "$str1" \> "$str2" ]` |

```bash
#!/bin/bash

str1="hello"
str2="world"
str3="hello"

# 字符串比较
if [ "$str1" = "$str3" ]; then
    echo "str1 和 str3 相等"
fi

# 检查字符串是否为空
if [ -z "$str1" ]; then
    echo "str1 为空"
else
    echo "str1 不为空"
fi

# 字典序比较（在 [ ] 中需要转义）
if [ "$str1" \< "$str2" ]; then
    echo "$str1 排在 $str2 前面"
fi

# 在 [[ ]] 中不需要转义
if [[ "$str1" < "$str2" ]]; then
    echo "$str1 排在 $str2 前面"
fi
```

**重要提醒**：

- 字符串变量比较时，**变量必须用双引号括起来**
- 防止变量为空时导致语法错误：`[ "$var" = "value" ]`

```bash
# 错误示例（变量为空时会报错）
var=""
if [ $var = "hello" ]; then  # 错误！变成 [ = "hello" ]
    echo "相等"
fi

# 正确示例
var=""
if [ "$var" = "hello" ]; then  # 正确！变成 [ "" = "hello" ]
    echo "相等"
fi
```

### 数值比较运算符

| 运算符   | 说明                     | 示例                  |
| ----- | ---------------------- | ------------------- |
| `-eq` | 等于（equal）              | `[ "$a" -eq "$b" ]` |
| `-ne` | 不等于（not equal）         | `[ "$a" -ne "$b" ]` |
| `-gt` | 大于（greater than）       | `[ "$a" -gt "$b" ]` |
| `-lt` | 小于（less than）          | `[ "$a" -lt "$b" ]` |
| `-ge` | 大于等于（greater or equal） | `[ "$a" -ge "$b" ]` |
| `-le` | 小于等于（less or equal）    | `[ "$a" -le "$b" ]` |

```bash
#!/bin/bash

a=10
b=20

if [ "$a" -eq "$b" ]; then
    echo "$a 等于 $b"
elif [ "$a" -gt "$b" ]; then
    echo "$a 大于 $b"
else
    echo "$a 小于 $b"
fi
# 输出: 10 小于 20

# 使用 (( )) 进行数值比较（更简洁）
if (( a > b )); then
    echo "$a 大于 $b"
else
    echo "$a 小于等于 $b"
fi
```

**数值比较注意事项**：

- 使用 `[ ]` 时，必须用 `-eq`、`-gt` 等运算符，不能用 `==`、`>`
- 使用 `(( ))` 时，可以直接用 `==`、`>` 等数学运算符
- 变量最好用双引号括起来

```bash
# 错误示例
a=10
b=20
if [ "$a" > "$b" ]; then  # 错误！> 是重定向，不是比较
    echo "$a 大于 $b"
fi

# 正确示例
if [ "$a" -gt "$b" ]; then
    echo "$a 大于 $b"
fi
```

### 逻辑运算符

#### 在 \[ ] 中使用

| 运算符  | 说明       | 示例                              |
| ---- | -------- | ------------------------------- |
| `-a` | 逻辑与（AND） | `[ "$a" -gt 5 -a "$b" -lt 10 ]` |
| `-o` | 逻辑或（OR）  | `[ "$a" -gt 5 -o "$b" -lt 10 ]` |
| `!`  | 逻辑非（NOT） | `[ ! -f "$file" ]`              |

```bash
#!/bin/bash

a=10
b=5
file="/etc/passwd"

# 逻辑与
if [ "$a" -gt 5 -a "$b" -lt 10 ]; then
    echo "两个条件都成立"
fi

# 逻辑或
if [ "$a" -gt 15 -o "$b" -lt 10 ]; then
    echo "至少一个条件成立"
fi

# 逻辑非
if [ ! -f "$file" ]; then
    echo "$file 不是文件"
fi
```

#### 在 \[\[ ]] 中使用

```bash
# 直接使用 && || ! 运算符
if [[ "$a" -gt 5 && "$b" -lt 10 ]]; then
    echo "两个条件都成立"
fi

if [[ "$a" -gt 15 || "$b" -lt 10 ]]; then
    echo "至少一个条件成立"
fi

if [[ ! -f "$file" ]]; then
    echo "$file 不是文件"
fi
```

#### 使用括号分组

```bash
# 使用括号分组（需要转义或使用 [[ ]]）
if [ \( "$a" -gt 5 -a "$a" -lt 20 \) -o "$b" -eq 0 ]; then
    echo "条件成立"
fi

# 在 [[ ]] 中更清晰
if [[ ( "$a" -gt 5 && "$a" -lt 20 ) || "$b" -eq 0 ]]; then
    echo "条件成立"
fi
```

### if 语句

#### 基本语法

```bash
if [ 条件 ]; then
    命令
fi
```

#### if-else 语法

```bash
if [ 条件 ]; then
    命令1
else
    命令2
fi
```

#### if-elif-else 语法

```bash
if [ 条件1 ]; then
    命令1
elif [ 条件2 ]; then
    命令2
elif [ 条件3 ]; then
    命令3
else
    命令4
fi
```

```bash
#!/bin/bash

score=85

if [ "$score" -ge 90 ]; then
    echo "优秀"
elif [ "$score" -ge 80 ]; then
    echo "良好"
elif [ "$score" -ge 70 ]; then
    echo "中等"
elif [ "$score" -ge 60 ]; then
    echo "及格"
else
    echo "不及格"
fi
# 输出: 良好
```

### case 语句

`case` 语句用于多条件匹配，比多个 `if-elif` 更清晰。

#### 基本语法

```bash
case 变量 in
    模式1)
        命令1
        ;;
    模式2)
        命令2
        ;;
    模式3)
        命令3
        ;;
    *)
        默认命令
        ;;
esac
```

```bash
#!/bin/bash

read -p "请输入一个字符: " char

case "$char" in
    [a-z])
        echo "小写字母"
        ;;
    [A-Z])
        echo "大写字母"
        ;;
    [0-9])
        echo "数字"
        ;;
    *)
        echo "其他字符"
        ;;
esac
```

#### 模式匹配特性

```bash
#!/bin/bash

file="document.txt"

case "$file" in
    *.txt)
        echo "文本文件"
        ;;
    *.jpg|*.png|*.gif)
        echo "图片文件"
        ;;
    *.sh)
        echo "Shell 脚本"
        ;;
    *)
        echo "未知类型"
        ;;
esac
# 输出: 文本文件
```

#### 使用 | 分隔多个模式

```bash
#!/bin/bash

day="Saturday"

case "$day" in
    Monday|Tuesday|Wednesday|Thursday|Friday)
        echo "工作日"
        ;;
    Saturday|Sunday)
        echo "周末"
        ;;
    *)
        echo "无效日期"
        ;;
esac
# 输出: 周末
```

### 条件判断实用示例

#### 检查文件是否存在

```bash
#!/bin/bash

file="/etc/passwd"

if [ -f "$file" ]; then
    echo "$file 存在"
    if [ -r "$file" ]; then
        echo "$file 可读"
    fi
else
    echo "$file 不存在"
fi
```

#### 检查目录是否存在

```bash
#!/bin/bash

dir="/home/user/documents"

if [ ! -d "$dir" ]; then
    echo "目录不存在，正在创建..."
    mkdir -p "$dir"
else
    echo "目录已存在"
fi
```

#### 检查用户输入

```bash
#!/bin/bash

read -p "请输入用户名: " username

if [ -z "$username" ]; then
    echo "错误: 用户名不能为空"
    exit 1
fi

if [ ${#username} -lt 3 ]; then
    echo "错误: 用户名长度至少3个字符"
    exit 1
fi

echo "用户名: $username"
```

#### 检查命令是否存在

```bash
#!/bin/bash

if command -v git &> /dev/null; then
    echo "Git 已安装"
    git --version
else
    echo "Git 未安装"
fi

if command -v docker &> /dev/null; then
    echo "Docker 已安装"
else
    echo "Docker 未安装"
fi
```

#### 检查进程是否存在

```bash
#!/bin/bash

process_name="nginx"

if pgrep -x "$process_name" > /dev/null; then
    echo "$process_name 正在运行"
else
    echo "$process_name 未运行"
fi
```

#### 检查网络连接

```bash
#!/bin/bash

host="google.com"

if ping -c 1 "$host" &> /dev/null; then
    echo "网络连接正常"
else
    echo "网络连接失败"
fi
```

### 常见错误与解决方案

| 错误写法                 | 正确写法                   | 原因                            |
| -------------------- | ---------------------- | ----------------------------- |
| `[ $var = "value" ]` | `[ "$var" = "value" ]` | 变量为空时语法错误                     |
| `[ $a > $b ]`        | `[ "$a" -gt "$b" ]`    | `>` 是重定向，不是比较                 |
| `[ $a == $b ]`       | `[ "$a" = "$b" ]`      | `[ ]` 中用 `=`，`[[ ]]` 中可用 `==` |
| `[ -f $file ]`       | `[ -f "$file" ]`       | 文件名含空格时出错                     |
| `if [$a -gt $b]`     | `if [ "$a" -gt "$b" ]` | 缺少空格                          |
| `[-f "$file"]`       | `[ -f "$file" ]`       | 方括号内缺空格                       |
| `stat -c %s "file"`  | `stat -c %s "$file"`   | 变量名缺 `$` 符号                   |

### 最佳实践

1. **变量加双引号**：防止变量为空或含空格时出错
   ```bash
   [ "$var" = "value" ]  # 推荐
   [ $var = "value" ]    # 不推荐
   ```
2. **使用 \[\[ ]] 替代 \[ ]**：功能更强，语法更安全
   ```bash
   [[ "$var" == "value" ]]  # 推荐
   ```
3. **数值比较用 (( ))**：更直观
   ```bash
   (( a > b ))  # 推荐
   [ "$a" -gt "$b" ]  # 可用
   ```
4. **字符串比较始终加引号**：
   ```bash
   [[ "$str1" == "$str2" ]]
   ```
5. **使用命令检查代替直接执行**：
   ```bash
   if command -v cmd &> /dev/null; then
       cmd --version
   fi
   ```

### 常用判断条件速查表

#### 文件/目录判断

| 条件               | 说明      | 示例                        |
| ---------------- | ------- | ------------------------- |
| `[ -f "$file" ]` | 是否为普通文件 | `if [ -f "/etc/passwd" ]` |
| `[ -d "$dir" ]`  | 是否为目录   | `if [ -d "/home/user" ]`  |
| `[ -e "$path" ]` | 是否存在    | `if [ -e "/tmp/test" ]`   |
| `[ -r "$file" ]` | 是否可读    | `if [ -r "$file" ]`       |
| `[ -w "$file" ]` | 是否可写    | `if [ -w "$file" ]`       |
| `[ -x "$file" ]` | 是否可执行   | `if [ -x "$file" ]`       |
| `[ -s "$file" ]` | 文件是否非空  | `if [ -s "$file" ]`       |
| `[ -L "$file" ]` | 是否为符号链接 | `if [ -L "$file" ]`       |

#### 字符串判断

| 条件                        | 说明    | 示例                          |
| ------------------------- | ----- | --------------------------- |
| `[ -z "$str" ]`           | 字符串为空 | `if [ -z "$name" ]`         |
| `[ -n "$str" ]`           | 字符串非空 | `if [ -n "$name" ]`         |
| `[ "$str1" = "$str2" ]`   | 字符串相等 | `if [ "$a" = "$b" ]`        |
| `[ "$str1" != "$str2" ]`  | 字符串不等 | `if [ "$a" != "$b" ]`       |
| `[[ "$str" == pattern ]]` | 模式匹配  | `if [[ "$file" == *.txt ]]` |
| `[[ "$str" =~ regex ]]`   | 正则匹配  | `if [[ "$email" =~ @ ]]`    |

#### 数值判断

| 条件                  | 说明     | 示例                    |
| ------------------- | ------ | --------------------- |
| `[ "$a" -eq "$b" ]` | 等于     | `if [ "$a" -eq 0 ]`   |
| `[ "$a" -ne "$b" ]` | 不等于    | `if [ "$a" -ne 0 ]`   |
| `[ "$a" -gt "$b" ]` | 大于     | `if [ "$a" -gt 10 ]`  |
| `[ "$a" -lt "$b" ]` | 小于     | `if [ "$a" -lt 100 ]` |
| `[ "$a" -ge "$b" ]` | 大于等于   | `if [ "$a" -ge 18 ]`  |
| `[ "$a" -le "$b" ]` | 小于等于   | `if [ "$a" -le 65 ]`  |
| `(( a > b ))`       | 大于（推荐） | `if (( a > 10 ))`     |

#### 逻辑运算

| 条件                         | 说明      | 示例                                  |
| -------------------------- | ------- | ----------------------------------- |
| `[ cond1 ] && [ cond2 ]`   | 逻辑与     | `if [ -f "$f" ] && [ -r "$f" ]`     |
| `[ cond1 ] \|\| [ cond2 ]` | 逻辑或     | `if [ "$a" = 1 ] \|\| [ "$a" = 2 ]` |
| `[ ! cond ]`               | 逻辑非     | `if [ ! -f "$file" ]`               |
| `[[ cond1 && cond2 ]]`     | 逻辑与（推荐） | `if [[ -f "$f" && -r "$f" ]]`       |
| `[[ cond1 \|\| cond2 ]]`   | 逻辑或（推荐） | `if [[ "$a" = 1 \|\| "$a" = 2 ]]`   |

#### 常用组合条件示例

```bash
# 检查文件是否存在且可读
if [ -f "$file" ] && [ -r "$file" ]; then
    cat "$file"
fi

# 检查目录是否存在，不存在则创建
if [ ! -d "$dir" ]; then
    mkdir -p "$dir"
fi

# 检查用户输入是否为空
if [ -z "$input" ]; then
    echo "输入不能为空"
    exit 1
fi

# 检查数字是否在范围内
if [ "$age" -ge 18 ] && [ "$age" -le 65 ]; then
    echo "成年人"
fi

# 检查命令是否存在
if command -v git &> /dev/null; then
    echo "Git 已安装"
fi

# 检查进程是否运行
if pgrep -x "nginx" > /dev/null; then
    echo "nginx 正在运行"
fi

# 检查网络连接
if ping -c 1 "google.com" &> /dev/null; then
    echo "网络正常"
fi

# 检查文件权限
if [ -f "$file" ] && [ -x "$file" ]; then
    echo "文件存在且可执行"
fi
```

***

## 6. Shell 循环

### for 循环

#### 基本语法

```bash
for 变量 in 列表; do
    命令
done
```

#### 遍历列表

```bash
#!/bin/bash

# 1. 直接列出值
for color in red green blue; do
    echo "颜色: $color"
done

# 2. 遍历命令输出
for file in $(ls *.txt); do
    echo "文件: $file"
done

# 3. 遍历数组
arr=("apple" "banana" "cherry")
for fruit in "${arr[@]}"; do
    echo "水果: $fruit"
done

# 4. 使用通配符
for file in /var/log/*.log; do
    echo "日志文件: $file"
done
```

#### C 风格 for 循环

```bash
#!/bin/bash

# 基本语法
for ((初始化; 条件; 步进)); do
    命令
done

# 示例1：数字循环
for ((i=1; i<=10; i++)); do
    echo "数字: $i"
done

# 示例2：倒序循环
for ((i=10; i>=1; i--)); do
    echo "倒数: $i"
done

# 示例3：步长为2
for ((i=0; i<=10; i+=2)); do
    echo "偶数: $i"
done
```

#### seq 命令

```bash
#!/bin/bash

# 基本用法
for i in $(seq 1 10); do
    echo $i
done

# 指定步长
for i in $(seq 0 2 10); do
    echo $i  # 0, 2, 4, 6, 8, 10
done

# 倒序
for i in $(seq 10 -1 1); do
    echo $i
done
```

#### 花括号展开

```bash
#!/bin/bash

# 数字序列
for i in {1..10}; do
    echo $i
done

# 指定步长（Bash 4+）
for i in {0..10..2}; do
    echo $i  # 0, 2, 4, 6, 8, 10
done

# 字母序列
for c in {a..z}; do
    echo -n "$c "
done
echo ""
```

### while 循环

#### 基本语法

```bash
while [ 条件 ]; do
    命令
done
```

#### 基本示例

```bash
#!/bin/bash

# 1. 计数器
count=1
while [ $count -le 5 ]; do
    echo "第 $count 次循环"
    count=$((count + 1))
done

# 2. 读取文件
while read -r line; do
    echo "行: $line"
done < /etc/hosts

# 3. 无限循环
while true; do
    echo "运行中..."
    sleep 1
done

# 4. 条件循环
while [ -f /tmp/lock ]; do
    echo "等待锁文件删除..."
    sleep 1
done
```

#### while read 循环

```bash
#!/bin/bash

# 1. 读取文件每一行
while IFS= read -r line; do
    echo "内容: $line"
done < file.txt

# 2. 读取命令输出
ls -la | while read -r line; do
    echo "行: $line"
done

# 3. 读取CSV文件
while IFS=',' read -r name age city; do
    echo "姓名: $name, 年龄: $age, 城市: $city"
done < data.csv

# 4. 处理管道数据
cat /etc/passwd | while IFS=':' read -r user _ uid gid _ home shell; do
    echo "用户: $user, UID: $uid, Shell: $shell"
done
```

### until 循环

#### 基本语法

```bash
until [ 条件 ]; do
    命令
done
```

#### 基本示例

```bash
#!/bin/bash

# 1. 计数器
count=1
until [ $count -gt 5 ]; do
    echo "第 $count 次循环"
    count=$((count + 1))
done

# 2. 等待条件满足
until [ -f /tmp/ready ]; do
    echo "等待就绪文件..."
    sleep 1
done
echo "就绪！"

# 3. 等待服务启动
until curl -s http://localhost:8080 > /dev/null; do
    echo "等待服务启动..."
    sleep 2
done
echo "服务已启动"
```

### 循环控制

#### break —— 跳出循环

```bash
#!/bin/bash

# 1. 跳出单层循环
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break
    fi
    echo $i
done
# 输出: 1 2 3 4

# 2. 跳出多层循环（break n）
for i in {1..3}; do
    for j in {1..3}; do
        if [ $j -eq 2 ]; then
            break 2  # 跳出2层循环
        fi
        echo "$i $j"
    done
done
# 输出: 1 1
```

#### continue —— 跳过本次循环

```bash
#!/bin/bash

# 1. 跳过本次迭代
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo $i
done
# 输出: 1 2 4 5

# 2. 跳过多层循环的本次迭代（continue n）
for i in {1..3}; do
    for j in {1..3}; do
        if [ $j -eq 2 ]; then
            continue 2  # 跳过外层循环的本次迭代
        fi
        echo "$i $j"
    done
done
# 输出: 1 1  2 1  3 1
```

### 嵌套循环

```bash
#!/bin/bash

# 1. 九九乘法表
for ((i=1; i<=9; i++)); do
    for ((j=1; j<=i; j++)); do
        printf "%d×%d=%-4d" $j $i $((i*j))
    done
    echo ""
done

# 2. 打印三角形
for ((i=1; i<=5; i++)); do
    for ((j=1; j<=5-i; j++)); do
        echo -n " "
    done
    for ((k=1; k<=2*i-1; k++)); do
        echo -n "*"
    done
    echo ""
done

# 3. 二维数组模拟
declare -A matrix
for ((i=0; i<3; i++)); do
    for ((j=0; j<3; j++)); do
        matrix[$i,$j]=$((i*3+j))
    done
done

# 打印矩阵
for ((i=0; i<3; i++)); do
    for ((j=0; j<3; j++)); do
        printf "%4d" ${matrix[$i,$j]}
    done
    echo ""
done
```

### 实用示例

#### 批量操作文件

```bash
#!/bin/bash

# 1. 批量重命名
for file in *.txt; do
    mv "$file" "${file%.txt}.bak"
done

# 2. 批量压缩
for dir in */; do
    tar -czf "${dir%/}.tar.gz" "$dir"
done

# 3. 批量查找并替换
for file in *.txt; do
    sed -i 's/old/new/g' "$file"
done

# 4. 批量删除
for file in *.tmp; do
    rm -f "$file"
done
```

#### 处理 CSV 文件

```bash
#!/bin/bash

# 读取CSV并处理
while IFS=',' read -r name age city; do
    # 跳过标题行
    [ "$name" = "姓名" ] && continue

    echo "处理: $name"
    echo "  年龄: $age"
    echo "  城市: $city"

    # 根据条件处理
    if [ "$age" -ge 18 ]; then
        echo "  状态: 成年"
    else
        echo "  状态: 未成年"
    fi
    echo "---"
done < data.csv
```

#### 进度条

```bash
#!/bin/bash

# 进度条函数
progress_bar() {
    local current=$1
    local total=$2
    local width=50
    local percentage=$((current * 100 / total))
    local filled=$((current * width / total))
    local empty=$((width - filled))

    printf "\r进度: ["
    for ((i=0; i<filled; i++)); do printf "█"; done
    for ((i=0; i<empty; i++)); do printf "░"; done
    printf "] %d%%" $percentage
}

# 使用进度条
total=100
for ((i=1; i<=total; i++)); do
    progress_bar $i $total
    sleep 0.1
done
echo ""
echo "完成！"
```

#### 菜单循环

```bash
#!/bin/bash

while true; do
    echo "===================="
    echo "  系统管理工具"
    echo "===================="
    echo "1) 查看系统信息"
    echo "2) 查看磁盘使用"
    echo "3) 查看内存使用"
    echo "4) 退出"
    echo "===================="
    read -p "请选择: " choice

    case $choice in
        1) uname -a ;;
        2) df -h ;;
        3) free -h ;;
        4) echo "退出"; break ;;
        *) echo "无效选项" ;;
    esac

    echo ""
    read -p "按回车继续..."
done
```

#### 重试机制

```bash
#!/bin/bash

# 重试函数
retry() {
    local max_attempts=$1
    local command=$2
    local attempt=1

    while [ $attempt -le $max_attempts ]; do
        echo "尝试 $attempt/$max_attempts: $command"
        if eval "$command"; then
            echo "成功！"
            return 0
        fi
        echo "失败，等待重试..."
        attempt=$((attempt + 1))
        sleep 2
    done

    echo "达到最大重试次数"
    return 1
}

# 使用示例
retry 3 "curl -s http://example.com"
```

### 循环与数组

```bash
#!/bin/bash

# 1. 遍历数组
arr=("apple" "banana" "cherry" "date")

# 方式1：for...in
for fruit in "${arr[@]}"; do
    echo "$fruit"
done

# 方式2：带索引遍历
for i in "${!arr[@]}"; do
    echo "索引 $i: ${arr[$i]}"
done

# 2. 数组过滤
numbers=(1 2 3 4 5 6 7 8 9 10)
even_numbers=()

for num in "${numbers[@]}"; do
    if (( num % 2 == 0 )); then
        even_numbers+=($num)
    fi
done

echo "偶数: ${even_numbers[@]}"
```

### 常见错误

| 错误写法 | 正确写法 | 原因 |
|----------|----------|------|
| `for i in {1..10}` | `for i in {1..10}; do` | 缺少 do |
| `while [ $i -lt 10 ]` | `while [ $i -lt 10 ]; do` | 缺少 do |
| `for ((i=0; i<10; i++))` | `for ((i=0; i<10; i++)); do` | 缺少 do |
| `done` | 确保与 do 配对 | done 必须与 do 配对 |
| `break` 在函数中 | `break` 只能在循环中 | break 只用于循环 |

***

## 7. 打包和解包 —— tar 命令

### 基本概念

| 术语 | 说明 | 命令 |
|------|------|------|
| **打包** | 将多个文件/目录合并为一个文件 | `tar -cf` |
| **解包** | 将打包文件还原为原始文件 | `tar -xf` |
| **压缩** | 减小文件大小 | `gzip`/`bzip2`/`xz` |
| **解压缩** | 还原压缩文件 | `gunzip`/`bunzip2`/`unxz` |

### tar 命令基本语法

```bash
tar [选项] [归档文件] [源文件/目录]
```

### 常用选项

| 选项 | 说明 | 示例 |
|------|------|------|
| `-c` | 创建归档（打包） | `tar -cf archive.tar file1 file2` |
| `-x` | 提取归档（解包） | `tar -xf archive.tar` |
| `-t` | 列出归档内容 | `tar -tf archive.tar` |
| `-v` | 显示详细过程 | `tar -cvf archive.tar file` |
| `-f` | 指定归档文件名 | `tar -cf archive.tar file` |
| `-z` | 使用 gzip 压缩 | `tar -czf archive.tar.gz file` |
| `-j` | 使用 bzip2 压缩 | `tar -cjf archive.tar.bz2 file` |
| `-J` | 使用 xz 压缩 | `tar -cJf archive.tar.xz file` |
| `-C` | 指定解压目录 | `tar -xf archive.tar -C /tmp` |
| `-p` | 保留权限 | `tar -cpf archive.tar file` |
| `--exclude` | 排除文件 | `tar -cf archive.tar --exclude="*.log" dir` |

### 打包（创建归档）

```bash
# 1. 打包单个文件
tar -cf archive.tar file.txt

# 2. 打包多个文件
tar -cf archive.tar file1.txt file2.txt file3.txt

# 3. 打包目录
tar -cf archive.tar /home/ty/project

# 4. 打包并显示过程
tar -cvf archive.tar file1.txt file2.txt

# 5. 打包当前目录所有文件
tar -cf archive.tar *

# 6. 打包并排除某些文件
tar -cf archive.tar --exclude="*.log" --exclude="*.tmp" /var/log

# 7. 使用通配符打包
tar -cf archive.tar *.txt
```

### 解包（提取归档）

```bash
# 1. 解包到当前目录
tar -xf archive.tar

# 2. 解包到指定目录
tar -xf archive.tar -C /tmp

# 3. 解包并显示过程
tar -xvf archive.tar

# 4. 解包特定文件
tar -xf archive.tar file1.txt

# 5. 解包并保留权限
tar -xpf archive.tar
```

### 查看归档内容

```bash
# 1. 查看归档文件列表
tar -tf archive.tar

# 2. 查看详细信息
tar -tvf archive.tar

# 3. 查看压缩归档内容
tar -tzf archive.tar.gz
tar -tjf archive.tar.bz2
tar -tJf archive.tar.xz
```

### 压缩和解压缩

#### gzip 压缩（.tar.gz）

```bash
# 打包并压缩
tar -czf archive.tar.gz file1.txt file2.txt

# 解压缩并解包
tar -xzvf archive.tar.gz

# 查看内容
tar -tzf archive.tar.gz
```

#### bzip2 压缩（.tar.bz2）

```bash
# 打包并压缩（压缩率更高）
tar -cjf archive.tar.bz2 file1.txt file2.txt

# 解压缩并解包
tar -xjvf archive.tar.bz2

# 查看内容
tar -tjf archive.tar.bz2
```

#### xz 压缩（.tar.xz）

```bash
# 打包并压缩（压缩率最高）
tar -cJf archive.tar.xz file1.txt file2.txt

# 解压缩并解包
tar -xJvf archive.tar.xz

# 查看内容
tar -tJf archive.tar.xz
```

### 压缩格式对比

| 格式 | 扩展名 | 压缩率 | 速度 | 说明 |
|------|--------|--------|------|------|
| gzip | `.tar.gz` / `.tgz` | 中等 | 快 | 最常用 |
| bzip2 | `.tar.bz2` | 高 | 慢 | 压缩率比 gzip 好 |
| xz | `.tar.xz` | 最高 | 最慢 | 压缩率最好 |

### 实用示例

#### 备份目录

```bash
#!/bin/bash

# 备份 /home 目录
backup_dir="/backup"
date=$(date +%Y%m%d)
tar -czf "$backup_dir/home_$date.tar.gz" /home

echo "备份完成: home_$date.tar.gz"
```

#### 增量备份

```bash
#!/bin/bash

# 创建快照文件
tar -czf backup.tar.gz \
    --listed-incremental=/backup/snapshot.snar \
    /home/ty/project

# 后续增量备份
tar -czf backup_incremental.tar.gz \
    --listed-incremental=/backup/snapshot.snar \
    /home/ty/project
```

#### 排除文件打包

```bash
#!/bin/bash

# 排除日志和临时文件
tar -czf project_backup.tar.gz \
    --exclude="*.log" \
    --exclude="*.tmp" \
    --exclude=".git" \
    --exclude="node_modules" \
    /home/ty/project
```

#### 解压到指定目录

```bash
#!/bin/bash

# 解压到 /tmp 目录
tar -xzf archive.tar.gz -C /tmp

# 解压到新建目录
mkdir -p /tmp/extracted
tar -xzf archive.tar.gz -C /tmp/extracted
```

#### 打包远程文件

```bash
#!/bin/bash

# 通过 SSH 打包远程文件
ssh user@remote "tar -czf - /home/user/project" > remote_backup.tar.gz

# 解压远程文件到本地
cat remote_backup.tar.gz | ssh user@remote "tar -xzf - -C /tmp"
```

#### 分卷打包

```bash
#!/bin/bash

# 分卷打包（每卷 1GB）
tar -czf - /large/directory | split -b 1G - archive.tar.gz.

# 合并分卷并解压
cat archive.tar.gz.* | tar -xzf -
```

### 常见错误

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `tar: Cowardly refusing to create an empty archive` | 未指定源文件 | 检查命令参数 |
| `tar: Error is not recoverable` | 文件不存在 | 检查文件路径 |
| `tar: This does not look like a tar archive` | 文件损坏或格式错误 | 重新下载或创建 |
| `gzip: stdin: not in gzip format` | 压缩文件损坏 | 检查文件完整性 |
| `tar: Exiting with failure status` | 权限不足 | 使用 sudo 或检查权限 |

### 注意事项

```bash
# 1. 选项顺序很重要
tar -czf archive.tar.gz file    # 正确
tar -cfz archive.tar.gz file    # 错误！f 后面必须跟文件名

# 2. 相对路径 vs 绝对路径
tar -cf archive.tar /home/ty    # 包含绝对路径
tar -cf archive.tar home/ty     # 包含相对路径

# 3. 保留权限
tar -cpf archive.tar /etc       # 保留权限（备份系统文件时重要）

# 4. 处理大文件
tar -cf - /large/dir | gzip > archive.tar.gz  # 管道压缩

# 5. 验证归档完整性
tar -df archive.tar             # 验证归档文件
```

***

## 8. Shell 函数

### 函数定义

```bash
# 方式1：推荐写法
function_name() {
    命令
    ...
}

# 方式2：function 关键字
function function_name {
    命令
    ...
}
```

### 基本示例

```bash
#!/bin/bash

# 定义函数
hello() {
    echo "Hello, World!"
}

# 调用函数
hello
```

### 函数参数

```bash
#!/bin/bash

# 函数使用 $1, $2, ... 接收参数
greet() {
    echo "Hello, $1!"
    echo "You are $2 years old"
}

# 调用函数并传递参数
greet "Alice" 25
```

### 参数处理

```bash
#!/bin/bash

show_args() {
    echo "函数名: $FUNCNAME"
    echo "参数个数: $#"
    echo "所有参数: $@"
    echo "第一个参数: $1"
    echo "第二个参数: $2"
}

show_args arg1 arg2 arg3
```

### 返回值

```bash
#!/bin/bash

# 方式1：使用 return 返回整数（0-255）
add() {
    result=$(( $1 + $2 ))
    return $result
}

add 3 5
echo "返回值: $?"  # 8

# 方式2：使用 echo 返回字符串
get_name() {
    echo "Alice"
}

name=$(get_name)
echo "名字: $name"

# 方式3：使用全局变量
result=0
calculate() {
    result=$(( $1 * $2 ))
}

calculate 3 5
echo "结果: $result"  # 15
```

### 局部变量

```bash
#!/bin/bash

my_func() {
    local local_var="局部变量"
    global_var="全局变量"
    echo "函数内: $local_var"
    echo "函数内: $global_var"
}

my_func
echo "函数外: $global_var"
# echo "函数外: $local_var"  # 错误！局部变量不可见
```

### 函数作用域

```bash
#!/bin/bash

var="全局变量"

my_func() {
    local var="局部变量"
    echo "函数内: $var"
}

my_func
echo "函数外: $var"
```

### 递归函数

```bash
#!/bin/bash

# 阶乘
factorial() {
    if [ $1 -le 1 ]; then
        echo 1
    else
        local prev=$(factorial $(( $1 - 1 )))
        echo $(( $1 * prev ))
    fi
}

result=$(factorial 5)
echo "5! = $result"  # 120
```

### 实用示例

#### 日志函数

```bash
#!/bin/bash

log() {
    local level=$1
    local message=$2
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] [$level] $message"
}

log "INFO" "脚本开始执行"
log "ERROR" "发生错误"
log "DEBUG" "调试信息"
```

#### 错误处理函数

```bash
#!/bin/bash

error_exit() {
    echo "错误: $1" >&2
    exit 1
}

# 使用示例
[ -f "$file" ] || error_exit "文件不存在: $file"
```

#### 确认函数

```bash
#!/bin/bash

confirm() {
    local prompt="$1"
    read -p "$prompt (y/n): " -n 1 -r
    echo ""
    [[ $REPLY =~ ^[Yy]$ ]]
}

if confirm "确定要继续吗?"; then
    echo "继续执行"
else
    echo "已取消"
    exit 0
fi
```

#### 菜单函数

```bash
#!/bin/bash

show_menu() {
    echo "===================="
    echo "  系统管理工具"
    echo "===================="
    echo "1) 查看系统信息"
    echo "2) 查看磁盘使用"
    echo "3) 查看内存使用"
    echo "4) 退出"
    echo "===================="
    read -p "请选择: " choice
    echo $choice
}

choice=$(show_menu)
case $choice in
    1) uname -a ;;
    2) df -h ;;
    3) free -h ;;
    4) exit 0 ;;
    *) echo "无效选项" ;;
esac
```

#### 文件检查函数

```bash
#!/bin/bash

check_file() {
    local file=$1
    if [ ! -f "$file" ]; then
        echo "错误: 文件不存在 - $file"
        return 1
    fi
    if [ ! -r "$file" ]; then
        echo "错误: 文件不可读 - $file"
        return 2
    fi
    echo "文件检查通过: $file"
    return 0
}

check_file "/etc/passwd"
```

### 函数库

```bash
#!/bin/bash
# 文件名: lib.sh

# 定义函数库
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

error() {
    echo "[ERROR] $1" >&2
}

confirm() {
    read -p "$1 (y/n): " -n 1 -r
    echo ""
    [[ $REPLY =~ ^[Yy]$ ]]
}
```

```bash
#!/bin/bash
# 使用函数库

# 加载函数库
source ./lib.sh
# 或
. ./lib.sh

# 使用函数
log "脚本开始"
confirm "继续?" && echo "继续"
```

### 常见错误

| 错误写法 | 正确写法 | 原因 |
|----------|----------|------|
| `function name() {}` | `name() {}` | 不需要 function 和 () 同时使用 |
| `return "字符串"` | `echo "字符串"` | return 只能返回整数 |
| `local var=value` 在函数外 | 只在函数内使用 | local 只能在函数内使用 |

***

## 9. Shell 工具

### cut 命令 —— 文本切割

```bash
# 基本语法
cut [选项] 文件

# 常用选项
# -d: 指定分隔符
# -f: 指定字段
# -c: 指定字符
```

#### 示例

```bash
# 1. 按分隔符切割
echo "root:x:0:0:root:/root:/bin/bash" | cut -d: -f1
# 输出: root

# 2. 提取多个字段
echo "root:x:0:0:root:/root:/bin/bash" | cut -d: -f1,7
# 输出: root:/bin/bash

# 3. 提取字符范围
echo "Hello World" | cut -c1-5
# 输出: Hello

# 4. 从文件读取
cut -d: -f1 /etc/passwd
# 输出所有用户名

# 5. 提取第3个字段
df -h | cut -d' ' -f5
# 提取使用率
```

### sort 命令 —— 排序

```bash
# 基本语法
sort [选项] 文件

# 常用选项
# -n: 按数值排序
# -r: 逆序排序
# -k: 指定排序字段
# -t: 指定分隔符
# -u: 去重
# -o: 输出到文件
```

#### 示例

```bash
# 1. 基本排序
echo -e "banana\napple\ncherry" | sort
# 输出:
# apple
# banana
# cherry

# 2. 数值排序
echo -e "10\n2\n30\n1" | sort -n
# 输出:
# 1
# 2
# 10
# 30

# 3. 逆序排序
echo -e "1\n2\n3" | sort -r
# 输出:
# 3
# 2
# 1

# 4. 按指定字段排序
sort -t: -k3 -n /etc/passwd
# 按 UID 排序

# 5. 去重排序
echo -e "apple\nbanana\napple\ncherry" | sort -u
# 输出:
# apple
# banana
# cherry
```

### wc 命令 —— 统计

```bash
# 基本语法
wc [选项] 文件

# 常用选项
# -l: 统计行数
# -w: 统计单词数
# -c: 统计字节数
# -m: 统计字符数
```

#### 示例

```bash
# 1. 统计行数
wc -l /etc/passwd
# 输出: 45 /etc/passwd

# 2. 统计单词数
wc -w /etc/hosts

# 3. 统计字节数
wc -c /etc/passwd

# 4. 完整统计
wc /etc/passwd
# 输出: 行数 单词数 字节数 文件名

# 5. 管道统计
cat /etc/passwd | wc -l
```

### uniq 命令 —— 去重

```bash
# 基本语法
uniq [选项] 文件

# 常用选项
# -c: 统计重复次数
# -d: 只显示重复行
# -u: 只显示不重复行
# -i: 忽略大小写
```

#### 示例

```bash
# 1. 去重（需要先排序）
echo -e "apple\nbanana\napple\ncherry" | sort | uniq
# 输出:
# apple
# banana
# cherry

# 2. 统计重复次数
echo -e "apple\nbanana\napple\ncherry" | sort | uniq -c
# 输出:
#       2 apple
#       1 banana
#       1 cherry

# 3. 只显示重复行
echo -e "apple\nbanana\napple\ncherry" | sort | uniq -d
# 输出: apple

# 4. 只显示不重复行
echo -e "apple\nbanana\napple\ncherry" | sort | uniq -u
# 输出:
# banana
# cherry
```

### tee 命令 —— 分流

```bash
# 基本语法
tee [选项] 文件

# 常用选项
# -a: 追加模式
```

#### 示例

```bash
# 1. 输出到屏幕和文件
echo "Hello" | tee output.txt
# 屏幕输出: Hello
# 文件内容: Hello

# 2. 追加模式
echo "World" | tee -a output.txt
# 文件内容: Hello\nWorld

# 3. 管道中使用
ls -la | tee file_list.txt | wc -l
# 同时保存文件列表和统计行数

# 4. 同时输出到多个文件
echo "test" | tee file1.txt file2.txt
```

### tr 命令 —— 字符转换

```bash
# 基本语法
tr [选项] 字符集1 字符集2

# 常用选项
# -d: 删除字符
# -s: 压缩重复字符
# -c: 取反
```

#### 示例

```bash
# 1. 大小写转换
echo "Hello World" | tr 'a-z' 'A-Z'
# 输出: HELLO WORLD

# 2. 删除字符
echo "Hello 123 World" | tr -d '0-9'
# 输出: Hello  World

# 3. 压缩重复字符
echo "Hello   World" | tr -s ' '
# 输出: Hello World

# 4. 替换字符
echo "Hello World" | tr ' ' '\n'
# 输出:
# Hello
# World

# 5. 删除换行符
cat file.txt | tr -d '\n'
```

### diff 命令 —— 文件比较

```bash
# 基本语法
diff [选项] 文件1 文件2

# 常用选项
# -u: 统一格式
# -c: 上下文格式
# -r: 递归比较目录
# -q: 只报告是否不同
```

#### 示例

```bash
# 1. 基本比较
diff file1.txt file2.txt

# 2. 统一格式（更易读）
diff -u file1.txt file2.txt

# 3. 比较目录
diff -r dir1/ dir2/

# 4. 只报告是否不同
diff -q file1.txt file2.txt
```

### awk 命令 —— 文本处理

```bash
# 基本语法
awk '模式 {动作}' 文件

# 内置变量
# $0: 整行
# $1, $2, ...: 第1, 2, ...个字段
# NR: 当前行号
# NF: 当前行字段数
# FS: 输入字段分隔符
# OFS: 输出字段分隔符
```

#### 示例

```bash
# 1. 打印特定字段
echo "Hello World" | awk '{print $1}'
# 输出: Hello

# 2. 指定分隔符
awk -F: '{print $1, $7}' /etc/passwd

# 3. 条件过滤
awk -F: '$3 >= 1000 {print $1}' /etc/passwd
# 打印 UID >= 1000 的用户

# 4. 格式化输出
awk -F: '{printf "%-20s %s\n", $1, $7}' /etc/passwd

# 5. 计算
awk '{sum += $1} END {print sum}' numbers.txt

#筛选后打印整行内容
awk -F',' '$2 > 25' data.csv  # 省略了{print ...}，默认打印整行内容
```

### sed 命令 —— 流编辑器

```bash
# 基本语法
sed [选项] '命令' 文件

# 常用命令
# s: 替换
# d: 删除
# p: 打印
# a: 追加
# i: 插入
# g: 全局匹配(末尾的 g 是 global 的意思，表示替换该行中所有匹配项)
```

#### 示例

```bash
# 1. 替换文本
sed 's/old/new/' file.txt
sed 's/old/new/g' file.txt  # 全局替换

# 2. 删除行
sed '3d' file.txt          # 删除第3行
sed '/pattern/d' file.txt  # 删除匹配行

# 3. 打印特定行
sed -n '5p' file.txt       # 打印第5行
sed -n '2,5p' file.txt     # 打印2-5行

# 4. 原地修改
sed -i 's/old/new/g' file.txt

# 5. 插入和追加
sed '2a\新行内容' file.txt  # 在第2行后追加
sed '2i\新行内容' file.txt  # 在第2行前插入
```

***

## 10. 正则表达式

### 基本概念

正则表达式（Regular Expression，简称 regex）是一种用于匹配字符串的模式。

### 基础元字符

| 元字符 | 说明 | 示例 | 匹配 |
|--------|------|------|------|
| `.` | 匹配任意单个字符 | `a.c` | abc, a1c, a c |
| `^` | 匹配行首 | `^Hello` | Hello World |
| `$` | 匹配行尾 | `World$` | Hello World |
| `*` | 匹配前一个字符0次或多次 | `ab*` | a, ab, abb |
| `+` | 匹配前一个字符1次或多次 | `ab+` | ab, abb |
| `?` | 匹配前一个字符0次或1次 | `ab?` | a, ab |
| `[]` | 字符集合 | `[abc]` | a, b, c |
| `[^]` | 否定字符集 | `[^abc]` | d, e, f |
| `\` | 转义字符 | `\.` | . |

### 字符类

| 字符类 | 说明 | 等价 |
|--------|------|------|
| `[0-9]` | 数字 | `[[:digit:]]` |
| `[a-z]` | 小写字母 | `[[:lower:]]` |
| `[A-Z]` | 大写字母 | `[[:upper:]]` |
| `[a-zA-Z]` | 字母 | `[[:alpha:]]` |
| `[a-zA-Z0-9]` | 字母和数字 | `[[:alnum:]]` |
| `[ \t]` | 空白字符 | `[[:space:]]` |

### 量词

| 量词 | 说明 | 示例 |
|------|------|------|
| `{n}` | 匹配n次 | `a{3}` 匹配 aaa |
| `{n,}` | 匹配至少n次 | `a{2,}` 匹配 aa, aaa, ... |
| `{n,m}` | 匹配n到m次 | `a{2,4}` 匹配 aa, aaa, aaaa |

### 分组和引用

```bash
# 分组
\(pattern\)

# 引用
\1, \2, ...  # 引用第1, 2, ...个分组
```

### 常用正则表达式

#### 邮箱验证

```bash
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

#### 手机号验证

```bash
^1[3-9][0-9]{9}$
```

#### IP 地址验证

```bash
^([0-9]{1,3}\.){3}[0-9]{1,3}$
```

#### URL 验证

```bash
https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

#### 日期格式

```bash
^[0-9]{4}-[0-9]{2}-[0-9]{2}$
```

### grep 正则表达式

```bash
# 基本正则表达式（BRE）
grep 'pattern' file

# 扩展正则表达式（ERE）
grep -E 'pattern' file
# 或
egrep 'pattern' file
```

#### 示例

```bash
# 1. 匹配数字
grep -E '[0-9]+' file.txt

# 2. 匹配邮箱
grep -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' file.txt

# 3. 匹配IP地址
grep -E '([0-9]{1,3}\.){3}[0-9]{1,3}' file.txt

# 4. 匹配空行
grep -n '^$' file.txt

# 5. 匹配注释行
grep -n '^#' file.txt

# 6. 匹配非注释行
grep -v '^#' file.txt
```

### sed 正则表达式

```bash
# 基本语法
sed 's/pattern/replacement/' file

# 使用扩展正则
sed -E 's/pattern/replacement/' file
```

#### 示例

```bash
# 1. 替换数字
sed -E 's/[0-9]+/NUMBER/g' file.txt

# 2. 删除空行
sed '/^$/d' file.txt

# 3. 提取邮箱
sed -n 's/.*\([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\).*/\1/p' file.txt

# 4. 格式化日期
sed -E 's/([0-9]{4})([0-9]{2})([0-9]{2})/\1-\2-\3/' file.txt
```

### awk 正则表达式

```bash
# 基本语法
awk '/pattern/ {action}' file

# 使用正则
awk '{if ($0 ~ /pattern/) print}' file
```

#### 示例

```bash
# 1. 匹配包含数字的行
awk '/[0-9]+/ {print}' file.txt

# 2. 匹配特定字段
awk -F: '$1 ~ /^user/ {print $1, $7}' /etc/passwd

# 3. 排除匹配行
awk '!/pattern/ {print}' file.txt
```

### 正则表达式工具

#### 在线工具

- [Regex101](https://regex101.com/)
- [RegExr](https://regexr.com/)
- [Debuggex](https://www.debuggex.com/)

#### 命令行工具

```bash
# 使用 grep 测试
echo "test string" | grep -E 'pattern'

# 使用 sed 测试
echo "test string" | sed -E 's/pattern/replacement/'

# 使用 awk 测试
echo "test string" | awk '/pattern/ {print}'
```

### 常见错误

| 错误 | 说明 | 解决方案 |
|------|------|----------|
| 忘记转义特殊字符 | `.`、`*`、`+` 等需要转义 | 使用 `\` 转义 |
| 贪婪匹配 | `.*` 匹配尽可能多 | 使用 `.*?` 非贪婪 |
| 忘记锚定 | 匹配部分字符串 | 使用 `^` 和 `$` |
| 字符集错误 | `[a-z]` 包含所有小写字母 | 注意字符顺序 |

***

*持续更新中...*
