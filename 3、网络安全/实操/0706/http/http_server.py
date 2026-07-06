"""
HTTP 服务器实现原理 - 从 Socket 层面手写 HTTP 服务器
不依赖任何 HTTP 框架，直接用 socket 编程实现 HTTP/1.1 协议
"""
import socket
import threading
import time
from datetime import datetime


class HTTPRequest:
    """HTTP 请求解析器 - 将原始字节流解析为结构化的请求对象"""

    def __init__(self, raw_data: bytes):
        self.method = ""
        self.path = ""
        self.version = ""
        self.headers = {}
        self.body = ""
        self._parse(raw_data)

    def _parse(self, raw_data: bytes):
        """解析 HTTP 请求的三个部分：请求行、请求头、请求体"""
        text = raw_data.decode("utf-8", errors="replace")

        # ---- 1. 分离 header 和 body（以 \r\n\r\n 为分界）----
        if "\r\n\r\n" in text:
            header_part, self.body = text.split("\r\n\r\n", 1)
        else:
            header_part = text
            self.body = ""

        # ---- 2. 解析请求行（第一行）：方法 路径 版本 ----
        lines = header_part.split("\r\n")
        request_line = lines[0]
        parts = request_line.split(" ")
        if len(parts) >= 3:
            self.method = parts[0]       # GET / POST / PUT / DELETE ...
            self.path = parts[1]         # /index.html?name=tom
            self.version = parts[2]      # HTTP/1.1

        # ---- 3. 解析请求头（后续每一行都是 key: value）----
        for line in lines[1:]:
            if ": " in line:
                key, value = line.split(": ", 1)
                self.headers[key.lower()] = value

    def __repr__(self):
        return f"HTTPRequest({self.method} {self.path} {self.version})"


class HTTPResponse:
    """HTTP 响应构建器 - 根据状态码和内容生成符合协议的响应"""

    # 常见状态码与原因短语的映射
    STATUS_PHRASES = {
        200: "OK",
        301: "Moved Permanently",
        304: "Not Modified",
        400: "Bad Request",
        404: "Not Found",
        405: "Method Not Allowed",
        500: "Internal Server Error",
    }

    def __init__(self):
        self.status_code = 200
        self.headers = {
            "Server": "MyPythonHTTP/1.0",
            "Connection": "close",
        }
        self.body = ""

    def set_status(self, code: int):
        self.status_code = code
        return self

    def set_header(self, key: str, value: str):
        self.headers[key] = value
        return self

    def set_body(self, body: str):
        self.body = body
        self.headers["Content-Length"] = str(len(body.encode("utf-8")))
        self.headers["Content-Type"] = "text/html; charset=utf-8"
        return self

    def build(self) -> bytes:
        """
        将响应对象序列化为 HTTP 响应报文（字节流）
        格式：状态行 + 响应头 + 空行 + 响应体
        """
        phrase = self.STATUS_PHRASES.get(self.status_code, "Unknown")

        # 状态行
        status_line = f"HTTP/1.1 {self.status_code} {phrase}\r\n"

        # 响应头
        header_lines = ""
        for key, value in self.headers.items():
            header_lines += f"{key}: {value}\r\n"

        # 拼接完整响应：状态行 + 响应头 + 空行 + 响应体
        response = status_line + header_lines + "\r\n" + self.body
        return response.encode("utf-8")


