"""
使用 http.client 发送 POST 请求获取 flag
与 01_post_manual.py 功能相同，但使用 Python 标准库
适合快速修改参数测试不同 CTF 题目
"""

import http.client

HOST = "124.221.18.25"
PORT = 15615


def get_flag():
    conn = http.client.HTTPConnection(HOST, PORT, timeout=10)

    # GET 参数通过路径传递: /?a=love
    # POST 参数通过 body 传递: b=ctf
    body = "b=ctf"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": str(len(body)),
    }

    try:
        conn.request("POST", "/?a=love", body=body, headers=headers)
        resp = conn.getresponse()

        print(f"[状态码] {resp.status} {resp.reason}")
        print(f"[响应头]")
        for key, val in resp.getheaders():
            print(f"  {key}: {val}")
        print(f"\n[响应体]")
        print(resp.read().decode("utf-8", errors="replace"))

    except Exception as e:
        print(f"[!] 错误: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    get_flag()
