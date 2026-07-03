# 第二天：操作系统安全配置

---

## 学习目标

- 掌握Linux用户安全检测方法
- 学会检查空密码用户和UID为0的用户
- 理解/etc/passwd和/etc/shadow文件结构
- 掌握系统安全审计技巧

---

## 一、Linux用户安全检测

### 1.1 检测用户密码是否为空

**方法1：查看/etc/shadow文件**
```bash
# 查看密码字段（第二个字段）
# 空密码表示为 !! 或 空字段
sudo cat /etc/shadow | awk -F: '($2 == "" || $2 == "!!") {print $1}'
```

**方法2：使用passwd命令检查**
```bash
# 查看密码状态
passwd -S username

# 输出示例：
# username P 2024-01-01 0 99999 7 -1
# P = 设置密码
# L = 锁定
# NP = 无密码（空密码）
```

**方法3：批量检查空密码用户**
```bash
# 检查所有空密码用户
sudo awk -F: '($2 == "" || $2 == "!") {print $1}' /etc/shadow

# 或者
sudo awk -F: '($2 == "!!" || $2 == "*" || $2 == "") {print $1, "无密码或锁定"}' /etc/shadow
```

### 1.2 检测UID为0的用户

**方法1：直接查找UID为0的用户**
```bash
# 查找UID为0的用户（应该是只有root）
awk -F: '$3 == 0 {print $1}' /etc/passwd
```

**方法2：详细查看UID为0的用户信息**
```bash
# 显示UID为0用户的详细信息
awk -F: '$3 == 0 {print "用户名:", $1, "UID:", $3, "Shell:", $7}' /etc/passwd
```

**方法3：检查非root的UID为0用户（安全隐患）**
```bash
# 查找UID为0但不是root的用户（后门用户）
awk -F: '$3 == 0 && $1 != "root" {print $1}' /etc/passwd
```

### 1.3 综合安全检测脚本

```bash
#!/bin/bash
echo "=== Linux用户安全检测 ==="

echo -e "\n1. 检测空密码用户:"
awk -F: '($2 == "" || $2 == "!!" || $2 == "!") {print "  警告: 用户 " $1 " 无密码或已锁定"}' /etc/shadow

echo -e "\n2. 检测UID为0的用户:"
awk -F: '$3 == 0 {print "  用户: " $1 " (UID=0)"}' /etc/passwd

echo -e "\n3. 检测非root的UID为0用户（潜在后门）:"
awk -F: '$3 == 0 && $1 != "root" {print "  危险: 用户 " $1 " 拥有root权限!"}' /etc/passwd

echo -e "\n4. 检测可登录的系统用户:"
awk -F: '$3 >= 1000 && $3 < 65534 && $7 != "/sbin/nologin" {print "  可登录用户: " $1 " (UID=" $3 ")"}' /etc/passwd
```

### 1.4 相关文件结构说明

**/etc/passwd文件格式：**
```
用户名:密码占位:UID:GID:注释:家目录:Shell
root:x:0:0:root:/root:/bin/bash
```

**/etc/shadow文件格式：**
```
用户名:加密密码:最后修改:最小天数:最大天数:警告天数:失效天数:保留
root:$6$xxx:19000:0:99999:7:::
```

**密码字段含义：**
```
空或!!  - 无密码/未设置
*       - 账户锁定
$6$xxx  - SHA-512加密密码
!       - 密码已锁定
```

### 1.5 密码复杂度查看与配置

**查看当前密码策略：**
```bash
# 查看pwquality配置
cat /etc/security/pwquality.conf

# 或查看非注释内容
grep -v "^#" /etc/security/pwquality.conf | grep -v "^$"

# 查看密码过期策略
grep -E "^PASS_" /etc/login.defs

# 查看用户密码过期信息
chage -l username
```

**pwquality.conf配置参数：**
```bash
# 编辑配置文件
sudo vi /etc/security/pwquality.conf

# 主要参数：
minlen = 8          # 最小密码长度
dcredit = -1        # 至少包含1个数字
ucredit = -1        # 至少包含1个大写字母
lcredit = -1        # 至少包含1个小写字母
ocredit = -1        # 至少包含1个特殊字符
minclass = 3        # 至少包含3种字符类型
maxrepeat = 3       # 最多连续重复3个字符
maxclassrepeat = 3  # 最多连续3个同类字符
```

**login.defs密码策略：**
```bash
# 查看配置
grep -E "^PASS_" /etc/login.defs

# 主要参数：
PASS_MAX_DAYS   90    # 密码最长使用天数
PASS_MIN_DAYS   0     # 密码最短使用天数
PASS_MIN_LEN    8     # 密码最小长度
PASS_WARN_AGE   7     # 密码过期警告天数
```

**PAM模块配置：**
```bash
# Ubuntu/Debian
grep pam_pwquality /etc/pam.d/common-password

# CentOS/RHEL
grep pam_pwquality /etc/pam.d/system-auth
```

