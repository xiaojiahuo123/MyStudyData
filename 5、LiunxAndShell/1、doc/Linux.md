# Linux 基础命令学习笔记

***

## ubuntu的一些注意点

如果是在虚拟机运行，跨设备(a电脑连接b电脑的ubuntu虚拟机，需要虚拟机是桥接模式-复制网络连接状态，并且可能需要手动启动网卡)

```shell
sudo ip link set ens33 up  # 启动ens33网卡
sudo dhclient ens33  # 请求分配ip,通过DHCP

```

一定情况下，更常见的问题是复制过去的虚拟机的桥接模式，VM的在虚拟网络编辑器里，需要更改设置，让桥接的(通常是vm0)选择的是当前实际使用的网卡

## 1. mv 命令 —— 移动与重命名

### 基本用法

```bash
mv [源路径] [目标路径]
```

### 注意事项

重命名时，如果不在文件所在目录操作，且目标路径没有指定目录，文件会被移到**当前执行命令的目录**。

### 实例演示

假设当前在 Desktop 目录下执行：

```bash
mv test001/test002/test001.txt test002.txt
```

这条命令的效果是：把文件从 `test001/test002/` **移到当前目录**，并重命名为 `test002.txt`。

**目录结构变化**：

```
Desktop/
├── test001/
│   └── test002/        ← 空的
├── test002/
│   └── test001.txt     ← 原本就在这个目录里的
└── test002.txt         ← 从 test001/test002/ 移出来的
```

### 三种常见需求

| 意图 | 命令 |
|------|------|
| 移到 test002 目录下，保持原名 | `mv test001/test002/test001.txt test002/` |
| 移到 test002 目录下，改名 | `mv test001/test002/test001.txt test002/test002.txt` |
| 移到当前目录，改名 | `mv test001/test002/test001.txt test002.txt` |

> **提示**：目标路径末尾加 `/` 表示"这是一个目录"，确保文件放入目录中。

***

## 2. rm 命令 —— 文件与目录删除

### 基本用法

```bash
rm [选项] 文件/目录
```

### 删除文件

```bash
# 删除单个文件
rm file.txt

# 删除多个文件
rm file1.txt file2.txt file3.txt

# 使用通配符删除
rm *.log
rm *.tmp
```

### 常用选项

| 选项 | 说明 | 示例 |
|------|------|------|
| `-i` | 删除前确认 | `rm -i file.txt` |
| `-f` | 强制删除，不提示 | `rm -f file.txt` |
| `-r` | 递归删除目录 | `rm -r directory` |
| `-v` | 显示删除过程 | `rm -v file.txt` |
| `-rf` | 强制递归删除 | `rm -rf directory` |

### 删除目录

```bash
# 删除空目录
rmdir directory

# 删除非空目录（递归删除）
rm -r directory

# 强制删除目录（不提示）
rm -rf directory
```

### 安全删除建议

```bash
# 删除前先确认文件
ls -la file.txt
rm file.txt

# 使用 -i 选项防止误删
rm -i *.log

# 删除前先查看要删除的文件
ls *.log
rm *.log

# 使用 -v 选项显示删除过程
rm -v *.tmp
```

### 危险操作警告

```bash
# 千万不要执行！
rm -rf /          # 删除根目录，会删除整个系统
rm -rf *          # 删除当前目录所有文件
rm -rf ~          # 删除用户目录
rm -rf /*         # 同 rm -rf /
```

### 实际应用场景

```bash
# 1. 清理临时文件
rm -rf /tmp/*

# 2. 清理日志文件
rm -f /var/log/*.log.*

# 3. 删除前确认
rm -i important_file.txt

# 4. 批量删除特定类型文件
find /tmp -name "*.tmp" -exec rm {} \;

# 5. 删除空目录
rmdir empty_dir

# 6. 删除目录及其内容
rm -r project_backup/
```

### 常见错误

| 错误操作 | 后果 | 预防措施 |
|----------|------|----------|
| `rm -rf /` | 删除整个系统 | 永远不要执行 |
| `rm -rf *` | 删除当前目录所有文件 | 先 `ls` 确认 |
| `rm -rf ~` | 删除用户主目录 | 永远不要执行 |
| `rm file *` | 删除 file 和所有文件 | 使用 `rm file` |

### 与 find 命令组合

```bash
# 查找并删除特定文件
find /tmp -name "*.tmp" -exec rm {} \;

# 查找并删除空文件
find /home -type f -empty -delete

# 查找并删除超过30天的文件
find /var/log -name "*.log" -mtime +30 -delete

# 查找并删除特定大小的文件
find / -type f -size +100M -exec rm {} \;
```

***

## 3. /etc/passwd —— 用户账户信息文件

### 文件格式

`/etc/passwd` 是 Linux 系统中用户账户信息的核心文件，每一行代表一个用户，格式如下：

```
用户名:密码占位符:UID:GID:用户描述:家目录:登录Shell
```

**示例**：

```bash
root:x:0:0:root:/root:/bin/bash
ty:x:1000:1000:ty,,,:/home/ty:/bin/bash
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
```

### 各字段含义

| 字段 | 含义 | 安全意义 |
|------|------|----------|
| 用户名 | 登录账号 | 攻击者可枚举系统中存在哪些用户 |
| x | 密码占位符 | 实际密码存储在 `/etc/shadow`（更安全） |
| UID | 用户ID | 0 = root，1000+ = 普通用户 |
| GID | 组ID | 用户所属主组 |
| 用户描述 | 备注信息 | 可能泄露真实姓名/用途 |
| 家目录 | 用户主目录路径 | 了解文件存放位置 |
| 登录Shell | 默认Shell | `/bin/bash` 可登录，`/usr/sbin/nologin` 禁止登录 |

### 网络安全角度的意义

#### 信息泄露风险

```bash
# 攻击者可以读取此文件，枚举系统用户
cat /etc/passwd
```

- 泄露所有用户名，为暴力破解提供目标
- 泄露 UID/GID，了解权限结构
- 泄露 Shell 类型，判断哪些用户可登录

