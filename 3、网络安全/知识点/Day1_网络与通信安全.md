# 第一天：网络与通信安全

---

## 学习目标

- 掌握常见应用层协议的工作原理
- 学会使用SSH安全连接网络设备
- 理解TCP/UDP攻击原理及防护方法
- 掌握三层交换机VLAN配置
- 学会使用端口镜像进行流量监控
- 掌握ACL访问控制配置
- 学会使用Wireshark进行流量分析

---

## 一、应用层协议串讲

### 1.1 HTTP/HTTPS协议

**HTTP协议特点：**
```
- 明文传输，不加密
- 默认端口：80
- 无状态协议
- 请求/响应模型
```

**HTTP请求结构：**
```http
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

**HTTP响应结构：**
```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

**HTTPS协议：**
```
- HTTP + SSL/TLS加密
- 默认端口：443
- 证书验证机制
- 数据加密传输
```

**常见状态码：**
```
200 OK                    - 请求成功
301 Moved Permanently     - 永久重定向
302 Found                 - 临时重定向
400 Bad Request           - 请求错误
401 Unauthorized          - 未授权
403 Forbidden             - 禁止访问
404 Not Found             - 未找到
500 Internal Server Error - 服务器内部错误
```

### 1.2 FTP协议

**FTP工作原理：**
```
- 文件传输协议
- 默认端口：20(数据)、21(控制)
- 主动模式 vs 被动模式
- 明文传输用户名密码
```

**主动模式(Active)：**
```
客户端 -> 服务器: 21端口(控制连接)
服务器 -> 客户端: 20端口(数据连接)
```

**被动模式(Passive)：**
```
客户端 -> 服务器: 21端口(控制连接)
客户端 -> 服务器: 随机端口(数据连接)
```

**主动模式与被动模式区别：**
```
主动模式(Active)：
- 服务器主动从20端口发起数据连接到客户端
- 客户端防火墙可能阻止入站连接
- 适用于客户端无防火墙限制的场景

被动模式(Passive)：
- 客户端主动发起数据连接到服务器的随机端口
- 解决客户端防火墙阻止入站连接的问题
- 现代FTP客户端默认使用被动模式
- 更安全且能穿透防火墙
```

**FTP安全风险：**
```
- 明文传输用户名和密码
- 数据传输未加密
- 建议使用SFTP(SSH文件传输)或FTPS(FTP over SSL)替代
```

### 1.3 SMTP/POP3/IMAP协议

**邮件协议对比：**
```
SMTP  - 发送邮件，端口25/587
POP3  - 接收邮件，端口110，下载后删除服务器邮件
IMAP  - 接收邮件，端口143，同步服务器邮件
```

### 1.4 DNS协议

**DNS解析流程：**
```
1. 浏览器缓存
   - 浏览器首先检查自身DNS缓存
   - 缓存时间由TTL值决定
   - 命中则直接返回IP地址

2. 系统hosts文件
   - 检查操作系统本地hosts文件（Windows: C:\Windows\System32\drivers\etc\hosts）
   - 静态域名映射，优先级高于DNS服务器
   - 常用于本地开发和屏蔽广告

3. 本地DNS服务器
   - 网络配置中指定的DNS服务器（如运营商DNS）
   - 负责递归查询，代替客户端完成解析
   - 会缓存查询结果，提高解析效率

4. 根DNS服务器
   - 全球共13组根服务器（A-M）
   - 负责返回顶级域服务器地址
   - 不直接解析域名，只指引查询方向

5. 顶级域DNS服务器
   - 管理特定顶级域（如.com、.cn、.org）
   - 返回该域名的权威DNS服务器地址
   - 例如：查询www.example.com，返回example.com的权威服务器

6. 权威DNS服务器
   - 域名的最终管理者
   - 存储该域名的所有DNS记录
   - 返回最终的IP地址解析结果
```

**DNS查询类型：**
```
A记录     - 域名到IPv4
AAAA记录  - 域名到IPv6
CNAME记录 - 域名别名
MX记录    - 邮件交换
NS记录    - 域名服务器
PTR记录   - 反向解析
```

**DNS协议特点：**
```
- 使用UDP 53端口进行查询
- 使用TCP 53端口进行区域传送
- 明文传输，易被监听和篡改
- 无加密和认证机制
```

**DNS安全威胁：**
```
1. DNS劫持：篡改DNS解析结果，引导用户到恶意网站
2. DNS缓存投毒：污染DNS缓存，影响后续解析
3. DNS放大攻击：利用DNS响应进行DDoS攻击
4. DNS隧道：利用DNS协议进行数据外泄
```

