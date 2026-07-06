"""
配合 http_capture.py 使用的测试脚本
通过代理发送 HTTP 请求，让抓包工具捕获并展示 HTTP 报文
"""
import socket


def send_via_proxy(proxy_host, proxy_port, target_host, target_path="/"):
    """通过代理发送 HTTP 请求"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((proxy_host, proxy_port))

    # 构造 HTTP 请求（代理模式下 Host 头指向真实目标）
    request = (
        f"GET {target_path} HTTP/1.1\r\n"
        f"Host: {target_host}\r\n"
        f"User-Agent: CaptureTest/1.0\r\n"
        f"Accept: text/html\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )

    print(f"发送请求 -> {target_host}{target_path}")
    sock.sendall(request.encode("utf-8"))

    # 接收响应
    response = b""
    while True:
        try:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk
        except socket.timeout:
            break

    sock.close()

    # 打印响应摘要
    text = response.decode("utf-8", errors="replace")
    status_line = text.split("\r\n")[0] if "\r\n" in text else text[:100]
    print(f"收到响应: {status_line}\n")


if __name__ == "__main__":
    PROXY = ("127.0.0.1", 9090)

    print("HTTP 抓包测试 - 请先运行 http_capture.py\n")

    # 测试 1: 请求 example.com
    print("--- 测试 1: GET example.com ---")
    send_via_proxy(*PROXY, "example.com", "/")

    # 测试 2: 请求 example.com 带路径
    print("--- 测试 2: GET example.com/test ---")
    send_via_proxy(*PROXY, "example.com", "/test?name=hello")

    # 测试 3: 请求 httpbin（如果可访问）
    # print("--- 测试 3: GET httpbin.org ---")
    # send_via_proxy(*PROXY, "httpbin.org", "/get")
