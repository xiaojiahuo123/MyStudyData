"""
Session 存储后端实现
演示不同的 Session 存储方式：内存、文件、Redis（模拟）
"""
import json
import os
import time
import pickle
import threading
import secrets


# ==================== 1. 内存存储 ====================
class MemorySessionStore:
    """
    最简单的 Session 存储 - 内存字典
    优点：速度最快、实现简单
    缺点：服务器重启丢失、无法多机共享、内存泄漏风险
    适用：开发测试、单机小型应用
    """

    def __init__(self):
        self._store = {}
        self._lock = threading.Lock()  # 线程安全锁

    def set(self, session_id: str, data: dict, ttl: int = 3600):
        with self._lock:
            self._store[session_id] = {
                "data": data,
                "expires_at": time.time() + ttl,
            }

    def get(self, session_id: str) -> dict | None:
        with self._lock:
            entry = self._store.get(session_id)
            if not entry:
                return None
            if time.time() > entry["expires_at"]:
                del self._store[session_id]
                return None
            return entry["data"]

    def delete(self, session_id: str):
        with self._lock:
            self._store.pop(session_id, None)

    def cleanup(self) -> int:
        """清理过期 Session"""
        with self._lock:
            now = time.time()
            expired = [k for k, v in self._store.items() if now > v["expires_at"]]
            for k in expired:
                del self._store[k]
            return len(expired)

    def count(self) -> int:
        return len(self._store)


# ==================== 2. 文件存储 ====================
class FileSessionStore:
    """
    文件系统存储 - 每个 Session 一个文件
    优点：服务器重启不丢失、实现相对简单
    缺点：磁盘 IO 慢、文件锁竞争、目录文件数膨胀
    适用：单机应用、无 Redis 环境
    """

    def __init__(self, directory: str = "./sessions"):
        self._dir = directory
        os.makedirs(self._dir, exist_ok=True)

    def _path(self, session_id: str) -> str:
        # 安全：只允许十六进制字符，防止路径穿越
        safe_id = "".join(c for c in session_id if c in "0123456789abcdef")
        return os.path.join(self._dir, f"{safe_id}.json")

    def set(self, session_id: str, data: dict, ttl: int = 3600):
        entry = {"data": data, "expires_at": time.time() + ttl}
        with open(self._path(session_id), "w", encoding="utf-8") as f:
            json.dump(entry, f, ensure_ascii=False)

    def get(self, session_id: str) -> dict | None:
        path = self._path(session_id)
        if not os.path.exists(path):
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                entry = json.load(f)
            if time.time() > entry["expires_at"]:
                os.remove(path)
                return None
            return entry["data"]
        except (json.JSONDecodeError, KeyError):
            return None

    def delete(self, session_id: str):
        path = self._path(session_id)
        if os.path.exists(path):
            os.remove(path)

    def cleanup(self) -> int:
        count = 0
        now = time.time()
        for fname in os.listdir(self._dir):
            if fname.endswith(".json"):
                path = os.path.join(self._dir, fname)
                try:
                    with open(path, "r") as f:
                        entry = json.load(f)
                    if now > entry["expires_at"]:
                        os.remove(path)
                        count += 1
                except Exception:
                    pass
        return count

    def count(self) -> int:
        return len([f for f in os.listdir(self._dir) if f.endswith(".json")])


