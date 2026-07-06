"""
HTTP 抓包分析工具 - 抓取并分析 HTTP 协议的原始报文
通过在本地搭建代理服务器，拦截并展示 HTTP 请求和响应的完整报文
"""
import socket
import threading
import datetime


class HTTPCapture:
    """
    HTTP 抓包代理 - 监听本地端口，拦截 HTTP 流量并打印原始报文
    原理：
    1. 在本地启动一个 TCP 服务器（代理）
    2. 客户端连接到代理，发送 HTTP 请求
    3. 代理读取请求，打印原始报文
    4. 代理将请求转发给真实服务器
    5. 代理读取响应，打印原始报文
    6. 代理将响应返回给客户端
    """

    def __init__(self, listen_host="127.0.0.1", listen_port=9090):
        self.listen_host = listen_host
        self.listen_port = listen_port
        self.request_count = 0

    def _parse_host_from_request(self, raw_data: bytes) -> tuple:
        """从 HTTP 请求中提取目标主机和端口"""
        text = raw_data.decode("utf-8", errors="replace")
        for line in text.split("\r\n"):
            if line.lower().startswith("host:"):
                host_value = line.split(":", 1)[1].strip()
                if ":" in host_value:
                    host, port = host_value.rsplit(":", 1)
                    return host, int(port)
                return host_value, 80
        return None, None

    def _print_raw(self, title: str, data: bytes):
        """打印原始报文（十六进制 + ASCII 双栏对照）"""
        print(f"\n{'='*70}")
        print(f"  {title}")
        print(f"  ({len(data)} 字节)")
        print(f"{'='*70}")

        # 打印可读文本
        try:
            text = data.decode("utf-8", errors="replace")
            # 只打印头部（不含 body），避免输出太长
            if "\r\n\r\n" in text:
                header, body = text.split("\r\n\r\n", 1)
                print(header)
                print()
                print(f"  [请求体/响应体: {len(body)} 字符]")
                if len(body) < 500:
                    print(body)
                else:
                    print(body[:500] + "...")
            else:
                print(text)
        except:
            print(f"  (无法解码为文本，原始字节: {data[:100]}...)")

        print(f"{'='*70}")

    def _forward_data(self, src: socket.socket, dst: socket.socket,
                      direction: str, capture: bool = True) -> bytes:
        """转发数据，可选是否抓取"""
        data = b""
        while True:
            try:
                chunk = src.recv(8192)
                if not chunk:
                    break
                data += chunk
                dst.sendall(chunk)
            except Exception:
                break
        return data

    def _handle_client(self, client_socket: socket.socket, client_addr):
        """处理单个客户端连接"""
        self.request_count += 1
        req_id = self.request_count

        try:
            # 1. 读取客户端发来的 HTTP 请求
            request_data = client_socket.recv(8192)
            if not request_data:
                return

            # 2. 打印抓到的请求报文
            self._print_raw(
                f"[#{req_id}] 请求  {client_addr[0]}:{client_addr[1]} -> 服务器",
                request_data
            )

            # 3. 从请求中解析目标主机
            target_host, target_port = self._parse_host_from_request(request_data)
            if not target_host:
                print(f"[#{req_id}] 无法解析目标主机，丢弃")
                return

            print(f"[#{req_id}] 目标: {target_host}:{target_port}")

            # 4. 连接真实目标服务器
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.settimeout(10)
            server_socket.connect((target_host, target_port))

            # 5. 转发请求到服务器
            server_socket.sendall(request_data)

            # 6. 接收服务器响应
            response_data = b""
            while True:
                try:
                    chunk = server_socket.recv(8192)
                    if not chunk:
                        break
                    response_data += chunk
                    client_socket.sendall(chunk)
                except socket.timeout:
                    break

            server_socket.close()

            # 7. 打印抓到的响应报文
            if response_data:
                self._print_raw(
                    f"[#{req_id}] 响应  服务器 -> {client_addr[0]}:{client_addr[1]}",
                    response_data
                )

        except Exception as e:
            print(f"[#{req_id}] 错误: {e}")
        finally:
            client_socket.close()
            print(f"[#{req_id}] 连接结束\n")

    def start(self):
        """启动抓包代理"""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.listen_host, self.listen_port))
        server.listen(10)

        print(f"HTTP 抓包代理已启动")
        print(f"监听地址: {self.listen_host}:{self.listen_port}")
        print(f"使用方法:")
        print(f"  1. 修改浏览器代理设置为 {self.listen_host}:{self.listen_port}")
        print(f"  2. 或者用 curl: curl -x {self.listen_host}:{self.listen_port} http://example.com")
        print(f"  3. 或者运行本目录下的 http_capture_test.py")
        print(f"\n等待流量中... (Ctrl+C 停止)\n")

        try:
            while True:
                client_socket, addr = server.accept()
                thread = threading.Thread(
                    target=self._handle_client,
                    args=(client_socket, addr)
                )
                thread.daemon = True
                thread.start()
        except KeyboardInterrupt:
            print(f"\n\n抓包结束，共抓取 {self.request_count} 个请求")
        finally:
            server.close()


if __name__ == "__main__":
    capture = HTTPCapture(listen_host="127.0.0.1", listen_port=9090)
    capture.start()
