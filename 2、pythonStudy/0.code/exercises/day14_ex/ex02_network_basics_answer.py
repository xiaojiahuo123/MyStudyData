"""
Day14 练习2 - 网络编程基础（答案版）
版本: v1.0
最后更新: 2026-07-13
"""

import socket
import json


# ============================================================
#                      第一部分: 基础题 (40%)
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 网络概念辨析 -----
# 知识点: IP 地址、端口号、协议

# 问题1: socket.AF_INET 表示什么？
# ____ 答案: IPv4 地址族 (Address Family INET)，即使用 IPv4 协议

# 问题2: SOCK_STREAM 对应的是 TCP 还是 UDP？
# ____ 答案: TCP（面向连接的可靠字节流）

# 问题3: SOCK_DGRAM 对应的是 TCP 还是 UDP？
# ____ 答案: UDP（无连接的数据报）

# 问题4: 端口号的范围是 0-65535，其中 0-1023 是什么端口？
# ____ 答案: 知名端口 (Well-Known Ports)，如 HTTP=80, HTTPS=443, FTP=21

# 问题5: TCP 通信中，客户端用 connect()，服务端用哪三个方法建立连接？
# ____ 答案: bind() 绑定地址，listen() 开始监听，accept() 接受连接

print("请在代码注释中作答")
print()

# ----- 题2: UDP 服务端代码预测 -----
# 知识点: socket.AF_INET + SOCK_DGRAM, bind, recvfrom, sendto

# 问题1: recvfrom(1024) 中的 1024 表示什么？
# ____ 答案: 一次最多接收的字节数（缓冲区大小），UDP 数据报超过此大小会被截断

# 问题2: recvfrom 返回几个值？分别是什么？
# ____ 答案: 返回 2 个值: (data, client_addr)
#            data: 接收到的字节数据
#            client_addr: 发送方的地址元组 (ip, port)

# 问题3: sendto 需要哪两个参数？
# ____ 答案: (data, address)，data 是要发送的字节数据，address 是目标地址元组 (ip, port)

# 问题4: UDP 服务端需要 listen() 和 accept() 吗？
# ____ 答案: 不需要！UDP 是无连接的，直接用 recvfrom 接收任意客户端的数据即可

print("请在代码注释中作答")
print()

# ----- 题3: TCP 服务端代码预测 -----
# 知识点: socket.AF_INET + SOCK_STREAM, bind, listen, accept, recv, send

# 问题1: listen(5) 中的 5 表示什么？
# ____ 答案: 等待连接的队列最大长度（backlog），即最多允许 5 个客户端排队等待 accept

# 问题2: accept() 返回几个值？分别是什么？
# ____ 答案: 返回 2 个值: (client_socket, client_addr)
#            client_socket: 新的 socket 对象，专门用于与该客户端通信
#            client_addr: 客户端的地址元组 (ip, port)

# 问题3: TCP 服务端需要用 sendto 发送数据吗？为什么？
# ____ 答案: 不需要。TCP 已建立连接，用 client_socket.send(data) 即可，
#            因为连接已经确定了通信对象，不需要每次指定地址

# 问题4: 与 UDP 相比，TCP 服务端多了哪两个关键步骤？
# ____ 答案: listen()（开始监听连接请求）和 accept()（接受客户端连接，返回专用 socket）

print("请在代码注释中作答")
print()

# ----- 题4: TCP vs UDP 对比填空 -----

print("TCP vs UDP 对比:")
print("-" * 50)

comparison = {
    "连接方式": ("面向连接 (三次握手)", "无连接"),
    "可靠性":   ("可靠 (确认重传机制)", "不可靠 (尽最大努力交付)"),
    "传输方式": ("字节流 (stream)", "数据报 (datagram)"),
    "速度":     ("较慢 (有连接/确认开销)", "较快 (无连接开销)"),
    "适用场景": ("文件传输/网页/邮件", "视频直播/游戏/DNS"),
}