#### 常见安全检查

```bash
# 1. 查找 UID=0 的用户（应该只有 root）
awk -F: '$3 == 0 {print $1}' /etc/passwd

# 2. 查找可登录的用户
grep -v '/nologin\|/false' /etc/passwd

# 3. 查找空密码的用户（危险！）
awk -F: '$2 == "" {print $1}' /etc/passwd

# 4. 查找非系统用户的异常账户
awk -F: '$3 >= 1000 {print $1, $3, $7}' /etc/passwd
```

### 安全加固建议

| 措施 | 说明 |
|------|------|
| 密码迁移到 `/etc/shadow` | shadow 文件只有 root 可读，更安全（现代系统默认已配置） |
| 禁用不需要的用户 | 将 Shell 设为 `/usr/sbin/nologin` 或 `/bin/false` |
| 限制文件权限 | `chmod 644 /etc/passwd`（所有人可读，仅 root 可写） |
| 定期审计 | 检查异常用户、UID=0 的账户、可登录账户数量 |

### /etc/passwd vs /etc/shadow

| 文件 | 权限 | 内容 |
|------|------|------|
| `/etc/passwd` | `-rw-r--r--` (644) | 用户信息，所有人可读 |
| `/etc/shadow` | `-rw-r-----` (640) | 加密密码，仅 root 可读 |

```bash
# 查看 shadow 文件权限
ls -la /etc/shadow
# -rw-r----- 1 root shadow 1234 ... /etc/shadow
```

### 总结

`/etc/passwd` 是系统的"用户花名册"，虽然现代 Linux 已将密码移到 `/etc/shadow`，但它仍然是攻击者信息收集的重要目标。安全运维中应定期审计此文件，确保没有异常账户和权限配置。

***

## 4. tail 命令 —— 文件尾部查看与实时监视

### 基本用法

```bash
tail [选项] [文件]
```

| 选项 | 说明 |
|------|------|
| `-n N` | 显示文件末尾 N 行（默认 10 行） |
| `-f` | 跟踪文件**描述符**，实时监视新内容 |
| `-F` | 跟踪文件**名称**，文件被删后可自动重新打开 |

### -f 与 -F 的区别

| 参数 | 说明 | 文件被删除/轮转 |
|------|------|-----------------|
| `-f` | 跟踪文件描述符 | 无法恢复，需手动重启 |
| `-F` | 跟踪文件名称 | 自动重新打开同名文件 |

> **建议**：监视日志文件时优先使用 `-F`，防止日志轮转导致监视中断。

### 实时监视示例

```bash
# 终端1：监视文件
tail -F /var/log/syslog

# 终端2：追加内容
echo "new log entry" >> /var/log/syslog

# 终端1 立即显示：
# new log entry
```

### 行为说明

| 场景 | 行为 |
|------|------|
| 有人追加新内容 | **实时显示**新追加的行 |
| 没有新内容 | 命令**一直等待**，不退出 |
| 文件被删除/轮转 | `-F` 自动重新打开同名文件 |

### 实际应用场景

#### 实时监控各种日志

```bash
# Web 服务器日志
tail -F /var/log/nginx/access.log

# 系统日志
tail -F /var/log/syslog

# 应用日志
tail -F /var/log/mysql/error.log

# 自定义日志
tail -F /home/ty/myapp.log
```

#### 运维/开发中的典型用途

| 场景 | 用途 |
|------|------|
| 排查报错 | 实时看错误日志，出问题立刻看到 |
| 调试程序 | 边运行程序边看日志输出 |
| 监控攻击 | 实时看 Web 日志，发现异常请求 |
| 部署上线 | 观察新版本启动是否正常 |

### 日志轮转

日志轮转是系统把 `access.log` 改名为 `access.log.1`，然后新建一个 `access.log`。用 `-F` 才能持续跟下去。

| 命令 | 区别 |
|------|------|
| `tail -f` | 监视文件，文件被轮转后就断了 |
| `tail -F` | 监视文件，文件被轮转后自动重新打开新文件 |

### 组合用法

```bash
# 实时过滤含 "ERROR" 的日志
tail -F /var/log/syslog | grep "ERROR"

# 实时统计访问量（每秒刷新）
tail -F /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c

# 同时监视多个日志
tail -F /var/log/*.log
```

***

## 5. 重定向 —— > 与 >>

### 基本概念

| 符号 | 名称 | 作用 |
|------|------|------|
| `>` | 输出重定向 | **覆盖**写入到文件 |
| `>>` | 追加重定向 | **追加**写入到文件末尾 |

### 示例

```bash
# > 覆盖写入（文件不存在则创建，存在则清空重写）
echo "hello" > test.txt      # test.txt 内容为 "hello"
echo "world" > test.txt      # test.txt 内容为 "world"（hello 被覆盖）

# >> 追加写入（文件不存在则创建，存在则在末尾追加）
echo "hello" >> test.txt     # test.txt 内容为 "hello"
echo "world" >> test.txt     # test.txt 内容为 "hello\nworld"（追加）
```

### 文件不存在时

两种符号在文件不存在时都会**自动创建**文件：

```bash
echo "data" > newfile.txt   # 创建 newfile.txt 并写入 "data"
echo "more" >> newfile.txt  # 追加 "more" 到末尾
```

### 常见用途

```bash
# 将命令输出保存到文件
ls -la > filelist.txt          # 覆盖
echo "backup done" >> log.txt  # 追加

# 清空文件
> logfile.txt                  # 文件内容被清空

# 合并文件
cat file1.txt >> file2.txt     # 将 file1 内容追加到 file2
```

### 2>&1：错误输出也重定向

```bash
# 标准输出（stdout）重定向
echo "hello" > output.txt

# 错误输出（stderr）也重定向到同一文件
command > output.txt 2>&1

# 标准输出追加，错误输出也追加
command >> output.txt 2>&1
```

