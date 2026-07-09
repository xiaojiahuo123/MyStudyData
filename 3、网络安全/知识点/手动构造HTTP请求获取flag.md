# 手动构造 HTTP 请求获取 Flag

## 使用工具：Burp Suite

Burp Suite 是一个 Web 安全测试工具，它的 **Repeater** 功能可以手动修改并重发 HTTP 请求，非常适合 CTF 中手动构造请求。

***

## 实战题目

**目标**：`124.221.18.25:15615`

**要求**：同时传入 GET 参数和 POST 参数

***

## 第一步：抓取原始请求

1. 浏览器配置 Burp Suite 代理（默认 `127.0.0.1:8080`）
2. 打开 Burp Suite → Proxy → Open Browser
3. 在浏览器中访问目标地址
4. 在 Proxy → HTTP history 中找到对应的请求

***

## 第二步：修改请求

在 Burp Suite 中右键请求 → **Send to Repeater**，切换到 Repeater 标签页。

手动构造以下请求：

### 原始报文

```
POST /?a=love HTTP/1.1
Host: 124.221.18.25:15615
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 5

b=ctf
```

### 报文逐行解析

```
第 1 行 ── 请求行
POST /?a=love HTTP/1.1
│     │       │
│     │       └── 协议版本
│     └── GET 参数 ?a=love（URL 中问号后面）
└── 请求方法 POST

第 2-11 行 ── 请求头
Host: 124.221.18.25:15615                    ← 目标地址
Content-Type: application/x-www-form-urlencoded ← 告诉服务器 body 是表单格式
Content-Length: 5                             ← body 的字节长度（b=ctf 刚好 5 个字符）

第 12 行 ── 空行（\r\n）
分隔请求头和请求体

第 13 行 ── 请求体
b=ctf                                        ← POST 参数
```

### 关键要点

| 要点                  | 说明                                  |
| ------------------- | ----------------------------------- |
| GET 参数写在路径里         | `POST /?a=love HTTP/1.1`            |
| POST 参数写在 body 里    | 最后一行 `b=ctf`                        |
| 必须有 Content-Type    | `application/x-www-form-urlencoded` |
| Content-Length 必须正确 | `b=ctf` 是 5 个字节，所以填 5               |
| 空行不可省略              | 头部和体之间必须有一个空行                       |

***

## 第三步：点击 Send 获取 Flag

在 Repeater 中点击 **Send**，右侧响应面板会显示服务器返回的内容，从中找到 flag。

***

![image-20260706160318629](C:\Users\79849\AppData\Roaming\Typora\typora-user-images\image-20260706160318629.png)

## 常见参数传递方式对比

```
GET 参数：    写在 URL 路径中    POST /?a=love HTTP/1.1
POST 参数：   写在请求体中      b=ctf
Cookie：      写在 Cookie 头中   Cookie: session=abc123
自定义头：    写在请求头中       X-Forwarded-For: 127.0.0.1
```

***

## Python 脚本复现

也可以用 Python 脚本自动发送同样的请求：

```python
import socket

# 构造原始 HTTP 报文
request = (
    "POST /?a=love HTTP/1.1\r\n"
    "Host: 124.221.18.25:15615\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 5\r\n"
    "Connection: close\r\n"
    "\r\n"
    "b=ctf"
)

# 建立 TCP 连接并发送
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("124.221.18.25", 15615))
sock.sendall(request.encode())

# 接收响应
response = sock.recv(4096).decode()
print(response)
sock.close()
```

***

## 总结

```
手动构造请求的核心就是自己拼接 HTTP 报文：

┌──────────────────────────────┐
│  请求行（方法 + 路径 + 版本）   │  ← GET 参数写在路径里
├──────────────────────────────┤
│  请求头（键: 值）              │  ← 必须包含 Host 和 Content-Type
├──────────────────────────────┤
│  空行                        │  ← 必须有！
├──────────────────────────────┤
│  请求体                      │  ← POST 参数写在这里
└──────────────────────────────┘
```

![image-20260706164500465](C:\Users\79849\AppData\Roaming\Typora\typora-user-images\image-20260706164500465.png)

这道题的关键在于绕过 `md5($p) == md5($n)` 的弱类型比较（`==`）。由于 PHP 的 `md5()` 函数返回十六进制字符串，当字符串以 `0e` 开头且后面全是数字时，`==` 会将其解释为科学计数法（即 `0`），于是 `0 == 0` 成立。

因此，你需要找两个**不同**的字符串，但它们的 MD5 值都以 `0e` 开头且后面全是数字。

------

### ✅ 最经典的绕过 Payload

| 参数 | 值          | MD5 值                             |
| :--- | :---------- | :--------------------------------- |
| `p`  | `QNKCDZO`   | `0e830400451993494058024219903391` |
| `n`  | `240610708` | `0e462097431906509019562988736854` |

- `s878926199a` → `0e545993274517709034328855841020`
- `s155964671a` → `0e342768416822451524974117254469`
- `214587387a` → `0e848240448830537924465865611904`

将它们填入 URL：

```
http://124.221.18.25:39738/?p=QNKCDZO&n=240610708
```

访问后即可得到 `$flag`。

![image-20260706164720548](C:\Users\79849\AppData\Roaming\Typora\typora-user-images\image-20260706164720548.png)

![image-20260706165519315](C:\Users\79849\AppData\Roaming\Typora\typora-user-images\image-20260706165519315.png)

在php中，md5的算法出现接收参数不是字符串的时候不会报错，会报异常，返回flase，然后继续执行

所以这里直接传数组

![image-20260706170553906](C:\Users\79849\AppData\Roaming\Typora\typora-user-images\image-20260706170553906.png)

这里还是一样的，v1和v2可以用数组绕过或者特殊的0e开头的md5值绕过，对于strcmp：

1. ### **`strcmp` 数组绕过**：当 `strcmp()` 的参数为**数组**时，返回 `NULL`，而 `!NULL` 为 `true`，从而绕过与 `$flag` 的比较。

![image-20260706170715897](C:\Users\79849\AppData\Roaming\Typora\typora-user-images\image-20260706170715897.png)
