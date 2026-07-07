# HTTP 协议详解

---

## 学习目标

- 掌握 HTTP 协议的工作原理和报文结构
- 理解 HTTP 请求方法、状态码、头部字段的含义
- 了解 HTTP 连接管理机制（短连接、长连接、多路复用）
- 掌握 HTTP 各版本的演进与区别
- 理解 HTTP 无状态特性的原因与解决方案

---

## 一、HTTP 协议概述

### 1.1 什么是 HTTP

HTTP（HyperText Transfer Protocol，超文本传输协议）是万维网的基础通信协议，用于客户端（浏览器）与服务器之间的数据传输。

```
核心特点：
- 基于请求/响应模型：客户端发请求，服务器返回响应
- 无状态协议：服务器不保留之前请求的信息
- 明文传输：数据不加密，可被中间人截获（HTTPS 解决此问题）
- 默认端口：80（HTTP）/ 443（HTTPS）
- 基于 TCP 协议之上
```

### 1.2 HTTP 通信模型

```
客户端 (浏览器)                              服务器 (Web Server)
    │                                            │
    │  ──── TCP 三次握手 (建立连接) ────────────>  │
    │  <────────────────────────────────────────  │
    │                                            │
    │  ──── HTTP 请求报文 (GET /index.html) ───>  │
    │                                            │
    │  <──── HTTP 响应报文 (200 OK + HTML) ─────  │
    │                                            │
    │  ──── TCP 四次挥手 (断开连接) ────────────>  │
    │  <────────────────────────────────────────  │
    │                                            │
    v                                            v
```

### 1.3 为什么 HTTP 是无状态的

```
设计原因：
1. 简单可靠 —— 服务器不需要维护客户端状态，逻辑更简单
2. 高性能   —— 不需要为每个用户分配内存存储状态
3. 易扩展   —— 任何一台服务器都能处理任何请求，便于负载均衡
```

**无状态不代表"无法识别用户"**，通过外挂机制实现状态保持：

| 机制 | 原理 |
|------|------|
| Cookie | 服务器在响应中设置 ID，浏览器下次请求自动带上 |
| Session | 服务器根据 Cookie 中的 ID 查找用户数据 |
| Token (JWT) | 用户信息加密编码在令牌里，每次请求带上，服务器解密识别 |

---

## 二、HTTP 请求报文

### 2.1 请求报文结构

```http
GET /index.html?name=tom&age=18 HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: session_id=abc123; user=admin

```

**报文由三部分组成**：

```
┌─────────────────────────────────────┐
│  请求行 (Request Line)               │  ← 第一行
├─────────────────────────────────────┤
│  请求头 (Request Headers)            │  ← 键值对，每行一个
├─────────────────────────────────────┤
│  空行 (CRLF)                        │  ← \r\n，分隔头部和体
├─────────────────────────────────────┤
│  请求体 (Body)                      │  ← GET 请求无体，POST 有
└─────────────────────────────────────┘
```

### 2.2 请求行详解

```
GET /index.html?name=tom&age=18 HTTP/1.1
│    │                    │          │
│    │                    │          └── 协议版本
│    │                    └── 查询参数（? 后面，& 分隔多个）
│    └── 路径（服务器上的资源位置）
└── 请求方法
```

### 2.3 常见请求头

| 请求头 | 说明 | 示例 |
|--------|------|------|
| Host | 请求的目标主机（必填） | `Host: www.example.com` |
| User-Agent | 客户端类型信息 | `Mozilla/5.0 (Windows NT 10.0)` |
| Accept | 客户端能接受的响应格式 | `text/html, application/json` |
| Accept-Language | 偏好的语言 | `zh-CN,zh;q=0.9,en;q=0.8` |
| Accept-Encoding | 支持的压缩方式 | `gzip, deflate, br` |
| Connection | 连接管理方式 | `keep-alive`（长连接） |
| Cookie | 携带的 Cookie 数据 | `session_id=abc123` |
| Content-Type | 请求体的数据格式 | `application/json`（POST 用） |
| Content-Length | 请求体的字节长度 | `1024`（POST 用） |
| Authorization | 认证凭证 | `Bearer eyJhbGciOi...` |
| Referer | 来源页面 URL | `https://www.example.com/home` |