class SimpleHTTPServer:
    """
    简易 HTTP 服务器
    核心流程：
    1. 创建 TCP socket，绑定端口，开始监听
    2. 循环 accept 客户端连接
    3. 读取原始字节流，解析为 HTTP 请求
    4. 根据请求路径生成 HTTP 响应
    5. 发送响应，关闭连接
    """

    def __init__(self, host="127.0.0.1", port=8080):
        self.host = host
        self.port = port
        self.routes = {}   # 路由表：(方法, 路径) -> 处理函数

    def route(self, path, method="GET"):
        """路由装饰器 - 注册 URL 路径与处理函数的映射"""
        def decorator(func):
            self.routes[(method.upper(), path)] = func
            return func
        return decorator

    def _handle_client(self, client_socket: socket.socket, addr):
        """处理单个客户端连接"""
        try:
            # 1. 接收原始数据
            raw_data = client_socket.recv(4096)
            if not raw_data:
                return

            # 2. 解析 HTTP 请求
            request = HTTPRequest(raw_data)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                  f"{addr[0]}:{addr[1]} -> {request.method} {request.path}")

            # 3. 查找路由处理函数
            response = HTTPResponse()
            handler = self.routes.get((request.method, request.path))

            if handler:
                # 调用用户注册的处理函数
                body = handler(request)
                response.set_body(body)
            else:
                # 404 Not Found
                response.set_status(404)
                body = f"<h1>404 Not Found</h1><p>路径 {request.path} 不存在</p>"
                response.set_body(body)

            # 4. 发送响应
            client_socket.sendall(response.build())

        except Exception as e:
            print(f"[ERROR] 处理请求时出错: {e}")
            error_resp = HTTPResponse()
            error_resp.set_status(500)
            error_resp.set_body(f"<h1>500 Internal Server Error</h1><p>{e}</p>")
            client_socket.sendall(error_resp.build())
        finally:
            client_socket.close()

    def start(self):
        """启动服务器 - 进入主循环等待连接"""
        # 创建 TCP socket（IPv4, TCP）
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许端口复用（避免重启时 "Address already in use"）
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)  # 等待队列长度

        print(f"HTTP 服务器已启动: http://{self.host}:{self.port}")
        print(f"已注册路由: {[(m, p) for m, p in self.routes.keys()]}")
        print("等待连接中... (Ctrl+C 停止)\n")

        try:
            while True:
                # accept() 阻塞等待客户端连接
                client_socket, addr = server_socket.accept()
                # 每个连接用一个新线程处理（多线程并发）
                thread = threading.Thread(
                    target=self._handle_client,
                    args=(client_socket, addr)
                )
                thread.daemon = True
                thread.start()
        except KeyboardInterrupt:
            print("\n服务器已停止")
        finally:
            server_socket.close()


# ==================== 创建服务器并注册路由 ====================
app = SimpleHTTPServer(host="127.0.0.1", port=8080)


@app.route("/", method="GET")
def index(request: HTTPRequest):
    return """<html>
<head><title>HTTP 协议演示</title></head>
<body>
    <h1>Hello, HTTP!</h1>
    <p>这是一个用 Python socket 手写的 HTTP 服务器</p>
    <ul>
        <li><a href="/time">/time</a> - 查看服务器时间</li>
        <li><a href="/headers">/headers</a> - 查看请求头</li>
        <li><a href="/form">/form</a> - 提交表单 (POST)</li>
    </ul>
</body>
</html>"""


@app.route("/time", method="GET")
def show_time(request: HTTPRequest):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""<html>
<body>
    <h1>服务器时间</h1>
    <p>当前时间: {now}</p>
    <p><a href="/">返回首页</a></p>
</body>
</html>"""


@app.route("/headers", method="GET")
def show_headers(request: HTTPRequest):
    rows = ""
    for key, value in request.headers.items():
        rows += f"<tr><td><b>{key}</b></td><td>{value}</td></tr>\n"

    return f"""<html>
<body>
    <h1>你的请求头</h1>
    <table border="1" cellpadding="8">
        <tr><th>Header</th><th>Value</th></tr>
        {rows}
    </table>
    <p><a href="/">返回首页</a></p>
</body>
</html>"""


@app.route("/form", method="GET")
def show_form(request: HTTPRequest):
    return """<html>
<body>
    <h1>表单提交 (POST)</h1>
    <form method="POST" action="/form">
        <p>用户名: <input type="text" name="username"></p>
        <p>密码: <input type="password" name="password"></p>
        <p><input type="submit" value="提交"></p>
    </form>
    <p><a href="/">返回首页</a></p>
</body>
</html>"""


@app.route("/form", method="POST")
def handle_form(request: HTTPRequest):
    return f"""<html>
<body>
    <h1>表单提交成功</h1>
    <p>收到的 POST 数据:</p>
    <pre>{request.body}</pre>
    <p><a href="/">返回首页</a></p>
</body>
</html>"""


if __name__ == "__main__":
    app.start()
