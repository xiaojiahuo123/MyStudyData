# Day14 知识点总结

## 1. 线程安全 - 买票系统

```python
lock = threading.Lock()

def func():
    global ticket_num
    while True:
        lock.acquire()           # 获取锁
        if ticket_num <= 0:
            lock.release()       # break 前必须释放锁
            break
        ticket_num -= 1
        lock.release()           # 操作完释放锁
```

- 多线程共享全局变量时，修改操作必须加锁
- `break` 前必须先 `release()`，否则其他线程死锁

---

## 2. Socket 创建参数

```python
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # UDP
socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP
```

| 参数 | 含义 |
|------|------|
| `socket.AF_INET` | IPv4 协议（`AF_INET6` 是 IPv6） |
| `socket.SOCK_DGRAM` | **UDP** 协议，无连接 |
| `socket.SOCK_STREAM` | **TCP** 协议，面向连接 |

---

## 3. bind 绑定地址

```python
socket.bind(('127.0.0.1', 8888))
#          └── 一个元组参数 ──┘
```

- `bind` 只接收**一个参数**：地址元组，不是分别传 IP 和端口
- IPv4 格式：`(IP地址, 端口号)`
- `0.0.0.0` 表示监听所有网卡，`127.0.0.1` 只监听本机

---

## 4. recvfrom 返回值

```python
recv_data, client_info = socket.recvfrom(1024)
```

- `1024`：缓冲区大小（最多接收 1024 字节）
- `recv_data`：接收到的数据（`bytes` 类型，用 `.decode('utf-8')` 转字符串）
- `client_info`：发送方地址元组 `('IP', 端口)`，可用于回复消息
- `recvfrom` 会**阻塞**，直到收到数据

---

## 5. UDP 通信

### 5.1 UDP 服务器

```python
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server.bind(('127.0.0.1', 8888))
recv_data, client_info = socket_server.recvfrom(1024)  # 接收数据
socket_server.sendto("你好".encode('utf-8'), client_info)  # 发送数据
```

### 5.2 UDP 客户端

```python
socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_client.sendto("消息".encode('utf-8'), ('127.0.0.1', 8888))
recv_data, server_info = socket_client.recvfrom(1024)
```

- UDP **无连接**，直接 `sendto`/`recvfrom`
- `recvfrom(1024)` 返回 `(数据, 发送方地址信息)`
- 数据需要 `.encode('utf-8')` 编码发送，`.decode('utf-8')` 解码接收

---

## 6. TCP 通信

### 6.1 TCP 服务器

```python
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.bind(('0.0.0.0', 9999))
socket_tcp.listen(5)                           # 监听，参数为最大排队数
socket_client, client_info = socket_tcp.accept() # 等待连接（阻塞）
recv_data = socket_client.recv(1024)            # 接收数据
socket_client.send("你好".encode('utf-8'))       # 发送数据
```

### 6.2 TCP 客户端

```python
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.connect(('192.168.34.78', 9999))     # 连接服务器
socket_tcp.send("消息".encode('utf-8'))
recv_data = socket_tcp.recv(1024)
```

### 6.3 多线程 TCP 服务器

```python
def handle(socket_client, client_info):
    try:
        while True:
            recv_data = socket_client.recv(1024)
            if not recv_data:        # 客户端断开
                break
            socket_client.send("回复".encode('utf-8'))
    except Exception:
        pass
    finally:
        socket_client.close()        # 确保关闭连接

while True:
    socket_client, client_info = socket_tcp.accept()
    threading.Thread(target=handle, args=(socket_client, client_info)).start()
```

---

## 7. UDP vs TCP 对比

| | UDP | TCP |
|---|---|---|
| 连接 | 无连接，直接发 | 需要先 `connect` 建立连接 |
| 可靠性 | 不可靠，可能丢包 | 可靠，保证数据到达 |
| 速度 | 快（无握手） | 相对慢（三次握手） |
| 创建方式 | `SOCK_DGRAM` | `SOCK_STREAM` |
| 发送/接收 | `sendto`/`recvfrom` | `send`/`recv` |
| 典型场景 | 视频通话、游戏 | 网页、文件传输、聊天 |

---

## 8. HTTP 请求（requests 库）

```python
import requests

url = 'https://international.v1.hitokoto.cn'
params = {'c': 'a', 'encode': 'json'}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()         # 解析 JSON 响应
    print(data['hitokoto'])
```

- `requests.get(url, params=)` 发送 GET 请求
- `response.status_code` 状态码：200 成功，404 未找到，500 服务器错误
- `response.json()` 将响应体解析为 Python 字典

---

## 9. Starlette Web 服务

```python
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn

async def homepage(request):
    return JSONResponse({"key": "value"})

app = Starlette(routes=[Route('/', homepage)])
uvicorn.run(app, host='0.0.0.0', port=8000)
```

- **Starlette**：轻量级异步 Web 框架
- **uvicorn**：ASGI 服务器，运行 Starlette 应用
- 路由通过 `Route(路径, 处理函数)` 定义
- 处理函数是 `async`，返回 `JSONResponse`

---

## 10. send vs sendto、recv vs recvfrom

### 核心区别

TCP 建立连接后通信对象固定，不需要每次指定地址；UDP 无连接，必须每次指定目标：

```python
# UDP - 无连接，必须指定目标地址
socket.sendto("你好".encode('utf-8'), ('127.0.0.1', 8888))
recv_data, client_info = socket.recvfrom(1024)  # 返回 (数据, 地址)

# TCP - 已连接，对象固定，直接收发
socket_client.send("你好".encode('utf-8'))
recv_data = socket_client.recv(1024)            # 只返回数据
```

### 对比

| | UDP | TCP |
|---|---|---|
| 发送 | `sendto(数据, 目标地址)` | `send(数据)` |
| 接收 | `recvfrom(缓冲区)` → `(数据, 地址)` | `recv(缓冲区)` → `数据` |
| 原因 | 无连接，不知道谁发的 | 已连接，对象固定 |

**类比**：
- UDP = 寄快递，每次都要写收件人地址（`sendto`），收快递也要看寄件人信息（`recvfrom`）
- TCP = 打电话，接通后直接说话（`send`）和听（`recv`），不需要每次报号码

### 变量名遮蔽问题

```python
# ❌ 错误：socket 变量覆盖了 socket 模块
import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 模块被覆盖

# ✅ 正确：用有意义的变量名
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

### 端口复用

```python
# 防止 "端口已占用" 错误（OSError: [WinError 10048]）
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8888))
```

`while True` 循环中的 `socket.close()` 是死代码，强制终止后端口被 OS 保留，加上 `SO_REUSEADDR` 可以立即重新绑定。

### TCP 服务器 listen 参数

```python
socket_tcp.listen(5)
```

参数 `5` 是**等待连接的最大排队数**（backlog），不是最大连接数。当多个客户端同时请求连接时，超出的会被拒绝。