for key, (tcp_val, udp_val) in comparison.items():
    print(f"  {key:6s}  TCP: {tcp_val:30s}  UDP: {udp_val}")
print()


# ============================================================
#                     第二部分: 进阶题 (35%)
# ============================================================

print("=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题5: TCP 多线程服务器代码补全 -----
# 知识点: 为每个客户端连接开一个线程处理

import threading

def handle_client(client_socket, client_addr):
    """处理单个客户端连接的函数"""
    try:
        while True:
            data = client_socket.recv(1024)     # 接收客户端数据
            if not data:                         # 客户端断开时 data 为空字节
                break
            message = data.decode('utf-8')
            print(f"客户端 {client_addr[0]} 说: {message}")
            client_socket.send(f"服务器已收到: {message}".encode('utf-8'))
    except Exception as e:
        print(f"与客户端 {client_addr[0]} 通信异常: {e}")
    finally:
        client_socket.close()                    # 关闭客户端 socket

def run_tcp_server():
    """启动 TCP 多线程服务器（仅阅读，不需要运行）"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("服务器已启动，等待连接...")

    while True:
        client_socket, client_addr = server.accept()
        threading.Thread(
            target=handle_client,
            args=(client_socket, client_addr)
        ).start()

# 问题: 为什么 handle_client 需要用 try-except-finally？
# ____ 答案: try: 捕获通信过程中的异常（如客户端强制断开、网络中断）
#            except: 打印错误日志，防止异常导致服务器崩溃
#            finally: 确保客户端 socket 被关闭，防止资源泄漏

# 问题: 如果不使用多线程，一次能处理几个客户端？
# ____ 答案: 只能处理 1 个。单线程下 recv 会阻塞，第一个客户端连接期间
#            服务器无法调用 accept() 接受新连接。

print("请在 TODO 和注释中作答")
print()

# ----- 题6: HTTP GET 请求 -----
# 知识点: requests 库的 get 方法、params 参数、status_code、json()

# 问题1: requests.get(url, params=params) 中，params 会如何拼接到 URL？
# ____ 答案: 最终请求的 URL 是: https://api.example.com/data?key=abc&type=1
#            params 字典会被编码为查询字符串 (query string) 拼接到 URL 的 ? 后面

# 问题2: response.status_code == 200 表示什么？
# ____ 答案: HTTP 请求成功 (OK)，服务器正常返回了请求的数据

# 问题3: response.json() 的作用是什么？返回什么类型？
# ____ 答案: 将响应体 (response body) 解析为 JSON 格式，返回字典 (dict) 或列表 (list)。
#            如果响应不是合法 JSON，会抛出 json.JSONDecodeError 异常

# 问题4: 如果请求失败需要捕获什么异常？
# ____ 答案: requests.RequestException（所有 requests 异常的基类），
#            常见子类包括: Timeout（超时）、ConnectionError（连接错误）、HTTPError（HTTP 错误）

print("请在代码注释中作答")
print()

# ----- 题7: HTTP 状态码处理 -----
# 知识点: 常见 HTTP 状态码的含义和处理逻辑

def handle_response(status_code):
    """根据 HTTP 状态码返回提示信息"""
    if status_code == 200:
        return "请求成功"
    elif status_code == 301:
        return "永久重定向"
    elif status_code == 404:
        return "资源未找到"
    elif status_code == 500:
        return "服务器内部错误"
    else:
        return f"未知状态码: {status_code}"

# 预测输出
print(handle_response(200))     # ____ 答案: 请求成功
print(handle_response(404))     # ____ 答案: 资源未找到
print(handle_response(500))     # ____ 答案: 服务器内部错误
print(handle_response(403))     # ____ 答案: 未知状态码: 403

print()

# ----- 题8: Starlette 路由基本结构 -----
# 知识点: Starlette 框架, Route, JSONResponse, uvicorn

# 问题1: Route 的第一个参数是什么？第二个参数是什么？
# ____ 答案: 第一个参数是 URL 路径 (path)，如 '/' 或 '/user/{user_id}'
#            第二个参数是处理函数 (endpoint)，接收 request 参数并返回 Response

# 问题2: JSONResponse 的作用是什么？
# ____ 答案: 将 Python 字典/列表自动序列化为 JSON 格式的 HTTP 响应，
#            并自动设置 Content-Type 为 application/json

# 问题3: homepage 函数为什么要用 async def？
# ____ 答案: Starlette 是异步框架，路由处理函数需要用 async def 定义，
#            以便使用 await 关键字调用异步操作（如数据库查询、HTTP 请求等），
#            实现非阻塞 I/O，提高并发性能

# 问题4: request.path_params['user_id'] 如何获取 URL 中的参数？
# ____ 答案: Starlette 会自动解析 URL 路径中 {user_id} 部分，
#            将匹配到的值存入 request.path_params 字典。
#            访问 "/user/42" 时，user_id 的值是字符串 "42"（注意是字符串，不是整数）

print("请在代码注释中作答")
print()


# ============================================================
#                    第三部分: 深入理解题 (25%) [选做]
# ============================================================

print("=" * 50)
print("第三部分: 深入理解题 [选做]")
print("=" * 50)

# ----- 题9: UDP 与 TCP 的选择场景分析 -----

print("请为以下场景选择 UDP 或 TCP，并说明理由:")
print("-" * 50)

answers = {
    "1. 在线视频直播": (
        "UDP",
        "实时性要求高，偶尔丢几帧可接受，UDP 无连接开销小、延迟低"
    ),
    "2. 文件传输": (
        "TCP",
        "要求数据完整无误，TCP 有确认重传机制保证可靠性"
    ),
    "3. 网络游戏角色位置同步": (
        "UDP",
        "位置信息频繁更新，丢失旧数据可接受，新数据会覆盖旧数据"
    ),
    "4. 电子邮件发送": (
        "TCP",
        "邮件内容必须完整到达，可靠性优先"
    ),
    "5. DNS 域名解析": (
        "UDP",
        "请求-响应模式，数据量小（通常 < 512 字节），UDP 开销更小"
    ),
}

for scenario, (protocol, reason) in answers.items():
    print(f"  {scenario}")
    print(f"    协议: {protocol}  理由: {reason}")
print()

# ----- 题10: HTTP 请求异常处理最佳实践 -----
# 知识点: requests 库的异常层次结构和处理策略

def safe_http_get(url, params=None, timeout=5):
    """安全的 HTTP GET 请求，包含完善的异常处理"""
    import requests
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()                # 非 2xx 状态码时抛出 HTTPError
        return {"success": True, "data": response.json()}

    except requests.exceptions.Timeout:
        return {"success": False, "error": "请求超时，请检查网络连接"}

    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "连接失败，请检查网络或目标地址"}

    except requests.exceptions.HTTPError as e:
        return {"success": False, "error": f"HTTP 错误: {e.response.status_code}"}

    except requests.exceptions.RequestException as e:
        return {"success": False, "error": f"请求异常: {str(e)}"}

# 问题: 异常捕获的顺序为什么很重要？为什么 RequestException 放在最后？
# ____ 答案: Python 的 except 按从上到下匹配，子类异常必须在父类之前捕获。
#            Timeout、ConnectionError、HTTPError 都是 RequestException 的子类，
#            如果把 RequestException 放在前面，子类异常会被它先捕获，
#            后面的 except 分支永远不会执行。
#            RequestException 放在最后作为兜底，捕获其他未预期的 requests 异常。

# 问题: timeout 参数有什么作用？不设置会怎样？
# ____ 答案: timeout 设置请求的超时时间（秒），超过后抛出 Timeout 异常。
#            如果不设置，requests 会无限期等待服务器响应，
#            如果服务器不响应，程序会一直卡住（hang）。
#            生产环境中必须设置 timeout！

print("请在 TODO 和注释中作答")
print()

# ----- 题11: 综合应用 - 简易 TCP 聊天室 -----

import threading

clients = []
clients_lock = threading.Lock()

def broadcast(message, sender_socket):
    """向所有客户端广播消息（除发送者外）"""
    with clients_lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except Exception:
                    clients.remove(client)        # 发送失败则移除断开的客户端

def handle_chat_client(client_socket, client_addr):
    """处理聊天室客户端连接"""
    with clients_lock:
        clients.append(client_socket)             # 将新客户端添加到列表

    welcome = f"欢迎 {client_addr[0]} 加入聊天室！"
    broadcast(welcome, client_socket)

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = f"[{client_addr[0]}]: {data.decode('utf-8')}"
            print(message)
            broadcast(message, client_socket)     # 广播消息给其他客户端
    except Exception:
        pass
    finally:
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)     # 移除断开的客户端
        client_socket.close()
        broadcast(f"{client_addr[0]} 离开了聊天室", client_socket)

def run_chat_server():
    """启动聊天室服务器（仅阅读，不需要运行）"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8888))
    server.listen(10)
    print("聊天室服务器已启动...")

    while True:
        client_socket, client_addr = server.accept()
        thread = threading.Thread(
            target=handle_chat_client,
            args=(client_socket, client_addr)
        )
        thread.start()

# 问题: 为什么 clients 列表需要用 clients_lock 保护？
# ____ 答案: 多个线程会并发访问 clients 列表（添加新客户端、移除断开的客户端、
#            遍历广播消息）。如果不加锁，可能出现:
#            - 遍历时修改列表导致 RuntimeError
#            - 并发 append/remove 导致数据丢失
#            这是典型的读写并发问题。

# 问题: broadcast 函数中为什么要用 try-except？
# ____ 答案: 广播时某个客户端可能已经断开连接，send() 会抛出异常。
#            如果不捕获异常，一个客户端断开会导致整个广播中断。
#            用 try-except 可以跳过断开的客户端，继续向其他客户端发送。

# 问题: finally 块中为什么要先移除客户端再广播退出消息？
# ____ 答案: 先移除再广播是为了避免向已断开的客户端发送 "退出" 消息（自欺欺人）。
#            如果先广播再移除，broadcast 会尝试向这个已断开的 socket 发数据，导致异常。

print("请在 TODO 和注释中作答")
print()

# ----- 题12: 调试修复题 -----
# 知识点: 识别网络编程中的常见错误

# BUG 1 修复: UDP 客户端发送数据
# 原代码: client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ____ 答案: 应该用 SOCK_DGRAM（UDP），不是 SOCK_STREAM（TCP）
# 修复后:
"""
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 修复: SOCK_DGRAM
client.sendto("Hello".encode(), ('127.0.0.1', 8888))
"""

# BUG 2 修复: TCP 服务端处理客户端断开
# 原代码: data = client.recv(1024) 之后直接 print(data.decode('utf-8'))
# ____ 答案: 客户端断开时 recv() 返回空字节 b''，直接 decode 会得到空字符串，
#           但后续 send() 会向已断开的连接发送数据导致异常。
#           应该检查 data 是否为空，为空则 break 退出循环。
# 修复后:
"""
data = client.recv(1024)
if not data:          # 修复: 检查客户端是否断开
    break
print(data.decode('utf-8'))
client.send("OK".encode())
"""

# BUG 3 修复: HTTP 请求处理
# 原代码: response = requests.get('https://api.example.com/data') 没有 timeout 和异常处理
# ____ 答案: 两个问题:
#   (1) 没有设置 timeout，如果服务器不响应会永久阻塞
#   (2) 没有 try-except，网络错误或 JSON 解析错误会直接崩溃
# 修复后:
"""
import requests
try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()
    data = response.json()
    print(data['result'])
except requests.RequestException as e:
    print(f"请求失败: {e}")
except KeyError:
    print("响应中没有 'result' 字段")
"""
