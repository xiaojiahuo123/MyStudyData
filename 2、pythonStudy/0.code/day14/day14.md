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