**DNS安全防护：**
```
1. DNSSEC：DNS安全扩展，提供数据完整性验证
2. DoH (DNS over HTTPS)：加密DNS查询
3. DoT (DNS over TLS)：使用TLS加密DNS
4. 使用可信的DNS服务器（如8.8.8.8、114.114.114.114）
```

### 1.5 DHCP协议

**DHCP工作流程：**
```
1. DHCP Discover - 客户端广播发现
2. DHCP Offer    - 服务器提供IP
3. DHCP Request  - 客户端请求IP
4. DHCP ACK      - 服务器确认分配
```

---

## 二、SSH实操训练

### 2.1 SSH协议原理

**SSH加密过程：**
```
1. 版本协商
2. 密钥交换(DH算法)
3. 服务器认证(主机密钥)
4. 会话密钥生成
5. 数据加密传输
```

**加密基本概念：**
```
明文（Plaintext）：原始可读的数据
密文（Ciphertext）：加密后不可读的数据

传输过程：
客户端 --[明文]--> 加密 --[密文]--> 网络传输 --[密文]--> 解密 --[明文]--> 服务器

为什么需要加密：
- 网络传输中数据可能被黑客截获
- 黑客抓包获取的是密文，无法直接读取
- 没有密钥无法将密文还原为明文
- 保证数据的机密性和完整性
```

**对称加密（Symmetric Encryption）：**
```
定义：加密和解密使用相同的密钥

工作流程：
客户端                           服务器
   |                               |
   |  [明文 + 密钥K] --> 加密算法 --> [密文]  |
   |                               |
   |  [密文] -----网络传输------> [密文]     |
   |                               |
   |  [密文] --> 解密算法 + 密钥K --> [明文]  |

常见对称加密算法：
- AES（高级加密标准）- 最常用，安全性高
- DES/3DES - 较老，已不推荐
- Blowfish/Twofish
- RC4 - 已不安全，不推荐使用

优点：加密解密速度快，适合大量数据加密
缺点：密钥分发困难，密钥管理复杂
```

**非对称加密（Asymmetric Encryption）：**
```
定义：使用一对密钥（公钥和私钥）

工作流程：
- 公钥：公开分享，用于加密
- 私钥：自己保存，用于解密

加密过程：
发送方用接收方的公钥加密 --> 接收方用自己的私钥解密

常见非对称加密算法：
- RSA：最常用，安全性高
- DSA：数字签名算法
- ECC：椭圆曲线加密，密钥更短

优点：解决了密钥分发问题
缺点：加密解密速度慢，不适合大量数据
```

**SSH混合加密机制：**
```
SSH采用混合加密结合两者优点：

1. 密钥交换阶段（非对称加密）：
   - 使用DH算法安全交换对称密钥
   - 解决对称加密的密钥分发问题

2. 数据传输阶段（对称加密）：
   - 使用交换的对称密钥加密数据
   - 保证加密解密速度

流程：
客户端 <--[非对称加密交换对称密钥]--> 服务器
         <--[对称加密传输数据]-->
```

**SSH安全性保障：**
```
为什么黑客无法破解：
1. 黑客只能截获密文
2. 对称密钥通过非对称加密安全交换
3. 没有密钥，密文无法还原为明文
4. 现代加密算法计算上不可破解
```

**SSH认证方式：**
```
- 密码认证：使用用户名密码
- 密钥认证：使用公私钥对（更安全）
```

### 2.2 eNSP实操：配置交换机SSH登录

**实验拓扑：**
```
[PC] ---- [交换机S5700]
```

**步骤1：配置交换机基本网络**
```bash
<Huawei>system-view
[Huawei]sysname SW1
[SW1]interface Vlanif 1          # 进入VLANIF 1接口配置模式（VLANIF是三层逻辑接口，用于VLAN间路由）
[SW1-Vlanif1]ip address 192.168.1.1 24  # 配置IP地址192.168.1.1，子网掩码24位（255.255.255.0）
[SW1-Vlanif1]quit
```

- 交换机的物理接口（如GigabitEthernet 0/0/1）默认工作在**二层（数据链路层）**，负责转发数据帧，**没有IP地址的概念**。
- **Vlanif（VLAN Interface）** 是一个**三层逻辑接口**。您配的IP `192.168.1.1`，实际上是这台交换机作为**网关**的地址。

**步骤2：生成RSA密钥对**