**密码策略检查脚本：**
```bash
#!/bin/bash
echo "=== 密码策略检查 ==="

echo -e "\n1. pwquality配置:"
grep -v "^#" /etc/security/pwquality.conf | grep -v "^$"

echo -e "\n2. 密码过期策略:"
grep -E "^PASS_" /etc/login.defs

echo -e "\n3. PAM密码模块配置:"
grep pam_pwquality /etc/pam.d/common-password 2>/dev/null || \
grep pam_pwquality /etc/pam.d/system-auth 2>/dev/null

echo -e "\n4. 当前用户密码状态:"
chage -l $(whoami) 2>/dev/null || echo "无法获取"
```

### 1.6 Ubuntu新创建用户

**基本创建：**
```bash
# 交互式创建用户（推荐，会提示设置密码和填写信息）
sudo adduser username

# 非交互式创建用户
sudo useradd -m -s /bin/bash username
# -m：自动创建家目录
# -s：指定登录shell
```

**示例1：交互式创建用户**
```bash
$ sudo adduser testuser
Adding user `testuser' ...
Adding new group `testuser' (1001) ...
Adding new user `testuser' (1001) with group `testuser' ...
Creating home directory `/home/testuser' ...
Copying files from `/etc/skel' ...
New password:                  # 输入密码
Retype new password:           # 确认密码
passwd: password updated successfully
Changing the user information for testuser
Enter the new value, or press ENTER for the default
	Full Name []: Test User
	Room Number []: 101
	Work Phone []: 
	Home Phone []: 
	Other []: 
Is the information correct? [Y/n] Y
```

**示例2：非交互式创建用户**
```bash
# 创建用户并指定shell
$ sudo useradd -m -s /bin/bash newuser
$ echo "newuser:123456" | sudo chpasswd   # 设置密码

# 验证创建结果
$ cat /etc/passwd | grep newuser
newuser:x:1002:1002::/home/newuser:/bin/bash

$ ls -la /home/newuser/
total 20
drwxr-xr-x 2 newuser newuser 4096 Jun 29 10:00 .
drwxr-xr-x 3 root    root    4096 Jun 29 10:00 ..
-rw-r--r-- 1 newuser newuser  220 Jun 29 10:00 .bash_logout
-rw-r--r-- 1 newuser newuser 3771 Jun 29 10:00 .bashrc
-rw-r--r-- 1 newuser newuser  807 Jun 29 10:00 .profile
```

**创建用户并设置密码：**
```bash
# 创建用户
sudo useradd -m username

# 设置密码
sudo passwd username
```

**示例3：设置密码并验证**
```bash
$ sudo passwd testuser
New password: ********
Retype new password: ********
passwd: password updated successfully

# 查看密码状态
$ sudo passwd -S testuser
testuser P 2024-06-29 0 99999 7 -1

# P = 已设置密码
# L = 账户锁定
# NP = 无密码
```

**赋予sudo权限：**
```bash
# 将用户加入sudo组
sudo usermod -aG sudo username

# 或编辑sudoers文件
sudo visudo
# 添加：username ALL=(ALL:ALL) ALL
```

**示例4：赋予sudo权限并验证**
```bash
# 将testuser加入sudo组
$ sudo usermod -aG sudo testuser

# 验证sudo权限
$ groups testuser
testuser : testuser sudo

# 测试sudo权限
$ su - testuser
$ sudo whoami
[sudo] password for testuser: ********
root
```

**查看创建的用户：**
```bash
# 查看所有用户
cat /etc/passwd | tail -5

# 查看用户ID和组
id username
groups username

# 查看用户密码过期信息
chage -l username
```

**示例5：查看用户详细信息**
```bash
# 查看用户ID
$ id testuser
uid=1001(testuser) gid=1001(testuser) groups=1001(testuser),27(sudo)

# 查看用户组
$ groups testuser
testuser : testuser sudo

# 查看密码过期信息
$ sudo chage -l testuser
Last password change                : Jun 29, 2024
Password expires                    : never
Password inactive                   : never
Account expires                     : never
Minimum number of days between password change : 0
Maximum number of days between password change : 99999
Number of days of warning before password expires : 7
```

**删除用户：**
```bash
# 删除用户（保留家目录）
sudo deluser username

# 删除用户（同时删除家目录）
sudo userdel -r username
```

**示例6：删除用户并验证**
```bash
# 删除testuser（保留家目录）
$ sudo deluser testuser
Removing user `testuser' ...
Warning: group `testuser' has no more members.
Done.

# 验证用户已删除
$ cat /etc/passwd | grep testuser
（无输出）

# 家目录仍然存在
$ ls /home/
testuser  newuser
```

**常用参数说明：**
```
-m          自动创建家目录
-s          指定shell（/bin/bash、/bin/sh、/sbin/nologin）
-g          指定主组
-G          指定附加组
-d          指定家目录路径
-e          设置账户过期日期
```

### 1.7 安全建议

```
1. 确保只有root用户UID为0
2. 禁止空密码用户存在
3. 定期检查/etc/passwd和/etc/shadow
4. 使用强密码策略
5. 禁用不必要的系统账户
```

---

## 二、Linux文件权限安全

### 2.1 关键文件权限检查

```bash
# 检查/etc/passwd权限（应为644）
ls -la /etc/passwd

