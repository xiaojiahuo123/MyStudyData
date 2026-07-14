"""
Day14 练习2 - 网络编程基础
由浅入深掌握 UDP/TCP 编程、HTTP 请求、Web 服务

参考源码: day14/P02_UDP_Server.py
         day14/P03_UDP_Client.py
         day14/P04_TCP_Server.py
         day14/P05_TCP_Client.py
         day14/P06_Http.py
         day14/P07_Starlette.py
版本: v1.0
最后更新: 2026-07-13
"""

# 注意: 本练习以代码阅读和 API 理解为主，服务端代码不需要实际运行
# 需要实际运行的代码已标注 [可运行]

import socket
import json


# ============================================================
#                      第一部分: 基础题 (40%)
# ============================================================

print("=" * 50)
print("第一部分: 基础题")
print("=" * 50)

# ----- 题1: 网络概念辨析 [必做] -----
# 知识点: IP 地址、端口号、协议
# 预测以下代码的输出结果

# 问题1: socket.AF_INET 表示什么？ ____
# 问题2: SOCK_STREAM 对应的是 TCP 还是 UDP？ ____
# 问题3: SOCK_DGRAM 对应的是 TCP 还是 UDP？ ____
# 问题4: 端口号的范围是 0-65535，其中 0-1023 是什么端口？ ____
# 问题5: TCP 通信中，客户端用 connect()，服务端用哪三个方法建立连接？
#        ____, ____, ____

print("请在代码注释中作答")
print()

# ----- 题2: UDP 服务端代码预测 [必做] -----
# 知识点: socket.AF_INET + SOCK_DGRAM, bind, recvfrom, sendto
# 参考: P02_UDP_Server.py
# 预测以下 UDP 服务端代码的执行流程和输出

# --- 模拟 UDP 服务端（仅代码阅读，不需要运行）---
"""
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8888))

while True:
    data, client_addr = server.recvfrom(1024)
    print(f"收到来自 {client_addr} 的消息: {data.decode('utf-8')}")
    server.sendto("已收到".encode('utf-8'), client_addr)
"""

# 问题1: recvfrom(1024) 中的 1024 表示什么？ ____
# 问题2: recvfrom 返回几个值？分别是什么？ ____
# 问题3: sendto 需要哪两个参数？ ____
# 问题4: UDP 服务端需要 listen() 和 accept() 吗？ ____

print("请在代码注释中作答")
print()

# ----- 题3: TCP 服务端代码预测 [必做] -----
# 知识点: socket.AF_INET + SOCK_STREAM, bind, listen, accept, recv, send
# 参考: P04_TCP_Server.py 基本版
# 预测以下 TCP 服务端代码的执行流程

# --- 模拟 TCP 服务端（仅代码阅读，不需要运行）---
"""
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen(5)

client, addr = server.accept()
print(f"客户端 {addr} 已连接")

while True:
    data = client.recv(1024)
    print(f"客户端说: {data.decode('utf-8')}")
    client.send("你好".encode('utf-8'))
"""

# 问题1: listen(5) 中的 5 表示什么？ ____
# 问题2: accept() 返回几个值？分别是什么？ ____
# 问题3: TCP 服务端需要用 sendto 发送数据吗？为什么？ ____
# 问题4: 与 UDP 相比，TCP 服务端多了哪两个关键步骤？ ____

print("请在代码注释中作答")
print()

# ----- 题4: TCP vs UDP 对比填空 [必做] -----
# 知识点: 理解两种协议的核心区别

print("TCP vs UDP 对比:")
print("-" * 50)

comparison = {
    "连接方式": ("____ (面向连接/无连接)", "____ (面向连接/无连接)"),
    "可靠性":   ("____ (可靠/不可靠)", "____ (可靠/不可靠)"),
    "传输方式": ("____ (字节流/数据报)", "____ (字节流/数据报)"),
    "速度":     ("____ (较慢/较快)", "____ (较慢/较快)"),
    "适用场景": ("____ ", "____ "),
}

# 格式: 左列填 TCP，右列填 UDP
for key, (tcp_val, udp_val) in comparison.items():
    print(f"  {key:6s}  TCP: {tcp_val:30s}  UDP: {udp_val}")
print()


# ============================================================
#                     第二部分: 进阶题 (35%)
# ============================================================

print("=" * 50)
print("第二部分: 进阶题")
print("=" * 50)