```bash
[SW1]rsa local-key-pair create
# 这条命令是在为交换机生成 RSA主机密钥对，它是开启SSH（安全远程登录）功能的核心前置步骤
# 密钥对包含一个私钥（交换机自己保密，用于解密）和一个公钥（发给SSH客户端，用于加密和验证身份）。有了它，后续SSH登录时的数据交互才是加密的，否则只能用不安全的Telnet
The key name will be: SW1_Host
The range of public key size is (2048 ~ 2048).
Input the bits in the modulus[default = 2048]:
Generating keys...
```

**步骤3：配置SSH用户**
```bash
[SW1]ssh user admin
# 在交换机本地创建名为 admin 的SSH用户
[SW1]ssh user admin authentication-type password
# 设置该用户的认证方式为密码认证
[SW1]ssh user admin service-type stelnet
# 设置该用户允许使用的SSH服务类型为 stelnet（即安全的Telnet，允许命令行登录）。
#补充：这是最常见的SSH服务类型。还有其他类型如 sftp（文件传输）或 all（全部），这里指定为 stelnet 相当于是给这个“工卡”授权了“仅允许命令行访问”的门禁权限。
```

**步骤4：配置VTY线路**

```bash
[SW1]user-interface vty 0 4
# 进入VTY（虚拟类型终端）线路视图，并指定线路编号范围
#VTY是交换机的“远程登录虚拟端口”。0 4 表示同时允许 5个用户（0、1、2、3、4）通过远程方式（Telnet或SSH）登录这台交换机。第6个用户尝试连接时会被拒绝
[SW1-ui-vty0-4]authentication-mode aaa
#设置这些VTY线路的认证模式为 AAA（认证、授权、计费）
#有人远程连接时，不要用简单的密码验证，去查我之前在AAA视图下配置的local-user账号密码表。”这条命令将您之前配置的AAA本地用户（含自定义用户名和密码）与远程登录通道绑定在了一起
[SW1-ui-vty0-4]protocol inbound ssh
#指定该VTY线路只允许 SSH 协议接入
[SW1-ui-vty0-4]quit
```

**步骤5：配置AAA认证**
```bash
[SW1]aaa
[SW1-aaa]local-user admin password cipher Huawei@123
#创建一个本地用户，用户名为 admin，密码为 Huawei@123，并使用 cipher（密文）方式存储。
#ssh user是系统视图，记录是哪些用户能够访问，以及他们用什么方式验证，local-user是AAA视图，登记了“admin”的真实身份证号（密码）和特权等级（权限15）
[SW1-aaa]local-user admin privilege level 15
#赋予该用户 权限等级15
[SW1-aaa]local-user admin service-type ssh
#限制该用户只能通过SSH方式登录
[SW1-aaa]quit
```

**步骤6：启用SSH服务**
```bash
[SW1]stelnet server enable
```

**步骤7：PC端SSH连接**
```bash
# 使用SecureCRT或PuTTY连接
# 主机：192.168.1.1
# 端口：22
# 用户名：admin
# 密码：Huawei@123
```

### 2.3 Wireshark抓包分析SSH

**实验步骤：**
```
1. 打开Wireshark，选择对应网卡
2. 设置过滤器：tcp.port == 22
3. 开始捕获
4. 使用SSH连接交换机
5. 观察SSH握手过程
```

**SSH握手过程分析：**
```
1. TCP三次握手
2. SSH版本协商
3. 密钥交换
4. 用户认证
5. 加密数据传输
```

---

## 三、TCP-SYN防护实操训练

### 3.1 TCP三次握手原理

**正常三次握手：**
```
客户端                服务器
  |---- SYN seq=x ------>|
  |<--- SYN+ACK seq=y ack=x+1 ---|
  |---- ACK ack=y+1 ---->|
  |      连接建立          |
```

**SYN Flood攻击原理：**
```
攻击者                服务器
  |---- SYN seq=x ------>|  (伪造源IP)
  |<--- SYN+ACK seq=y ack=x+1 ---|
  |                       |  (半连接队列满)
  |---- SYN seq=x2 ----->|  (持续发送)
  |<--- SYN+ACK seq=y2 ack=x2+1 ---|
  |                       |  (服务器资源耗尽)
```

### 3.2 eNSP实操：配置SYN Flood防护

**实验拓扑：**
```
[攻击者PC] ---- [防火墙USG6000] ---- [服务器PC]
```

**配置防火墙SYN Cookie防护：**
```bash
<USG6000>system-view
[USG6000]firewall defend syn-flood enable
[USG6000]firewall defend syn-flood zone trust threshold 1000
[USG6000]firewall defend syn-flood zone untrust threshold 1000
```

**配置连接数限制：**
```bash
[USG6000]firewall session-link-limit enable
[USG6000]firewall session-link-limit 100
```

### 3.3 Wireshark抓包分析SYN Flood

