# HTTP 协议实现原理 - Python 实操

## 文件说明

| 文件 | 说明 |
|------|------|
| `http_protocol_demo.py` | HTTP 报文格式详解（纯本地，无需网络） |
| `http_server.py` | 手写 HTTP 服务器（基于 socket） |
| `http_client.py` | 手写 HTTP 客户端（基于 socket） |
| `http_capture.py` | HTTP 抓包代理工具 |
| `http_capture_test.py` | 配合抓包工具的测试脚本 |

## 使用顺序

### 1. 先看协议结构（无需网络）

```bash
python http_protocol_demo.py
```

展示 HTTP 请求/响应报文的逐字节解析，包括状态码、请求方法、连接生命周期。

### 2. 运行 HTTP 服务器

```bash
python http_server.py
# 浏览器访问 http://127.0.0.1:8080
```

### 3. 运行 HTTP 客户端

```bash
python http_client.py
```

### 4. 抓包分析（两个终端）

```bash
# 终端 1：启动抓包代理
python http_capture.py

# 终端 2：发送测试请求
python http_capture_test.py
```

## HTTP 协议核心要点

- HTTP 是基于 TCP 的应用层协议
- 报文格式：请求行/状态行 + 头部字段 + 空行 + 可选的 Body
- 默认端口 80（HTTP）/ 443（HTTPS）
- HTTP/1.0 短连接，HTTP/1.1 默认长连接，HTTP/2 多路复用