### 2.4 URL 结构

```
https://www.example.com:443/path/to/page?id=1&name=tom#section
│       │                 │   │                  │         │
│       │                 │   │                  │         └── 锚点
│       │                 │   │                  └── 查询参数
│       │                 │   └── 路径
│       │                 └── 端口号
│       └── 主机名（域名）
└── 协议
```

---

## 三、HTTP 响应报文

### 3.1 响应报文结构

```http
HTTP/1.1 200 OK
Date: Sun, 06 Jul 2026 12:00:00 GMT
Server: Apache/2.4.41
Content-Type: text/html; charset=utf-8
Content-Length: 52
Set-Cookie: session_id=xyz789; Path=/
Connection: keep-alive

<html><body><h1>Hello World</h1></body></html>
```

### 3.2 状态行详解

```
HTTP/1.1 200 OK
│        │    │
│        │    └── 原因短语（Reason Phrase）
│        └── 状态码（Status Code）
└── 协议版本
```

### 3.3 常见响应头

| 响应头 | 说明 | 示例 |
|--------|------|------|
| Date | 服务器生成响应的时间 | `Sun, 06 Jul 2026 12:00:00 GMT` |
| Server | 服务器软件信息 | `Apache/2.4.41` / `Nginx/1.18` |
| Content-Type | 响应体的 MIME 类型和编码 | `text/html; charset=utf-8` |
| Content-Length | 响应体的字节长度 | `52` |
| Set-Cookie | 设置 Cookie（服务器→浏览器） | `session_id=xyz789; Path=/` |
| Location | 重定向的目标 URL | `https://www.example.com/new` |
| Cache-Control | 缓存策略 | `max-age=3600`（缓存1小时） |
| Last-Modified | 资源最后修改时间 | `Wed, 01 Jan 2025 00:00:00 GMT` |
| ETag | 资源的唯一标识（版本号） | `"abc123"` |

---

## 四、HTTP 请求方法

| 方法 | 用途 | 是否幂等 | 是否有请求体 |
|------|------|----------|-------------|
| GET | 获取资源 | 是 | 无 |
| POST | 提交数据 / 创建资源 | 否 | 有 |
| PUT | 更新资源（全量替换） | 是 | 有 |
| DELETE | 删除资源 | 是 | 无/有 |
| PATCH | 更新资源（部分修改） | 否 | 有 |
| HEAD | 只获取响应头（不获取体） | 是 | 无 |
| OPTIONS | 查询服务器支持的方法 | 是 | 无 |

**什么是幂等**：同一个请求发多次，服务器产生的效果和发一次相同。

```
GET /users/1    → 每次都返回用户1，结果一样     → 幂等
POST /users     → 每次都创建一个新用户，结果不同 → 非幂等
PUT /users/1    → 每次都覆盖更新用户1，结果一样 → 幂等
DELETE /users/1 → 每次都删除用户1，结果一样     → 幂等
```

---

## 五、HTTP 状态码

### 5.1 状态码分类

| 范围 | 类别 | 含义 |
|------|------|------|
| 1xx | 信息性 | 请求已接收，继续处理 |
| 2xx | 成功 | 请求成功接收并处理 |
| 3xx | 重定向 | 需要进一步操作才能完成请求 |
| 4xx | 客户端错误 | 请求有语法错误或无法完成 |
| 5xx | 服务端错误 | 服务器处理请求时出错 |

### 5.2 常见状态码详解

**2xx 成功**

| 状态码 | 含义 | 使用场景 |
|--------|------|---------|
| 200 OK | 请求成功 | GET 请求返回数据、POST 请求返回结果 |
| 201 Created | 已创建 | POST 创建资源成功 |
| 204 No Content | 无内容 | DELETE 删除成功，无需返回体 |

