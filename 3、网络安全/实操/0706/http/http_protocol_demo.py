"""
HTTP 协议结构演示 - 逐字节解析 HTTP 报文格式
不发送任何网络请求，纯粹展示 HTTP 报文的构成
"""


def demo_request_format():
    """演示 HTTP 请求报文格式"""
    print("=" * 60)
    print("  HTTP 请求报文格式")
    print("=" * 60)

    # 模拟一个浏览器发送的 HTTP 请求
    raw_request = (
        "GET /index.html?name=tom&age=18 HTTP/1.1\r\n"  # 请求行
        "Host: www.example.com\r\n"                       # 请求头
        "User-Agent: Mozilla/5.0\r\n"                     # 请求头
        "Accept: text/html,application/xhtml+xml\r\n"     # 请求头
        "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n"   # 请求头
        "Accept-Encoding: gzip, deflate, br\r\n"          # 请求头
        "Connection: keep-alive\r\n"                       # 请求头
        "Cookie: session_id=abc123; user=admin\r\n"       # 请求头
        "\r\n"                                              # 空行（分隔头和体）
    )

    print("\n[原始报文]")
    print(repr(raw_request))

    print("\n[人类可读格式]")
    print(raw_request)

    print("\n[逐行解析]")
    lines = raw_request.split("\r\n")

    # 第 1 行：请求行
    method, path, version = lines[0].split(" ", 2)  # 请求方法，路径(服务器上的路径)，协议版本
    print(f"┌─ 请求行 (Request Line)")
    print(f"│  方法 (Method) : {method}")
    print(f"│  路径 (URI)    : {path}")
    print(f"│    └─ 路径部分 : /index.html")
    print(f"│    └─ 查询参数 : name=tom&age=18")
    print(f"│  版本 (Version): {version}")

    # 请求头
    print(f"├─ 请求头 (Request Headers)")
    for line in lines[1:]:
        if ": " in line:
            key, value = line.split(": ", 1)
            print(f"│  {key}: {value}")

    # 空行
    print(f"├─ 空行 (CRLF)  : 标记头部结束")
    print(f"└─ 请求体 (Body): (GET 请求无请求体)")


def demo_response_format():
    """演示 HTTP 响应报文格式"""
    print("\n\n" + "=" * 60)
    print("  HTTP 响应报文格式")
    print("=" * 60)

    body = "<html><body><h1>Hello World</h1></body></html>"

    raw_response = (
        "HTTP/1.1 200 OK\r\n"                             # 状态行
        "Date: Sun, 06 Jul 2026 12:00:00 GMT\r\n"         # 响应头
        "Server: Apache/2.4.41\r\n"                        # 响应头
        "Content-Type: text/html; charset=utf-8\r\n"      # 响应头
        f"Content-Length: {len(body)}\r\n"                 # 响应头
        "Set-Cookie: session_id=xyz789; Path=/\r\n"       # 响应头
        "Connection: keep-alive\r\n"                        # 响应头
        "\r\n"                                              # 空行
        f"{body}"                                           # 响应体
    )

    print("\n[原始报文]")
    print(repr(raw_response[:200]) + "...")

    print("\n[人类可读格式]")
    print(raw_response)

    print("\n[逐行解析]")
    # 分离头部和体
    header_part, body_content = raw_response.split("\r\n\r\n", 1)
    lines = header_part.split("\r\n")

    # 状态行
    version, status_code, reason = lines[0].split(" ", 2)
    print(f"┌─ 状态行 (Status Line)")
    print(f"│  版本 (Version)  : {version}")
    print(f"│  状态码 (Code)   : {status_code}")
    print(f"│  原因短语 (Reason): {reason}")

    # 响应头
    print(f"├─ 响应头 (Response Headers)")
    for line in lines[1:]:
        if ": " in line:
            key, value = line.split(": ", 1)
            desc = {
                "Date": "服务器生成响应的时间",
                "Server": "服务器软件信息",
                "Content-Type": "响应体的 MIME 类型和编码",
                "Content-Length": "响应体的字节长度",
                "Set-Cookie": "设置 Cookie（用于会话管理）",
                "Connection": "连接管理方式",
            }.get(key, "")
            note = f"  ← {desc}" if desc else ""
            print(f"│  {key}: {value}{note}")

    print(f"├─ 空行 (CRLF)   : 标记头部结束")
    print(f"└─ 响应体 (Body) : {body_content}")


