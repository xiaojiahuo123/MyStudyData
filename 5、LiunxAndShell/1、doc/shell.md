# Shell 脚本学习笔记

***

## 1. 脚本的执行方式与权限

### Shebang（#!）—— 脚本开头

```bash
#!/bin/bash
```

`#!/bin/bash` **不是必须的**，但**强烈建议加上**。

| 情况 | 说明 |
|------|------|
| 有 `#!/bin/bash` | 系统用 `/bin/bash` 解释执行 |
| 有 `#!/bin/sh` | 系统用 `/bin/sh` 解释执行（可能是 dash） |
| 有 `#!/usr/bin/env bash` | 从环境变量中查找 bash |
| 没有 shebang | 由**当前使用的 Shell** 解释执行（不确定用哪个 Shell） |

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

| 方式 | 需要执行权限 | 使用 shebang | 说明 |
|------|-------------|-------------|------|
| `sh test.sh` | 不需要 | 忽略 | 强制用 sh 解释 |
| `bash test.sh` | 不需要 | 忽略 | 强制用 bash 解释 |
| `./test.sh` | **需要** | 使用 | 根据 shebang 决定解释器 |

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

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| `Permission denied` | 文件没有执行权限 | `chmod +x script.sh` |
| `command not found` | 路径不对或没有 `./` | 使用 `./script.sh` 或完整路径 |
| `bad interpreter` | shebang 路径错误 | 检查 `#!/bin/bash` 路径是否正确 |
| Windows 编辑的脚本报错 | 换行符是 `\r\n` | `sed -i 's/\r$//' script.sh` |

***

## 2. Shell 变量

### 变量定义

```bash
# 等号两边不能有空格！
name="hello"
age=18
path=/home/ty
```

| 正确 | 错误 |
|------|------|
| `name="hello"` | `name = "hello"` |
| `age=18` | `age= 18` |

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

| 阶段 | 发生了什么 |
|------|-----------|
| `files=$(ls -la)` | 执行 `ls -la`，输出结果存为字符串 |
| `echo $files` | 把那个字符串打印出来，**不再执行命令** |

> **注意**：`echo` 本身不会执行变量中的命令，它只是打印文本。

### 变量作用域

| 类型 | 说明 | 用法 |
|------|------|------|
| 局部变量 | 仅在当前 Shell 进程中有效 | 直接赋值 |
| 全局变量 | 子进程也可访问 | `export 变量名` |
| 环境变量 | 系统级全局变量 | 写入 `/etc/profile` 或 `~/.bashrc` |

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

| 变量 | 含义 |
|------|------|
| `$HOME` | 当前用户家目录 |
| `$USER` | 当前用户名 |
| `$PWD` | 当前工作目录 |
| `$SHELL` | 当前 Shell 路径 |
| `$PATH` | 命令搜索路径 |
| `$HOSTNAME` | 主机名 |
| `$RANDOM` | 随机数（0-32767） |
| `$?` | 上一个命令的退出状态码（0表示成功） |
| `$$` | 当前 Shell 进程的 PID |
| `$0` | 脚本名称 |
| `$1-$9` | 脚本参数（第1-9个） |
| `$#` | 脚本参数个数 |
| `$@` | 所有参数（独立字符串） |
| `$*` | 所有参数（单个字符串） |

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

| 状态码 | 含义 | 常见原因 |
|--------|------|----------|
| **0** | 成功 | 命令正常执行 |
| **1** | 一般错误 | 通用错误 |
| **2** | 误用 Shell 命令 | 语法错误 |
| **126** | 权限不够 | 文件没有执行权限 |
| **127** | 命令未找到 | 命令拼写错误或未安装 |
| **130** | Ctrl+C 终止 | 用户手动中断 |

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

*持续更新中...*