**过滤器设置：**
```
# 显示所有SYN包
tcp.flags.syn == 1 and tcp.flags.ack == 0

# 显示半连接
tcp.flags.syn == 1 and tcp.flags.ack == 0 and tcp.analysis.retransmission
```

**攻击特征识别：**
```
- 大量SYN包，无ACK完成握手
- 源IP地址随机或伪造
- 短时间内大量半连接
- 服务器响应SYN+ACK但无后续
```

---

## 四、UDP Flood攻击

### 4.1 UDP Flood攻击原理

**UDP Flood特点：**
```
- UDP无连接协议
- 攻击者发送大量UDP包
- 目标端口未开放时返回ICMP不可达
- 消耗目标带宽和处理能力
```

**UDP放大攻击：**
```
攻击者 ----小包----> 放大器(DNS/NTP)
目标   <----大包---- 放大器(DNS/NTP)

放大比例可达10-100倍
```

### 4.2 eNSP实操：配置UDP Flood防护

**配置限流策略：**
```bash
[USG6000]traffic classifier UDP_FLOOD
[USG6000-classifier-UDP_FLOOD]if-match udp
[USG6000-classifier-UDP_FLOOD]quit

[USG6000]traffic behavior LIMIT
[USG6000-behavior-LIMIT]car cir 1000 cbs 100000
[USG6000-behavior-LIMIT]quit

[USG6000]policy UDP_FLOOD_POLICY
[USG6000-policy-UDP_FLOOD_POLICY]classifier UDP_FLOOD behavior LIMIT
[USG6000-policy-UDP_FLOOD_POLICY]quit

[USG6000]interface GigabitEthernet1/0/0
[USG6000-GigabitEthernet1/0/0]traffic-policy UDP_FLOOD_POLICY inbound
```

### 4.3 Wireshark抓包分析UDP Flood

**过滤器设置：**
```
# 显示所有UDP流量
udp

# 显示特定端口UDP流量
udp.port == 53

# 统计UDP流量
Statistics -> Conversations -> UDP
```

### 4.4 ICMP Flood攻击

**ICMP协议基础：**
```
- Internet Control Message Protocol（互联网控制报文协议）
- 工作在网络层（三层），用于传递控制信息和错误报告
- 常见类型：
  * Echo Request（类型8）：ping请求
  * Echo Reply（类型0）：ping响应
  * Destination Unreachable（类型3）：目标不可达
  * Time Exceeded（类型11）：超时
- 默认不基于端口，直接封装在IP报文中
```

**ICMP Flood攻击原理：**
```
攻击者                         目标服务器
   |                              |
   |--- ICMP Echo Request ------>|  （大量伪造/真实的ping请求）
   |--- ICMP Echo Request ------>|
   |--- ICMP Echo Request ------>|
   |--- ICMP Echo Request ------>|
   |           ...                |
   |                              |  （CPU资源耗尽，忙于处理和回复）
   |                              |  （网络带宽被占满）
   |                              |  （正常服务不可用）
```

**攻击特征：**
```
1. 大量ICMP Echo Request（ping）包涌入目标
2. 目标被迫对每个请求生成Echo Reply响应
3. 消耗目标的：
   - CPU资源（生成和处理ICMP报文）
   - 网络带宽（请求+响应双向占用）
   - 内存资源（维护连接状态）
4. 严重时导致目标主机宕机或网络瘫痪
```

**ICMP Flood vs 其他Flood攻击对比：**
```
攻击类型        协议层级    无连接    放大效应    主要消耗
─────────────────────────────────────────────────────────
SYN Flood       传输层(TCP)  否      无         半连接队列
UDP Flood       传输层(UDP)  是      可放大     带宽+CPU
ICMP Flood      网络层       是      可放大     带宽+CPU
```

**ICMP放大攻击（Smurf Attack变种）：**
```
攻击者 ----伪造源IP(受害者)----> 广播地址/放大网络
目标受害者 <----大量ICMP Reply---- 放大网络

原理：
1. 攻击者发送ICMP请求，源IP伪造为受害者的IP
2. 请求发送到广播地址或大量主机
3. 所有收到请求的主机将Reply发给受害者
4. 流量被放大数十甚至数百倍
```

**ICMP Flood防护方法：**
```
1. 限制ICMP速率：
   - 在防火墙上配置ICMP报文速率限制
   - 超过阈值的ICMP包直接丢弃

2. 禁止不必要的ICMP响应：
   - 关闭对外部的ping响应
   - 仅允许内网特定网段使用ICMP

3. 防火墙ACL过滤：
   - 配置ACL拒绝来自外部的ICMP Echo Request
   - 允许必要的ICMP类型（如Path MTU Discovery需要的Type 3/4）

4. 启用DDoS防护：
   - 使用专业的DDoS清洗设备
   - 部署流量清洗服务（如云厂商的Anti-DDoS）

5. 网络架构优化：
   - 入口过滤（BCP38）：阻止源IP伪造
   - 流量限速和整形
```