def demo_post_request():
    """演示 POST 请求（带请求体）"""
    print("\n\n" + "=" * 60)
    print("  HTTP POST 请求（带请求体）")
    print("=" * 60)

    body_data = '{"username": "admin", "password": "123456"}'

    raw_request = (
        "POST /api/login HTTP/1.1\r\n"
        "Host: www.example.com\r\n"
        "Content-Type: application/json\r\n"
        f"Content-Length: {len(body_data)}\r\n"
        "Accept: application/json\r\n"
        "\r\n"
        f"{body_data}"
    )

    print("\n[原始报文]")
    print(raw_request)

    print("\n[解析]")
    print(f"┌─ 请求行 : POST /api/login HTTP/1.1")
    print(f"├─ Header : Content-Type: application/json")
    print(f"│          → 告诉服务器请求体是 JSON 格式")
    print(f"├─ Header : Content-Length: {len(body_data)}")
    print(f"│          → 请求体的字节长度（服务器据此读取完整 body）")
    print(f"├─ 空行   : 分隔 header 和 body")
    print(f"└─ Body   : {body_data}")


def demo_status_codes():
    """展示常见 HTTP 状态码"""
    print("\n\n" + "=" * 60)
    print("  常见 HTTP 状态码")
    print("=" * 60)

    codes = [
        (200, "OK", "请求成功"),
        (301, "Moved Permanently", "永久重定向"),
        (302, "Found", "临时重定向"),
        (304, "Not Modified", "资源未修改，使用缓存"),
        (400, "Bad Request", "请求格式错误"),
        (401, "Unauthorized", "未认证（需要登录）"),
        (403, "Forbidden", "无权限访问"),
        (404, "Not Found", "资源不存在"),
        (405, "Method Not Allowed", "请求方法不允许"),
        (500, "Internal Server Error", "服务器内部错误"),
        (502, "Bad Gateway", "网关错误"),
        (503, "Service Unavailable", "服务不可用"),
    ]

    print(f"\n{'状态码':<8} {'原因短语':<25} {'含义'}")
    print("-" * 60)
    for code, phrase, desc in codes:
        category = f"{code // 100}xx"
        print(f"{code:<8} {phrase:<25} {desc}")


def demo_methods():
    """展示 HTTP 请求方法"""
    print("\n\n" + "=" * 60)
    print("  HTTP 请求方法")
    print("=" * 60)

    methods = [
        ("GET", "获取资源", "幂等", "无"),
        ("POST", "提交数据/创建资源", "非幂等", "有（表单/JSON等）"),
        ("PUT", "更新资源（全量替换）", "幂等", "有"),
        ("DELETE", "删除资源", "幂等", "无/有"),
        ("PATCH", "更新资源（部分修改）", "非幂等", "有"),
        ("HEAD", "只获取响应头", "幂等", "无"),
        ("OPTIONS", "查询服务器支持的方法", "幂等", "无"),
    ]

    print(f"\n{'方法':<10} {'用途':<28} {'幂等':<8} {'请求体'}")
    print("-" * 60)
    for method, usage, idempotent, has_body in methods:
        print(f"{method:<10} {usage:<28} {idempotent:<8} {has_body}")


def demo_connection_lifecycle():
    """展示 HTTP 连接的完整生命周期"""
    print("\n\n" + "=" * 60)
    print("  HTTP 连接的完整生命周期 (TCP 层面)")
    print("=" * 60)

    print("""
客户端                                            服务器
  │                                                  │
  │  ──────── TCP 三次握手 (SYN/SYN-ACK/ACK) ──────>  │
  │  <──────────────────────────────────────────────  │
  │                                                  │
  │  ──────── HTTP 请求报文 (GET /index.html) ──────>  │
  │                                                  │
  │  <──────── HTTP 响应报文 (200 OK + HTML) ─────────  │
  │                                                  │
  │  ──────── TCP 四次挥手 (FIN/ACK/FIN/ACK) ───────  │
  │  <──────────────────────────────────────────────  │
  │                                                  │
  v                                                  v

  HTTP/1.0: 每个请求一个 TCP 连接（短连接）
  HTTP/1.1: 默认 keep-alive，一个连接可发多个请求（长连接）
  HTTP/2:   多路复用，一个连接并发多个请求（二进制帧）
  HTTP/3:   基于 QUIC/UDP，0-RTT 建立连接
    """)


if __name__ == "__main__":
    print("=" * 60)
    print("  HTTP 协议结构详解 - 纯本地演示")
    print("  不发送任何网络请求，仅展示报文格式")
    print("=" * 60)

    demo_request_format()
    demo_response_format()
    demo_post_request()
    demo_status_codes()
    demo_methods()
    demo_connection_lifecycle()

    print("\n演示结束。")
