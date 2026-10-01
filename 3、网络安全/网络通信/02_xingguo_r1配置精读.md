# xingguo_r1 配置精读

> 设备：**华为路由器**（VRP 系统，版本 V200R009C00SPC600）
> 配置导出时间：2025/8/22 11:50:13
> 前置阅读：`01_网络基础预备知识.md`
>
> **第三个重要说明（2026-09-10 更新）**：拿到了**备份路由器 xingguo_r2 的实际配置**，
> 本文档中所有"推测"已用 r2 的真实配置逐条核对，并新增第十章「双机对照」。
> 核对结果：**大部分推测被证实，但有 3 处必须修正**（r2 的 Local_Pref 是 **300** 不是 200、
> r2 **没有**宁都方向的 BGP 邻居、两台设备的 NTP 服务器**不是同一台**）。
> 修正清单见 [第十章](#十双机对照r1-与-r2-的完整对比)。
>
> **第二个重要说明**：本文档经过一轮外部审阅，**同步修正了基础文档里的 9 处错误**
> （其中 MAC 不可改、level 3 = 只读、AS 号范围等是实质性错误，清单见基础文档开头的修订说明）。
>
> 本文档对应修正的地方：
> - 接口表新增"三层口"的严谨说明 —— 只有 5 个口可确定
> - 权限级别章节重写 —— **level 3 不是只读**，并指出"SSH 开了但 admin 反而不能用 SSH 登"的荒诞之处
> - "主用/备用"全部改为"链路 A / 链路 B"，并说明配置实际保证了什么
> - 自测题 Q5 追加：Loopback 建邻在本网**并未兑现抗故障能力**
> - 场景 3 标注为高不确定性推断
> - **新增安全审计第 13 项：路由协议无认证**（这是审阅过程中新发现的控制平面问题）
>
> **第一个重要说明（纠正）**：这份配置**不是赫斯曼（Hirschmann）设备**的。
> `sysname` / `dis cur` / `acl number 2002` / `vrrp vrid` / `undo portswitch` / `bgp 2014` 全部是**华为 VRP** 的语法。
> 赫斯曼是工业以太网交换机厂商，它的 CLI 是另一套（HiOS/HiPerOS，命令像 `enable`、`vlan modi` 之类）。
> 如果这个项目里确实有赫斯曼设备，那它的配置在别的文件里，这是另一台华为路由器。

---

## 目录

1. [一图看懂：还原出来的网络拓扑](#一图看懂还原出来的网络拓扑)
2. [这台设备是谁：身份信息](#这台设备是谁身份信息)
3. [接口全景表](#接口全景表)
4. [逐段精读](#逐段精读)
   - [4.1 全局基础设置](#41-全局基础设置)
   - [4.2 ACL —— 全篇的"白名单"](#42-acl--全篇的白名单)
   - [4.3 接口与 IP 地址](#43-接口与-ip-地址)
   - [4.4 VRRP —— 网关冗余](#44-vrrp--网关冗余)
   - [4.5 OSPF —— 内部互通](#45-ospf--内部互通)
   - [4.6 BGP —— 与外界交换路由](#46-bgp--与外界交换路由)
   - [4.7 Route-Policy 与 Local_Preference](#47-route-policy-与-local_preference)
   - [4.8 AAA 与用户管理](#48-aaa-与用户管理)
   - [4.9 远程管理：SSH / HTTPS / VTY](#49-远程管理ssh--https--vty)
   - [4.10 SNMP —— 网管监控](#410-snmp--网管监控)
   - [4.11 NTP —— 时间同步](#411-ntp--时间同步)
   - [4.12 可以忽略的默认模板](#412-可以忽略的默认模板)
5. [完整走一遍：一个数据包的旅程](#完整走一遍一个数据包的旅程)
6. [设计意图总结：为什么这么设计](#设计意图总结为什么这么设计)
7. [安全审计：这份配置的 16 个问题](#安全审计这份配置的-16-个问题)
8. [命令速查表](#命令速查表)
9. [自测题（带答案）](#自测题带答案)
10. [双机对照：r1 与 r2 的完整对比](#十双机对照r1-与-r2-的完整对比)
    - [10.1 为什么要看第二台](#101-为什么要看第二台)
    - [10.2 基本信息对照](#102-基本信息对照)
    - [10.3 接口对照](#103-接口对照)
    - [10.4 BGP 邻居对照](#104-bgp-邻居对照)
    - [10.5 ACL 对照](#105-acl-对照)
    - [10.6 路由策略对照：400 vs 300](#106-路由策略对照400-vs-300)
    - [10.7 VRRP 对照](#107-vrrp-对照)
    - [10.8 管理面与运维对照](#108-管理面与运维对照)
    - [10.9 差异汇总：哪些是真问题](#109-差异汇总哪些是真问题)
    - [10.10 此前推测的核对结果](#1010-此前推测的核对结果)
    - [10.11 会话日志里的意外收获](#1011-会话日志里的意外收获)

---

## 一图看懂：还原出来的网络拓扑

从配置里的 `description`、IP 网段、BGP peer 关系可以反推出这张图：

```
                        上级 / 南昌
                          AS 1001
              ┌──────────────┬──────────────┐
              │ 192.80.1.1   │              │ 192.80.9.1
              │ (南昌主站)    │              │ (南昌备用方向)
              └──────┬───────┘              └──────┬───────┘
                     │ 192.80.1.0/24               │ 192.80.9.0/24
                     │ 链路 A（r1 专用）             │ 链路 A'（r2 专用）
                     │                              │
  ┌──────────────────┴──────────────────────────────┴────────────┐
  │                    兴国本地 AS 2014                            │
  │                                                               │
  │   ┌─────────────────┐         ┌─────────────────┐            │
  │   │  xingguo_r1     │         │  xingguo_r2     │            │
  │   │  (本设备，主)     │  iBGP   │  (备)            │            │
  │   │  Lo0: .30.53    │◄═══════►│  Lo0: .30.54    │            │
  │   │  ✅ 已核实        │         │  ✅ 已核实        │            │
  │   └────┬───────┬────┘         └────┬───────┬────┘            │
  │        │       │                   │       │                 │
  │        │  G0/0/4: 10.10.1.53/30 ───┘       │                 │
  │        │       └──── G0/0/4: 10.10.1.54/30 ┘                 │
  │        │         OSPF Area 0（内部互联）                       │
  │        │                                                      │
  │        │   ┌────────────────────┐  ┌────────────────────┐    │
  │        │   │ VRRP 组 10  LAN A  │  │ VRRP 组 11  LAN B  │    │
  │        │   │ VIP: 192.20.27.20  │  │ VIP: 192.20.28.20  │    │
  │        │   │ r1 .27.18 prio 120 │  │ r1 .28.18 prio 120 │    │
  │        │   │ r2 .27.19 prio 100 │  │ r2 .28.19 prio 100 │    │
  │        │   │ → r1 双 Master ✅   │  │ → r1 双 Master ✅   │    │
  │        │   └─────────┬──────────┘  └─────────┬──────────┘    │
  │        │      192.20.27.0/24            192.20.28.0/24        │
  │        │      (业务网段 A)               (业务网段 B)           │
  │        │                                                      │
  │   NTP: r1→192.20.27.30          SNMP 网管: 173.20.1.178 (iMC) │
  │        r2→192.20.28.30          （两台都上报，注意源地址不同）    │
  │                                                               │
  └───────────────────┬───────────────────────────────────────────┘
                      │ G0/0/11: 192.80.106.1/30
                      │ DDN 2M 专线（上行 B，仅 2M）
                      │ ⚠️ 只有 r1 有，r2 上没有这条链路 → 单点
                      │
                ┌─────┴──────┐
                │ 宁都方向    │
                │ AS 3002    │
                │ .106.2     │
                └────────────┘
```

> 图中 r2 的信息全部来自 r2 的实际配置（`兴国站自控B路由器_2025-08-22_11_22_25.log`），不再是推测。
> **最关键的一处修正**：r2 的上行**不是**备用同一条 192.80.1.0/24，而是**另一条 192.80.9.0/24**（description `to nanchang bei`）。
> 也就是说两台路由器各有各的上行，不是"主链路 + 备链路"，而是**双出口 + 内部择优**。

### 关键结论

| 项目 | 结论 |
|---|---|
| 设备角色 | 兴国站点**主路由器**（r1），有一台备份 r2（**配置已核实**） |
| 本地 AS | **2014**（两台同 AS，iBGP 互联） |
| r1 上行 | G0/0/10 → 192.80.1.1（南昌，AS 1001），192.80.1.0/24 |
| r2 上行 | G0/0/10 → 192.80.9.1（南昌，AS 1001），192.80.9.0/24 ← **与 r1 不是同一条** |
| r1 第二条上行 | G0/0/11 → 192.80.106.2（宁都，AS 3002），DDN 专线仅 2M ← **r2 上没有** |
| 下行业务网段 | 192.20.27.0/24（LAN A）、192.20.28.0/24（LAN B） |
| 内网互联 | 10.10.1.52/30（r1 .53 / r2 .54）、10.10.30.53/32、10.10.30.54/32 |
| 内部协议 | OSPF（只跑基础设施） |
| 外部协议 | BGP（跑业务路由 + 严格过滤） |

> ✅ **拿到 r2 配置后可以确认的三件事**（此前都只是推测）
>
> | 问题 | 核实结果 | 依据 |
> |---|---|---|
> | r2 的 LAN 地址是多少？ | **192.20.27.19 / 192.20.28.19** | r2 的 G0/0/2、G0/0/3 |
> | r2 是 VRRP Master 吗？ | **不是**，两个组都是 Backup | r2 **没有配 priority**，用默认 100 < r1 的 120 |
> | r2 的 Local_Pref 是多少？ | **300**（不是原先猜的 200） | r2 的 `route-policy lp01 permit node 10` |
>
> ⚠️ **注意用词：不要直接说"A 是主用、B 是备用"**
>
> 主备关系**部分兑现**，分路由看：
>
> | 路由 | 配置是否保证优先走 r1 | 依据 |
> |---|---|---|
> | 173.20.1.0/24、173.21.1.0/24 | ✅ **是，已确认** | r1 打 lp=400，r2 打 lp=300，LP 在 AS 内传递 → 全网优选 r1 学到的那条 |
> | 192.20.27.0/24（LAN A 出网） | ✅ 基本是 | 两台都向 AS 1001 通告 LAN A；回程由 VRRP（r1 Master）+ LP 共同决定 |
> | 192.20.28.0/24（LAN B） | ⚠️ 不对称 | r1 通过 ACL 2004 只向宁都通告 LAN A；**LAN B 只能走南昌方向** |
> | 192.20.102.0/24（从宁都收） | ❌ 无策略 | 完全交给默认 BGP 选路，且**只有 r1 有这条链路** |
>
> 要确认最终选路结果，仍需在设备上 `display bgp routing-table`。
> **但现在已经可以说：对 173 网段，主备关系是配置明确保证的**（400 > 300），这一点比原先的判断更乐观。

---

## 这台设备是谁：身份信息

```
[V200R009C00SPC600]                    ← VRP 版本号
sysname xingguo_r1                     ← 设备名
snmp-agent local-engineid 800007DB038446FE3D5453
```

**engineid 里藏着 MAC 地址**：`800007DB03` 是固定前缀，后面 `8446FE3D5453` 就是设备的 MAC 地址 `84:46:FE:3D:54:53`。

> 这也是个信息泄露点——设备的 MAC 地址暴露了。MAC 前 3 字节 `84:46:FE` 是 **IEEE OUI**，可以查到厂商（华为）。攻击者拿到 MAC 就能判断设备型号，甚至伪造 MAC 做某些二层攻击。

**型号推断**：有 `Cellular0/0/0`、`Cellular0/0/1`（4G/5G 模块）、有 `wlan ac`（无线控制器）、14 个千兆口 —— 这是**华为 AR 系列企业路由器**（大概率 AR2200/AR3200 系列），带 3G/4G 备份链路和无线 AC 功能。

---

## 接口全景表

| 接口 | IP 地址 | description | 状态 | 用途 |
|---|---|---|---|---|
| G0/0/0 | 无 | — | 空置 | 未使用 |
| G0/0/1 | 无 | to nanchang zhu | 空置 | **原计划接南昌主站，实际没配 IP**（被 G0/0/10 取代） |
| **G0/0/2** | 192.20.27.18/24 | to LAN A | 三层口 | 业务网段 A，VRRP vrid 10 主 |
| **G0/0/3** | 192.20.28.18/24 | to LAN B | 三层口 | 业务网段 B，VRRP vrid 11 主 |
| **G0/0/4** | 10.10.1.53/30 | Connect to xingguo_r2 | 三层口 | 与备路由器互联 |
| G0/0/5 ~ G0/0/8 | 无 | — | 空置 | 预留/未使用 |
| G0/0/9 | 无 | — | 空置 | 被指定为 HTTP 管理口（但没 IP，等于关闭） |
| **G0/0/10** | 192.80.1.54/24 | to nanchang zhu | 三层口 | 上行链路 A → AS 1001，以太网，带宽充裕 |
| **G0/0/11** | 192.80.106.1/30 | To_NingDu-DDN-2M | 三层口 | 上行链路 B → AS 3002，DDN 专线仅 2M |
| G0/0/12 | 无 | — | 空置 | 未使用 |
| G0/0/13 | 无 | VirtualPort | 空置 | 未使用 |
| Cellular0/0/0~1 | 无 | — | 空置 | 4G/5G 备份模块，未配置 |
| **LoopBack0** | 10.10.30.53/32 | — | 永 up | Router-ID、iBGP 源地址、NTP 源 |
| NULL0 | — | — | 永 up | 系统保留，黑洞接口 |

> **关于"三层口"这一列的严谨说明**
>
> 表中标"三层口"的 5 个接口（G0/0/2、3、4、10、11），是因为配置里**明确出现了 `undo portswitch`**，可以确定是三层路由口。
>
> 其余标"空置"的接口，配置里只有一行 `interface GigabitEthernet0/0/X` 后跟空行，
> **这只能说明它们没有非默认配置，不能断定其是二层还是三层**——华为不同型号、不同接口类型的
> 默认模式不一样。要确认得看 `display interface` 或查型号文档。
>
> 不过从"是否参与业务转发"的角度，它们都没配 IP，一律不参与三层转发。

**注意 G0/0/1 和 G0/0/10 的 description 都是 `to nanchang zhu`** —— 说明施工时改过方案，从 G0/0/1 换到了 G0/0/10，但旧口的描述没清理。**这种残留是运维的大敌**，半年后没人记得哪个口是真在用的。

### 地址规划规律

```
10.10.1.53/32    → 互联链路（r1 用 .53，r2 用 .54）
10.10.30.53/32   → Loopback（r1 用 .53，r2 用 .54）
```

看出规律了吗？**同一设备在不同网段用相同的主机位**（都是 .53）。这是很好的规划习惯——看到 .53 就知道是 r1，看到 .54 就知道是 r2。排障时能少掉一半头发。

> ✅ **r2 配置已证实这个规律**：r2 确实是 `10.10.1.54` 和 `10.10.30.54`，LAN 侧是 `.27.19`/`.28.19`。
> 顺带一个细节：两台设备的 MAC 是 `84:46:FE:3D:54:53`（r1）和 `84:46:FE:3D:56:15`（r2），
> **MAC 也是连号的**——说明是同一批采购、同一批次上架的设备。

---

## 逐段精读

### 4.1 全局基础设置

```huawei
sysname xingguo_r1
```
设备名。不设的话提示符是 `Huawei`，多台设备时根本分不清是谁。**这是任何设备的第一条必配命令。**

```huawei
drop illegal-mac alarm
```
**丢弃非法 MAC 并告警。** "非法 MAC" 指源 MAC 是广播地址、组播地址、全 0 等根本不该出现在源字段的地址。正常主机不会发出这种帧，只有攻击工具或故障网卡才会。

> **安全视角**：这是防 MAC 泛洪/欺骗类二层攻击的基础措施。但注意它只是 `alarm`（告警），而且是**缺省配置**（华为很多型号默认就开着），不能算主动加固。

```huawei
clock timezone EST add 08:00:00
```
设置时区。`EST` 通常是美国东部时间（UTC-5），但这里 `add 08:00:00` 加了 8 小时 —— 这是把 EST 这个**名字**当壳子，硬凑出东八区（北京时间）。

**这是个偷懒但常见的写法**，问题在于日志里时区显示成 EST，会误导人。正确写法应该用 `CST`（中国标准时间）或直接配置 `clock timezone BeiJing add 08:00:00`。

> **为什么时区对安全重要？** 时间戳错了，跨设备日志关联就失效。出事之后审计时，几台设备的时间对不上 = 无法还原攻击链。

```huawei
dhcp enable
```
开启 DHCP 服务。**但配置里没有任何地址池（`ip pool`）配置** —— 说明开了服务却没真正用，或者地址池在别的设备上（下联交换机）。**这是个配置残留**，应该关掉：`undo dhcp enable`。多开一个服务就多一份攻击面。

```huawei
fib regularly-refresh disable
```
关闭 FIB（转发表）定期刷新。默认是开启的（用于刷新硬件表项、修正偶发的表项老化错误）。关掉可以**减少 CPU 占用、提高转发稳定性**。

> 工业网络追求的是**稳定压倒一切**，宁可牺牲一点自愈能力也不希望周期性刷新引起丢包抖动。这个命令在很多实时性要求高的专网上会关掉。

---

### 4.2 ACL —— 全篇的"白名单"

```huawei
acl number 2002
 rule 5 permit source 192.20.27.0 0.0.0.255
 rule 10 permit source 192.20.28.0 0.0.0.255

acl number 2003
 rule 5 permit source 173.20.1.0 0.0.0.255
 rule 10 permit source 173.21.1.0 0.0.0.255

acl number 2004
 rule 5 permit source 192.20.27.0 0.0.0.255

acl number 2005
 rule 5 permit source 192.20.102.0 0.0.0.255
```

**这几个 ACL 是全篇的核心控制点**，先记住它们的含义：

| ACL | 匹配内容 | 用在哪里 | 方向 | 作用 |
|---|---|---|---|---|
| **2002** | 192.20.27.0/24 + 192.20.28.0/24（本地两个业务网段） | peer 192.80.1.1 | **export** | 只向南昌主站**通告**本地业务网段 |
| **2003** | 173.20.1.0/24 + 173.21.1.0/24（上级业务网段） | peer 192.80.1.1 | **import** | 只从南昌主站**接收**这两个网段 |
| **2004** | 192.20.27.0/24（**只有 LAN A**） | peer 192.80.106.2 | **export** | 只向宁都通告 LAN A |
| **2005** | 192.20.102.0/24 | peer 192.80.106.2 | **import** | 只从宁都接收这一个网段 |

#### 三个必须掌握的点

**① ACL 2000-2999 是"基本 ACL"**
只能匹配**源 IP 地址**，不能匹配目的 IP、端口、协议。要匹配更多用 3000-3999（高级 ACL）。这里用来筛路由，只看源（= 网段），基本 ACL 够了。

**② ACL 末尾有一条隐藏的 `deny any`**
ACL 是"白名单思维"：写了 permit 的通过，**没写的一律拒绝**。所以 2002 只 permit 了两个网段，等于"除了这两个，其他一概不通告"。

**③ 这里的 ACL 不是用来过滤数据包的！**
**这是最容易混淆的地方。** 同一个 ACL 有两种完全不同的用法：

```huawei
# 用法 A：过滤数据包（要应用到接口上）
interface GigabitEthernet0/0/2
 traffic-filter inbound acl 3000      ← 真正的访问控制，挡流量

# 用法 B：筛选路由（在路由协议里引用）  ← 本配置是这种
bgp 2014
 peer 192.80.1.1 filter-policy 2002 export   ← 只影响"通告哪些路由"
```

**ACL 2002~2005 在接口上完全没被调用，所以它们对普通数据包转发零影响。** 一个 192.20.27.100 的 PC 要访问互联网，不会被这些 ACL 拦住——它们只决定路由表里能出现什么。

> **考试/面试高频坑**：看到 ACL 就以为在做访问控制。一定要看它被 `traffic-filter` 引用了（过滤数据），还是被 `filter-policy` / `route-policy` 引用了（过滤路由）。

---

### 4.3 接口与 IP 地址

```huawei
interface GigabitEthernet0/0/2
 undo portswitch
 description to LAN A
 ip address 192.20.27.18 255.255.255.0
 vrrp vrid 10 virtual-ip 192.20.27.20
 vrrp vrid 10 priority 120
```

逐行：

| 命令 | 解释 |
|---|---|
| `undo portswitch` | 把二层交换口**切成三层路由口**。华为 AR 系列部分以太网口默认工作在二层模式，不切这个就没法配 IP |
| `description to LAN A` | 纯注释，但**极其重要**——半年后靠它救命 |
| `ip address 192.20.27.18 255.255.255.0` | 接口 IP。所在网段 192.20.27.0/24，可用主机 254 个 |
| `vrrp vrid 10 virtual-ip 192.20.27.20` | 创建 VRRP 组 10，虚拟网关 IP 是 .20 |
| `vrrp vrid 10 priority 120` | 优先级 120（默认 100），**我是 Master** |

```huawei
interface GigabitEthernet0/0/4
 undo portswitch
 description Connect to xingguo_r2
 ip address 10.10.1.53 255.255.255.252
```

`/30` = 255.255.255.252，只有 2 个可用地址：

```
192.80.106.0/30 拆开看（以 G0/0/11 为例）：
  10.10.1.52  → 网段地址（不可用）
  10.10.1.53  → 本端 r1        ← 这里
  10.10.1.54  → 对端 r2
  10.10.1.55  → 广播地址（不可用）
```

**为什么点对点链路用 /30 而不是 /24？** 省地址只是小原因，更重要的是：
1. 广域网接口带宽贵、地址资源紧张
2. **限制广播域**——/30 只有 2 台设备，不会有乱七八糟的主机接入
3. 排障简单——链路两端就这俩地址

```huawei
interface LoopBack0
 ip address 10.10.30.53 255.255.255.255
```

/32 掩码，一个地址就是一整个网段。Loopback 的特点：
- **永远不会 down**（除非手动 shutdown）
- 不依赖任何物理线路
- 用作 Router-ID 和 iBGP 源地址 → **任何一条物理链路断了，只要还有别的路径能到 Loopback，BGP 邻居就不掉**

---

### 4.4 VRRP —— 网关冗余

```huawei
interface GigabitEthernet0/0/2
 vrrp vrid 10 virtual-ip 192.20.27.20
 vrrp vrid 10 priority 120

interface GigabitEthernet0/0/3
 vrrp vrid 11 virtual-ip 192.20.28.20
 vrrp vrid 11 priority 120
```

#### 工作机制

```
   PC (192.20.27.100)
   网关: 192.20.27.20        ← PC 只知道这个虚拟 IP
        │
   ┌────┴─────────────────┐
   │  VRRP 组 10          │
   ├──────────┬───────────┤
   │ r1: .18  │ r2: .19   │  ← r2 地址已从实际配置核实
   │ prio 120 │ prio 100  │  ← r2 未配 priority，用默认值
   │ MASTER   │ BACKUP    │
   │ 实际转发  │ 只在旁边听 │
   └──────────┴───────────┘
        ↑ 每 1 秒发一次 VRRP 通告
```

1. 两台路由器加入同一个 VRRP 组，共享虚拟 IP `.20`
2. **优先级高的当 Master**（120 > 100），实际转发流量
3. Master 周期性发 VRRP 通告（默认 1 秒）
4. Backup 收不到通告（默认 3 个周期 = 约 3 秒）→ 顶上去当 Master
5. PC 全程无感知，网关 IP 从未变过

#### 这份配置的设计选择

| 观察 | 结论 |
|---|---|
| r1 两个 VRRP 组优先级**都是 120** | r1 是两个网段的主，**全部流量走 r1** |
| r2 **完全没有 priority 配置** | ✅ 已核实：r2 用默认 100，**两个组都是 Backup** |
| 两台都**没有** `vrrp vrid X track interface` | ⚠️ **没有上行链路跟踪**（见下） |
| 两台都**没有** `preempt` | 用默认（**抢占开启**），修好后会自动切回来 |
| 两台都**没有** `vrrp vrid X authentication-mode` | ⚠️ VRRP 报文无认证，可伪造（新增审计项 15） |

> ✅ **核实结果**：r2 的 VRRP 配置是
> ```
> interface GigabitEthernet0/0/2
>  vrrp vrid 10 virtual-ip 192.20.27.20        ← 没有 priority 行！
> interface GigabitEthernet0/0/3
>  vrrp vrid 11 virtual-ip 192.20.28.20        ← 同上
> ```
> **只写虚拟 IP 不写优先级**，说明配置者知道"默认 100 就够当备机了"——这是对的，
> 但也意味着**r1 一旦整机宕机，切换完全依赖 VRRP 的 3 秒超时**，没有任何加速手段（没配 BFD）。

#### ⚠️ 一个真实的设计缺陷：没有链路跟踪

想象这个场景：

```
    上级 AS 1001
         ✗  ← r1 的上行链路断了！
         │
    ┌────┴────┐
    │   r1    │ ← 但 G0/0/2 还好好的，VRRP 通告照发
    │ MASTER  │    r2 以为一切正常，继续当 Backup
    └────┬────┘
         │
       PC ── 流量全发给 r1 ── r1 没有上行 ── 黑洞！
```

**r1 自己都上不去了，却还是网关，所有流量被它吞掉。**

正确做法应该配置上行链路跟踪：

```huawei
interface GigabitEthernet0/0/2
 vrrp vrid 10 track interface GigabitEthernet0/0/10 reduced 30
 # 上行口 G0/0/10 断了 → 优先级 120-30=90 < 100 → r2 自动接管
```

甚至应该结合 BFD/NQA 跟踪上行可达性（因为上行口 up 但上级路由器挂了的情况，接口跟踪也发现不了）。

> **这是配置里最值得注意的技术缺陷。** 有 VRRP 不等于有高可用——没有跟踪的 VRRP 在"上行断了但下行没断"这个最常见的故障场景下完全失效。

---

### 4.5 OSPF —— 内部互通

```huawei
ospf 1 router-id 10.10.30.53
 area 0.0.0.0
  network 10.10.1.53 0.0.0.0
  network 10.10.30.53 0.0.0.0
```

#### 逐行解读

| 命令 | 解释 |
|---|---|
| `ospf 1` | 启动 OSPF 进程 1（进程号只在本机有意义，不同路由器可以不同） |
| `router-id 10.10.30.53` | 路由器在 OSPF 域内的身份证，**必须全网唯一**。手工指定（否则自动选，可能变） |
| `area 0.0.0.0` | 区域 0 = **骨干区域**，所有非骨干区域必须连到它 |
| `network 10.10.1.53 0.0.0.0` | 通配符全 0 = 精确匹配。**谁能匹配这个地址，谁就跑 OSPF** → 就是 G0/0/4 |
| `network 10.10.30.53 0.0.0.0` | 精确匹配 Loopback0 → 把 Loopback 网段也宣告进去 |

**宣告结果是**：只有 `10.10.1.52/30`（互联链路）和 `10.10.30.53/32`（Loopback）进 OSPF。

**业务网段 192.20.27.0/24 和 192.20.28.0/24 没有进 OSPF！** 这是**刻意的设计**，原因见下一节。

#### OSPF 在这里的唯一使命

```
                    iBGP 邻居 10.10.30.54
                    （用 Loopback 建）
                           │
                    需要能路由到 10.10.30.54
                           │
                    谁来保证？ → OSPF
```

**OSPF 只负责打通基础设施地址，业务路由交给 BGP。** 这是中大型网络的标准架构：

| 协议 | 承载什么 | 为什么不合并 |
|---|---|---|
| **OSPF** | 只跑 Loopback + 互联链路（少量、稳定、内部可信） | 收敛快，但策略控制能力弱 |
| **BGP** | 跑所有业务网段 | 能做精细过滤和属性操控，但重 |

如果业务网段也进 OSPF：
- 路由表会被业务路由灌满，OSPF 的 SPF 计算变慢
- 无法用 Local_Preference 之类的属性做主备控制
- 无法对上级做严格的进出过滤（OSPF 的过滤能力远弱于 BGP）

#### OSPF 的基本防环/区域概念

- **Area 0（骨干区域）**：所有多区域网络必须有 Area 0，其他区域必须物理/逻辑连到它
- 单区域网络（像这份配置）全部放 Area 0 是最简单也最常见的做法
- OSPF 是**链路状态协议**：每台路由器都知道整个区域的完整拓扑，各自独立跑 SPF 算法算最短路径

---

### 4.6 BGP —— 与外界交换路由

这是配置里最复杂的部分，也是最有价值的部分。

```huawei
bgp 2014
 router-id 10.10.30.53
 timer keepalive 5 hold 15
 peer 10.10.30.54 as-number 2014
 peer 10.10.30.54 connect-interface LoopBack0
 peer 192.80.1.1 as-number 1001
 peer 192.80.106.2 as-number 3002
 #
 ipv4-family unicast
  undo synchronization
  network 192.20.27.0
  network 192.20.28.0
  peer 10.10.30.54 enable
  peer 10.10.30.54 next-hop-local
  peer 10.10.30.54 route-update-interval 5
  peer 192.80.1.1 enable
  peer 192.80.1.1 filter-policy 2003 import
  peer 192.80.1.1 filter-policy 2002 export
  peer 192.80.1.1 route-policy lp01 import
  peer 192.80.1.1 route-update-interval 5
  peer 192.80.106.2 enable
  peer 192.80.106.2 filter-policy 2005 import
  peer 192.80.106.2 filter-policy 2004 export
```

#### 6.1 三个邻居，两类关系

| Peer | AS | 类型 | 是谁 | 建邻方式 |
|---|---|---|---|---|
| **10.10.30.54** | 2014（同 AS） | **iBGP** | xingguo_r2（备份路由器） | 用 Loopback0 建 |
| **192.80.1.1** | 1001（不同 AS） | **eBGP** | 南昌主站 / 上级 | 直连接口（G0/0/10 网段） |
| **192.80.106.2** | 3002（不同 AS） | **eBGP** | 宁都方向 | 直连接口（G0/0/11 网段） |

```
                    eBGP (AS 1001)
                   192.80.1.1
                        │
   ┌────────────────────┼────────────────────┐
   │              AS 2014 (兴国)              │
   │                    │                    │
   │  r1 ═══════ iBGP ═══════ r2             │
   │  .53               │              .54   │
   │                    │                    │
   └────────────────────┼────────────────────┘
                        │
                    eBGP (AS 3002)
                  192.80.106.2
```

#### 6.2 全局参数

```huawei
router-id 10.10.30.53
```
BGP Router-ID，要求和邻居都不同。和 OSPF 用同一个（都是 Loopback 地址），便于记忆和排障。

```huawei
timer keepalive 5 hold 15
```
**默认值是 keepalive 60 / hold 180**（Cisco 是 60/180，华为默认也是 60/180）。

改成 5/15 意味着：
- 每 **5 秒**发一次 keepalive 保活报文
- **15 秒**收不到任何报文就判定邻居死亡，立即撤销路由

| | 默认值 | 本配置 | 效果 |
|---|---|---|---|
| 故障检测时间 | 最长 180 秒 | 最长 15 秒 | **快 12 倍** |
| 代价 | 低 CPU | CPU 和带宽占用明显上升 | 邻居多时会吃不消 |

> **为什么敢这么激进？** 因为这是工业/电力专网，业务中断几秒可能就是事故。而且只有 3 个邻居，CPU 完全扛得住。**如果是互联网核心路由器有几百个邻居，这么配会直接把设备拖死。**

```huawei
peer 10.10.30.54 connect-interface LoopBack0
```
指定用 Loopback0 作为建立 iBGP 连接的源接口。

**为什么？**（这是理解 iBGP 的关键）

```
方案 A（错误）：peer 10.10.1.54  ← 用物理接口建邻
    G0/0/4 链路断了 → BGP 邻居立刻 down
    即使 r1 和 r2 之间还有别的路可以走，BGP 也断了

方案 B（正确）：peer 10.10.30.54 + connect-interface LoopBack0
    G0/0/4 链路断了 → 只要有别的路径能到 10.10.30.54，BGP 就还活着
    前提：Loopback 之间要能互通 → 所以必须跑 OSPF
```

**这就是"OSPF 支撑 iBGP"的完整逻辑闭环。**

#### 6.3 宣告本地网段

```huawei
network 192.20.27.0
network 192.20.28.0
```

**注意这里没有写掩码！** 华为 VRP 中，`network` 不带掩码时按**自然掩码（有类）**处理：

```
192.20.27.0  → C 类地址 → 自然掩码 /24 → 等价于 network 192.20.27.0 255.255.255.0
192.20.28.0  → C 类地址 → 自然掩码 /24
```

**BGP 的 network 命令有个硬性前提**（很多人踩坑）：
> 要宣告的网段**必须已经精确存在于 IP 路由表中**，否则 BGP 不会宣告它。

这里 G0/0/2 配置了 `192.20.27.18/24`，路由表里有 `192.20.27.0/24` 的直连路由，精确匹配，所以能宣告成功。

如果你想宣告一个聚合网段（比如把两个 /24 合成一个 /23），BGP 的 `network` 就不行了，得用 `aggregate`。

#### 6.4 出口过滤（export）—— 我告诉你什么

```huawei
peer 192.80.1.1 filter-policy 2002 export    # ACL 2002 = 192.20.27.0/24 + 192.20.28.0/24
peer 192.80.106.2 filter-policy 2004 export  # ACL 2004 = 192.20.27.0/24（只有 LAN A）
```

**为什么要限制出口通告？** 三个真实原因：

**① 防止成为"过路通道"（Transit AS）**
```
如果不做过滤，r1 会把从宁都(AS3002)学来的 192.20.102.0/24
也通告给南昌(AS1001)。
→ 南昌去宁都的流量全部从兴国绕行
→ 兴国的 2M 小水管被别人的流量撑爆
→ 兴国变成了 AS 3002 和 AS 1001 之间的中转站（免费给人家当快递站）
```

**② 防止路由泄漏引发环路或黑洞**
BGP 是"我说什么你信什么"的协议。错误通告可能让整个专网的路歪掉，甚至形成路由环路。

**③ 安全：不暴露内部拓扑**
只通告该通告的，外界无法从路由表推断你内部有什么网段。

**为什么给宁都只通告 LAN A（192.20.27.0/24）？**
因为那是 **2M 的 DDN 专线**，带宽极小。备份链路只承载最关键的网段（LAN A），LAN B 的流量宁可断掉也不走这条小水管——否则 2M 被撑满，关键业务也跟着卡死。

> 这是**分级降级**的思路：备份链路不是"全都走"，而是"只保最重要的"。

#### 6.5 入口过滤（import）—— 我接收什么

```huawei
peer 192.80.1.1 filter-policy 2003 import    # 只收 173.20.1.0/24 + 173.21.1.0/24
peer 192.80.106.2 filter-policy 2005 import  # 只收 192.20.102.0/24
```

**这是整份配置最重要的安全措施。** 为什么？

**BGP 是"无条件信任"的协议。** 对端发什么路由你就收什么，默认没有任何限制。如果上级路由器被入侵或者配置失误，发给你一条 `0.0.0.0/0`（默认路由）或者一个错误的网段：

```
后果 1：流量劫持
     attacker 在上级注入 173.20.1.0/24 → 指向攻击者的路由器
     → 你去省公司的所有流量（含账号密码）都被送到攻击者那里
     → 这就是 BGP 劫持（BGP Hijacking），互联网上真实发生过无数次

后果 2：路由黑洞
     收到一条错误的明细路由 → 流量发给一个不可达的下一跳 → 业务全断

后果 3：路由表爆炸
     对端误配，把互联网全表 90 万条灌给你 → 设备内存耗尽 → 整机瘫痪
```

**入口白名单就是最后一道防线。** 不管上级发什么，我只收 ACL 里列的两个网段，其他一律丢弃。

> **这是这份配置做得最好的地方。** 很多中小网络完全没有入口过滤，完全信任对端。这个配置做到了"最小权限原则"。

#### 6.6 剩下的三条

```huawei
undo synchronization
```
关闭 BGP 同步。同步规则是**历史遗留**：从 iBGP 学到的路由，必须先通过 IGP 也学到，才会被放进路由表并通告给 eBGP 邻居。现代网络（iBGP 全互联或路由反射器）下这条规则没用还添乱，**所有厂商默认都是关闭的**，这里只是显式确认。

```huawei
peer 10.10.30.54 next-hop-local
```
**对 iBGP 邻居通告路由时，把下一跳改成自己。**

为什么必须配？（这也是经典坑）

```
场景：r1 从 eBGP 邻居 192.80.1.1 学到 173.20.1.0/24，下一跳 = 192.80.1.1

r1 把这条路由通告给 iBGP 邻居 r2：
  ❌ 不配 next-hop-local：下一跳仍是 192.80.1.1
     r2 查路由表：192.80.1.0/24 在哪？不知道！（那是 r1 的直连）
     → 路由不可达 → 不装表 → r2 收不到这条路

  ✅ 配了 next-hop-local：下一跳改成 10.10.30.53（r1 自己）
     r2 查路由表：10.10.30.53 通过 OSPF 可达 ✓
     → 路由生效 → r2 能用这条路
```

**为什么 eBGP 不需要这个？** 因为 eBGP 通告时默认就会把下一跳改成自己，只有 iBGP 默认保持不变（设计如此，为了减少路由抖动）。

```huawei
peer 10.10.30.54 route-update-interval 5
peer 192.80.1.1 route-update-interval 5
```
路由更新间隔改为 5 秒（默认：iBGP 15 秒，eBGP 30 秒）。加快收敛，配合前面的 `timer keepalive 5 hold 15`，整体收敛时间压到 10~20 秒量级。

---

### 4.7 Route-Policy 与 Local_Preference

```huawei
route-policy lp01 permit node 10
 if-match acl 2003
 apply local-preference 400

route-policy lp01 permit node 20
```

```huawei
peer 192.80.1.1 route-policy lp01 import
```

#### Route-Policy 的执行逻辑

Route-Policy 是一串**按顺序执行的节点（node）**，类似程序里的 if-else 链：

```
从 node 10 开始检查
   ↓
node 10:  if 匹配 acl 2003 ?
          ├─ 是 → 执行 apply local-preference 400，permit 通过 → 结束
          └─ 否 ↓
node 20:  if-match 为空 = 匹配所有
          → permit 通过，不修改任何属性 → 结束
   ↓
（如果所有 node 都不匹配 → 隐含 deny all，路由被丢弃）
```

**`node 20` 没有 if-match 也没有 apply，作用是"兜底放通其余所有路由"。**
如果删掉 node 20，那么不匹配 ACL 2003 的路由会被**隐含的 deny all 全部拒绝**——连别的网段都学不到了。

> **这是路由策略最经典的写法**：前面几个 node 做特殊处理，最后一个空 node 兜底。

#### Local_Preference 是什么

BGP 选路有一套**严格的优先级顺序**，Local_Pref 排在第一位（在 Weight 之后，华为默认无 Weight）：

| 顺序 | 属性 | 规则 | 传播范围 |
|---|---|---|---|
| 1 | **Local_Preference** | **越大越优** | **仅在 AS 内部传递** |
| 2 | AS_PATH | 越短越优 | 全网 |
| 3 | Origin | IGP > EGP > Incomplete | 全网 |
| 4 | MED | 越小越优 | 相邻 AS 之间 |
| 5 | EBGP 优于 IBGP | - | - |

**默认值是 100。这里设成 400，意味着"极度优先"。**

#### 这个配置在干什么

```
                 AS 1001 (南昌主站)
                      │
        ┌─────────────┼─────────────┐
        │ 173.20.1.0/24, 173.21.1.0/24│
        │                            │
   直连 eBGP                    经由 r2 转告
        │                            │
   ┌────┴────┐              ┌────────┴────┐
   │   r1    │◄─── iBGP ───►│     r2      │
   │ lp=400  │              │  lp=300 ✅  │
   └─────────┘              └─────────────┘
   
   r1 收到两条去 173.20.1.0/24 的路：
     A: 从 eBGP 直连学的，lp = 400   ← 自己打上去的
     B: 从 iBGP (r2) 学的，lp = 300  ← r2 打上去的
   
   400 > 300 → 选 A → 流量走自己的上行
```

**目的：让 r1 优先用自己的上行链路，而不是绕道 r2。**

✅ **r2 的实际配置**（此前只能猜）：

```huawei
route-policy lp01 permit node 10
 if-match acl 2003
 apply local-preference 300        ← 不是原先猜的 200，是 300
```

于是完整的优先级体系是：

| 路由来源 | Local_Pref | 谁用 |
|---|---|---|
| r1 从自己上行（192.80.1.1）学到的 173 网段 | **400** | r1 优选，且通过 iBGP 传给 r2 |
| r2 从自己上行（192.80.9.1）学到的 173 网段 | **300** | r2 传给 r1，作为备选 |
| 其他所有路由（node 20 兜底，不打标） | 100 | 默认 |

- r1 上看：400（自己）> 300（经 r2）→ **走自己的上行** ✓
- r2 上看：400（经 r1，iBGP 学来）> 300（自己）→ **也绕道 r1** ✓
- r1 上行断了 → r1 只剩 300 那条 → **自动改走 r2** ✓，r2 也回到自己的 300 ✓

> 🔑 **这才是这套设计的精髓**：LP 是**在 AS 内部传递**的，所以只要 r1 打 400、r2 打 300，
> **两台设备会得出同一个结论——优先走 r1**。不需要任何额外协商，全网选路自动一致。
>
> 这也解释了为什么两台设备的 `route-policy` 名字都叫 `lp01`、`if-match` 都用 ACL 2003，
> **只有 `apply local-preference` 那一行不同**：这是一套**成对设计**的策略。
> 以后改主备关系，只要改这两个数字的大小关系即可。

> 注意：从 `route-policy lp01 permit node 20` 可以看出，**不匹配 ACL 2003 的路由保持默认 lp=100**。所以整个 r1 上的优先级体系是：**173 网段 400 > 其他 100**。

#### 一个可以改进的地方

`filter-policy 2003 import` 和 `route-policy lp01 import` 里的 `if-match acl 2003` **重复了**：

```huawei
peer 192.80.1.1 filter-policy 2003 import      # 只放行 173.20.1.0/24 + 173.21.1.0/24
peer 192.80.1.1 route-policy lp01 import       # lp01 node10 又匹配了一次 acl 2003
```

执行顺序是 filter-policy 先过滤，再交给 route-policy。经过 filter-policy 之后，剩下的路由**本来就全是 173 网段**，route-policy 的 if-match 判断恒为真。

这不是错误（防御性冗余，改其中一个不会立刻出事），但说明配置者思路有点乱。更清晰的写法是二选一：

```huawei
# 写法 A：只用 route-policy（推荐，一个地方管完）
peer 192.80.1.1 route-policy lp01 import

# 写法 B：filter-policy 过滤 + route-policy 无条件打标
route-policy lp01 permit node 10
 apply local-preference 400
peer 192.80.1.1 filter-policy 2003 import
peer 192.80.1.1 route-policy lp01 import
```

---

### 4.8 AAA 与用户管理

```huawei
aaa
 authentication-scheme default
 authentication-scheme radius
  authentication-mode radius
 authorization-scheme default
 accounting-scheme default
 domain default
  authentication-scheme default
 domain default_admin
  authentication-scheme default
 local-user admin password irreversible-cipher $1a$Wm!,...
 local-user admin privilege level 15
 local-user admin service-type telnet http
 local-user jxtrq password irreversible-cipher $1a$)8lSSg_TR0$...
 local-user jxtrq privilege level 3
 local-user jxtrq service-type terminal ssh ftp
```

#### 两个账号对比

| | admin | jxtrq |
|---|---|---|
| 密码存储 | `irreversible-cipher`（不可逆）✅ | `irreversible-cipher` ✅ |
| 权限级别 | **15**（最高） | 3（管理级，**不是只读**） |
| 允许的服务 | **telnet, http** | terminal(console), ssh, **ftp** |
| 安全评价 | 🔴 最高权限 + 明文协议 | ⚠️ 权限被低估 + FTP 明文 |

#### 关键知识点

**① `irreversible-cipher` vs `cipher`**

| | cipher | irreversible-cipher |
|---|---|---|
| 算法 | 可逆加密 | 哈希（不可逆） |
| 设备能否还原明文 | **能** | 不能 |
| 原因 | 某些协议（如 CHAP、IPsec 预共享密钥）需要明文参与计算 | 纯登录认证只需比对哈希 |
| 安全性 | 较低 | **高** ✅ |

**② 权限级别（华为 0-15）—— 这里有个常见误解**

```
命令级别（决定这条命令需要多大权限才能执行）
  level 0   参观级  ping、tracert、telnet、display version
  level 1   监控级  大部分 display，不能改配置
  level 2   配置级  业务配置：接口 IP、路由协议、ACL
  level 3   管理级  文件系统、FTP/TFTP、reboot、用户管理、改命令级别
  level 4-15       默认未使用；可用 command-privilege 把个别命令提到更高级

判断规则（就这么简单）：用户级别 ≥ 命令级别 → 允许执行
```

> ⚠️ **纠正：level 3 不是"只读账号"**
>
> 本文档初稿把 jxtrq（level 3）写成"只能看，不能改"，**这是错的**，必须纠正：
>
> 1. **华为命令默认最高级别就是 3。** 用户级别 ≥ 3 即可执行全部命令，
>    包括 `reboot`、下载配置、改其他用户密码。level 3 已经是很高的权限。
> 2. **真正的只读应该设 level 1**（只能 display，进不了 system-view 改配置）。
> 3. **命令级别可改**：`command-privilege level 15 view shell reboot` 能把 reboot 提到 15 级。
>    所以同一级别在不同设备上的实际能力可能不同。
> 4. **实际权限是四处叠加的结果**：
>    ```
>    ① local-user privilege level（admin=15, jxtrq=3）
>    ② 用户接口下的 user privilege level（本例 vty 0 设了 15）
>    ③ 命令自身级别（默认 0-3，或已被 command-privilege 改过）
>    ④ AAA domain 下的认证/授权方案
>    ```
>    特别是第 ② 条：本例 `user-interface vty 0` 设了 `user privilege level 15`，
>    **可能把低级别账号从该通道登录时的权限直接抬到 15**。
>
> **结论**：jxtrq 是管理级账号，权限不低；它与 admin 的差距没有"3 和 15"看起来那么大。

`admin` 是 15 级 —— 拿到它就等于拿到了这台设备的**完整控制权**。

**③ `service-type` 是白名单**
`admin` 的 service-type 是 `telnet http`，意味着：
- ✅ 能 telnet 登录
- ✅ 能 http 登录
- ❌ **不能 ssh 登录**（虽然 SSH 服务开了）
- ❌ 不能 console 登录
- ❌ 不能 ftp

> 这里出现了一个**荒诞但真实的情况**：设备唯一开了 SSH（`stelnet server enable`），
> 但**最高权限账号 admin 反而不能用 SSH 登录**——它的 service-type 里没有 ssh。
>
> 结果就是：想用安全的方式（SSH）管理设备，只能用低权限的 jxtrq；
> 想用 admin 管理，就必须走明文协议（Telnet/HTTP）。**安全配置和使用需求完全对不上。**

#### ⚠️ 严重问题：Telnet 和 HTTP（明文协议）

```
local-user admin privilege level 15
local-user admin service-type telnet http    ← 一个 15 级账号走明文协议！
```

**Telnet 的所有流量（包括用户名密码）都是明文在网线上传输。** 任何人在这条链路上的任意一点抓包，都能拿到完整的 15 级账号密码。

```
抓包结果示意：
  ...  A  d  m  i  n  @  1  2  3  ...
       └─ 15 级最高权限账号的密码，明文可见 ─┘
```

**HTTP 同理**，Web 管理页面的登录表单也是明文提交。

#### 🔴 最严重的问题：密码已经泄露在这份文本里

看配置文件最后几行：

```
<xingguo_r1>Admin@123
            ^
Error: Unrecognized command found at '^' position.
```

**这是操作员把密码直接敲进了命令行提示符！** 因为 `<xingguo_r1>` 是用户视图提示符，不是密码输入框，所以密码被当成命令执行，报了"无法识别的命令"错误，然后**回显在日志里**。

所以这份配置文件的泄露范围包括：
- ✅ 15 级账号 `admin` 的密码：**`Admin@123`**
- ✅ Console 登录密码（被加密存储，但可能是弱密码）
- ✅ 设备 MAC 地址
- ✅ 完整网络拓扑和 IP 规划
- ✅ SNMP community（虽然是密文存储，但 v2c 本身可被抓包获取）
- ✅ 所有内部网段和路由策略

**`Admin@123` 是典型的弱密码**：常见单词 + 简单数字后缀，在几乎所有密码字典的前 1000 条里。

> **给你的实战提醒**：任何导出的配置文件，在发给别人（或上传到知识库、AI）之前，都应该检查末尾有没有误敲的内容。这类"手滑把密码敲进命令行"的事故在真实运维中**极其常见**。

---

### 4.9 远程管理：SSH / HTTPS / VTY

```huawei
ssh client first-time enable
stelnet server enable

http secure-server ssl-policy default_policy
http secure-server enable
http server permit interface GigabitEthernet0/0/9
```

| 命令 | 解释 |
|---|---|
| `stelnet server enable` | 开启 SSH（华为叫 Stelnet）服务端 ✅ |
| `ssh client first-time enable` | 作为 SSH 客户端时，首次连接自动信任对端公钥（不需要手动确认）。**方便但有中间人攻击风险** |
| `http secure-server enable` | 开启 HTTPS 管理 ✅ |
| `http server permit interface G0/0/9` | **只允许从 G0/0/9 口访问 HTTP 服务** |

**关于 `http server permit interface G0/0/9`**：G0/0/9 **没有配置 IP 地址**，等于这个口根本不通。所以这行配置的效果是——**HTTP/HTTPS 管理实际上无法从任何地方访问**。

这可能是：
- (a) 故意的安全加固（关闭 Web 管理，只用命令行）✅ 如果是这样，做得对
- (b) 配置遗漏（想开放但忘了配 IP）❌ 那 Web 管理就是坏的

从整体看倾向 (a)：把管理面收敛到命令行 + SSH，是更安全的做法。

#### SSL 策略的问题

```huawei
ssl policy default_policy type server
 pki-realm default
 version tls1.0 tls1.1
 ciphersuite rsa_aes_128_cbc_sha
```

| 项目 | 配置 | 评价 |
|---|---|---|
| TLS 版本 | **TLS 1.0 / 1.1** | 🔴 **早已被废弃**（RFC 8996 正式弃用），PCI-DSS 等合规标准禁止使用 |
| 加密套件 | RSA-AES-128-CBC-SHA | ⚠️ CBC 模式有 BEAST、Lucky13 等已知攻击；**RSA 密钥交换无前向保密(PFS)** |
| 支持的版本 | 没有 TLS 1.2 / 1.3 | 🔴 现代浏览器（Chrome/Firefox 新版）**会直接拒绝连接** |

**应该改成**：
```huawei
ssl policy default_policy type server
 version tls1.2 tls1.3
 ciphersuite ecdhe_rsa_aes128_gcm_sha256 ecdhe_rsa_aes256_gcm_sha384
```

> **前向保密（PFS）是什么**：用 RSA 密钥交换时，如果攻击者录下了你的加密流量，日后拿到了服务器私钥，就能**解密全部历史流量**。用 ECDHE 的话，每次会话的密钥都是临时生成的，私钥泄露也解不开历史记录。

#### VTY 登录通道

```huawei
user-interface con 0
 authentication-mode password
 set authentication password cipher %^%#i/[&C:aP@(_52@&M>...

user-interface vty 0
 authentication-mode aaa
 user privilege level 15

user-interface vty 1 4
 authentication-mode aaa
```

| 通道 | 认证方式 | 权限 | 问题 |
|---|---|---|---|
| `con 0`（Console 口） | 只要密码，不要用户名 | 默认 3 级 | ⚠️ 无用户名，无法追溯"谁用串口登录过" |
| `vty 0` | AAA（用户名+密码） | **15 级** | 🔴 一登录就是最高权限 |
| `vty 1 4` | AAA | 默认（0 级） | - |

**`vty 0 4` 表示 vty 0 到 4 共 5 个通道 = 最多 5 人同时远程登录。**

🔴 **最严重的缺失：VTY 没有 ACL 限制**

正确做法应该是：

```huawei
acl 2000
 rule 5 permit source 173.20.1.178 0        # 只允许网管服务器
 rule 10 permit source 192.20.27.30 0       # 只允许运维主机
 rule 100 deny source any
user-interface vty 0 4
 acl 2000 inbound                            # 应用 ACL
```

现在的状态是：**全网任何一个角落（包括下级单位、被入侵的办公 PC）都能尝试 SSH 登录这台核心路由器。** 配合弱密码 `Admin@123`，这就是一条完整的攻击链。

---

### 4.10 SNMP —— 网管监控

```huawei
snmp-agent local-engineid 800007DB038446FE3D5453
snmp-agent community read %^%#yHC(I9(!g)...  mib-view iso
snmp-agent sys-info contact call tel at 13986101665
snmp-agent sys-info location XingGuo-R1
snmp-agent sys-info version v2c
snmp-agent target-host trap-hostname imc address 173.20.1.178 udp-port 162 trap-paramsname imc
snmp-agent target-host trap-paramsname imc v2c securityname %^%#1fYV,bw#l2$_6w;yvM!...
snmp-agent mib-view iso include iso
snmp-agent trap source GigabitEthernet0/0/2
snmp-agent trap enable
snmp-agent
```

#### SNMP 是什么

```
┌──────────┐                    ┌──────────┐
│ 网管系统  │  SNMP Get (161) →  │  路由器   │   "你的 CPU 多少？接口流量多少？"
│  (iMC)   │  ← SNMP Trap(162)  │  (Agent)  │   "我 G0/0/10 断了！"（主动上报）
└──────────┘                    └──────────┘
```

| 概念 | 解释 |
|---|---|
| **NMS** | 网管系统（这里是 H3C iMC，地址 173.20.1.178） |
| **Agent** | 跑在被管设备上的 SNMP 服务 |
| **MIB** | 管理信息库，一棵树状结构，每个节点是一个可查询的变量（如接口流量、CPU） |
| **OID** | MIB 树上的节点编号，如 `1.3.6.1.2.1.1.1` 是设备描述 |
| **Community** | v1/v2c 的"密码"，**明文传输** |
| **Trap** | 设备主动向 NMS 发送的事件通知（UDP 162） |
| **Get** | NMS 主动查询（UDP 161） |

#### 这段配置在干什么

| 命令 | 含义 |
|---|---|
| `community read ...` | 只读 community 字符串（已在配置文件中加密显示） |
| `sys-info version v2c` | 使用 SNMP **v2c** 版本 |
| `target-host trap-hostname imc address 173.20.1.178 udp-port 162` | Trap 发给网管服务器 173.20.1.178 |
| `trap source GigabitEthernet0/0/2` | Trap 报文的源 IP 用 G0/0/2 的地址（192.20.27.18） |
| `trap enable` | 开启 Trap 上报 |
| `sys-info contact call tel at 13986101665` | 联系人信息（**这里泄露了手机号**） |

#### ⚠️ 安全问题

**① SNMP v2c 的致命缺陷**

```
v2c 数据包（明文）：
  ┌────────────────────────────────┐
  │ community: "public"  ← 明文！   │
  │ 查询内容: 接口流量、配置...      │
  └────────────────────────────────┘
```

- Community 字符串**明文传输**，抓包即见
- **没有加密、没有完整性校验**
- 有了 read community，攻击者能读取设备的完整配置和所有接口流量数据
- 如果是 write community，攻击者能**直接修改配置**（比如下载路由、改 ACL）

**应该升级到 SNMPv3**：

```huawei
snmp-agent sys-info version v3
snmp-agent group v3 netadmin privacy
snmp-agent usm-user v3 monitor group netadmin
snmp-agent usm-user v3 monitor authentication-mode sha2-256 密码
snmp-agent usm-user v3 monitor privacy-mode aes256 密码
```

v3 提供：认证（确认你是谁）+ 加密（数据不可见）+ 基于视图的访问控制（VACM）。

**② `mib-view iso include iso` = 暴露整棵 MIB 树**

`iso` 是 MIB 树的根（OID 1）。`include iso` 意味着**这个 community 能读取设备上的所有 MIB 对象**，包括：
- 完整 running-config
- 所有接口的实时流量
- ARP 表、MAC 表、路由表
- 甚至某些 MIB 能读到用户列表

**应该按需最小化授权**，只开放需要的子树（比如只开放接口流量统计 `1.3.6.1.2.1.2`）。

**③ Trap 源地址用了物理接口**

```
snmp-agent trap source GigabitEthernet0/0/2   → 源 IP = 192.20.27.18
```

问题：如果 r1 宕机或 VRRP 主备切换，网管看到的 Trap 源地址会从 `.18` 变成 `.19`（r2），**同一台"逻辑设备"有两个身份**，网管的告警关联和拓扑图会错乱。

**应该用 Loopback0**（`snmp-agent trap source LoopBack0`），源地址固定为 `10.10.30.53`，与设备身份绑定，不随链路变化。

**④ 个人信息泄露**

`snmp-agent sys-info contact call tel at 13986101665` —— 手机号明文写在配置里。任何有 read community 的人都能拿到。这既是隐私问题，也是**社会工程学攻击的素材**（攻击者冒充运维人员打电话给这个号码套取信息）。

---

### 4.11 NTP —— 时间同步

```huawei
ntp-service source-interface LoopBack0
ntp-service unicast-server 192.20.27.30
```

| 命令 | 解释 |
|---|---|
| `unicast-server 192.20.27.30` | 从 LAN A 里的 `192.20.27.30` 这台服务器同步时间（单播模式） |
| `source-interface LoopBack0` | NTP 报文源地址用 `10.10.30.53` ✅ **这是对的** |

对比一下 SNMP 用物理口、NTP 用 Loopback —— **同一份配置里两种做法，说明配置不够规范统一。**

#### 为什么时间同步是安全基础设施

```
场景：发生了安全事件，需要还原攻击链

设备 A 日志：10:23:15  异常登录
设备 B 日志：10:31:02  配置被改
设备 C 日志：10:19:48  流量异常

如果时间不同步（各差几分钟）→ 无法确定先后顺序 → 无法判断因果关系
→ 事件调查失败
```

NTP 还影响：
- 数字证书有效期验证（时间错了，证书会被判定为"未生效"或"已过期"）
- 计费系统（按时间计费的话）
- 日志轮转和归档
- 双因素认证（TOTP 动态口令依赖时间）

#### 可以改进的地方

1. **只有一个 NTP 服务器** —— 单点故障，应该配 2~3 个
2. **没有认证** —— NTP 可以被欺骗（NTP 放大攻击、时间偏移攻击）。应该配置 `ntp-service authentication`
3. **192.20.27.30 是内网服务器** —— 它自己从哪同步？如果是手动设的，整网时间会慢慢漂

---

### 4.12 可以忽略的默认模板

配置里有大段"看起来很厉害但什么都没干"的内容，它们是**设备出厂自带的默认模板**，了解一下就行，不要被吓到：

```huawei
# 认证相关（802.1x / MAC / Portal 认证）—— 全是空模板，没启用
authentication-profile name default_authen_profile
authentication-profile name dot1x_authen_profile
authentication-profile name mac_authen_profile
authentication-profile name portal_authen_profile
...
dot1x-access-profile name dot1x_access_profile
mac-access-profile name mac_access_profile
free-rule-template name default_free_rule
portal-access-profile name portal_access_profile

# RADIUS 服务器模板 —— 空的，没配服务器地址
radius-server template default

# PKI 证书域 —— 空的
pki realm default

# IPsec IKE 提议 —— 默认模板，且配置里没有任何 ipsec policy 引用它
ike proposal default
 encryption-algorithm aes-256
 dh group14
 authentication-algorithm sha2-256
 authentication-method pre-share
 integrity-algorithm hmac-sha2-256
 prf hmac-sha2-256

# 无线控制器（WLAN AC）—— 全是默认 profile，没建 AP
wlan ac
 traffic-profile name default
 security-profile name default
 ssid-profile name default
 ...

# 防火墙区域 —— 只有个空壳
firewall zone Local

# 其他
ops
autostart
secelog
```

#### 几个值得单独说的

**① IKE proposal —— 配置了但没用**

```huawei
ike proposal default
 encryption-algorithm aes-256
 dh group14
 authentication-algorithm sha2-256
 authentication-method pre-share
 integrity-algorithm hmac-sha2-256
 prf hmac-sha2-256
```

这套参数本身是**相当不错的安全配置**（AES-256 + DH group14 + SHA2-256，都不落后）。

**但是**：整个配置文件里**没有任何 `ipsec policy` 或 `ipsec profile` 引用它**，也没有 `ike peer`。也就是说——

> **IPsec VPN 根本没有部署，这只是一个默认的空提议。**

这意味着：**所有跨越专网的业务数据都是明文传输的**。如果这段链路（尤其是宁都那条 DDN 2M 专线，很可能是租用运营商线路）被窃听，数据直接可见。

**② `security-profile name default-wds` 里有一个无线密码**

```huawei
security-profile name default-wds
 security wpa2 psk pass-phrase %^%#y]5mB7S=,Q4\JTMUXb\Y%H>A40VL\GZCPLK|::#J%^%# aes
```

这是默认的 WDS（无线分布式系统）安全模板，出厂自带，而且**没有被任何 AP 或 VAP 引用**，所以没有实际风险。但要知道它存在。

**③ `firewall zone Local`**

只有一个空的本地区域定义，没有任何区域间策略。**这台设备的防火墙功能等于没启用**——它就是一台纯路由器。访问控制完全依赖路由层面的过滤（BGP filter-policy），**而不是数据包层面的过滤**。

> **重要认知**：这份配置里**没有任何一条真正的数据包过滤规则**。没有任何 `traffic-filter`、没有 `firewall packet-filter`、没有安全策略。所有 ACL 都是用来筛路由的。
>
> 这意味着：**只要路由可达，任何流量都能通过**。访问控制是在"路由"这个层面做的（我不告诉别人怎么来找我），而不是在"包"这个层面做的（我拒绝某些包）。
>
> 这是专网路由器的典型做法（相信内部，边界靠物理隔离），但从纵深防御角度看是不足的。

---

## 完整走一遍：一个数据包的旅程

理论讲完了，跟着一个真实的包走一遍，把所有知识串起来。

### 场景：LAN A 的一台 PC（192.20.27.100）访问省公司服务器（173.20.1.50）

#### 第 1 步：PC 判断要不要走网关

```
PC 配置：IP 192.20.27.100/24，网关 192.20.27.20

目的 IP: 173.20.1.50
计算: 173.20.1.50 AND 255.255.255.0 = 173.20.1.0
我的网段: 192.20.27.0
173.20.1.0 ≠ 192.20.27.0
→ 不在同一网段，发给网关 192.20.27.20
```

#### 第 2 步：ARP 解析网关的 MAC

```
PC 广播: "谁是 192.20.27.20？告诉我你的 MAC"

r1 (VRRP Master) 回应: "我是 192.20.27.20，MAC 是 84:46:FE:3D:54:53"
                        ↑ 注意：回的是虚拟 MAC，不是物理 MAC
                          VRRP 虚拟 MAC 格式: 00-00-5E-00-01-{vrid}
                          vrid 10 → 00-00-5E-00-01-0A

r2 (Backup): 保持沉默，不回应
```

**VRRP 虚拟 MAC 的规律**：`0000.5E00.01XX`，XX 是 VRID 的十六进制。vrid 10 = 0x0A，所以是 `00-00-5E-00-01-0A`。

#### 第 3 步：PC 封装并发送

```
以太网帧:
  目的 MAC: 00-00-5E-00-01-0A   ← VRRP 虚拟 MAC（r1 在响应）
  源   MAC: PC 的 MAC
IP 包:
  源   IP: 192.20.27.100
  目的 IP: 173.20.1.50
TCP:
  源端口: 51000  目的端口: 443
```

#### 第 4 步：接入交换机转发

交换机根据目的 MAC `00-00-5E-00-01-0A` 查 MAC 地址表 → 从连接 r1 的口转发出去。

#### 第 5 步：r1 收到帧，查路由表

```
r1 查路由表，找能匹配 173.20.1.50 的最精确路由:

Destination/Mask    Proto  Pre  Cost  NextHop       Interface
173.20.1.0/24       BGP    255  0     192.80.1.1    G0/0/10    ← 命中！
0.0.0.0/0           ...                                        （更不精确，不用）

这条路由哪来的？
  从 eBGP peer 192.80.1.1 学来
  经过 filter-policy 2003 import 检查（173.20.1.0/24 在 ACL 2003 里，放行）✓
  经过 route-policy lp01，打上 local-preference 400 ✓
```

#### 第 6 步：r1 重新封装并从上行口发出

```
新以太网帧:
  目的 MAC: 192.80.1.1 的 MAC（通过 ARP 学到）
  源   MAC: G0/0/10 的 MAC
IP 包:
  源   IP: 192.20.27.100   ← 没变！
  目的 IP: 173.20.1.50     ← 没变！
```

**这就是第 1 节说的"IP 不变，MAC 每跳重写"。**

#### 第 7 步：上级 AS 1001 继续转发到省公司

#### 第 8 步：回程流量

回程包 目的 IP = 192.20.27.100。上级路由器怎么知道 192.20.27.0/24 在哪？

```
因为 r1 用 network 192.20.27.0 向 192.80.1.1 宣告了这个网段，
而且 filter-policy 2002 export 允许通告它（192.20.27.0/24 在 ACL 2002 里）✓
```

**如果忘了 `network` 或者被 `filter-policy` 挡掉，去程能通、回程不通 —— 这是最常见的"单向通"故障。**

### 场景 2：主用上行链路断了，发生了什么？

```
时间 T+0s:   G0/0/10 链路物理中断
             r1 的 G0/0/10 接口 down
             → 直连路由 192.80.1.0/24 消失
             → 从 192.80.1.1 学来的 BGP 路由全部失效

时间 T+0~5s: BGP 开始发 keepalive，但发不出去

时间 T+15s:  hold timer 超时（hold 15）
             → BGP 判定 peer 192.80.1.1 死亡
             → 撤销从它学来的所有路由（173.20.1.0/24、173.21.1.0/24）

时间 T+15s:  路由表里现在还有一条去 173.20.1.0/24 的路吗？
             → 有！从 iBGP peer 10.10.30.54 (r2) 学来的，lp = 300 ✅（r2 配置已核实）
             → 装表，下一跳 10.10.30.54

时间 T+15.1s: r1 通过 OSPF 查到 10.10.30.54 可达（走 10.10.1.54）
             → 流量改道：PC → r1 → r2 → r2 的上行 → 省公司

总收敛时间: 约 15 秒 + 少量处理时间
```

**如果配了 `timer keepalive 60 hold 180`（默认），这个过程要 3 分钟。** 这就是那三行 timer 配置的价值。

#### 但是！VRRP 的问题暴露了

```
关键：G0/0/10 断了，但 G0/0/2（下行到 LAN A）还好好的

r1 依然是 VRRP Master（因为没配 track）
→ PC 依旧把流量发给 192.20.27.20（r1）
→ r1 收到后，通过 iBGP 转到 r2
→ 能通！（因为 r1-r2 之间有 G0/0/4 互联）
```

**幸好 r1 和 r2 之间有 iBGP + 互联链路，流量能绕过去。** 所以实际不会断网，只是**路径多绕了一跳**。

但如果：
- r1 整机宕机 → VRRP 正常切换到 r2 ✓
- r1 上行断 + G0/0/4 也断 → r1 成为孤岛，VRRP 却不切换 → **黑洞** ✗

**所以 `vrrp vrid 10 track interface G0/0/10 reduced 30` 还是应该配上**，能让流量在第一跳就走最优路径，而不是绕道。

### 场景 3：宁都那条 2M 链路什么时候用？

✅ **拿到 r2 配置后，这里可以少一个问号了：r2 上没有宁都方向的邻居。**

r2 的 BGP 只有两个 peer（`10.10.30.53` 和 `192.80.9.1`），**没有 `192.80.106.2`**；
r2 的 ACL 也只有 2002/2003，**没有 2004/2005**。所以：

```
宁都 2M 链路是 r1 独有的，r2 上完全没有对应配置。

正常情况:
  LAN A/B → r1 → 192.80.1.1 (AS 1001, 以太网高速)
  宁都链路: r1 的 BGP 里只有 LAN A 被通告过去（export ACL 2004）
            → 作为 173 网段的兜底 / 或承载宁都方向的业务

r1 链路 A 断:
  → 走 r2（lp 300），宁都用不上

r1 链路 A 断 + r2 上行(192.80.9.1)也断:
  → 只剩宁都 2M（前提是宁都方向能通到上级）
  → 只有 LAN A 的流量能走（export 2004 只通告 LAN A）
  → LAN B 断网

r1 整机宕机:
  → VRRP 切到 r2，但 r2 没有宁都链路
  → 宁都方向业务彻底中断 ← ⚠️ 这是 r1 单点故障，双机冗余覆盖不到
```

> ⚠️ **仍有两处需要实地确认**：
> 1. **宁都方向到底能不能通到上级？** 配置里看不出来——r1 只是和 192.80.106.2 建了 eBGP，
>    对端后面是什么、能不能到达 173.20/173.21 网段，需要看收到的实际路由。
> 2. **实际的 BGP 选路结果是什么？** 只有 `display bgp routing-table` 能告诉你真相。
>
> ~~r2 是否有对称配置~~ —— **已确认：没有。** 宁都链路是 r1 独占的单点。

---

## 设计意图总结：为什么这么设计

把散落的点收拢成体系。这份配置体现了**一个中型行业专网汇聚站点的标准设计范式**：

### 原则 1：消除所有单点故障

| 单点 | 冗余方案 | 配置体现 | ✅ 双机视角复核 |
|---|---|---|---|
| 上行链路（南昌方向） | 两台各有一条上行 | r1: 192.80.1.1；r2: 192.80.9.1 | ✅ **冗余成立** |
| 上行链路（宁都 2M） | ❌ **无冗余** | 只有 r1 有 G0/0/11 → 192.80.106.2 | 🔴 **r2 上没有，单点** |
| 路由器 | 双机 VRRP | r1 prio 120 / r2 默认 100 | ✅ **冗余成立** |
| 内部互联 | 一条互联链路 | G0/0/4（10.10.1.52/30）+ OSPF | ⚠️ 只有一条物理路径 |
| BGP 会话 | Loopback 建邻 | connect-interface LoopBack0 | ⚠️ 但 Loopback 只有一条物理路径可达 |
| NTP | ❌ **无冗余** | r1→192.20.27.30；r2→192.20.28.30 | ⚠️ **各指一台，且不是同一台** |
| 远程接入 | 4G 模块（未配置） | Cellular0/0/0~1 | ❌ 有硬件无配置 |

> **复核结论**：双机冗余**只覆盖了"南昌方向"这一个出口**。
> 宁都 2M 这条链路在 r2 上完全没有对应配置，**r1 整机宕机 = 宁都方向业务中断**。
> 这是"买了两台路由器"容易被误认为"什么都有冗余"的典型盲区——
> **冗余是按链路、按业务逐条算的，不是按设备台数算的。**

### 原则 2：快速故障检测和收敛

```
BGP timer: 60/180 → 5/15          （故障检测从 3 分钟 → 15 秒）
route-update-interval: 15/30 → 5  （路由传播快 3~6 倍）
```

代价：CPU 占用上升。因为只有 3 个邻居，完全可以承受。

### 原则 3：最小权限 —— 只说该说的，只听该听的

```
出口过滤: 我只通告本地业务网段，不当中转站，不泄露内部拓扑
入口过滤: 我只接收白名单网段，防止路由劫持和路由表爆炸
```

**这是 BGP 最重要的安全实践。** 互联网上大量的 BGP 事故（巴基斯坦电信劫持 YouTube、Level3 泄漏导致日本全国断网）都是因为没做这个。

### 原则 4：协议分工清晰

```
OSPF:  基础设施（Loopback + 互联），求快
BGP:   业务路由，求可控
VRRP:  网关冗余，对用户透明
```

不混用，各司其职。

### 原则 5：可预测的路径选择

用 Local_Preference 显式指定优先级，而不是依赖默认的自动选路。

✅ **r2 配置到手后，这一点从"推测"变成了"确凿"**：

```
r1:  apply local-preference 400     ← 从自己上行学到的 173 网段
r2:  apply local-preference 300     ← 从自己上行学到的 173 网段
```

两台设备用**同一个 route-policy 名字、同一条 ACL、只差一个数字**，
构成一个 `400 > 300 > 100` 的三级体系。因为 LP 在 AS 内传递，
**两台设备会独立算出同一个结论：优先走 r1。**

**可预测 > 最优。** 出故障时你能准确预判流量会怎么走，比"理论上最优"重要得多。

### 原则 6：可运维性

```
description to LAN A / to nanchang zhu / Connect to xingguo_r2
sysname xingguo_r1 / xingguo_r2
SNMP 上报到网管 iMC（两台都配了）
NTP 时间同步（但两台指的不是同一台服务器 ⚠️）
主机位规划一致（r1=.53, r2=.54）✅ 已核实
```

> ⚠️ **NTP 这个细节值得单独说**：r1 指向 `192.20.27.30`，r2 指向 `192.20.28.30`。
> 这是"各自用本网段的服务器"的思路，看似合理，实际有两个问题：
> ① **两台设备时间可能差几毫秒到几秒**，跨设备比对日志时（比如查一次故障的先后顺序）会很痛苦；
> ② 两台都没有第二个 NTP 源，任何一台服务器挂了，对应设备的时间就开始漂移。
> 正确做法是**两台都配相同的 2~3 个 NTP 源**，让它们同步到同一个时间基准。

### 一份成熟度评分（已按双机视角重评）

| 维度 | 评分 | 说明 |
|---|---|---|
| 高可用性设计 | ⭐⭐⭐（↓1） | 南昌方向双机冗余成立；但**宁都链路 r1 独占**、缺 VRRP 上行跟踪、互联只有一条物理路径 |
| 路由策略控制 | ⭐⭐⭐⭐⭐ | 进出口过滤完整，Local_Pref 成对设计（400/300），**双机选路一致** |
| 收敛速度 | ⭐⭐⭐⭐⭐ | 参数激进，符合专网需求 |
| 地址规划 | ⭐⭐⭐⭐⭐ | 有规律（r1=.53/r2=.54），**已核实两台都遵守** |
| 配置一致性 | ⭐⭐⭐ | 主体对称，但 r2 缺 ACL 2004/2005、缺宁都邻居、NTP 源不同（新增审计项 15） |
| **管理面安全** | ⭐⭐ | 🔴 **Telnet/HTTP、弱密码、无登录源限制、TLS1.0** |
| **监控与日志** | ⭐⭐ | SNMP v2c 明文、无日志外发、NTP 不同源、Trap 源用物理口 |
| 文档规范性 | ⭐⭐ | 有 description，但有残留配置未清理（r1 的 G0/0/1） |
| **数据加密** | ⭐ | 🔴 **IPsec 未部署，业务数据明文传输** |

**总结一句话：这是一份网络设计水平不错、但安全意识明显滞后的配置。典型的"重连通、轻安全"的工程现场产物。**

---

## 安全审计：这份配置的 16 个问题

> **按三个平面分类看，问题分布是这样的**（详见基础文档第 12 节）：
>
> | 平面 | 这份配置的问题 |
> |---|---|
> | **管理平面** | 问题 1、2、3、4、5、6、10、11、12、**14** —— 占了绝大多数 |
> | **控制平面** | 问题 **13**（路由协议无认证）、**15**（VRRP 无认证 + 双机配置不一致）—— 条数少但后果严重 |
> | **数据平面** | 问题 7、8 —— 无加密、无过滤 |
> | **可用性** | 问题 9、**16**（宁都链路单点 / 时钟异常）—— 不是"被攻击"，但一样会断业务 |
>
> 这也印证了那句话：**设备被控，绝大多数是从管理平面进来的。**
>
> 🆕 **第 14、15、16 项是拿到 r2 配置后新增的**——单看一台设备根本发现不了。

按严重程度排序。这些是你作为网络安全方向学习者最该关注的部分。

### 🔴 P0 级（高危，应立即修复）

**1. 15 级最高权限账号密码泄露且为弱密码**
```
证据: <xingguo_r1>Admin@123 → Error: Unrecognized command
影响: 拿到 admin = 完全控制核心路由器 = 可以劫持全网流量
修复: 立即改密码；用 12 位以上随机密码；定期轮换
```

**2. Telnet 明文协议被用于 15 级账号**
```
证据: local-user admin privilege level 15
      local-user admin service-type telnet http
影响: 抓包即可获得最高权限凭证
修复: service-type 改为 ssh；全局 undo telnet server enable
```

**3. VTY 无登录源限制**
```
证据: user-interface vty 0 4 下无 acl inbound
影响: 全网任意位置可暴力破解
修复: 配置 ACL 只允许运维管理网段登录
```

**4. VTY 0 直接赋予 15 级权限**
```
证据: user-interface vty 0 / user privilege level 15
影响: 绕过 AAA 授权，登录即最高权限
修复: 删除该行，让权限由 AAA 用户级别决定
```

### 🟠 P1 级（中高危，应尽快修复）

**5. TLS 仅支持 1.0/1.1，加密套件过时**
```
证据: version tls1.0 tls1.1 / ciphersuite rsa_aes_128_cbc_sha
影响: 中间人攻击、无前向保密、合规不达标
修复: 升级 TLS1.2/1.3 + ECDHE + GCM 套件
```

**6. SNMP v2c + community 明文 + 全 MIB 视图**
```
证据: sys-info version v2c / mib-view iso include iso
影响: 抓包获取 community → 读取完整配置和流量数据
修复: 升级 SNMPv3（认证+加密）；MIB 视图最小化
```

**7. IPsec 未实际部署，业务数据明文**
```
证据: 有 ike proposal default，但无 ipsec policy / ike peer 引用
影响: 租用线路上的数据可被窃听
修复: 评估是否需要加密；至少加密宁都 DDN 这类租用链路
```

**8. 无任何数据包过滤**
```
证据: 无 traffic-filter / 无防火墙安全策略；所有 ACL 只用于路由过滤
影响: 只要路由可达，任意流量可通；无内网横向隔离
修复: 在边界和关键网段间部署 ACL；启用安全策略
```

### 🟡 P2 级（中危，计划修复）

**9. VRRP 无上行链路跟踪**
```
影响: 上行断但下行正常时，流量被"黑洞"
修复: vrrp vrid 10 track interface G0/0/10 reduced 30
```

**10. 无日志外发（syslog）**
```
证据: 有 secelog 但无 info-center loghost 配置
影响: 设备重启/被篡改后日志丢失；无集中审计
修复: info-center loghost 173.20.1.178
```

**11. NTP 单点且无认证**
```
影响: 时间被篡改可破坏日志取证链和证书验证
修复: 配置 2~3 个 NTP 源；启用 ntp-service authentication
```

**12. 配置残留与信息泄露**
```
证据: dhcp enable 但无地址池
      G0/0/1 description 与实际使用口不符
      snmp contact 含手机号 13986101665
      engineid 暴露 MAC 地址
修复: 关闭无用服务；清理 description；联系信息脱敏
```

**13. 🔴 控制平面：OSPF 和 BGP 都没有配置认证**（审阅后补充，级别 P1）
```
证据: ospf 1 下无 authentication-mode
      bgp 2014 下无 peer X.X.X.X password
影响: 任何人接入 10.10.1.52/30 网段就能与 r1 建立 OSPF 邻居并注入路由，
      把全网流量引到自己机器上 —— 这条路径不需要任何账号密码
      同理，伪造 BGP 邻居可发起路由劫持
修复: ospf 1 / area 0 / authentication-mode hmac-sha256 1 cipher <密码>
      bgp 2014 / peer 10.10.30.54 password cipher <密码>
      bgp 2014 / peer 192.80.1.1 password cipher <密码>
```

为什么容易被忽略：大家只盯着 SSH、密码这些"管理平面"的东西，
但路由协议是设备之间自动协商的，**攻击面在另一层**。
三个平面都要看，才能不漏。

**14. 🆕 弱口令被明文记在导出的会话日志里**（P0，双机都有）
```
证据: A 日志末尾  <xingguo_r1>Admin@123 → Error: Unrecognized command
      B 日志末尾  <xingguo_r2>Admin@123 → Error: Unrecognized command
影响: ① 口令 Admin@123 是弱口令，且两台设备很可能用的是同一个
      ② 它被完整记录在导出的 .log 文件里，随配置文件一起流转
      ——拿到日志 = 拿到口令，连破解都不用
      ③ 更糟的是：这行出现在"用户视图提示符"后面，说明操作员是
         在已经登录的状态下又敲了一遍口令，等于主动把口令打进了屏幕记录
修复: 立即改口令；禁止在会话中明文输入口令；
      导出的日志按敏感级别管理，不得随意外发
```
> 💡 **这件事的方法论价值**：很多人做安全审计只看 `display current-configuration`，
> 但**操作过程本身也是证据**。会话日志、截图、录屏、聊天记录里的命令行，
> 往往比配置文件泄露得更多。审计时把"配置 + 操作记录"一起看。

**15. 🆕 VRRP 无认证 + 双机配置不对称**（P1）
```
证据: 两台都没有 vrrp vrid X authentication-mode
      r2 缺 ACL 2004/2005、缺 peer 192.80.106.2、缺 priority
      NTP: r1→192.20.27.30，r2→192.20.28.30（不同源）
影响: ① VRRP 报文无认证 → 接入 LAN 的机器可伪造高优先级通告抢占网关，
         把全网流量引到自己身上做中间人（不需要任何账号密码）
      ② 配置不对称导致"看起来有冗余，实际没有"——
         r1 整机宕机时宁都方向业务直接中断
      ③ 两台时钟不同源，跨设备日志无法精确对齐，影响事后取证
修复: vrrp vrid 10 authentication-mode md5 <密码>（两台一致）
      补 r2 的宁都方向链路，或明确接受该业务无冗余
      两台配置相同的 2~3 个 NTP 源 + 启用 NTP 认证
```

**16. 🆕 设备时钟异常，NTP 实际可能未生效**（P2）
```
证据: r2 登录后回显的日志时间戳是 "Sep 10 2019 01:13:48+08:00"
      而配置导出时间是 2025/8/22 —— 差了将近 6 年
影响: ① 日志时间戳不可信 → 事后取证、故障时间线还原全部失效
      ② 证书校验、日志关联、计费/审计类功能会出错
      （注：这条日志是设备缓存的"上次登录"记录，也可能是设备自 2019 年
       以来长期未重启；两种情况都值得实地核实时钟）
修复: 登录后先 display clock 和 display ntp-service status 确认；
      修好 NTP 后检查日志时间戳是否恢复
```

### 修复优先级建议

```
立即（本周）：1, 2, 3, 4, 14     ← 这些都是"拿密码就能控网"级别
短期（本月）：5, 6, 8, 13, 15    ← 需要变更窗口；13/15 涉及邻居与网关重建，要挑窗口
中期（季度）：7, 9, 10, 11, 12, 16 ← 需要方案设计和测试
```

> **双机视角带来的最大变化**：第 14 项说明**口令问题不是单台的，是整站的**；
> 第 15 项说明**冗余是有边界的**。这两条在只看 r1 时都看不出来。
> **审计一个站点，永远要看成对的设备。**

> **变更风险提示**：第 13 项（路由协议认证）配置时会**导致邻居重建、业务瞬断**，
> 必须在变更窗口操作，且建议先在一侧配好再配另一侧，并提前确认密码一致。
> 这类"看起来只是加一行密码"的操作，在生产网里是高危变更。

---

## 命令速查表

### 查看类（排障用）

```huawei
display current-configuration                  # 查看当前配置（= dis cur）
display ip interface brief                     # 所有接口 IP 概览
display ip routing-table                       # 查看 IP 路由表
display ip routing-table 173.20.1.50           # 查某个目的 IP 走哪条路
display bgp peer                               # BGP 邻居状态（重点看 State）
display bgp routing-table                      # BGP 路由表
display bgp routing-table 173.20.1.0           # 查某条 BGP 路由详情和属性
display ospf peer                              # OSPF 邻居状态
display ospf routing                           # OSPF 学到的路由
display vrrp                                   # VRRP 状态（谁是 Master）
display vrrp interface GigabitEthernet0/0/2    # 指定接口的 VRRP
display acl all                                # 所有 ACL
display interface GigabitEthernet0/0/10        # 接口详细信息（看是否 up、有无错包）
display logbuffer                              # 查看日志缓冲区
display users                                  # 谁在登录
display ssh server status                      # SSH 服务状态
display cpu-usage / display memory-usage       # CPU / 内存
```

### 诊断类

```huawei
ping 173.20.1.50                               # 连通性
ping -a 10.10.30.53 173.20.1.50                # 指定源地址 ping（测回程）
tracert 173.20.1.50                            # 路径追踪
display arp | include 192.20.27.20             # 查 ARP（看虚拟 MAC 是谁响应）
```

### 配置类（对照本配置）

```huawei
# 接口
interface GigabitEthernet0/0/2
 undo portswitch
 ip address 192.20.27.18 255.255.255.0
 description to LAN A
 vrrp vrid 10 virtual-ip 192.20.27.20
 vrrp vrid 10 priority 120
 vrrp vrid 10 track interface GigabitEthernet0/0/10 reduced 30   ← 建议补充

# ACL
acl 2002
 rule 5 permit source 192.20.27.0 0.0.0.255
 rule 10 permit source 192.20.28.0 0.0.0.255

# OSPF
ospf 1 router-id 10.10.30.53
 area 0
  network 10.10.1.53 0.0.0.0
  network 10.10.30.53 0.0.0.0

# BGP
bgp 2014
 router-id 10.10.30.53
 timer keepalive 5 hold 15
 peer 10.10.30.54 as-number 2014
 peer 10.10.30.54 connect-interface LoopBack0
 ipv4-family unicast
  network 192.20.27.0
  peer 10.10.30.54 next-hop-local
  peer 192.80.1.1 filter-policy 2003 import
  peer 192.80.1.1 filter-policy 2002 export
  peer 192.80.1.1 route-policy lp01 import

# 路由策略
route-policy lp01 permit node 10
 if-match acl 2003
 apply local-preference 400
route-policy lp01 permit node 20
```

### 安全加固类（建议补充）

```huawei
# 1. 关闭 Telnet 和 HTTP
undo telnet server enable
undo http server enable
# 只保留
stelnet server enable
http secure-server enable

# 2. 限制登录源
acl 2000
 rule 5 permit source 173.20.1.178 0
 rule 100 deny source any
user-interface vty 0 4
 acl 2000 inbound
 user privilege level 1              # 登录给低权限，靠 AAA 用户级别授权
 idle-timeout 10 0                   # 10 分钟无操作自动断开

# 3. 升级 TLS
ssl policy default_policy type server
 version tls1.2 tls1.3

# 4. 升级 SNMPv3
snmp-agent sys-info version v3
snmp-agent group v3 netadmin privacy read-view iso
snmp-agent usm-user v3 monitor group netadmin
snmp-agent usm-user v3 monitor authentication-mode sha2-256 <密码>
snmp-agent usm-user v3 monitor privacy-mode aes256 <密码>

# 5. 日志外发
info-center enable
info-center loghost 173.20.1.178
info-center source default channel 2 log level warning

# 6. 清理无用服务
undo dhcp enable

# 7. Trap 源用 Loopback
snmp-agent trap source LoopBack0
```

---

## 自测题（带答案）

先自己想，再看答案。

### 基础题

**Q1. `192.80.106.1/30` 这个网段有几个可用 IP？对端地址是多少？**

<details>
<summary>答案</summary>

**2 个可用 IP**：192.80.106.1（本端）和 192.80.106.2（对端）。

/30 = 255.255.255.252，总共 4 个地址：
- .0 网段地址（不可用）
- .1 本端
- .2 对端（配置里 BGP peer 192.80.106.2 证实了这一点）
- .3 广播地址（不可用）
</details>

**Q2. `rule 5 permit source 192.20.27.0 0.0.0.255` 中的 `0.0.0.255` 是子网掩码吗？它表示什么范围？**

<details>
<summary>答案</summary>

**不是，是通配符掩码（反掩码）**，逻辑与子网掩码相反：0 = 必须匹配，1 = 不在乎。

`0.0.0.255` = 前 24 位必须等于 192.20.27，后 8 位任意
= 匹配 `192.20.27.0` ~ `192.20.27.255`，即整个 `192.20.27.0/24`。

换算公式：`通配符 = 255.255.255.255 - 子网掩码`
</details>

**Q3. PC 的网关配的是 192.20.27.20，但配置里没有任何接口的 IP 是 .20。为什么能通？**

<details>
<summary>答案</summary>

因为 `.20` 是 **VRRP 虚拟 IP**：

```
vrrp vrid 10 virtual-ip 192.20.27.20
```

r1（.18，priority 120）和 r2（推测 .19，priority 100）组成一个虚拟路由器，共同"持有" `.20` 这个 IP。优先级高的 r1 是 Master，实际响应 ARP 并转发流量。

r1 挂了，r2 自动接管 `.20`，PC 完全无感知（PC 的网关配置从不需要改）。
</details>

### 进阶题

**Q4. ACL 2002 允许 192.20.27.0/24 通过。这是否意味着 192.20.27.100 的 PC 能访问外网？**

<details>
<summary>答案</summary>

**不能这么理解。ACL 2002 在这里对数据包转发零影响。**

ACL 2002 是被 `peer 192.80.1.1 filter-policy 2002 export` 引用的，所以它只在 **BGP 通告路由时**起作用，决定"哪些网段会被通告给上级"。

要过滤数据包，必须：
1. 用 `traffic-filter inbound acl xxxx` 应用到接口上，或
2. 配置防火墙安全策略

**这份配置里没有任何数据包过滤规则** —— 只要路由可达，任何流量都能过。
</details>

**Q5. 为什么 iBGP 用 Loopback 建邻，而不是用物理接口地址？**

<details>
<summary>答案</summary>

**通用理由是"让 BGP 会话不依赖单条物理链路"。**

如果用物理接口 `10.10.1.53` 建邻：那条链路一断，BGP 邻居立刻 down，即使两台路由器之间还有别的路能通。

用 Loopback `10.10.30.53` 建邻：只要 r1 和 r2 之间**还存在任意一条可达路径**，BGP 会话就存活。

代价是必须保证 Loopback 之间路由可达 —— 这就是 OSPF 的作用：
```
ospf 1
 network 10.10.1.53 0.0.0.0     # 互联链路
 network 10.10.30.53 0.0.0.0    # Loopback
```

> ⚠️ **但在这个加分题上，要看到这份配置并没有真正兑现这个好处**
>
> OSPF 只宣告了 `10.10.1.52/30` 这**一条**互联链路。也就是说，r1 到 r2 的 Loopback
> （10.10.30.54）**只有 G0/0/4 这一条路**：
>
> ```
> G0/0/4 断 → OSPF 邻居 down → 到 10.10.30.54 的路由消失 → iBGP 照样 down
> ```
>
> **所以在这里，Loopback 建邻换来的不是"抗故障"，而是另外两个好处：**
> 1. **配置解耦**：互联网段地址改了，BGP peer 地址不用动
> 2. **Router-ID 稳定**：Loopback 不因接口 down 而消失
>
> 想让它真正抗链路故障，需要**至少两条物理独立的路径都跑 OSPF**（比如再加一条 r1-r2 备份互联）。
>
> **这题的教训**：看到一个"最佳实践"的配置片段，要追问一句——
> **让它发挥作用的前提条件，在这个网络里满足了吗？**
> 抄对命令不等于达到目的。
</details>

**Q6. `peer 10.10.30.54 next-hop-local` 有什么用？不配会怎样？**

<details>
<summary>答案</summary>

**作用**：向 iBGP 邻居通告路由时，把下一跳改成自己的地址。

**不配的后果**：
```
r1 从 eBGP 邻居 192.80.1.1 学到 173.20.1.0/24，下一跳 = 192.80.1.1
r1 通告给 r2 时，下一跳保持 192.80.1.1 不变

r2 查路由表：192.80.1.0/24 怎么走？没有！（那是 r1 的直连网段）
→ 下一跳不可达 → 路由不装表 → r2 无法使用这条路
→ 主用链路故障时无法切换到 r2
```

**为什么 eBGP 不需要配？** 因为 eBGP 通告时默认就会把下一跳改成自己，只有 iBGP 默认保持不变（BGP 设计如此）。
</details>

**Q7. Local_Preference 设成 400 是什么意思？为什么是 400 而不是 4 或 4000？**

<details>
<summary>答案</summary>

**Local_Preference（本地优先级）**是 BGP 选路的**第一顺位属性**（华为中 Weight 之后），**值越大越优先，默认 100**。

设成 400 表示：这条路由在 AS 2014 内部享有极高优先级，r1 会优先用它，而不是其他路径（比如从 iBGP 邻居 r2 学来的、lp 更低的路）。

**为什么是 400 而不是 4 或 4000？**
- 取值本身没硬性规定，只要在合理范围（0 ~ 4294967295）内、且**高于其他备选路径的 lp 值**即可
- 用 400 说明配置者预留了空间：默认 100，主路径 400，还可以设 200、300 表示次优先
- 关键是**相对大小**，不是绝对值
- 有些团队会规范化：优先路径 200、次选 150、默认 100 —— 只要团队内部一致即可

✅ **实测补充（r2 配置到手后）**：r2 上配的正是 **300**，形成 `400 > 300 > 100` 的三级体系。
而且两台的 route-policy **名字、node 编号、if-match 用的 ACL 全部相同，只有 `apply local-preference`
那一行不同**——这是一套成对设计的策略。详见 [10.6](#106-路由策略对照400-vs-300)。
</details>

**Q8. 为什么向宁都（AS 3002）只通告 LAN A（192.20.27.0/24），不通告 LAN B？**

<details>
<summary>答案</summary>

因为那是 **2M 的 DDN 专线**（`description To_NingDu-DDN-2M`），带宽极小。

这是**分级降级（graceful degradation）**设计：
- 备份链路带宽有限，只承载最关键的网段（LAN A）
- 如果两个网段都走 2M，链路会被撑满，导致关键业务（LAN A）也卡死
- 宁可让 LAN B 完全断掉，也要保住 LAN A

对比主用链路（192.80.1.0/24 以太网，带宽充裕）：通告 LAN A + LAN B 两个网段（ACL 2002）。

**核心思想：备份不是"全都走"，而是"保最重要的"。**
</details>

### 安全题

**Q9. 找出这份配置中最严重的一个安全问题，并说明攻击链。**

<details>
<summary>答案</summary>

**最严重的是：15 级账号密码泄露 + Telnet 明文 + 无登录源限制，三者构成完整攻击链。**

完整攻击链：
```
步骤 1: 攻击者拿到这份配置文件（或内网任意一台 PC 被入侵）
        → 从文件末尾的 Admin@123 得到 15 级账号密码

步骤 2: 全网任意位置都能 SSH/Telnet 到路由器（VTY 无 ACL 限制）
        → ssh admin@192.20.27.18

步骤 3: 用 Admin@123 登录，获得 level 15 最高权限

步骤 4: 可以做任何事：
        - 修改路由，把全网流量劫持到攻击者的机器（中间人攻击）
        - 删除 BGP 过滤策略，让内部拓扑暴露
        - 添加后门账号
        - 清空日志
        - download 完整配置，得到所有网段和拓扑
```

即使没有泄露的密码，`Admin@123` 这种密码也能在几分钟内被暴力破解（在几乎所有密码字典的前 1000 条）。

**修复**：
1. 立即改强密码（16 位随机）
2. `undo telnet server enable`，只用 SSH
3. VTY 配置 `acl 2000 inbound` 限制登录源
4. 删除 `user privilege level 15`，让 AAA 决定权限
</details>

**Q10. 配置里有 `ike proposal default`（AES-256 + DH group14 + SHA2-256），参数看起来很强。是不是说明数据已经加密了？**

<details>
<summary>答案</summary>

**不是。IPsec 根本没有部署。**

判断方法：整个配置文件里**没有任何 `ipsec policy`、`ipsec profile` 或 `ike peer` 配置**，也没有任何接口引用 `ipsec policy`。

`ike proposal default` 只是**设备出厂自带的默认提议模板**，它本身不产生任何加密行为。IPsec 要生效至少需要：
```
ike proposal X
ike peer X
  pre-shared-key xxx
  remote-address x.x.x.x
ipsec proposal X
ipsec policy X 1 isakmp
  security acl 3xxx
  ike-peer X
  proposal X
interface GigabitEthernet0/0/11
  ipsec policy X          ← 必须应用到接口才生效
```

**结论：所有跨站点的业务数据都是明文传输的。** 尤其宁都那条 DDN 是租用运营商线路，物理上不可控，存在被窃听的风险。

**这个题的教训**：安全配置要验证"是否真的生效"，而不是"配置文件里有没有这段"。
</details>

**Q11. 为什么说"没有日志外发"是安全问题？**

<details>
<summary>答案</summary>

因为**日志是事后取证的唯一依据**，而设备本地日志缓冲区非常脆弱：

```
场景：攻击者入侵了路由器
  1. 登录、修改配置、劫持流量
  2. 执行 reset logbuffer（清空日志）
  3. 重启设备
  → 本地日志全部消失
  → 没有任何证据留下
  → 无法还原攻击时间、来源、做了什么
  → 事件调查完全失败
```

如果有日志外发（`info-center loghost`），日志实时写到远端 syslog 服务器，攻击者改不了（除非连 syslog 服务器也一起拿下）。

**而且这份配置连 NTP 都只有一个源且无认证** —— 时间可以不准，日志的时间戳就不可信，跨设备关联就失效。

**完整的安全日志体系需要**：日志外发 + 时间同步 + 集中存储 + 定期审计。这份配置三样里只做到了一半（NTP 有，但单点无认证）。
</details>

**Q12. 为什么说这份配置"重连通、轻安全"？举三个证据。**

<details>
<summary>答案</summary>

**网络设计层面做得很好（重连通）：**
- 双机 VRRP + 双上行链路，消除单点故障
- BGP 进出口严格过滤（filter-policy 2002~2005）
- Local_Preference 显式控制路径
- BGP timer 压到 5/15，快速收敛
- 地址规划有规律（r1=.53, r2=.54）

**安全层面明显滞后（轻安全），三个证据：**

1. **管理面完全裸奔**
   - 15 级账号走 Telnet/HTTP 明文协议
   - 弱密码 `Admin@123`
   - VTY 无登录源限制
   - 用 `display users` 都看不出异常（无登录告警）

2. **数据面无加密、无过滤**
   - IPsec 未部署（有模板无策略），业务数据明文
   - 零数据包过滤规则，所有 ACL 只用于筛路由
   - 信任模型是"路由可达即信任"

3. **监控审计能力薄弱**
   - SNMP v2c 明文 + 全 MIB 视图暴露
   - 无日志外发
   - TLS 1.0/1.1 已废弃
   - NTP 单点无认证

**根本原因**：这是一个"专网"，设计者默认物理隔离 = 安全。但专网也会通过租用线路、运维终端、下级单位接入点被渗透。**纵深防御（Defense in Depth）的思想缺失。**
</details>

### 双机专项题（第十章后新增）

**Q13. 站点有两台路由器，是不是就意味着所有业务都有冗余了？**

<details>
<summary>答案</summary>

**不是。冗余是按链路、按业务逐条算的，不是按设备台数算的。**

这个站点的实际情况：

| 业务/链路 | 是否有冗余 | 依据 |
|---|---|---|
| 南昌方向出网 | ✅ 有 | r1 走 192.80.1.1，r2 走 192.80.9.1，两条独立上行 |
| 局域网网关 | ✅ 有 | VRRP 双机，r1(prio 120) / r2(默认 100) |
| **宁都 2M 方向** | 🔴 **没有** | 只有 r1 配了 G0/0/11 和 peer 192.80.106.2，**r2 上完全没有** |
| NTP 时间源 | 🔴 没有 | 各指一台，且不是同一台；任一挂了对应设备时钟开始漂移 |

**所以：r1 整机宕机 = 宁都方向业务彻底中断**，双机冗余覆盖不到。

这类问题最危险的地方在于——**它不会报错，不会告警，平时完全看不出来**，
只有在主设备真的倒下的那一刻才暴露。所以审计时必须成对看配置。
</details>

**Q14. 会话日志末尾出现了 `<xingguo_r1>Admin@123` 这行，你能读出几条信息？**

<details>
<summary>答案</summary>

至少四条：

1. **口令是 `Admin@123`** —— 弱口令（厂商默认用户名格式 + 简单数字后缀）
2. **它是被当成命令敲进去的** —— 后面紧跟 `Error: Unrecognized command found at '^' position.`
   说明操作员在**已经登录**的状态下，又在用户视图敲了一遍口令
3. **它被完整记录并随配置一起导出了** —— 拿日志 = 拿口令，连破解都不用
4. **r2 的日志末尾有一模一样的一行** —— 两台很可能是**同一个口令**，攻破一台 = 攻破两台

还有一条延伸信息：敲口令的地方是**用户视图**（提示符是 `<>` 不是 `[]`），
说明操作员的习惯是"登录后再敲一次口令"——这种习惯在有屏幕录制、堡垒机审计、
或者像这次一样导出日志的环境里，等于**主动把口令写进审计记录**。

**正确做法**：口令只在认证提示（`Password:`）出现时输入，那时终端不回显、
也不会被当成命令行记录。
</details>

**Q15. 两台设备的 `route-policy lp01` 除了 400 和 300 之外完全一致，为什么这样设计？如果两台配置得完全一样（都是 400）会怎样？**

<details>
<summary>答案</summary>

**为什么这样设计**：Local_Preference 是**在 AS 内部传递**的属性。
两台用同一套策略（同名、同 node、同 ACL），只把 `apply local-preference` 设成不同的值，
就能让两台设备**独立算出同一个结论**，无需任何额外协商：

- r1 上看：自己打 400，从 iBGP 收到 r2 的 300 → 选 400（走自己上行）
- r2 上看：自己打 300，从 iBGP 收到 r1 的 400 → 选 400（绕道 r1）
- 结果：**两台都认为该走 r1**，选路一致 ✅

**如果两台都配 400 会怎样**：

- r1 上：自己 400 vs 从 r2 收到的 400 → **lp 打平**，进入下一条选路规则
- 下一条是 AS_PATH（长度相同）→ 再下一条 Origin（相同）→ 再下一条 MED → 最后比 EBGP 优于 IBGP
- 最终大概率**各自走自己的上行**（EBGP 优于 IBGP），结果就是"各走各的"
- 而 r2 上：自己 400 vs 从 r1 收到 400 → 同样打平 → 同样走自己的上行

**后果**：主备关系消失，变成"负载分担"。
这可能不是坏事（带宽利用率更高），但**它不再是设计者想要的可预测主备**——
出故障时你没法准确预判流量会怎么走，而且 173 网段的流量会从两个出口出去，
如果上级有基于源地址的策略或状态化设备（防火墙、NAT），**可能出现来回路径不一致导致丢包**。

**结论**：`400 / 300` 这对数字的价值不在于具体数值，而在于**制造了一个明确的大小关系**。
把它改成 `400 / 400`，等于把这个关系抹掉了。
</details>

---

## 十、双机对照：r1 与 r2 的完整对比

> 数据来源：
> - r1：`兴国站自控A路由器_2025-08-22_11_49_49.log`（导出时间 2025/8/22 11:50:13）
> - r2：`兴国站自控B路由器_2025-08-22_11_22_25.log`（导出时间 2025/8/22 11:22:44）
>
> 两台都是 V200R009C00SPC600，**同一版本、同一批设备**（MAC 连号）。

### 10.1 为什么要看第二台

单看一台设备的配置，你永远只能看到**一半的真相**：

| 只看 r1 时 | 拿到 r2 后 |
|---|---|
| "r2 的 LAN 地址大概是 .19 吧" | ✅ 确认 192.20.27.19 / 192.20.28.19 |
| "r2 的 Local_Pref 可能是 200" | ❌ **实际是 300**，纠正了一处错误推测 |
| "宁都链路也许是双机共享的" | ❌ **只有 r1 有**，r2 完全没有 → 单点 |
| "两台 NTP 应该指向同一台服务器" | ❌ **不是**，r1→.27.30，r2→.28.30 |
| "r2 大概是 Backup" | ✅ 确认，但方式是"不配 priority"用默认 100 |

**排障箴言：成对设备永远要成对看。** 双机配置不一致是生产环境里最隐蔽的故障源之一——
它不会报错，不会告警，只在主设备倒下的那一刻才暴露。

---

### 10.2 基本信息对照

| 项目 | xingguo_r1 | xingguo_r2 | 评价 |
|---|---|---|---|
| sysname | xingguo_r1 | xingguo_r2 | ✅ 命名规范一致 |
| VRP 版本 | V200R009C00SPC600 | V200R009C00SPC600 | ✅ **必须同版本** |
| Router-ID | 10.10.30.53 | 10.10.30.54 | ✅ 唯一且不冲突 |
| Loopback0 | 10.10.30.53/32 | 10.10.30.54/32 | ✅ |
| MAC（从 engineid 推） | 84:46:FE:3D:**54:53** | 84:46:FE:3D:**56:15** | 同批次采购 |
| engineid | ...3D5453 | ...3D5615 | 同前缀 800007DB03 |
| 本地 AS | 2014 | 2014 | ✅ iBGP 同 AS |
| 时钟时区 | `clock timezone EST add 08:00:00` | 同 | ⚠️ 名为 EST 实为东八区，命名误导 |

> ⚠️ **`clock timezone EST add 08:00:00` 是个典型的历史遗留坑**：
> 配置者随手用了模板里的名字 `EST`（美国东部时区），但偏移量填的是 `+08:00`（中国标准时间）。
> 结果是**时区名字是错的，时间是对的**。功能上不影响，但读配置的人会被误导，
> 而且跨设备、跨系统对日志时容易算错。规范写法应该是 `clock timezone CST add 08:00:00`。

---

### 10.3 接口对照

| 接口 | r1 | r2 | 说明 |
|---|---|---|---|
| G0/0/0 | 未配置 | 未配置 | 一致 |
| G0/0/1 | description `to nanchang zhu`，无 IP | 完全未配置 | ⚠️ r1 有残留描述 |
| **G0/0/2** | 192.20.27.18/24，VRRP vrid 10 prio **120** | 192.20.27.19/24，VRRP vrid 10 **无 priority** | ✅ r1 Master |
| **G0/0/3** | 192.20.28.18/24，VRRP vrid 11 prio **120** | 192.20.28.19/24，VRRP vrid 11 **无 priority** | ✅ r1 Master |
| **G0/0/4** | 10.10.1.53/30，desc `Connect to xingguo_r2` | 10.10.1.54/30，desc `Connect to xingguo_r1` | ✅ 互联，描述互为对端 |
| G0/0/9 | 无 IP（HTTP 管理口） | 无 IP（HTTP 管理口） | 一致，等于关闭 |
| **G0/0/10** | 192.80.1.54/24，desc `to nanchang zhu` | 192.80.9.54/24，desc `to nanchang **bei**` | 🔑 **两条不同的上行** |
| **G0/0/11** | 192.80.106.1/30，desc `To_NingDu-DDN-2M` | **完全未配置** | 🔴 **r2 没有这条链路** |
| Cellular0/0/0~1 | 未配置 | 未配置 | 一致（有硬件无配置） |

**最关键的一行是 G0/0/10**：两台的 description 一个是 `to nanchang zhu`，一个是 `to nanchang bei`，
IP 网段也不同（192.80.1.0/24 vs 192.80.9.0/24）。
**这不是"主链路 + 备链路"，而是"两个各自独立的出口"**——两台路由器各走各的上行，
再通过 iBGP + Local_Preference 在内部择优。这个理解上的修正，改变了整个主备模型的判断。

---

### 10.4 BGP 邻居对照

| | r1 | r2 |
|---|---|---|
| router-id | 10.10.30.53 | 10.10.30.54 |
| timer | keepalive 5 hold 15 | keepalive 5 hold 15 ✅ 一致 |
| **iBGP peer** | 10.10.30.54（connect-interface LoopBack0） | 10.10.30.53（同） |
| **eBGP peer（南昌）** | **192.80.1.1** AS 1001 | **192.80.9.1** AS 1001 |
| **eBGP peer（宁都）** | **192.80.106.2** AS 3002 | ❌ **无** |
| peer 数量 | 3 | 2 |
| network 宣告 | 192.20.27.0、192.20.28.0 | 192.20.27.0、192.20.28.0 ✅ 一致 |
| next-hop-local | ✅ 对 iBGP peer 配了 | ✅ 同样配了 |
| route-update-interval | 5（三个 peer 都配） | 5（两个 peer 都配） |

**过滤策略对照**：

| 策略 | r1 | r2 |
|---|---|---|
| 对南昌 peer 的 export | `filter-policy 2002`（LAN A + LAN B） | `filter-policy 2002` ✅ 一致 |
| 对南昌 peer 的 import | `filter-policy 2003` + `route-policy lp01` | 同 ✅ 一致 |
| 对宁都 peer 的 export | `filter-policy 2004`（仅 LAN A） | ❌ 无（没有这个 peer） |
| 对宁都 peer 的 import | `filter-policy 2005`（仅 192.20.102.0/24） | ❌ 无 |

> **r1 只有 3 个 peer 却用了 4 个 ACL，r2 只有 2 个 peer 用 2 个 ACL**——
> ACL 数量差异完全由"有没有宁都邻居"决定，逻辑上是自洽的。
> 但这恰恰说明：**r2 在设计上就没打算承载宁都方向的业务**。

---

### 10.5 ACL 对照

| ACL | r1 | r2 | 用途 |
|---|---|---|---|
| 2002 | 192.20.27.0/24 + 192.20.28.0/24 | ✅ 完全相同 | 向南昌通告本地业务网段 |
| 2003 | 173.20.1.0/24 + 173.21.1.0/24 | ✅ 完全相同 | 从南昌只接收这两个网段 |
| 2004 | 192.20.27.0/24（仅 LAN A） | ❌ **不存在** | 向宁都只通告 LAN A |
| 2005 | 192.20.102.0/24 | ❌ **不存在** | 从宁都只接收该网段 |

**ACL 2002/2003 两台逐字相同**——这是好事，说明这两条是"标准模板"复制过去的，不容易出错。
真正的差异（2004/2005）来自业务不对称，不是配置失误。

---

### 10.6 路由策略对照：400 vs 300

```huawei
# r1
route-policy lp01 permit node 10
 if-match acl 2003
 apply local-preference 400
route-policy lp01 permit node 20

# r2
route-policy lp01 permit node 10
 if-match acl 2003
 apply local-preference 300      ← 唯一不同的数字
route-policy lp01 permit node 20
```

**除了 `400` 和 `300`，两台的 route-policy 完全一致**（连名字、node 编号、ACL 都一样）。

这一对数字撑起了整个选路体系：

```
                    AS 2014 内部（iBGP 传递 LP）
   ┌──────────────────────────────────────────────┐
   │                                              │
   │   r1 打出 400  ────────────►  r2 收到 400    │
   │   r2 打出 300  ────────────►  r1 收到 300    │
   │                                              │
   │   r1 视角：400(自己) > 300(经r2) → 走自己     │
   │   r2 视角：400(经r1) > 300(自己) → 走 r1     │
   │                                              │
   │   两台结论一致：流量走 r1 的上行 ✅           │
   └──────────────────────────────────────────────┘
```

**为什么这个设计是漂亮的**：

1. **无需协商**：LP 随 iBGP 更新自动传播，两台各自独立算出同一结论
2. **切换自动**：r1 上行断了 → r1 上只剩 300 → 自动走 r2；r2 上 400 消失 → 自动回到自己的 300
3. **调整简单**：想让 r2 变主，只要把 r2 的 `apply local-preference` 改成 500，**改一个数字**
4. **可预测**：出故障时你能准确说出流量会怎么走

> 🔑 **这是本文档里最值得学习的配置手法。**
> "同一套策略、两个不同的值"——比"两台设备各配各的"可靠得多，
> 因为它保证了**两台设备看到的优先级体系是同一个体系**。

---

### 10.7 VRRP 对照

| | r1 | r2 |
|---|---|---|
| vrid 10 虚拟 IP | 192.20.27.20 | 192.20.27.20 ✅ 一致 |
| vrid 11 虚拟 IP | 192.20.28.20 | 192.20.28.20 ✅ 一致 |
| vrid 10 priority | **120** | 未配置 → 默认 **100** |
| vrid 11 priority | **120** | 未配置 → 默认 **100** |
| 角色 | **Master**（两个组都是） | **Backup**（两个组都是） |
| track interface | ❌ 无 | ❌ 无 |
| authentication-mode | ❌ 无 | ❌ 无 |
| preempt | 未配置（默认开启） | 未配置（默认开启） |

✅ **结论：r1 是两个 VRRP 组的 Master，全部 LAN 流量经 r1 转发。这与原判断一致。**

⚠️ **两台都缺的三样东西**：

| 缺失项 | 后果 | 建议配置 |
|---|---|---|
| `track interface` | r1 上行断了，VRRP 不切换，流量绕道（轻则多一跳，重则黑洞） | `vrrp vrid 10 track interface G0/0/10 reduced 30` |
| `authentication-mode` | 任何人接入 LAN 可伪造 VRRP 通告抢占网关（无需账号密码） | `vrrp vrid 10 authentication-mode md5 <密码>` |
| BFD 联动 | 切换依赖 3 秒超时，无法做到亚秒级 | `vrrp vrid 10 track bfd-session ...` |

> **VRRP 无认证是很容易被漏掉的攻击面。**
> 大家记得给 OSPF/BGP 配认证（问题 13），却常常忘记 VRRP 也是设备间自动协商的协议，
> 而且它直接决定"谁是网关"——抢到网关 = 全网流量过我的手。

---

### 10.8 管理面与运维对照

| 项目 | r1 | r2 | 评价 |
|---|---|---|---|
| 本地账号 | admin(15) / jxtrq(3) | admin(15) / jxtrq(3) | ✅ 一致 |
| admin 服务类型 | telnet http | telnet http | 🔴 同样的错误复制了两份 |
| jxtrq 服务类型 | terminal ssh ftp | terminal ssh ftp | ⚠️ 同样含 FTP |
| 密码存储 | irreversible-cipher | irreversible-cipher | ✅ |
| stelnet server | enable | enable | ✅ |
| telnet server | 未显式启用 | 未显式启用 | （所以 admin 实际只能用 http） |
| HTTP 限制 | `permit interface G0/0/9`（无 IP = 关） | 同 | ✅ 一致，等于关闭 |
| VTY 0 权限 | level 15 | level 15 | 🔴 同样的问题 |
| VTY ACL | 无 | 无 | 🔴 同样的问题 |
| console 认证 | password（cipher） | password（cipher） | ✅ |
| **SNMP** | 同 r2 的配置结构 | 同 r1 | — |
| SNMP location | XingGuo-R1 | XingGuo-R2 | ✅ 区分开了 |
| SNMP contact | 13986101665 | **13986101665** | 🔴 同一个手机号，明文 |
| SNMP 版本 | v2c | v2c | 🔴 都是明文版 |
| SNMP Trap 目标 | 173.20.1.178:162 | 173.20.1.178:162 | ✅ 同一个网管 |
| SNMP Trap 源 | **G0/0/2**（物理口） | **G0/0/2**（物理口） | 🔴 同样的错误 |
| SNMP community | 密文 A | 密文 B | ⚠️ 密文不同，但**无法判断是否同一个口令**（密文含随机盐，相同口令也会得到不同密文） |
| **NTP 服务器** | **192.20.27.30** | **192.20.28.30** | 🔴 **不同源** |
| NTP 源接口 | LoopBack0 | LoopBack0 | ✅ |
| syslog 外发 | ❌ 无 | ❌ 无 | 🔴 同样缺失 |
| IPsec | ❌ 未部署 | ❌ 未部署 | 🔴 |

> **管理面的问题两台是一模一样的**——因为它们大概率出自同一个模板、同一次施工。
> 这句话两面看：好消息是**改一处就能改两处**（批量脚本）；
> 坏消息是**一个弱口令就能控两台**（问题 14 的 `Admin@123` 就是证据）。

---

### 10.9 差异汇总：哪些是真问题

把两台的差异分成三类，处理优先级完全不同：

**✅ 合理的差异（不用改）**

| 差异 | 为什么合理 |
|---|---|
| LAN 地址 .18 vs .19 | 同一网段不同主机位，必须不同 |
| Loopback / 互联地址 .53 vs .54 | 同上 |
| Router-ID 不同 | 必须唯一 |
| sysname / SNMP location 不同 | 便于区分设备 |
| engineid 不同 | 设备固有 |
| community 密文不同 | 密文含随机盐，不说明口令一定不同（**待实地确认**） |
| r2 无 ACL 2004/2005 | r2 本来就没有宁都 peer |

**🔴 有问题的差异（要改）**

| 差异 | 问题 | 建议 |
|---|---|---|
| r2 无 G0/0/11 宁都链路 | **宁都业务单点** | 补链路，或书面接受该业务无冗余 |
| NTP 源不同（.27.30 vs .28.30） | 时钟不同步 + 各自单点 | 两台配相同的 2~3 个 NTP 源 |
| r2 登录日志时间戳停留在 2019 | NTP 可能未生效 / 长期未重启 | 实地 `display clock` 核实 |

**⚠️ 两台共同缺失（不是差异，但要一起改）**

VRRP track / VRRP 认证 / 路由协议认证 / syslog 外发 / 弱口令 / Telnet / TLS1.0 / SNMPv3。
**这些在两台上是"一致地错"，所以批量改一次就都解决了。**

---

### 10.10 此前推测的核对结果

| # | 原文档的推测 | r2 实际情况 | 判定 |
|---|---|---|---|
| 1 | r2 的 LAN 地址是 .27.19 / .28.19 | 确实是 | ✅ 证实 |
| 2 | r2 用默认 priority 100 当 Backup | 确实没配 priority | ✅ 证实 |
| 3 | r2 的 Local_Pref 大概是 200 | **实际是 300** | ❌ **修正** |
| 4 | r2 可能有宁都方向的对称配置 | **完全没有** | ❌ **修正** |
| 5 | 两台 NTP 可能指向同一台服务器 | **不是，各指一台** | ❌ **修正** |
| 6 | r2 有同样的 `route-policy lp01` 结构 | 完全一致，只差一个数字 | ✅ 证实 |
| 7 | r2 的 router-id 是 10.10.30.54 | 确实是 | ✅ 证实 |
| 8 | 两台同属 AS 2014 做 iBGP | 确实是 | ✅ 证实 |

**8 条推测里 5 条对、3 条错——错的那 3 条恰好都是"看起来最合理"的。**
这就是为什么网络工程里"推测"必须标注、必须找机会验证：**合理的推测仍然有一半概率是错的。**

---

### 10.11 会话日志里的意外收获

两份日志的末尾都有这么一段：

```
<xingguo_r1>Admin@123
            ^
Error: Unrecognized command found at '^' position.
<xingguo_r1>
```

**r2 的日志末尾一字不差地复现了同样的场景。** 三个信息：

1. **口令是 `Admin@123`** —— 典型的弱口令（厂商默认格式 + 简单后缀）
2. **两台很可能是同一个口令** —— 这意味着**攻破一台 = 攻破两台**
3. **它被完整记录并随配置一起导出** —— 日志比配置文件泄露得更彻底

另外 r2 的日志开头还有一段：

```
Login authentication
Password:
<xingguo_r2>
Sep 10 2019 01:13:48+08:00 xingguo_r2 LINE/4/USERLOGIN:OID ... A user login.
 (UserIndex=0, UserName=Console, UserIP=Console0, UserChannel=CON0)
```

设备回显的上一条登录记录来自 **Console 口**（`UserChannel=CON0`，与 `user-interface con 0` 配了
password 认证相吻合），时间戳停在 **2019 年**——要么设备长期未重启、日志没清，
要么时钟确实有问题（见审计项 16，**需要实地 `display clock` 才能定论**）。

> 📌 **方法论**：`dis cur` 只能告诉你"配了什么"，
> **登录方式、操作习惯、时间戳、报错信息**这些"元数据"往往透露更多信息。
> 做安全审计时，把整个会话日志通读一遍，不要只 grep 配置段。

---

### 10.12 这次双机核对的三条收获

1. **推测必须验证**：8 条推测错 3 条，而且错的都是"最合理"的（LP=200、宁都对称、NTP 同源）
2. **冗余要按业务逐条算**：有两台路由器 ≠ 什么都有冗余。宁都链路就是 r1 独占的单点
3. **成对设备的配置要成对审**：不一致不会报错，只在主设备倒下那一刻才暴露

> **顺带一提**：同目录下还有第三台 `兴国站视频路由器_2025-08-22_11_10_48.log`
> （sysname `XingGuo-AR1200E`，VRP V200R010C10SPC700，vlan batch 1000）。
> 型号和版本都不同，**不在本次双机对照范围内**。
> 它的日志开头有口令过期提示和多次认证失败记录，值得单独开一篇做审计。

---

## 下一步学什么

按这个顺序走，能建立完整的网络知识体系：

| 阶段 | 内容 | 推荐理由 |
|---|---|---|
| 1 | **深入 IP 与子网划分** | 反复练习 CIDR 计算、VLSM 划分，直到不用计算器 |
| 2 | **抓包分析（Wireshark）** | 亲眼看到 ARP、TCP 三次握手、BGP 报文，理论立刻变实感 |
| 3 | **OSPF 深入** | LSA 类型、DR/BDR 选举、区域设计、Cost 计算 |
| 4 | **BGP 深入** | 13 条选路规则、路由反射器、联盟、团体属性 |
| 5 | **网络模拟器实操** | **eNSP**（华为官方免费）或 EVE-NG，把这份配置搭出来跑一遍 |
| 6 | **网络安全** | 设备加固基线、ACL 设计、IPsec/SSL VPN、AAA/RADIUS |
| 7 | **认证** | HCIA → HCIP → HCIP-Security（华为）或 CCNA → CCNP（思科） |

### 强烈建议：把这份配置在 eNSP 里搭出来

华为 eNSP 是**免费的官方模拟器**，可以：
1. 建两台路由器，把这份配置敲进去
2. `display bgp peer` 看邻居状态
3. 手动 `shutdown` G0/0/10，观察收敛过程
4. 抓包看 VRRP 通告、BGP Open/Update 报文
5. 试着加 `vrrp track`，看行为变化

**读十遍配置，不如亲手敲一遍、断一次链路。**

### 推荐的验证命令

搭好环境后依次执行，验证你真的理解了：

```huawei
display bgp peer                      # r1 三个邻居、r2 两个邻居，都应 Established
display bgp routing-table             # r1 上 173.20.1.0/24 的 Local-Pref 应为 400
display ospf peer brief               # 应有一个 Full 状态的邻居
display vrrp brief                    # r1 应显示 Master，r2 应显示 Backup
display ip routing-table protocol bgp # 只看 BGP 路由
display ip routing-table 173.20.1.50  # 看最终选了哪条路
```

**双机专项验证**（搭两台时必做）：

```huawei
# 在 r1 和 r2 上各执行一次，重点比对输出
display bgp routing-table 173.20.1.0      # r1 应显示 400，r2 应显示 300（或经 r1 学来的 400）
display vrrp                              # 确认 Master/Backup 与优先级
display ntp-service status                # 确认是否真的同步上了
display clock                             # 确认两台时间是否一致（审计项 16）
display snmp-agent target-host            # 确认 Trap 目标和参数

# 故障演练（学习用，生产环境勿动）
# 1. 在 r1 上 shutdown G0/0/10 → 观察 BGP 收敛（约 15 秒）和 VRRP 是否切换（不会切！）
# 2. 在 r1 上 shutdown G0/0/2  → 观察 VRRP 是否切到 r2（会切）
# 3. 补上 vrrp track 后重复第 1 步 → 观察行为差异
```

---

*文档基于 `xingguo_r1_config.txt` 与两份兴国站会话日志（A/B 路由器，2025-08-22）编写。*
*2026-09-10 更新：已用 r2 实际配置完成双机核对，修正 3 处错误推测，新增第十章与安全审计第 14/15/16 项。*
*剩余未确认项：宁都方向的实际可达性、BGP 真实选路结果、设备时钟异常原因——这些需要登录实设备才能确认。*