**eNSP防火墙配置示例：**
```bash
# 限制ICMP报文速率
[USG6000]firewall defend icmp-flood enable
[USG6000]firewall defend icmp-flood zone untrust threshold 500

# ACL拒绝外部ICMP
[USG6000]acl 3000
[USG6000-acl-adv-3000]rule deny icmp source any destination any icmp-type echo
[USG6000-acl-adv-3000]quit

# 应用到接口
[USG6000]interface GigabitEthernet1/0/0
[USG6000-GigabitEthernet1/0/0]traffic-filter inbound acl 3000
```

**Wireshark抓包识别ICMP Flood：**
```
过滤器：
- icmp                          # 显示所有ICMP流量
- icmp.type == 8                # 仅显示ICMP Echo Request
- icmp.type == 0                # 仅显示ICMP Echo Reply

攻击特征：
- 短时间内出现大量ICMP Echo Request
- 源IP可能随机伪造（DDoS）或固定（单源攻击）
- 请求频率远超正常ping行为
- 统计视图中ICMP占比异常偏高
```

---

## 五、三层交换机组网实操训练

### 5.1 VLAN原理

**VLAN作用：**
```
- 逻辑隔离广播域
- 提高网络安全性
- 灵活网络规划
- 减少广播风暴
```

**VLAN类型：**
```
- 基于端口的VLAN
- 基于MAC地址的VLAN
- 基于协议的VLAN
- 基于子网的VLAN
```

### 5.2 eNSP实操：三层交换机VLAN配置

**实验拓扑：**
```
[PC1:192.168.10.1] ---- [S5700] ---- [PC2:192.168.20.1]
      VLAN 10                    VLAN 20
```

**步骤1：创建VLAN**
```bash
<Huawei>system-view
[Huawei]sysname SW1
[SW1]vlan batch 10 20
```

**步骤2：配置端口类型**
```bash
# 配置PC1接入端口
[SW1]interface GigabitEthernet0/0/1
[SW1-GigabitEthernet0/0/1]port link-type access
[SW1-GigabitEthernet0/0/1]port default vlan 10
[SW1-GigabitEthernet0/0/1]quit

# 配置PC2接入端口
[SW1]interface GigabitEthernet0/0/2
[SW1-GigabitEthernet0/0/2]port link-type access
[SW1-GigabitEthernet0/0/2]port default vlan 20
[SW1-GigabitEthernet0/0/2]quit
```

**步骤3：配置VLANIF接口（三层路由）**
```bash
[SW1]interface Vlanif 10
[SW1-Vlanif10]ip address 192.168.10.254 24
[SW1-Vlanif10]quit

[SW1]interface Vlanif 20
[SW1-Vlanif20]ip address 192.168.20.254 24
[SW1-Vlanif20]quit
```

**步骤4：配置PC网关**
```
PC1: IP 192.168.10.1/24, 网关 192.168.10.254
PC2: IP 192.168.20.1/24, 网关 192.168.20.254
```

**步骤5：测试连通性**
```bash
# 在PC1上ping PC2
ping 192.168.20.1
```

### 5.3 Wireshark抓包分析VLAN

**观察ARP请求：**
```
1. PC1 ping PC2
2. 抓取ARP广播
3. 观察VLAN标签
4. 分析三层路由过程
```

---

## 六、端口镜像实操训练

### 6.1 端口镜像原理

**端口镜像作用：**
```
- 流量监控与分析
- 安全审计
- 故障排查
- 入侵检测
```

**镜像类型：**
```
- 本地镜像：源端口和目的端口在同一设备
- 远程镜像：通过网络将流量发送到远端设备
```

### 6.2 eNSP实操：配置端口镜像

**实验拓扑：**
```
[PC1] ---- [S5700] ---- [PC2]
               |
          [监控PC]
```

**步骤1：配置观察端口**
```bash
<Huawei>system-view
[Huawei]sysname SW1
[SW1]observe-port 1 interface GigabitEthernet0/0/3
```

**步骤2：配置镜像端口**
```bash
# 镜像PC1端口的入方向流量
[SW1]interface GigabitEthernet0/0/1
[SW1-GigabitEthernet0/0/1]port-mirror to observe-port 1 inbound
[SW1-GigabitEthernet0/0/1]quit

# 镜像PC2端口的出方向流量
[SW1]interface GigabitEthernet0/0/2
[SW1-GigabitEthernet0/0/2]port-mirror to observe-port 1 outbound
[SW1-GigabitEthernet0/0/2]quit
```