| 文件描述符 | 名称 | 默认输出 |
|------------|------|----------|
| 0 | stdin（标准输入） | 键盘 |
| 1 | stdout（标准输出） | 终端 |
| 2 | stderr（错误输出） | 终端 |

***

## 6. 软链接（Symbolic Link）

### 基本概念

| 类型 | 命令 | 说明 |
|------|------|------|
| 软链接（符号链接） | `ln -s` | 类似 Windows 快捷方式，指向原文件路径 |
| 硬链接 | `ln` | 与原文件共享同一个 inode，删除原文件仍可访问 |

### 创建软链接

```bash
ln -s [原文件路径] [链接名]

# 示例
ln -s /var/log/nginx/access.log ~/access_link
```

### 软链接 vs 硬链接

| 特性 | 软链接（ln -s） | 硬链接（ln） |
|------|-----------------|--------------|
| 本质 | 指向原文件路径的快捷方式 | 与原文件共享同一个 inode |
| 跨文件系统 | 可以 | 不可以 |
| 链接目录 | 可以 | 不可以 |
| 原文件删除后 | 链接失效（悬空链接） | 仍可访问 |
| 文件大小 | 很小（只存路径） | 与原文件相同 |
| inode | 不同 | 相同 |

### 查看链接

```bash
# 查看文件是否为软链接
ls -la
# lrwxrwxrwx 1 user user 25 Jul 20 10:00 access_link -> /var/log/nginx/access.log
# ↑ 第一个字母 l 表示软链接

# 查看软链接指向的实际路径
readlink access_link
# /var/log/nginx/access.log

# 查看 inode
ls -i access_link
```

### 实际应用场景

```bash
# 1. 版本切换（如 Python、Node.js）
ln -s /usr/bin/python3.11 /usr/bin/python

# 2. 配置文件管理
ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled/mysite

# 3. 快速访问常用目录
ln -s /var/log/nginx ~/nginx_logs

# 4. 程序部署（将程序链接到 PATH 目录）
ln -s /opt/myapp/bin/myapp /usr/local/bin/myapp
```

### 注意事项

```bash
# 软链接使用相对路径时，是相对于链接文件所在目录，不是当前目录
ln -s ../config.txt link.txt  # 相对于 link.txt 所在目录

# 删除软链接时不要加 /（否则会删除链接指向的目录内容）
rm access_link      # 正确：只删除链接
rm access_link/     # 危险：可能删除原目录内容！
```

***

## 7. history 命令 —— 命令历史记录

### 基本用法

```bash
history            # 显示所有历史命令
history 10         # 显示最近10条
history -c         # 清空当前会话的历史记录
```

### 快捷操作

| 用法 | 说明 |
|------|------|
| `!!` | 重复执行上一条命令（常用 `sudo !!`） |
| `!n` | 执行第 n 条历史命令 |
| `!string` | 执行最近一条以 string 开头的命令 |
| `Ctrl+R` | 反向搜索历史命令 |

### 示例

```bash
# 常见用法：忘记加 sudo 时
apt update
# Permission denied
sudo !!              # 自动补上 sudo 执行上一条命令

# 执行历史中第42条命令
!42

# 执行最近以 ssh 开头的命令
!ssh
```

### 历史记录存储

历史记录存储在 `~/.bash_history` 文件中：

```bash
# 查看历史文件
cat ~/.bash_history

# 搜索历史中包含 "ssh" 的命令
history | grep ssh
```

***

## 8. 用户管理 —— 增、删、改

### 8.1 添加用户：useradd

```bash
useradd [选项] 用户名
```

| 选项 | 说明 |
|------|------|
| `-m` | 创建家目录（默认不创建） |
| `-d /home/xxx` | 指定家目录路径 |
| `-s /bin/bash` | 指定登录 Shell |
| `-g groupname` | 指定主组 |
| `-G group1,group2` | 指定附加组 |
| `-u 1001` | 指定 UID |
| `-c "描述"` | 添加用户描述 |
| `-e 2025-12-31` | 设置账户过期日期 |

```bash
# 基本创建（推荐加 -m 创建家目录）
sudo useradd -m ty

# 完整创建
sudo useradd -m -d /home/ty -s /bin/bash -g sudo -G docker,www-data -u 1001 -c "开发用户" ty

# 设置密码
sudo passwd ty
```

### 8.2 修改用户：usermod

```bash
usermod [选项] 用户名
```

| 选项 | 说明 |
|------|------|
| `-l 新用户名` | 修改用户名 |
| `-d /new/home` | 修改家目录（加 `-m` 同时迁移文件） |
| `-s /bin/zsh` | 修改登录 Shell |
| `-g groupname` | 修改主组 |
| `-G group1,group2` | 替换附加组（覆盖） |
| `-aG groupname` | **追加**附加组（不覆盖） |
| `-L` | 锁定账户（禁止登录） |
| `-U` | 解锁账户 |
| `-e 2025-12-31` | 设置账户过期日期 |

```bash
# 修改用户名
sudo usermod -l newname oldname

# 将用户加入 docker 组（-a 表示追加，不覆盖原有附加组）
sudo usermod -aG docker ty

# 修改登录 Shell 为 zsh
sudo usermod -s /bin/zsh ty

# 锁定账户
sudo usermod -L ty

# 解锁账户
sudo usermod -U ty
```

### 8.3 删除用户：userdel

```bash
userdel [选项] 用户名
```

| 选项 | 说明 |
|------|------|
| （无选项） | 只删除用户，保留家目录 |
| `-r` | 删除用户**同时删除家目录和邮件** |

```bash
# 只删除用户
sudo userdel ty

# 删除用户及其家目录
sudo userdel -r ty
```

### 8.4 修改密码：passwd

```bash
passwd [用户名]
```

| 用法 | 说明 |
|------|------|
| `passwd` | 修改当前用户密码 |
| `passwd ty` | 修改 ty 用户的密码（需要 root） |
| `passwd -l ty` | 锁定密码（禁止登录） |
| `passwd -u ty` | 解锁密码 |
| `passwd -e ty` | 强制下次登录时修改密码 |