**3xx 重定向**

| 状态码 | 含义 | 使用场景 |
|--------|------|---------|
| 301 Moved Permanently | 永久重定向 | 网站换域名，旧域名指向新域名 |
| 302 Found | 临时重定向 | 临时跳转，如登录后跳转 |
| 304 Not Modified | 未修改 | 浏览器缓存命中，无需重新传输 |

**4xx 客户端错误**

| 状态码 | 含义 | 使用场景 |
|--------|------|---------|
| 400 Bad Request | 请求格式错误 | 参数缺失、格式不对 |
| 401 Unauthorized | 未认证 | 未登录或 Token 过期 |
| 403 Forbidden | 无权限 | 已登录但没有访问权限 |
| 404 Not Found | 资源不存在 | URL 拼写错误、资源被删除 |
| 405 Method Not Allowed | 方法不允许 | 用 GET 请求了一个只接受 POST 的接口 |

**5xx 服务端错误**

| 状态码 | 含义 | 使用场景 |
|--------|------|---------|
| 500 Internal Server Error | 服务器内部错误 | 程序 Bug、未捕获的异常 |
| 502 Bad Gateway | 网关错误 | 上游服务器无响应 |
| 503 Service Unavailable | 服务不可用 | 服务器过载或维护中 |

---

## 六、POST 请求体格式

### 6.1 常见 Content-Type

| Content-Type | 格式 | 说明 |
|-------------|------|------|
| application/x-www-form-urlencoded | `key1=value1&key2=value2` | 表单默认格式 |
| multipart/form-data | 每个字段用分隔符隔开 | 文件上传用 |
| application/json | `{"key": "value"}` | JSON 格式，API 常用 |
| text/plain | 纯文本 | 少用 |

### 6.2 POST 请求示例

```http
POST /api/login HTTP/1.1
Host: www.example.com
Content-Type: application/json
Content-Length: 50
Accept: application/json

{"username": "admin", "password": "123456"}
```

```
关键点：
- 请求行用 POST 方法
- Content-Type 告诉服务器请求体是什么格式
- Content-Length 告诉服务器请求体有多长
- 空行之后的内容就是请求体
```

---

## 七、HTTP 连接管理

### 7.1 短连接（HTTP/1.0）

```
每次请求都经历：
1. 建立 TCP 连接（三次握手）
2. 发送请求 + 接收响应
4. 关闭 TCP 连接（四次挥手）

缺点：每次请求都要重新建连，开销大
```

### 7.2 长连接（HTTP/1.1 默认）

```
一个 TCP 连接上可以发送多个请求：
1. 建立 TCP 连接
2. 请求1 → 响应1
3. 请求2 → 响应2
4. 请求3 → 响应3
5. ...（复用同一个连接）
6. 关闭 TCP 连接

通过 Connection: keep-alive 头部控制
```

### 7.3 管线化（Pipelining）

```
客户端可以连续发送多个请求，不等待响应：
请求1 → 请求2 → 请求3 → ... → 响应1 → 响应2 → 响应3

问题：响应必须按请求顺序返回（队头阻塞）
实际很少使用
```

### 7.4 多路复用（HTTP/2）

```
一个连接上可以并发多个请求和响应：
请求1 ─┐
请求2 ─┼──→ 一个TCP连接 ──→ 响应2
请求3 ─┘                  响应1
                          响应3

特点：
- 二进制分帧：数据分为小帧传输
- 不再按序返回：哪个先准备好就先发
- 头部压缩：HPACK 算法压缩重复的头部
- 服务器推送：主动推送资源给客户端
```

### 7.5 HTTP/3（QUIC）

```
基于 UDP 而非 TCP：
- 0-RTT 建立连接（更快）
- 解决了 TCP 的队头阻塞问题
- 连接迁移（切换网络不中断）
- 内置 TLS 1.3 加密
```