# ----- 题5: TCP 多线程服务器代码补全 [必做] -----
# 知识点: 为每个客户端连接开一个线程处理
# 参考: P04_TCP_Server.py 优化3版本
# TODO: 补全以下 TCP 多线程服务器的代码

import threading

def handle_client(client_socket, client_addr):
    """处理单个客户端连接的函数"""
    try:
        while True:
            # TODO: 接收客户端数据
            data = None  # 替换为: client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"客户端 {client_addr[0]} 说: {message}")
            # TODO: 向客户端发送响应
            # 替换为: client_socket.send(f"服务器已收到: {message}".encode('utf-8'))
    except Exception as e:
        print(f"与客户端 {client_addr[0]} 通信异常: {e}")
    finally:
        # TODO: 关闭客户端 socket
        pass  # 替换为: client_socket.close()

def run_tcp_server():
    """启动 TCP 多线程服务器（仅阅读，不需要运行）"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("服务器已启动，等待连接...")

    while True:
        # TODO: 等待客户端连接
        client_socket, client_addr = None, None  # 替换为: server.accept()
        # TODO: 为每个客户端创建一个新线程
        # 替换为: threading.Thread(target=handle_client, args=(client_socket, client_addr)).start()

# 问题: 为什么 handle_client 需要用 try-except-finally？ ____
# 问题: 如果不使用多线程，一次能处理几个客户端？ ____

print("请在 TODO 和注释中作答")
print()

# ----- 题6: HTTP GET 请求 [必做] -----
# 知识点: requests 库的 get 方法、params 参数、status_code、json()
# 参考: P06_Http.py

# 以下代码演示了 requests 库的用法（可阅读理解，实际运行需要网络）

"""
import requests

# 一言网 API
url = 'https://international.v1.hitokoto.cn'
params = {
    'c': 'a',
    'encode': 'json'
}
response = requests.get(url, params=params)
"""

# 问题1: requests.get(url, params=params) 中，params 会如何拼接到 URL？
#        如果 url 是 "https://api.example.com/data"，params 是 {"key": "abc", "type": "1"}
#        最终请求的 URL 是什么？ ____

# 问题2: response.status_code == 200 表示什么？ ____

# 问题3: response.json() 的作用是什么？返回什么类型？ ____

# 问题4: 如果请求失败需要捕获什么异常？ ____

print("请在代码注释中作答")
print()

# ----- 题7: HTTP 状态码处理 [必做] -----
# 知识点: 常见 HTTP 状态码的含义和处理逻辑
# 预测以下代码的输出

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
print(handle_response(200))     # ____
print(handle_response(404))     # ____
print(handle_response(500))     # ____
print(handle_response(403))     # ____

print()

# ----- 题8: Starlette 路由基本结构 [必做] -----
# 知识点: Starlette 框架, Route, JSONResponse, uvicorn
# 参考: P07_Starlette.py

# 阅读以下 Starlette 应用代码，回答问题

"""
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn

async def homepage(request):
    return JSONResponse({"message": "Hello, World!"})

async def get_user(request):
    user_id = request.path_params['user_id']
    return JSONResponse({"user_id": user_id})

app = Starlette(routes=[
    Route('/', homepage),
    Route('/user/{user_id}', get_user),
])