```bash
# 设置/修改密码
sudo passwd ty
# 输入两次新密码

# 强制用户下次登录修改密码
sudo passwd -e ty
```

### 8.5 常用组合示例

```bash
# 创建一个完整的开发用户
sudo useradd -m -s /bin/bash -G sudo,docker -c "开发人员" devuser
sudo passwd devuser

# 禁用离职员工账户
sudo usermod -L -s /usr/sbin/nologin olduser

# 删除离职员工账户
sudo userdel -r olduser
```

***

## 9. 用户组管理

### 基本概念

Linux 中每个用户属于一个**主组**（primary group）和多个**附加组**（supplementary groups）。

| 概念 | 说明 |
|------|------|
| 主组 | 用户创建文件时的默认所属组（`/etc/passwd` 第4列） |
| 附加组 | 用户额外加入的组，用于获得额外权限 |
| `/etc/group` | 用户组信息文件 |

### /etc/group 文件格式

```
组名:密码占位符:GID:组成员列表
```

```bash
# 示例
root:x:0:
sudo:x:27:ty
docker:x:998:ty
www-data:x:33:
```

| 字段 | 说明 |
|------|------|
| 组名 | 组的名称 |
| x | 密码占位符（通常不使用） |
| GID | 组ID |
| 组成员列表 | 属于该附加组的用户（逗号分隔） |

### 添加组：groupadd

```bash
groupadd [选项] 组名
```

| 选项 | 说明 |
|------|------|
| `-g GID` | 指定 GID |
| `-r` | 创建系统组 |

```bash
# 创建普通组
sudo groupadd developers

# 指定 GID
sudo groupadd -g 1500 developers

# 创建系统组
sudo groupadd -r myservice
```

### 修改组：groupmod

```bash
groupmod [选项] 组名
```

| 选项 | 说明 |
|------|------|
| `-n 新组名` | 修改组名 |
| `-g 新GID` | 修改 GID |

```bash
# 修改组名
sudo groupmod -n newdev developers

# 修改 GID
sudo groupmod -g 1600 developers
```

### 删除组：groupdel

```bash
sudo groupdel 组名
```

> **注意**：不能删除用户的主组，需要先删除用户或将用户移到其他主组。

### 用户与组的关系管理

```bash
# 查看用户所属的组
groups ty
# ty : ty sudo docker

# 查看组的详细信息
id ty
# uid=1000(ty) gid=1000(ty) groups=1000(ty),27(sudo),998(docker)

# 将用户加入附加组（usermod -aG）
sudo usermod -aG developers ty

# 从组中移除用户（手动编辑 /etc/group，删除用户名）
sudo gpasswd -d ty developers
```

### 查看组信息

```bash
# 查看所有组
cat /etc/group

# 查看特定组
grep sudo /etc/group
# sudo:x:27:ty

# 查看组成员
getent group sudo
# sudo:x:27:ty
```

### 主组 vs 附加组

| 特性 | 主组 | 附加组 |
|------|------|--------|
| 数量 | 每个用户只有1个 | 可以有多个 |
| 配置位置 | `/etc/passwd` 第4列 | `/etc/group` 第4列 |
| 文件默认组 | 用户创建文件时自动归属 | 不影响默认组 |
| 修改方式 | `usermod -g` | `usermod -aG` |

```bash
# 修改主组
sudo usermod -g developers ty

# 追加附加组
sudo usermod -aG docker ty
```

### 安全意义

```bash
# 1. 查找 GID=0 的组（应该只有 root）
awk -F: '$3 == 0 {print $1}' /etc/group

# 2. 查找空成员的组
awk -F: '$4 == "" {print $1}' /etc/group

# 3. 查找 sudo 组的成员（高权限用户）
getent group sudo

# 4. 查找可登录组的异常成员
grep -E '^(sudo|wheel):' /etc/group
```

| 检查项 | 说明 |
|--------|------|
| GID=0 的组 | 应该只有 root 组 |
| sudo/wheel 组成员 | 拥有 root 权限，需严格控制 |
| 空组 | 可能是遗留组，建议清理 |

***

## 10. chmod 命令 —— 文件权限管理

### 基本概念

Linux 中每个文件/目录都有三组权限，分别对应三类用户：

| 权限 | 文件含义 | 目录含义 | 符号 | 数字 |
|------|----------|----------|------|------|
| 读（r） | 查看文件内容 | 列出目录内容（ls） | `r` | 4 |
| 写（w） | 修改文件内容 | 创建/删除目录内文件 | `w` | 2 |
| 执行（x） | 执行文件 | 进入目录（cd） | `x` | 1 |

| 用户类别 | 说明 | 标识 |
|----------|------|------|
| 所有者（Owner） | 文件的拥有者 | `u` |
| 所属组（Group） | 文件所属的用户组 | `g` |
| 其他人（Others） | 除以上两类的其他用户 | `o` |
| 所有人（All） | 以上三类全部 | `a` |

### 权限表示方式

```bash
# ls -la 输出示例
-rwxr-xr-- 1 ty sudo 4096 Jul 20 10:00 script.sh
```

```
-rwxr-xr--
│├─┤├─┤├─┤
│ │   │  │
│ │   │  └── 其他人权限：r-- = 只读(4)
│ │   └───── 所属组权限：r-x = 读+执行(5)
│ └───────── 所有者权限：rwx = 读+写+执行(7)
└─────────── 文件类型（- 文件, d 目录, l 软链接）

数字表示：754
```

### 符号模式

```bash
chmod [who][+/-][permission] 文件

# who: u(所有者) g(所属组) o(其他人) a(所有人)
# +/-: 添加/移除权限
# permission: r(读) w(写) x(执行)
```

```bash
# 给所有者添加执行权限
chmod u+x script.sh

# 给所有人添加读权限
chmod a+r file.txt

# 移除其他人的写权限
chmod o-w file.txt

# 给所有者读写执行，所属组读执行，其他人只读
chmod u=rwx,g=rx,o=r file.txt

# 给所有人添加执行权限
chmod +x script.sh
```

