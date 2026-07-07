"""
手动构造 HTTP POST 请求获取 flag
场景：CTF 题目
- GET 参数: ?a=love
- POST 参数: b=ctf
- 目标: 124.221.18.25:15615
"""

import socket


def build_http_request():
    """手动构造完整的 HTTP 请求报文"""
    # 请求行：POST 方法，路径带 GET 参数
    request_line = "POST /?a=love HTTP/1.1\r\n"

    # 请求头
    headers = (
        "Host: 124.221.18.25:15615\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        "Content-Length: 5\r\n"
        "Connection: close\r\n"
    )

    # POST 请求体
    body = "b=ctf"

    # 拼接完整报文（注意空行 \r\n 分隔头部和体）
    raw_request = request_line + headers + "\r\n" + body
    return raw_request


def send_request():
    """使用 socket 手动发送 HTTP 请求"""
    target_host = "124.221.18.25"
    target_port = 15615

    # 1. 构造请求报文
    raw_request = build_http_request()

    print("[*] 构造的 HTTP 请求报文：")
    print("-" * 50)
    print(raw_request)
    print("-" * 50)

    # 2. 建立 TCP 连接
    print(f"\n[*] 连接 {target_host}:{target_port} ...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)

    try:
        sock.connect((target_host, target_port))

        # 3. 发送原始 HTTP 报文（逐字节发送，模拟 Burp Suite）
        print("[*] 发送请求 ...")
        sock.sendall(raw_request.encode("utf-8"))

        # 4. 接收响应
        response = b""
        while True:
            data = sock.recv(4096)
            if not data:
                break
            response += data

        # 5. 解析并打印响应
        print("\n[*] 服务器响应：")
        print("=" * 50)
        print(response.decode("utf-8", errors="replace"))
        print("=" * 50)

    except socket.timeout:
        print("[!] 连接超时")
    except ConnectionRefusedError:
        print("[!] 连接被拒绝")
    except Exception as e:
        print(f"[!] 错误: {e}")
    finally:
        sock.close()
        print("\n[*] 连接已关闭")


if __name__ == "__main__":
    send_request()