### 7.6 版本对比

| 特性 | HTTP/1.0 | HTTP/1.1 | HTTP/2 | HTTP/3 |
|------|----------|----------|--------|--------|
| 连接方式 | 短连接 | 长连接 | 多路复用 | 多路复用 |
| 传输层 | TCP | TCP | TCP | UDP (QUIC) |
| 头部压缩 | 无 | 无 | HPACK | QPACK |
| 服务器推送 | 不支持 | 不支持 | 支持 | 支持 |
| 队头阻塞 | 有 | 有 | 有（TCP层） | 无 |

---

## 八、HTTPS 与 HTTP 的区别

```
HTTPS = HTTP + SSL/TLS 加密层

HTTP:   客户端 ←──明文──→ 服务器
HTTPS:  客户端 ←──加密──→ 服务器
                 ↑
              SSL/TLS
```

### 8.1 HTTPS 工作流程

```
1. 客户端发起 HTTPS 请求
2. 服务器返回 SSL 证书（含公钥）
3. 客户端验证证书的合法性
4. 客户端生成随机密钥，用公钥加密后发送给服务器
5. 服务器用私钥解密，得到随机密钥
6. 双方用随机密钥进行对称加密通信
```

### 8.2 HTTP vs HTTPS

| 特性 | HTTP | HTTPS |
|------|------|-------|
| 端口 | 80 | 443 |
| 安全性 | 明文传输，易被窃听 | 加密传输 |
| 证书 | 不需要 | 需要 SSL 证书 |
| 速度 | 较快 | 略慢（加密开销） |
| SEO | 无优势 | 搜索引擎优先收录 |

---

## 九、HTTP 安全相关

### 9.1 常见 HTTP 攻击

| 攻击方式 | 原理 | 防护措施 |
|---------|------|---------|
| 中间人攻击 (MITM) | 截获并篡改 HTTP 通信 | 使用 HTTPS |
| HTTP 劫持 | 篡改响应内容注入广告 | HTTPS + HSTS |
| Session 劫持 | 窃取 Cookie 冒充用户 | HttpOnly + Secure 标记 |
| CSRF | 伪造用户请求执行操作 | Token 验证、Referer 检查 |
| HTTP 响应头注入 | 注入恶意头部信息 | 过滤用户输入 |

### 9.2 重要请求头的安全意义

**X-Forwarded-For**

```
X-Forwarded-For: 127.0.0.1
```

```
作用：标识客户端的真实 IP 地址
原理：当请求经过代理/负载均衡时，每一层代理会在该头部追加客户端 IP
格式：X-Forwarded-For: 客户端IP, 代理1IP, 代理2IP

示例流程：
客户端(192.168.1.100) → Nginx(10.0.0.1) → Apache(10.0.0.2) → Web应用
最终头部：X-Forwarded-For: 192.168.1.100, 10.0.0.1, 10.0.0.2
```

```
在 Web 攻击中的作用：

1. IP 伪造绕过
   - 攻击者发送：X-Forwarded-For: 127.0.0.1
   - 如果服务器信任该头部，会误认为请求来自本地
   - 绕过基于 IP 的访问控制（如只允许 localhost 访问的管理后台）

2. IP 限制绕过
   - 网站对同一 IP 做了频率限制或黑名单封禁
   - 攻击者伪造不同的 X-Forwarded-For 值绕过限制

3. 日志污染
   - 伪造 IP 导致服务器日志记录虚假来源，干扰安全审计

防护措施：
- 服务器不要直接信任 X-Forwarded-For 头部
- 从右向左解析，跳过已知代理 IP，取第一个可信 IP
- 在 Nginx 中配置：proxy_set_header X-Real-IP $remote_addr
```

**Referer**

```
Referer: https://www.example.com/home
```

```
作用：标识当前请求是从哪个页面跳转过来的
原理：浏览器自动在请求中附加来源页面的 URL（拼写错误是历史原因）

示例：
用户在 https://www.example.com/home 点击链接跳转到 /about
浏览器发送：Referer: https://www.example.com/home
```