### 数字模式（推荐）

```bash
chmod [数字] 文件

# 数字 = 所有者 + 所属组 + 其他人
# 每位数字 = r(4) + w(2) + x(1)
```

```bash
# 754: 所有者rwx, 所属组r-x, 其他人r--
chmod 754 script.sh

# 644: 所有者rw-, 所属组r--, 其他人r--（常用文件权限）
chmod 644 config.txt

# 755: 所有者rwx, 所属组r-x, 其他人r-x（常用目录/脚本权限）
chmod 755 /var/www/html

# 700: 所有者rwx, 所属组和其他人无权限（私有目录）
chmod 700 ~/.ssh

# 600: 所有者rw-, 其他人无权限（私有文件）
chmod 600 ~/.ssh/id_rsa
```

### 常见权限组合速查

| 数字 | 权限 | 适用场景 |
|------|------|----------|
| `777` | `rwxrwxrwx` | 所有人完全控制（危险，慎用） |
| `755` | `rwxr-xr-x` | 可执行文件、目录、Web 服务目录 |
| `750` | `rwxr-x---` | 组内成员可执行，其他人无权限 |
| `700` | `rwx------` | 私有目录（如 `~/.ssh`） |
| `644` | `rw-r--r--` | 普通文件（所有者读写，其他人只读） |
| `600` | `rw-------` | 私有文件（如 SSH 私钥） |
| `444` | `r--r--r--` | 只读文件 |

### 递归修改

```bash
# 递归修改目录及所有子文件/目录的权限
chmod -R 755 /var/www/html

# -R 表示递归（Recursive）
```

### 注意事项

| 操作 | 说明 |
|------|------|
| `chmod 777` | 危险操作，任何人都能读写执行 |
| `chmod -R 777 /` | 极其危险，会破坏系统权限 |
| 可执行文件 | 必须有 `x` 权限才能运行 |
| 目录 | 必须有 `x` 权限才能 `cd` 进入 |

### 实际应用场景

```bash
# 1. Web 服务器目录权限
sudo chmod -R 755 /var/www/html    # 目录可读可执行
sudo chmod 644 /var/www/html/*.html # 文件只读

# 2. SSH 密钥权限
chmod 700 ~/.ssh                   # 私钥目录仅所有者可访问
chmod 600 ~/.ssh/id_rsa            # 私钥文件仅所有者可读写
chmod 644 ~/.ssh/id_rsa.pub        # 公钥所有人可读

# 3. 脚本文件权限
chmod +x deploy.sh                 # 添加执行权限

# 4. 日志文件权限
chmod 640 /var/log/syslog          # 所有者读写，所属组只读
```

***

## 11. find 命令 —— 文件查找

### 基本语法

```bash
find [搜索路径] [选项] [条件]
```

### 按名称查找

```bash
# 精确查找文件名
find / -name "passwd"

# 忽略大小写
find /home -iname "Readme.md"

# 通配符匹配
find /var -name "*.log"          # 所有 .log 文件
find /etc -name "nginx*"         # 以 nginx 开头的文件
find /home -name "?.txt"         # 文件名为单个字符的 .txt
```

### 按类型查找

| 类型 | 选项 | 说明 |
|------|------|------|
| 普通文件 | `-type f` | 查找文件 |
| 目录 | `-type d` | 查找目录 |
| 软链接 | `-type l` | 查找软链接 |

```bash
# 只查找文件
find /home -type f -name "*.py"

# 只查找目录
find /var -type d -name "log*"

# 只查找软链接
find /usr -type l
```

### 按大小查找

| 条件 | 说明 |
|------|------|
| `-size +100M` | 大于 100MB |
| `-size -10M` | 小于 10MB |
| `-size 0` | 空文件 |

```bash
# 查找大于 100MB 的文件
find / -type f -size +100M

# 查找大于 1GB 的文件
find /home -type f -size +1G

# 查找空文件
find /tmp -type f -size 0
```

### 按时间查找

| 选项 | 说明 |
|------|------|
| `-mtime -7` | 7天内修改过 |
| `-mtime +30` | 超过30天未修改 |
| `-mtime 0` | 今天修改过 |
| `-atime -1` | 1天内访问过 |
| `-ctime -7` | 7天内权限/属性改变过 |

```bash
# 查找7天内修改过的文件
find /var/log -type f -mtime -7

# 查找超过30天未修改的文件
find /tmp -type f -mtime +30

# 查找今天修改过的文件
find /home -type f -mtime 0
```

### 按权限查找

```bash
# 查找权限为 777 的文件（危险权限）
find / -type f -perm 777

# 查找所有者可执行的文件
find /home -type f -perm -u+x

# 查找其他人可写的文件（安全隐患）
find / -type f -perm -o+w
```

### 按所有者查找

```bash
# 查找属于 ty 用户的文件
find /home -user ty

# 查找属于 sudo 组的文件
find /etc -group sudo

# 查找没有所有者的文件
find / -nouser
```

### 组合条件

```bash
# AND：同时满足两个条件（默认）
find /home -type f -name "*.py"         # 是文件 AND 以 .py 结尾

# OR：满足任一条件
find /home -type f \( -name "*.py" -o -name "*.sh" \)

# NOT：排除条件
find /home -type f -not -name "*.py"    # 不是 .py 文件

# 查找并排除目录
find /home -path "/home/ty/.git" -prune -o -type f -print
```

### 查找并执行操作

```bash
# 查找并删除（-delete）
find /tmp -type f -name "*.tmp" -delete

# 查找并执行命令（-exec）
find /home -type f -name "*.log" -exec rm {} \;
# {} 代表找到的每个文件，\; 表示命令结束

# 查找并移动
find /tmp -type f -name "*.bak" -exec mv {} /backup/ \;

# 查找并修改权限
find /var/www -type d -exec chmod 755 {} \;
find /var/www -type f -exec chmod 644 {} \;

# 查找并列出详细信息（-ls）
find /home -type f -name "*.py" -ls
```

### 常用组合示例

