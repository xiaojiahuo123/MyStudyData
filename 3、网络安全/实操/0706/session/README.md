# Session 知识点与实现原理

## 文件说明

| 文件 | 内容 |
|------|------|
| `01_session_concept.py` | Session 工作原理演示（可运行的 HTTP 服务器，带登录功能） |
| `02_session_attack.py` | Session 安全攻防（固定攻击、劫持、Cookie 属性、JWT 对比） |
| `03_session_storage.py` | Session 存储后端实现（内存、文件、Redis 模拟） |

## 核心知识点

### 1. Session 是什么

```
HTTP 是无状态协议 -> 服务端不知道两次请求是否来自同一个用户
Session 就是服务端为每个用户创建的"会话档案"
通过 Session ID 将用户的多次请求关联起来
```

### 2. Session 工作流程

```
1. 用户首次访问 -> 服务端创建 Session，生成 Session ID
2. 服务端通过 Set-Cookie 把 Session ID 发给浏览器
3. 浏览器后续请求自动带上 Cookie: SESSIONID=xxx
4. 服务端根据 Session ID 查找对应的 Session 数据
5. 用户退出或 Session 过期 -> 服务端删除 Session
```

### 3. Session vs Cookie

```
Cookie: 存在客户端浏览器，有大小限制(4KB)，可被用户查看/篡改
Session: 存在服务端，无大小限制，安全，但占用服务器资源
关系: Session ID 通过 Cookie 传递（也可用 URL 参数，但不安全）
```

### 4. Session 安全威胁

| 攻击方式 | 原理 | 防御 |
|----------|------|------|
| Session 固定 | 攻击者指定 Session ID | 登录后重新生成 Session ID |
| Session 劫持 | 窃取 Session ID（XSS/嗅探） | HTTPS + HttpOnly |
| CSRF | 借助已登录状态发起恶意请求 | SameSite Cookie + CSRF Token |
| 暴力破解 | 枚举 Session ID | 使用足够长的随机 ID (>=128 bit) |

### 5. Cookie 安全属性

```
Set-Cookie: SESSIONID=xxx;
    HttpOnly;      # JS 无法读取（防 XSS）
    Secure;        # 只在 HTTPS 下发送（防嗅探）
    SameSite=Lax;  # 限制跨站发送（防 CSRF）
    Path=/;        # 作用范围
    Max-Age=3600;  # 过期时间
```

## 使用方式

```bash
# 1. 先看 Session 工作原理（启动 HTTP 服务器，浏览器访问登录）
python 01_session_concept.py
# 浏览器打开 http://127.0.0.1:8081

# 2. 看 Session 攻防演示
python 02_session_attack.py

# 3. 看不同存储后端的实现
python 03_session_storage.py
```