**步骤3：查看镜像配置**
```bash
[SW1]display observe-port
[SW1]display port-mirror
```

**步骤4：监控PC抓包**
```
1. 在监控PC上打开Wireshark
2. 选择对应网卡
3. 开始捕获
4. 在PC1和PC2之间产生流量
5. 观察监控PC捕获的镜像流量
```

---

## 七、访问控制列表知识串讲

### 7.1 ACL基本概念

**ACL定义：**
```
Access Control List - 访问控制列表
- 基于规则的流量过滤
- 按顺序匹配规则
- 匹配即执行，不再继续
```

**ACL分类：**
```
- 基本ACL：2000-2999，基于源IP
- 高级ACL：3000-3999，基于五元组
- 二层ACL：4000-4999，基于MAC地址
```

**ACL匹配规则：**
```
1. 按编号从小到大匹配
2. 匹配即执行permit/deny
3. 未匹配则执行默认规则（permit）
```

### 7.2 反掩码（Wildcard Mask）

**反掩码定义：**
```
反掩码 = 255.255.255.255 - 子网掩码
反掩码是子网掩码的"按位取反"（反码）

子网掩码：1表示网络位，0表示主机位
反掩码：  0表示必须精确匹配，1表示可以变化
```

**计算方法：**
```
方法1：按位取反
子网掩码 255.255.255.0 (11111111.11111111.11111111.00000000)
反掩码   0.0.0.255     (00000000.00000000.00000000.11111111)

方法2：用255减去每个八位组
255-255=0, 255-255=0, 255-255=0, 255-0=255
结果：0.0.0.255
```

**常见反掩码对照表：**
```
子网掩码          CIDR    反掩码
255.255.255.255   /32     0.0.0.0        （主机地址）
255.255.255.0     /24     0.0.0.255      （C类网段）
255.255.0.0       /16     0.0.255.255    （B类网段）
255.0.0.0         /8      0.255.255.255  （A类网段）
0.0.0.0           /0      255.255.255.255（任意地址）
```

**反掩码在ACL中的应用：**
```
[R1]acl 2000
[R1-acl-basic-2000]rule permit source 192.168.1.0 0.0.0.255
                                        ↑网络地址  ↑反掩码

含义：匹配192.168.1.0到192.168.1.255的所有地址
- 前24位（192.168.1）必须精确匹配
- 后8位（0-255）可以是任意值
```

**反掩码在OSPF中的应用：**
```bash
[R1-ospf-1-area-0.0.0.0]network 192.168.1.0 0.0.0.255
```

### 7.3 ACL应用场景

```
- 流量过滤：允许或拒绝特定流量
- 路由过滤：控制路由通告
- NAT：地址转换匹配
- QoS：流量分类与标记
- IPsec：感兴趣流量定义
```

---

## 八、基本ACL实操训练

### 8.1 eNSP实操：配置基本ACL

**实验拓扑：**
```
[PC1:192.168.1.1] ---- [R1] ---- [PC2:192.168.2.1]
      VLAN 10                  VLAN 20
```

**实验目标：**
```
- 允许PC1访问PC2
- 拒绝PC1访问服务器192.168.3.1
```

**步骤1：配置路由器接口**
```bash
<Huawei>system-view
[Huawei]sysname R1
[R1]interface GigabitEthernet0/0/0
[R1-GigabitEthernet0/0/0]ip address 192.168.1.254 24
[R1-GigabitEthernet0/0/0]quit

[R1]interface GigabitEthernet0/0/1
[R1-GigabitEthernet0/0/1]ip address 192.168.2.254 24
[R1-GigabitEthernet0/0/1]quit

[R1]interface GigabitEthernet0/0/2
[R1-GigabitEthernet0/0/2]ip address 192.168.3.254 24
[R1-GigabitEthernet0/0/2]quit
```

**步骤2：创建基本ACL**
```bash
# 允许192.168.1.0网段访问
[R1]acl 2000
[R1-acl-basic-2000]rule permit source 192.168.1.0 0.0.0.255
[R1-acl-basic-2000]rule deny source any
[R1-acl-basic-2000]quit
```

**步骤3：应用ACL到接口**
```bash
[R1]interface GigabitEthernet0/0/0
[R1-GigabitEthernet0/0/0]traffic-filter inbound acl 2000
[R1-GigabitEthernet0/0/0]quit
```