```bash
# 1. 查找大文件并按大小排序
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null | sort -k5 -h

# 2. 查找最近7天修改过的配置文件
find /etc -type f -name "*.conf" -mtime -7

# 3. 查找可被所有人写的文件（安全隐患）
find / -type f -perm -o+w 2>/dev/null

# 4. 查找 SUID/SGID 文件（特权文件，安全审计）
find / -type f \( -perm -4000 -o -perm -2000 \) 2>/dev/null

# 5. 清理超过30天的日志文件
find /var/log -type f -name "*.log" -mtime +30 -delete

# 6. 查找并压缩所有 .log 文件
find /var/log -type f -name "*.log" -exec gzip {} \;
```

### 输出重定向

```bash
# 将结果输出到文件
find /home -type f -name "*.py" > result.txt

# 忽略权限错误
find / -name "config" 2>/dev/null

# 统计找到的文件数量
find /home -type f -name "*.py" | wc -l
```

***

## 12. grep 与管道符 —— 文本过滤查找

### 管道符 `|`

管道符将前一个命令的**输出**作为后一个命令的**输入**，实现命令的串联。

```bash
# 基本格式
命令1 | 命令2 | 命令3
```

```bash
# 简单示例
cat /etc/passwd | grep "bash"     # 读取文件 → 过滤含 bash 的行
ls -la | grep ".txt"              # 列出文件 → 过滤含 .txt 的行
history | grep "ssh"              # 历史记录 → 过滤含 ssh 的行
```

### grep 基本语法

```bash
grep [选项] "匹配内容" 文件/输入
```

### 常用选项

| 选项 | 说明 |
|------|------|
| `-i` | 忽略大小写 |
| `-n` | 显示行号 |
| `-v` | 反向匹配（显示不匹配的行） |
| `-r` | 递归搜索目录下所有文件 |
| `-c` | 只显示匹配的行数 |
| `-l` | 只显示包含匹配内容的文件名 |
| `-w` | 全词匹配 |
| `-A N` | 显示匹配行**后**N行 |
| `-B N` | 显示匹配行**前**N行 |
| `-C N` | 显示匹配行**前后**N行 |
| `--color` | 高亮显示匹配内容 |

### 基本用法

```bash
# 在文件中搜索
grep "root" /etc/passwd

# 忽略大小写
grep -i "error" /var/log/syslog

# 显示行号
grep -n "root" /etc/passwd

# 反向匹配（排除）
grep -v "nologin" /etc/passwd

# 递归搜索目录
grep -r "TODO" /home/ty/project/

# 全词匹配（不会匹配到 "rooted" 中的 "root"）
grep -w "root" /etc/passwd
```

### 正则表达式匹配

```bash
# 以 xxx 开头
grep "^root" /etc/passwd

# 以 xxx 结尾
grep "bash$" /etc/passwd

# 匹配任意单个字符
grep "r..t" /etc/passwd

# 匹配多个任意字符
grep "ro*t" /etc/passwd

# 匹配多个选项之一
grep -E "error|warning|critical" /var/log/syslog

# 匹配 IP 地址（简单模式）
grep -E "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" /var/log/nginx/access.log
```

### 上下文显示

```bash
# 显示匹配行及其后3行
grep -A 3 "error" /var/log/syslog

# 显示匹配行及其前3行
grep -B 3 "error" /var/log/syslog

# 显示匹配行及其前后各3行
grep -C 3 "error" /var/log/syslog
```

### 管道符组合用法

#### 多级过滤

```bash
# 查找可登录的 root 用户
cat /etc/passwd | grep "bash" | grep "root"

# 查找占用内存最多的进程
ps aux | sort -k4 -r | head -5

# 查找大于 10MB 的文件
find / -type f -size +10M 2>/dev/null | head -20
```

#### 统计与排序

```bash
# 统计日志中 ERROR 出现的次数
cat /var/log/syslog | grep "ERROR" | wc -l

# 统计访问日志中各 IP 的访问次数（排序）
cat /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -r

# 统计文件行数
cat file.txt | wc -l

# 查看进程数量
ps aux | wc -l
```

#### 提取与处理

```bash
# 提取用户名列表
cat /etc/passwd | cut -d: -f1

# 提取可登录的用户名
cat /etc/passwd | grep "bash" | cut -d: -f1

# 提取最近5条 ssh 相关命令
history | grep "ssh" | tail -5

# 查看占用 CPU 最高的 5 个进程
ps aux | sort -k3 -r | head -5
```

### 实际应用场景

```bash
# 1. 实时监控并过滤日志
tail -F /var/log/syslog | grep "error"

# 2. 查找配置文件中的某项配置
grep -r "listen" /etc/nginx/ | grep -v "#"

# 3. 查找包含敏感信息的文件
grep -r "password" /var/www/ --include="*.php"

# 4. 查找异常登录记录
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -r

# 5. 查看特定服务的进程
ps aux | grep "nginx" | grep -v grep

# 6. 查看端口占用情况
ss -tlnp | grep ":80"

# 7. 查找文件中的 TODO 注释
grep -rn "TODO\|FIXME\|HACK" /home/ty/project/ --include="*.py"
```

### 常用命令组合速查

| 需求 | 命令 |
|------|------|
| 查找可登录用户 | `cat /etc/passwd \| grep "bash" \| cut -d: -f1` |
| 查看占用内存前5 | `ps aux \| sort -k4 -r \| head -5` |
| 统计错误日志条数 | `grep "error" /var/log/syslog \| wc -l` |
| 查找某 IP 的请求 | `grep "192.168.1.1" /var/log/nginx/access.log` |
| 查看端口占用 | `ss -tlnp \| grep ":443"` |
| 查找大文件 | `du -sh /* 2>/dev/null \| sort -r \| head -10` |
| 实时监控错误 | `tail -F /var/log/syslog \| grep -i "error"` |

***

## 13. tar 命令 —— 文件打包与压缩

### 基本概念

