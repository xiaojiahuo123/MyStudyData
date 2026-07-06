"""
Session 核心概念演示
展示 Session 的工作原理：服务端存储 + Cookie 传递 Session ID
"""
import socket
import threading
import time
import uuid
import json
from datetime import datetime


# ==================== Session 存储（服务端内存） ====================
# 真实场景中会用 Redis / 数据库替代内存字典
session_store = {}


def create_session(user_data: dict = None) -> str:
    """创建新的 Session，返回 Session ID"""
    session_id = str(uuid.uuid4())  # 生成唯一的 Session ID
    session_store[session_id] = {
        "created_at": datetime.now().isoformat(),
        "last_access": datetime.now().isoformat(),
        "data": user_data or {},
    }
    print(f"[Session] 创建: {session_id[:12]}... 数据: {user_data}")
    return session_id


def get_session(session_id: str) -> dict | None:
    """根据 Session ID 获取 Session 数据"""
    session = session_store.get(session_id)
    if session:
        session["last_access"] = datetime.now().isoformat()
    return session


def delete_session(session_id: str):
    """销毁 Session"""
    if session_id in session_store:
        del session_store[session_id]
        print(f"[Session] 销毁: {session_id[:12]}...")


# ==================== HTTP 工具函数 ====================
def parse_cookies(cookie_header: str) -> dict:
    """从 Cookie 头解析键值对"""
    cookies = {}
    if cookie_header:
        for pair in cookie_header.split(";"):
            pair = pair.strip()
            if "=" in pair:
                key, value = pair.split("=", 1)
                cookies[key.strip()] = value.strip()
    return cookies


def build_http_response(status_code: int, headers: dict, body: str) -> bytes:
    """构造 HTTP 响应报文"""
    status_phrases = {200: "OK", 302: "Found", 401: "Unauthorized", 404: "Not Found"}
    phrase = status_phrases.get(status_code, "OK")

    status_line = f"HTTP/1.1 {status_code} {phrase}\r\n"
    header_lines = ""
    for key, value in headers.items():
        header_lines += f"Set-Cookie: {value}\r\n" if key == "Set-Cookie" else f"{key}: {value}\r\n"

    return (status_line + header_lines + "\r\n" + body).encode("utf-8")


# ==================== 页面渲染 ====================
def render_login_page(error_msg: "") -> str:
    error_html = f'<p style="color:red">{error_msg}</p>' if error_msg else ""
    return f"""<html>
<head><title>登录</title></head>
<body>
    <h1>Session 登录演示</h1>
    {error_html}
    <form method="POST" action="/login">
        <p>用户名: <input name="username" value="admin"></p>
        <p>密  码: <input name="password" type="password" value="123"></p>
        <p><input type="submit" value="登录"></p>
    </form>
</body>
</html>"""


def render_dashboard_page(username: str, visit_count: int) -> str:
    return f"""<html>
<head><title>仪表盘</title></head>
<body>
    <h1>欢迎, {username}!</h1>
    <p>你是第 {visit_count} 次访问此页面</p>
    <p>Session 验证成功 - 服务端认识你</p>
    <ul>
        <li><a href="/dashboard">刷新页面</a> (访问次数 +1)</li>
        <li><a href="/profile">个人资料</a></li>
        <li><a href="/logout">退出登录</a> (销毁 Session)</li>
    </ul>
</body>
</html>"""


def render_profile_page(username: str, login_time: str) -> str:
    return f"""<html>
<head><title>个人资料</title></head>
<body>
    <h1>个人资料</h1>
    <p>用户名: {username}</p>
    <p>登录时间: {login_time}</p>
    <p><a href="/dashboard">返回仪表盘</a></p>
</body>
</html>"""


# ==================== 请求处理 ====================
def parse_request(raw_data: bytes) -> dict:
    """解析 HTTP 请求"""
    text = raw_data.decode("utf-8", errors="replace")
    header_part, body = (text.split("\r\n\r\n", 1) + [""])[:2]
    lines = header_part.split("\r\n")

    # 请求行
    method, path, _ = lines[0].split(" ", 2)

    # 请求头
    headers = {}
    for line in lines[1:]:
        if ": " in line:
            k, v = line.split(": ", 1)
            headers[k] = v

    return {"method": method, "path": path, "headers": headers, "body": body}


def handle_request(raw_data: bytes) -> bytes:
    """处理 HTTP 请求，根据路径和 Session 状态返回响应"""
    req = parse_request(raw_data)
    method, path = req["method"], req["path"]

    # 从 Cookie 中提取 Session ID
    cookies = parse_cookies(req["headers"].get("Cookie", ""))
    session_id = cookies.get("SESSIONID")
    session = get_session(session_id) if session_id else None

    print(f"[请求] {method} {path} | SessionID: {session_id[:12] if session_id else '无'}...")

    # ---- 路由处理 ----

    # 登录页面
    if path == "/" or path == "/login":
        if method == "GET":
            if session and session["data"].get("username"):
                return _redirect("/dashboard")
            return _response(200, render_login_page())

        elif method == "POST":
            # 解析表单数据
            form = dict(param.split("=", 1) for param in req["body"].split("&") if "=" in param)
            username = form.get("username", "")
            password = form.get("password", "")

            # 简单验证
            if username == "admin" and password == "123":
                # 登录成功 -> 创建 Session
                sid = create_session({"username": username, "login_time": datetime.now().isoformat()})
                return _response(200, render_dashboard_page(username, 1),
                                 extra_headers={"Set-Cookie": f"SESSIONID={sid}; Path=/"})
            else:
                return _response(200, render_login_page("用户名或密码错误"))

    # 仪表盘（需要登录）
    if path == "/dashboard":
        if not session or not session["data"].get("username"):
            return _redirect("/")

        session["data"]["visit_count"] = session["data"].get("visit_count", 0) + 1
        return _response(200, render_dashboard_page(
            session["data"]["username"],
            session["data"]["visit_count"]
        ))

    # 个人资料（需要登录）
    if path == "/profile":
        if not session or not session["data"].get("username"):
            return _redirect("/")
        return _response(200, render_profile_page(
            session["data"]["username"],
            session["data"].get("login_time", "未知")
        ))

    # 退出登录
    if path == "/logout":
        if session_id:
            delete_session(session_id)
        return _redirect("/")

    # 404
    return _response(404, "<h1>404 Not Found</h1>")


def _response(status: int, body: str, extra_headers: dict = None) -> bytes:
    headers = {
        "Content-Type": "text/html; charset=utf-8",
        "Content-Length": str(len(body.encode("utf-8"))),
        "Connection": "close",
    }
    if extra_headers:
        headers.update(extra_headers)
    return build_http_response(status, headers, body)


def _redirect(location: str) -> bytes:
    return build_http_response(302, {"Location": location, "Connection": "close"}, "")


# ==================== 服务器启动 ====================
def start_server(host="127.0.0.1", port=8081):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)

    print(f"Session 演示服务器启动: http://{host}:{port}")
    print(f"功能: 登录 -> 创建 Session -> 访问受保护页面 -> 退出销毁 Session\n")

    try:
        while True:
            client, addr = server.accept()
            raw = client.recv(8192)
            if raw:
                response = handle_request(raw)
                client.sendall(response)
            client.close()
    except KeyboardInterrupt:
        print(f"\n服务器停止")
        print(f"当前 Session 数: {len(session_store)}")
    finally:
        server.close()


if __name__ == "__main__":
    start_server()