**步骤4：查看ACL配置**
```bash
[R1]display acl 2000
[R1]display traffic-filter applied-record
```

### 8.2 Wireshark抓包验证

**验证步骤：**
```
1. 在R1的G0/0/1接口抓包
2. PC1 ping PC2 (192.168.2.1) - 应该成功
3. PC1 ping 服务器 (192.168.3.1) - 应该被拒绝
4. 观察ICMP请求是否被丢弃
```

---

## 九、高级ACL实操训练

### 9.1 eNSP实操：配置高级ACL

**实验拓扑：**
```
[PC1] ---- [R1] ---- [Web Server:192.168.2.1:80]
                 ---- [FTP Server:192.168.2.2:21]
```

**实验目标：**
```
- 允许PC1访问Web服务器的HTTP服务
- 拒绝PC1访问FTP服务器
- 允许PC1 ping所有服务器
```

**步骤1：创建高级ACL**
```bash
[R1]acl 3000
# 允许HTTP流量
[R1-acl-adv-3000]rule permit tcp source 192.168.1.0 0.0.0.255 destination 192.168.2.1 0 destination-port eq 80
# 允许ICMP流量
[R1-acl-adv-3000]rule permit icmp source 192.168.1.0 0.0.0.255 destination 192.168.2.0 0.0.0.255
# 拒绝其他所有流量
[R1-acl-adv-3000]rule deny ip source any destination any
[R1-acl-adv-3000]quit
```

**步骤2：应用ACL**
```bash
[R1]interface GigabitEthernet0/0/0
[R1-GigabitEthernet0/0/0]traffic-filter inbound acl 3000
[R1-GigabitEthernet0/0/0]quit
```

**步骤3：测试验证**
```bash
# PC1访问Web服务器 - 成功
http://192.168.2.1

# PC1访问FTP服务器 - 失败
ftp://192.168.2.2

# PC1 ping服务器 - 成功
ping 192.168.2.1
ping 192.168.2.2
```

### 9.2 配置时间段ACL

**步骤1：创建时间段**
```bash
[R1]time-range work-time 08:00 to 18:00 working-day
```

**步骤2：创建基于时间的ACL**
```bash
[R1]acl 3001
[R1-acl-adv-3001]rule permit tcp source 192.168.1.0 0.0.0.255 destination-port eq 80 time-range work-time
[R1-acl-adv-3001]rule deny ip source any destination any
[R1-acl-adv-3001]quit
```

**步骤3：查看时间段状态**
```bash
[R1]display time-range work-time
```

---

## 十、流量分析基础知识串讲

### 10.1 流量分析概念

**流量分析定义：**
```
- 监控网络数据包
- 分析流量模式
- 识别异常行为
- 安全威胁检测
```

**流量分析工具：**
```
- Wireshark：图形化抓包分析
- tcpdump：命令行抓包
- tshark：命令行版Wireshark
- NetworkMiner：网络取证
```

### 10.2 常见协议流量特征

**HTTP流量特征：**
```
- 明文传输
- 请求方法：GET/POST/PUT/DELETE
- 状态码：200/301/404/500
- 可见URL和参数
```

**DNS流量特征：**
```
- UDP 53端口（查询）
- TCP 53端口（区域传送）
- 查询域名和响应IP
- 可见解析过程
```

**TCP流量特征：**
```
- 三次握手：SYN -> SYN+ACK -> ACK
- 数据传输：PSH+ACK
- 四次挥手：FIN -> ACK -> FIN -> ACK
```

### 10.3 Wireshark常用过滤器

**显示过滤器：**
```
# IP地址过滤
ip.addr == 192.168.1.1
ip.src == 192.168.1.1
ip.dst == 192.168.2.1

# 协议过滤
tcp
udp
http
dns
icmp

# 端口过滤
tcp.port == 80
tcp.dstport == 443

# 组合过滤
ip.addr == 192.168.1.1 and tcp.port == 80
http.request.method == "GET"
```

---

## 十一、流量分析实战

### 11.1 Wireshark实操：分析Web流量

**实验步骤：**
```
1. 打开Wireshark
2. 选择网卡，开始捕获
3. 浏览器访问 http://www.example.com
4. 停止捕获
5. 应用过滤器：http
```

**分析HTTP请求：**
```
1. 找到HTTP GET请求
2. 查看请求头信息
3. 查看响应状态码
4. 分析响应内容
```

**分析TCP连接：**
```
1. 找到TCP三次握手
2. 分析序列号和确认号
3. 观察数据传输过程
4. 查看TCP四次挥手
```

### 11.2 Wireshark实操：分析DNS流量