| 概念 | 说明 |
|------|------|
| 打包（tar） | 将多个文件/目录合并为一个文件（`.tar`），不压缩 |
| 压缩（gzip） | 对文件进行压缩，减小体积（`.tar.gz`） |
| 解压 | 将压缩文件还原为原始文件 |

### 基本语法

```bash
tar [选项] 文件名.tar.gz [要打包的文件/目录]
```

### 常用选项

| 选项 | 说明 |
|------|------|
| `-c` | **创建**压缩包 |
| `-x` | **解压**压缩包 |
| `-v` | 显示详细过程（verbose） |
| `-f` | **指定文件名**（必须放在最后） |
| `-z` | 使用 **gzip** 压缩/解压（`.tar.gz`） |
| `-j` | 使用 **bzip2** 压缩/解压（`.tar.bz2`） |
| `-J` | 使用 **xz** 压缩/解压（`.tar.xz`） |
| `-t` | 查看压缩包内容（不解压） |
| `-C` | 指定解压目标目录 |
| `--exclude` | 排除指定文件/目录 |

### 打包压缩

```bash
# 打包并用 gzip 压缩
tar -czvf archive.tar.gz /home/ty/project/

# 打包并用 bzip2 压缩（压缩率更高，速度更慢）
tar -cjvf archive.tar.bz2 /home/ty/project/

# 打包并用 xz 压缩（压缩率最高）
tar -cJvf archive.tar.xz /home/ty/project/

# 打包多个文件/目录
tar -czvf backup.tar.gz file1.txt file2.txt /home/ty/docs/

# 打包时不显示过程（去掉 -v）
tar -czf archive.tar.gz /home/ty/project/

# 排除某些文件
tar -czvf backup.tar.gz --exclude="*.log" --exclude=".git" /home/ty/project/
```

### 解压

```bash
# 解压 .tar.gz 文件
tar -xzvf archive.tar.gz

# 解压 .tar.bz2 文件
tar -xjvf archive.tar.bz2

# 解压 .tar.xz 文件
tar -xJvf archive.tar.xz

# 解压到指定目录
tar -xzvf archive.tar.gz -C /opt/

# 解压单个文件
tar -xzvf archive.tar.gz path/to/file.txt
```

### 查看压缩包内容

```bash
# 查看 .tar.gz 中的文件列表
tar -tzvf archive.tar.gz

# 查看并过滤
tar -tzvf archive.tar.gz | grep "config"

# 查看压缩包大小
ls -lh archive.tar.gz
```

### 常见压缩格式速查

| 格式 | 创建 | 解压 | 说明 |
|------|------|------|------|
| `.tar.gz` / `.tgz` | `-czvf` | `-xzvf` | 最常用，gzip 压缩 |
| `.tar.bz2` | `-cjvf` | `-xjvf` | 压缩率更高 |
| `.tar.xz` | `-cJvf` | `-xJvf` | 压缩率最高 |
| `.tar` | `-cvf` | `-xvf` | 仅打包，不压缩 |
| `.gz` | `gzip file` | `gunzip file.gz` | 单文件压缩 |
| `.zip` | `zip -r a.zip dir/` | `unzip a.zip` | 兼容 Windows |

### 实际应用场景

```bash
# 1. 备份网站目录
tar -czvf /backup/site_$(date +%Y%m%d).tar.gz /var/www/html/

# 2. 备份配置文件
tar -czvf /backup/etc_$(date +%Y%m%d).tar.gz /etc/

# 3. 排除日志和缓存打包
tar -czvf project.tar.gz --exclude="*.log" --exclude="__pycache__" /home/ty/project/

# 4. 解压软件包到 /opt
tar -xzvf software.tar.gz -C /opt/

# 5. 查看压缩包内容再决定是否解压
tar -tzvf archive.tar.gz | head -20

# 6. 从压缩包中提取单个文件
tar -xzvf backup.tar.gz etc/nginx/nginx.conf

# 7. 增量打包（只打包修改过的文件）
tar -czvf incremental.tar.gz --newer-mtime="2025-07-01" /home/ty/project/
```

### -f 为什么必须放最后

```bash
# 正确：-f 后紧跟文件名
tar -czvf backup.tar.gz /home/

# 错误：-f 放中间会把后面的参数当文件名
tar -c -f -zvf backup.tar.gz /home/
# ↑ 会把 -zvf 当作文件名
```

### 解压其他格式

```bash
# 解压 .zip 文件
unzip archive.zip
unzip archive.zip -d /opt/

# 解压 .gz 文件（单文件）
gunzip file.gz

# 解压 .bz2 文件
bunzip2 file.bz2

# 解压 .xz 文件
unxz file.xz
```

***

## 14. 网络管理命令

### 网络信息查看

```bash
# 查看网络接口信息
ip addr                  # 推荐
ifconfig                 # 旧版，部分系统需安装 net-tools

# 查看路由表
ip route
route -n

# 查看 DNS 配置
cat /etc/resolv.conf

# 查看主机名
hostname
hostname -I              # 显示 IP 地址
```

### 网络连通性测试

```bash
# 测试网络连通
ping -c 4 baidu.com      # 发送4个包后停止

# 测试 DNS 解析
nslookup baidu.com
dig baidu.com

# 追踪路由路径
traceroute baidu.com

# 检查端口是否可达
telnet 192.168.1.1 80
nc -zv 192.168.1.1 80    # 更推荐
```

### 端口与连接查看

```bash
# 查看所有监听端口（推荐）
ss -tlnp

# 查看所有 TCP 连接
ss -tnp

# 查看所有网络连接
ss -anp

# 查看指定端口
ss -tlnp | grep ":80"

# 旧版命令（net-tools）
netstat -tlnp            # 查看监听端口
netstat -anp             # 查看所有连接
netstat -tlnp | grep ":22"
```

| 选项 | 说明 |
|------|------|
| `-t` | TCP 连接 |
| `-u` | UDP 连接 |
| `-l` | 仅显示监听状态 |
| `-n` | 显示数字地址（不解析域名） |
| `-p` | 显示进程信息 |

### 网络配置