# ==================== 3. Redis 模拟存储 ====================
class RedisSessionStore:
    """
    Redis 存储（模拟实现，展示接口设计）
    优点：高性能、支持 TTL 自动过期、支持多机共享、支持持久化
    缺点：需要额外部署 Redis 服务
    适用：生产环境、分布式系统

    实际生产环境使用:
        import redis
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.setex(f"session:{sid}", 3600, json.dumps(data))
    """

    def __init__(self):
        # 模拟 Redis 的数据结构
        self._store = {}       # key -> value
        self._ttls = {}        # key -> expire_timestamp
        self._lock = threading.Lock()

    def set(self, session_id: str, data: dict, ttl: int = 3600):
        """SETEX key ttl value"""
        key = f"session:{session_id}"
        with self._lock:
            self._store[key] = json.dumps(data)
            self._ttls[key] = time.time() + ttl

    def get(self, session_id: str) -> dict | None:
        """GET key"""
        key = f"session:{session_id}"
        with self._lock:
            if key not in self._store:
                return None
            if time.time() > self._ttls.get(key, 0):
                del self._store[key]
                del self._ttls[key]
                return None
            return json.loads(self._store[key])

    def delete(self, session_id: str):
        """DEL key"""
        key = f"session:{session_id}"
        with self._lock:
            self._store.pop(key, None)
            self._ttls.pop(key, None)

    def extend(self, session_id: str, ttl: int = 3600):
        """EXPIRE key ttl - 续期"""
        key = f"session:{session_id}"
        with self._lock:
            if key in self._store:
                self._ttls[key] = time.time() + ttl

    def count(self) -> int:
        return len(self._store)

    def cleanup(self) -> int:
        """Redis 自动过期，这里手动模拟"""
        with self._lock:
            now = time.time()
            expired = [k for k, t in self._ttls.items() if now > t]
            for k in expired:
                del self._store[k]
                del self._ttls[k]
            return len(expired)


# ==================== 统一接口 + 演示 ====================
class SessionManager:
    """统一的 Session 管理器，可切换不同的存储后端"""

    def __init__(self, store, prefix: str = ""):
        self.store = store
        self.prefix = prefix

    def create(self, data: dict = None, ttl: int = 3600) -> str:
        session_id = secrets.token_hex(32)
        self.store.set(session_id, data or {}, ttl)
        return session_id

    def get(self, session_id: str) -> dict | None:
        return self.store.get(session_id)

    def update(self, session_id: str, data: dict):
        existing = self.store.get(session_id)
        if existing:
            existing.update(data)
            self.store.set(session_id, existing)

    def destroy(self, session_id: str):
        self.store.delete(session_id)


def demo_store(name: str, store):
    """演示单个存储后端"""
    print(f"\n  [{name}]")

    manager = SessionManager(store)

    # 创建
    sid = manager.create({"username": "admin", "role": "admin"}, ttl=2)
    print(f"    创建: {sid[:16]}...")

    # 读取
    data = manager.get(sid)
    print(f"    读取: {data}")

    # 更新
    manager.update(sid, {"last_page": "/dashboard"})
    data = manager.get(sid)
    print(f"    更新: {data}")

    # 过期测试
    print(f"    等待 TTL 过期 (2秒)...")
    time.sleep(2.1)
    data = manager.get(sid)
    print(f"    过期后读取: {data}")

    # 清理
    for i in range(3):
        manager.create({"user": f"test_{i}"}, ttl=0)
    time.sleep(0.1)
    if hasattr(store, 'cleanup'):
        count = store.cleanup()
        print(f"    清理过期: {count} 个")


if __name__ == "__main__":
    print("=" * 60)
    print("  Session 存储后端对比演示")
    print("=" * 60)

    demo_store("内存存储", MemorySessionStore())

    # 文件存储（用完清理）
    file_store = FileSessionStore("./_temp_sessions")
    demo_store("文件存储", file_store)
    # 清理临时目录
    import shutil
    if os.path.exists("./_temp_sessions"):
        shutil.rmtree("./_temp_sessions")

    demo_store("Redis 模拟存储", RedisSessionStore())

    print("\n\n" + "=" * 60)
    print("  存储后端选型建议")
    print("=" * 60)
    print("""
    场景                        推荐方案
    ──────────────────────────────────────────────
    本地开发/测试               内存存储
    单机生产环境                文件存储 或 SQLite
    多机/分布式环境             Redis（首选）
    高可用要求                  Redis Cluster / 数据库
    无状态/微服务               JWT（不需要服务端存储）
    """)