**实验步骤：**
```
1. 开始捕获
2. 命令行执行：nslookup www.baidu.com
3. 停止捕获
4. 应用过滤器：dns
```

**DNS分析要点：**
```
1. 查询域名
2. 响应IP地址
3. 查询类型（A/AAAA/CNAME）
4. TTL值
5. DNS服务器地址
```

### 11.3 Wireshark实操：统计分析

**流量统计：**
```
Statistics -> Capture File Properties
- 总数据包数量
- 总字节数
- 平均包大小
- 持续时间
```

**协议层次统计：**
```
Statistics -> Protocol Hierarchy
- 各协议占比
- HTTP/TCP/UDP/ARP等
```

**会话统计：**
```
Statistics -> Conversations
- IP会话列表
- TCP会话列表
- 流量排名
```

**IO图表：**
```
Statistics -> I/O Graphs
- 流量时间趋势
- 协议流量对比
- 识别流量异常
```

---

## 十二、综合实操练习

### 12.1 练习1：网络攻击识别

**实验目标：**
```
使用Wireshark识别SYN Flood攻击
```

**实验步骤：**
```
1. 在eNSP中搭建网络环境
2. 配置防火墙防护策略
3. 使用工具模拟SYN Flood攻击
4. 使用Wireshark捕获攻击流量
5. 分析攻击特征
6. 验证防护效果
```

### 12.2 练习2：ACL配置与验证

**实验目标：**
```
配置ACL实现精细化访问控制
```

**实验步骤：**
```
1. 在eNSP中搭建多网段环境
2. 配置基本ACL限制源IP
3. 配置高级ACL限制服务
4. 使用Wireshark验证ACL效果
5. 分析被拒绝的数据包
```

### 12.3 练习3：VLAN隔离与路由

**实验目标：**
```
配置三层交换机实现VLAN间通信
```

**实验步骤：**
```
1. 在eNSP中配置多VLAN环境
2. 配置VLANIF接口实现路由
3. 使用Wireshark抓包分析
4. 观察VLAN标签变化
5. 验证VLAN间通信
```

---

## 课后作业

### 作业1：SSH安全配置
```
在eNSP中配置交换机SSH登录，要求：
1. 使用密钥认证
2. 限制特定IP访问
3. 配置登录超时
4. 使用Wireshark验证加密传输
```

### 作业2：ACL综合配置
```
在eNSP中配置ACL，要求：
1. 允许内网访问外网HTTP/HTTPS
2. 禁止内网访问外网FTP
3. 允许特定管理员访问所有服务
4. 使用Wireshark验证效果
```

### 作业3：流量分析报告
```
使用Wireshark捕获网络流量，分析：
1. 流量协议分布
2. Top10通信对
3. 异常流量识别
4. 撰写流量分析报告
```

---

## 常用命令速查

### 交换机/路由器命令
```bash
# 查看接口状态
display interface brief

# 查看VLAN信息
display vlan

# 查看路由表
display ip routing-table

# 查看ACL配置
display acl all

# 查看ARP表
display arp all
```

### Wireshark过滤器
```
# 基本过滤
ip.addr == x.x.x.x
tcp.port == xx
http

# 高级过滤
tcp.flags.syn == 1
http.request.method == "GET"
dns.qry.name contains "example"

# 组合过滤
(ip.addr == 192.168.1.1) and (tcp.port == 80)
```

### 常用网络命令
```bash
# Windows
ipconfig /all
ping x.x.x.x
tracert x.x.x.x
nslookup domain.com

# Linux
ifconfig
ping x.x.x.x
traceroute x.x.x.x
dig domain.com
```

---

## 学习资源

### 在线资源
- 华为官方文档：https://support.huawei.com
- Wireshark官方教程：https://www.wireshark.org/docs/
- 网络安全学习平台：https://www.hackthebox.com

### 推荐书籍
- 《Wireshark网络分析就这么简单》
- 《网络安全技术与实践》
- 《华为交换机学习指南》

### 视频教程
- B站搜索：Wireshark教程、eNSP教程
- 华为官方培训视频
- 网络安全实验教程

---

## 总结

第一天的学习重点：
1. **应用层协议**：理解HTTP、FTP、DNS等协议工作原理
2. **SSH安全**：掌握SSH配置和安全加固
3. **攻击防护**：理解SYN Flood和UDP Flood攻击及防护
4. **VLAN配置**：掌握三层交换机VLAN划分和路由
5. **ACL配置**：学会使用ACL进行访问控制
6. **流量分析**：掌握Wireshark使用和流量分析方法

通过今天的学习，你将具备网络通信安全的基础知识和实操能力，为后续学习打下坚实基础。