```bash
# 启用/禁用网络接口
sudo ip link set eth0 up
sudo ip link set eth0 down

# 设置 IP 地址
sudo ip addr add 192.168.1.100/24 dev eth0

# 删除 IP 地址
sudo ip addr del 192.168.1.100/24 dev eth0

# 添加默认网关
sudo ip route add default via 192.168.1.1

# 修改 DNS
sudo echo "nameserver 8.8.8.8" >> /etc/resolv.conf
```

### 防火墙（ufw）

```bash
# 查看防火墙状态
sudo ufw status

# 启用/禁用防火墙
sudo ufw enable
sudo ufw disable

# 允许端口
sudo ufw allow 80/tcp
sudo ufw allow 22/tcp
sudo ufw allow from 192.168.1.0/24 to any port 3306

# 拒绝端口
sudo ufw deny 23/tcp

# 删除规则
sudo ufw delete allow 80/tcp
```

### 网络安全排查

```bash
# 1. 查看异常监听端口
ss -tlnp | grep -v "127.0.0.1"

# 2. 查看异常外部连接
ss -tnp | grep ESTAB | grep -v "127.0.0.1"

# 3. 查看高流量连接
iftop                      # 需安装 iftop

# 4. 查看 ARP 表（检测 ARP 欺骗）
arp -a

# 5. 抓包分析
tcpdump -i eth0 port 80
tcpdump -i eth0 -w capture.pcap
```

***

## 15. 进程管理命令

### 查看进程

```bash
# 查看所有进程
ps aux                     # BSD 风格（推荐）
ps -ef                     # UNIX 风格

# 查看特定进程
ps aux | grep nginx
ps aux | grep python

# 查看进程树
pstree
pstree -p                  # 显示 PID

# 实时查看进程（类似任务管理器）
top
htop                       # 更美观（需安装）
```

### ps aux 输出说明

```bash
ps aux
```

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 169436 13200 ?        Ss   Jul20   0:03 /sbin/init
www-data   543  0.2  1.5 234560 31200 ?        S    Jul20   1:20 nginx: worker
```

| 字段 | 说明 |
|------|------|
| USER | 进程所有者 |
| PID | 进程 ID |
| %CPU | CPU 使用率 |
| %MEM | 内存使用率 |
| VSZ | 虚拟内存大小 |
| RSS | 实际物理内存大小 |
| STAT | 进程状态（S=休眠, R=运行, Z=僵尸, +=前台进程） |
| COMMAND | 启动命令 |

### 终止进程

```bash
# 发送终止信号（优雅终止，推荐）
kill PID
kill -15 PID              # 等同于 kill PID

# 强制终止
kill -9 PID               # 强制杀死，不可被捕获

# 按名称终止
killall nginx
pkill nginx

# 按名称模式终止
pkill -f "python app.py"

# 终止所有同名进程
killall -9 python
```

| 信号 | 编号 | 说明 |
|------|------|------|
| SIGHUP | 1 | 挂起信号 |
| SIGINT | 2 | 中断信号（Ctrl+C） |
| SIGTERM | 15 | 终止信号（默认，可被捕获） |
| SIGKILL | 9 | 强制终止（不可被捕获） |
| SIGSTOP | 19 | 暂停进程（Ctrl+Z） |
| SIGCONT | 18 | 继续运行暂停的进程 |

### 前后台管理

```bash
# 将当前任务放到后台（暂停）
Ctrl + Z

# 查看后台任务
jobs

# 将后台任务放到前台
fg %1                      # 将任务号为1的任务放到前台

# 让后台暂停的任务继续运行
bg %1

# 后台运行命令（不占用终端）
nohup python app.py &

# 后台运行并输出到文件
nohup python app.py > output.log 2>&1 &
```

### 系统资源监控

```bash
# 查看内存使用
free -h
free -m                    # 以 MB 显示

# 查看磁盘使用
df -h
df -h /home                # 查看特定分区

# 查看目录大小
du -sh /home/ty/
du -sh /var/log/*

# 查看 CPU 信息
lscpu
cat /proc/cpuinfo

# 查看系统负载
uptime
cat /proc/loadavg
```

### 服务管理（systemd）

```bash
# 查看服务状态
systemctl status nginx
systemctl status sshd

# 启动/停止/重启服务
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx

# 开机自启
sudo systemctl enable nginx
sudo systemctl disable nginx

# 查看所有服务状态
systemctl list-units --type=service

# 查看失败的服务
systemctl --failed
```

### 定时任务（cron）

```bash
# 编辑定时任务
crontab -e

# 查看当前用户的定时任务
crontab -l

# 定时任务格式：
# 分 时 日 月 周 命令
# *  *  *  *  *  command
```

| 示例 | 说明 |
|------|------|
| `0 2 * * * /backup.sh` | 每天凌晨2点执行 |
| `*/5 * * * * /check.sh` | 每5分钟执行 |
| `0 0 * * 0 /clean.sh` | 每周日0点执行 |
| `0 9 1 * * /report.sh` | 每月1号9点执行 |

```bash
# 定时备份数据库（每天凌晨3点）
0 3 * * * /usr/bin/mysqldump -u root mydb > /backup/db_$(date +\%Y\%m\%d).sql

# 定时清理日志（每周日凌晨）
0 0 * * 0 find /var/log -name "*.log" -mtime +30 -delete
```

### 安全相关

```bash
# 1. 查找异常进程（高 CPU 使用率）
ps aux --sort=-%cpu | head -10

# 2. 查找异常进程（高内存使用率）
ps aux --sort=-%mem | head -10

# 3. 查找僵尸进程
ps aux | grep "Z"

# 4. 查找隐藏进程（与 /proc 对比）
ps aux | wc -l
ls /proc | grep -E "^[0-9]" | wc -l

# 5. 查找挖矿进程（异常高 CPU）
top -b -n 1 | head -20

# 6. 查看进程打开的文件
lsof -p PID
lsof -i :80               # 查看占用80端口的进程
```

***

*持续更新中...*