```
在 Web 攻击中的作用：

1. CSRF 攻击绕过
   - 很多网站用 Referer 验证请求来源，判断是否为合法请求
   - 攻击者可以通过以下方式伪造或隐藏 Referer：
     a. 利用 <meta name="referrer" content="no-referrer"> 标签
     b. 利用 data: URL 或 javascript: URL 发起请求（部分浏览器不发送 Referer）
     c. HTTPS → HTTP 跳转时，浏览器不发送 Referer（协议降级）
     d. 自定义 Referer-Policy 响应头控制

2. 敏感信息泄露
   - URL 中可能包含敏感参数：
     https://example.com/transfer?token=abc123&to=hacker
   - Referer 被发送到第三方资源时，第三方可以看到完整 URL
   - 包含 token、用户名等敏感信息

3. 来源伪造
   - 攻击者构造页面让受害者点击，Referer 指向合法网站
   - 绕过简单的 Referer 来源检查

防护措施：
- 使用 CSRF Token 而非仅依赖 Referer 验证
- 设置 Referrer-Policy: strict-origin-when-cross-origin（只发送源信息，不发送完整路径）
- 敏感操作不要放在 URL 参数中
```

### 9.3 安全响应头

```http
# 防止点击劫持
X-Frame-Options: DENY

# 防止 MIME 类型嗅探
X-Content-Type-Options: nosniff

# 启用 XSS 过滤
X-XSS-Protection: 1; mode=block

# 严格传输安全（强制使用 HTTPS）
Strict-Transport-Security: max-age=31536000; includeSubDomains

# 内容安全策略（限制可加载的资源来源）
Content-Security-Policy: default-src 'self'
```

### 9.4 Cookie 安全属性

```http
Set-Cookie: session_id=abc123; Path=/; HttpOnly; Secure; SameSite=Strict
             │                  │       │        │       │
             │                  │       │        │       └── 防 CSRF
             │                  │       │        └── 仅 HTTPS 传输
             │                  │       └── JS 无法读取（防 XSS 窃取）
             │                  └── 作用路径
             └── Cookie 名称和值
```

---

## 十、实战：用 Wireshark 抓包分析 HTTP

### 10.1 抓包步骤

```
1. 打开 Wireshark，选择网卡开始抓包
2. 在过滤器中输入：http
3. 在浏览器中访问 http://www.example.com
4. 在 Wireshark 中找到 GET 请求和 200 响应
5. 右键 → Follow → TCP Stream 查看完整报文
```

### 10.2 报文分析要点

```
请求报文分析：
- 请求行：方法、路径、版本是否正确
- Host 头：目标主机是什么
- User-Agent：客户端是什么浏览器
- Cookie：携带了哪些会话信息

响应报文分析：
- 状态码：请求是否成功
- Content-Type：响应体是什么格式
- Content-Length：响应体多大
- Set-Cookie：服务器是否设置了新的 Cookie
```

---

## 知识速查表

### 常用状态码速记

```
200 → 成功
301 → 永久重定向    302 → 临时重定向    304 → 用缓存
400 → 格式错误      401 → 未登录        403 → 无权限    404 → 不存在
500 → 服务器内部错误  502 → 网关错误      503 → 服务不可用
```

### 请求方法速记

```
GET    → 获取（幂等、无体）
POST   → 创建（非幂等、有体）
PUT    → 全量更新（幂等、有体）
DELETE → 删除（幂等、无体/有体）
PATCH  → 部分更新（非幂等、有体）
```

### 版本演进速记

```
HTTP/1.0 → 短连接，每次请求建新连接
HTTP/1.1 → 长连接（keep-alive），一个连接多个请求
HTTP/2   → 多路复用，二进制帧，头部压缩，服务器推送
HTTP/3   → 基于 QUIC/UDP，0-RTT，解决队头阻塞
```