# 检查/etc/shadow权限（应为640或600）
ls -la /etc/shadow

# 检查/etc/group权限
ls -la /etc/group
```

### 2.2 SUID/SGID文件检测

```bash
# 查找SUID文件（可能存在提权风险）
find / -perm -4000 -type f 2>/dev/null

# 查找SGID文件
find / -perm -2000 -type f 2>/dev/null

# 查找所有SUID/SGID文件
find / -perm /6000 -type f 2>/dev/null
```

### 2.3 可写文件检测

```bash
# 查找全局可写文件
find / -perm -o+w -type f 2>/dev/null

# 查找全局可写目录
find / -perm -o+w -type d 2>/dev/null
```

---

## 三、Linux服务安全

### 3.1 检查运行服务

```bash
# 查看所有运行的服务
systemctl list-units --type=service --state=running

# 检查特定服务状态
systemctl status sshd
systemctl status firewalld
```

### 3.2 检查开放端口

```bash
# 查看监听的端口
netstat -tuln
# 或
ss -tuln

# 检查特定端口
netstat -tuln | grep :22
netstat -tuln | grep :80
```

### 3.3 防火墙配置检查

```bash
# 查看防火墙规则（iptables）
iptables -L -n

# 查看防火墙规则（firewalld）
firewall-cmd --list-all
```

---

## 四、Linux日志审计

### 4.1 关键日志文件

```
/var/log/auth.log      - 认证日志（Debian/Ubuntu）
/var/log/secure        - 认证日志（CentOS/RHEL）
/var/log/messages      - 系统日志
/var/log/syslog        - 系统日志
/var/log/cron          - 定时任务日志
```

### 4.2 登录日志检查

```bash
# 查看登录成功记录
last

# 查看登录失败记录
lastb

# 查看当前登录用户
who

# 查看最近登录历史
lastlog
```

### 4.3 日志分析命令

```bash
# 查看SSH登录失败记录
grep "Failed password" /var/log/auth.log

# 查看SSH登录成功记录
grep "Accepted password" /var/log/auth.log

# 查看sudo使用记录
grep "sudo:" /var/log/auth.log

# 统计登录失败次数
grep "Failed password" /var/log/auth.log | wc -l
```

---

## 五、Linux安全加固建议

### 5.1 账户安全

```
1. 禁用root远程登录
2. 使用普通用户+sudo方式
3. 设置密码复杂度策略
4. 定期更换密码
5. 锁定长时间未使用的账户
```

### 5.2 SSH安全配置

```bash
# 编辑SSH配置文件
vi /etc/ssh/sshd_config

# 安全配置建议：
PermitRootLogin no           # 禁止root登录
PasswordAuthentication no    # 禁用密码认证（使用密钥）
MaxAuthTries 3               # 最大尝试次数
LoginGraceTime 60            # 登录超时时间
AllowUsers user1 user2       # 允许特定用户登录
```

### 5.3 系统更新

```bash
# CentOS/RHEL
yum update

# Ubuntu/Debian
apt update && apt upgrade
```

---

## 常用命令速查

### 用户管理命令
```bash
# 查看用户信息
cat /etc/passwd
cat /etc/shadow

# 查看用户密码状态
passwd -S username

# 锁定/解锁用户
passwd -l username    # 锁定
passwd -u username    # 解锁

# 删除用户
userdel username
userdel -r username   # 同时删除家目录
```

### 权限检查命令
```bash
# 查看文件权限
ls -la /etc/passwd
ls -la /etc/shadow

# 修改文件权限
chmod 644 /etc/passwd
chmod 640 /etc/shadow

# 查找SUID文件
find / -perm -4000 -type f 2>/dev/null
```

### 日志查看命令
```bash
# 实时查看日志
tail -f /var/log/auth.log

# 搜索关键字
grep "Failed" /var/log/auth.log

# 统计数量
grep "Failed" /var/log/auth.log | wc -l
```

---

## 学习资源

### 在线资源
- Linux安全加固指南：https://wiki.centos.org/HowTos/OS_Protection
- SSH安全配置：https://www.ssh.com/academy/ssh/sshd_config
- Linux安全最佳实践：https://www.cisecurity.org/benchmark/linux

### 推荐书籍
- 《Linux系统安全：纵深防御、快速检测与恢复》
- 《Linux安全技术详解》
- 《UNIX/Linux系统管理技术手册》

---

## 总结

第二天的学习重点：
1. **用户安全检测**：掌握空密码和UID为0用户的检测方法
2. **文件权限安全**：理解关键文件权限和SUID/SGID风险
3. **服务安全**：学会检查运行服务和开放端口
4. **日志审计**：掌握日志分析和安全事件追踪
5. **安全加固**：了解Linux系统安全配置最佳实践

通过今天的学习，你将具备Linux系统安全检测和加固的基础能力。