uvicorn.run(app, host='0.0.0.0', port=8000)
"""

# 问题1: Route 的第一个参数是什么？第二个参数是什么？ ____
# 问题2: JSONResponse 的作用是什么？ ____
# 问题3: homepage 函数为什么要用 async def？ ____
# 问题4: request.path_params['user_id'] 如何获取 URL 中的参数？
#        如果访问 "/user/42"，user_id 的值是什么？ ____

print("请在代码注释中作答")
print()


# ============================================================
#                    第三部分: 深入理解题 (25%) [选做]
# ============================================================

print("=" * 50)
print("第三部分: 深入理解题 [选做]")
print("=" * 50)

# ----- 题9: UDP 与 TCP 的选择场景分析 [选做] -----
# 知识点: 根据应用场景选择合适的传输协议

print("请为以下场景选择 UDP 或 TCP，并说明理由:")
print("-" * 50)

scenarios = [
    "1. 在线视频直播（实时性要求高，偶尔丢几帧可接受）",
    "2. 文件传输（要求数据完整无误）",
    "3. 网络游戏中的角色位置同步（实时性优先）",
    "4. 电子邮件发送（可靠性优先）",
    "5. DNS 域名解析（请求-响应模式，数据量小）",
]

for s in scenarios:
    print(f"  {s}")
    print(f"    协议: ____  理由: ____")
print()

# ----- 题10: HTTP 请求异常处理最佳实践 [选做] -----
# 知识点: requests 库的异常层次结构和处理策略
# 参考: P06_Http.py 的 try-except 结构

# TODO: 补全以下 HTTP 请求函数，实现完善的异常处理

def safe_http_get(url, params=None, timeout=5):
    """
    安全的 HTTP GET 请求，包含完善的异常处理
    
    参数:
        url: 请求地址
        params: 查询参数字典
        timeout: 超时时间(秒)
    返回:
        成功时返回响应数据字典，失败时返回包含错误信息的字典
    """
    import requests
    try:
        # TODO: 发送 GET 请求，设置超时时间
        response = None  # 替换为: requests.get(url, params=params, timeout=timeout)

        # TODO: 检查状态码，非 200 时抛出 HTTPError
        # 提示: response.raise_for_status()

        # TODO: 解析并返回 JSON 数据
        return {}

    except requests.exceptions.Timeout:
        # TODO: 处理超时异常
        return {}

    except requests.exceptions.ConnectionError:
        # TODO: 处理连接错误（DNS 失败、拒绝连接等）
        return {}

    except requests.exceptions.HTTPError as e:
        # TODO: 处理 HTTP 错误状态码（4xx, 5xx）
        return {}

    except requests.exceptions.RequestException as e:
        # TODO: 捕获所有 requests 相关异常（兜底）
        return {}

# 问题: 异常捕获的顺序为什么很重要？为什么 RequestException 放在最后？ ____
# 问题: timeout 参数有什么作用？不设置会怎样？ ____

print("请在 TODO 和注释中作答")
print()

# ----- 题11: 综合应用 - 简易 TCP 聊天室 [选做] -----
# 知识点: TCP 多线程服务器 + 广播消息
# TODO: 补全一个简易的 TCP 聊天室服务器

import threading

# 存储所有已连接的客户端
clients = []
clients_lock = threading.Lock()

def broadcast(message, sender_socket):
    """向所有客户端广播消息（除发送者外）"""
    with clients_lock:
        for client in clients:
            if client != sender_socket:
                try:
                    # TODO: 向客户端发送消息
                    pass  # 替换为: client.send(message.encode('utf-8'))
                except Exception:
                    # TODO: 发送失败时移除该客户端
                    pass  # 替换为: clients.remove(client)

def handle_chat_client(client_socket, client_addr):
    """处理聊天室客户端连接"""
    with clients_lock:
        # TODO: 将新客户端添加到 clients 列表
        pass  # 替换为: clients.append(client_socket)

    welcome = f"欢迎 {client_addr[0]} 加入聊天室！"
    broadcast(welcome, client_socket)

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = f"[{client_addr[0]}]: {data.decode('utf-8')}"
            print(message)
            # TODO: 广播消息给其他客户端
            pass  # 替换为: broadcast(message, client_socket)
    except Exception:
        pass
    finally:
        with clients_lock:
            if client_socket in clients:
                # TODO: 移除断开的客户端
                pass  # 替换为: clients.remove(client_socket)
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

# 问题: 为什么 clients 列表需要用 clients_lock 保护？ ____
# 问题: broadcast 函数中为什么要用 try-except？ ____
# 问题: finally 块中为什么要先移除客户端再广播退出消息？ ____

print("请在 TODO 和注释中作答")
print()

# ----- 题12: 调试修复题 [选做] -----
# 知识点: 识别网络编程中的常见错误
# BUG: 以下代码有 3 处错误，请找出并修复

"""
# BUG 1: UDP 客户端发送数据
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # BUG: ____（提示: UDP 应该用什么类型？）
client.sendto("Hello".encode(), ('127.0.0.1', 8888))
"""

"""
# BUG 2: TCP 服务端处理客户端断开
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen(5)
client, addr = server.accept()
while True:
    data = client.recv(1024)
    print(data.decode('utf-8'))  # BUG: ____（提示: 客户端断开时 data 是什么？）
    client.send("OK".encode())
"""

"""
# BUG 3: HTTP 请求处理
import requests
response = requests.get('https://api.example.com/data')  # BUG: ____（提示: 超时？异常？）
data = response.json()  # 如果响应不是 JSON 格式会怎样？
print(data['result'])
"""

# 问题: 请找出每处 BUG 并写出修复代码
