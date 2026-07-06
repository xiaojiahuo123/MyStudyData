"""
HTTP 客户端实现原理 - 从 Socket 层面手写 HTTP 客户端
不依赖 requests/urllib 等库，直接用 socket 编程发送 HTTP 请求
"""
import socket
import ssl


class HTTPResponse:
    """HTTP 响应解析器 - 将原始字节流解析为结构化的响应对象"""

    def __init__(self, raw_data: bytes):
        self.version = ""
        self.status_code = 0
        self.status_phrase = ""
        self.headers = {}
        self.body = ""
        self._parse(raw_data)

    def _parse(self, raw_data: bytes):
        text = raw_data.decode("utf-8", errors="replace")

        # 分离 header 和 body
        if "\r\n\r\n" in text:
            header_part, self.body = text.split("\r\n\r\n", 1)
        else:
            header_part = text
            self.body = ""

        # 解析状态行
        lines = header_part.split("\r\n")
        status_line = lines[0]
        parts = status_line.split(" ", 2)
        if len(parts) >= 3:
            self.version = parts[0]
            self.status_code = int(parts[1])
            self.status_phrase = parts[2]

        # 解析响应头
        for line in lines[1:]:
            if ": " in line:
                key, value = line.split(": ", 1)
                self.headers[key.lower()] = value

    def __repr__(self):
        return f"HTTPResponse({self.status_code} {self.status_phrase})"


def http_request(host: str, port: int = 80, method: str = "GET",
                 path: str = "/", headers: dict = None, body: str = "",
                 use_ssl: bool = False) -> HTTPResponse:
    """
    手写 HTTP 请求的完整流程：
    1. 创建 TCP socket
    2. 建立 TCP 三次握手 (connect)
    3. 如果是 HTTPS，进行 TLS 握手
    4. 发送 HTTP 请求报文
    5. 接收 HTTP 响应报文
    6. 解析响应
    7. 关闭连接（四次挥手）
    """

    # ---- 1. 创建 TCP Socket ----
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)

    try:
        # ---- 2. TCP 三次握手 ----
        print(f"[TCP] 正在连接 {host}:{port} ...")
        sock.connect((host, port))
        print(f"[TCP] 连接建立成功 (三次握手完成)")

        # ---- 3. TLS 握手（HTTPS）----
        if use_ssl:
            context = ssl.create_default_context()
            sock = context.wrap_socket(sock, server_hostname=host)
            print(f"[TLS] TLS 握手完成，加密套件: {sock.cipher()[0]}")

        # ---- 4. 构造 HTTP 请求报文 ----
        if headers is None:
            headers = {}

        headers.setdefault("Host", host)
        headers.setdefault("User-Agent", "MyPythonHTTP/1.0")
        headers.setdefault("Accept", "text/html,*/*")
        headers.setdefault("Connection", "close")

        if body:
            headers["Content-Length"] = str(len(body.encode("utf-8")))

        # 请求行
        request_line = f"{method} {path} HTTP/1.1\r\n"

        # 请求头
        header_lines = ""
        for key, value in headers.items():
            header_lines += f"{key}: {value}\r\n"

        # 完整请求报文 = 请求行 + 请求头 + 空行 + 请求体
        raw_request = request_line + header_lines + "\r\n" + body

        print(f"\n{'='*50}")
        print(f"[发送的 HTTP 请求报文]")
        print(f"{'='*50}")
        print(raw_request)
        print(f"{'='*50}\n")

        # ---- 5. 发送 HTTP 请求 ----
        sock.sendall(raw_request.encode("utf-8"))
        print(f"[HTTP] 请求已发送: {method} {path}")

        # ---- 6. 接收 HTTP 响应 ----
        response_data = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response_data += chunk

        print(f"[HTTP] 收到响应 ({len(response_data)} 字节)")

        # ---- 7. 解析响应 ----
        response = HTTPResponse(response_data)

        print(f"\n{'='*50}")
        print(f"[解析后的 HTTP 响应]")
        print(f"{'='*50}")
        print(f"状态码: {response.status_code} {response.status_phrase}")
        print(f"响应头:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")
        print(f"响应体 ({len(response.body)} 字符):")
        print(response.body[:500])
        if len(response.body) > 500:
            print("... (内容已截断)")
        print(f"{'='*50}")

        return response

    finally:
        # ---- 8. 关闭连接（TCP 四次挥手）----
        sock.close()
        print(f"\n[TCP] 连接已关闭 (四次挥手完成)")


# ==================== 使用示例 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("  HTTP 协议客户端演示 - 从 Socket 层面理解 HTTP")
    print("=" * 60)

    # 示例 1: GET 请求
    print("\n\n>>> 示例 1: GET 请求")
    http_request(
        host="example.com",
        port=80,
        method="GET",
        path="/"
    )

    # 示例 2: 带自定义头的 GET 请求
    print("\n\n>>> 示例 2: 带自定义头的 GET 请求")
    http_request(
        host="example.com",
        port=80,
        method="GET",
        path="/",
        headers={
            "User-Agent": "Mozilla/5.0 (Custom)",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "X-Custom-Header": "Hello-HTTP",
        }
    )

    # 示例 3: POST 请求
    print("\n\n>>> 示例 3: POST 请求 (模拟表单提交)")
    post_data = "username=admin&password=123456"
    http_request(
        host="example.com",
        port=80,
        method="POST",
        path="/login",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body=post_data
    )

    # 示例 4: HTTPS 请求（如果需要）
    # print("\n\n>>> 示例 4: HTTPS 请求")
    # http_request(
    #     host="www.baidu.com",
    #     port=443,
    #     method="GET",
    #     path="/",
    #     use_ssl=True
    # )
