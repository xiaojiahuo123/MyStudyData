"""
从 PostgreSQL 导出的 JSON 文件导入到 MySQL

用法:
  1. 先安装依赖: pip install pymysql
  2. 先执行建表 SQL:  mysql -u root -p < schema.sql
  3. 运行此脚本:    python import_data.py

连接参数通过环境变量配置（均有默认值）:
  DB_HOST=localhost
  DB_PORT=3306
  DB_USER=root
  DB_PASSWORD=
  DB_NAME=my_study_data
"""

import json
import os
import sys
from pathlib import Path

import pymysql

# ---- 连接配置 ----
DB_CONFIG = {
    "host":     os.getenv("DB_HOST", "localhost"),
    "port":     int(os.getenv("DB_PORT", 3306)),
    "user":     os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "my_study_data"),
    "charset":  "utf8mb4",
}

BASE_DIR = Path(__file__).resolve().parent

# 批量插入大小
BATCH_SIZE = 500

# ---- 辅助函数 ----
def json_val(obj):
    """将 Python 对象转为 MySQL JSON 字符串，None 返回 SQL NULL"""
    if obj is None:
        return None
    return json.dumps(obj, ensure_ascii=False)


def parse_datetime(val):
    """将 ISO 时间字符串转为 MySQL 可接受的格式，None 返回 NULL"""
    if val is None:
        return None
    # PostgreSQL 导出的格式: "2026-04-27T10:25:22.31846"，MySQL 可直接接受
    return val


def bool_to_int(val):
    """Python bool -> MySQL TINYINT"""
    if val is None:
        return None
    return 1 if val else 0


# ---- 表 -> (文件, 插入SQL) 映射 ----
TABLES = [
    {
        "name": "users",
        "file": "users.json",
        "columns": ["id","username","password_hash","role","display_name","email",
                     "is_active","created_at","updated_at"],
        "transform": lambda r: (
            r["id"], r["username"], r["password_hash"], r["role"],
            r.get("display_name"), r.get("email"),
            bool_to_int(r.get("is_active")),
            parse_datetime(r.get("created_at")),
            parse_datetime(r.get("updated_at")),
        ),
    },
    {
        "name": "devices",
        "file": "devices.json",
        "columns": ["id","device_name","device_type","device_sn","mqtt_topic",
                     "location","status","is_online","last_seen","created_at"],
        "transform": lambda r: (
            r["id"], r["device_name"], r["device_type"], r["device_sn"],
            r.get("mqtt_topic"), r.get("location"),
            json_val(r.get("status")),
            bool_to_int(r.get("is_online")),
            parse_datetime(r.get("last_seen")),
            parse_datetime(r.get("created_at")),
        ),
    },
    {
        "name": "documents",
        "file": "documents.json",
        "columns": ["id","title","description","file_key","file_name","file_size",
                     "file_type","uploaded_by","download_count","created_at","updated_at"],
        "transform": lambda r: (
            r["id"], r["title"], r.get("description"),
            r.get("file_key"), r.get("file_name"),
            r.get("file_size"), r.get("file_type"),
            r.get("uploaded_by"), r.get("download_count", 0),
            parse_datetime(r.get("created_at")),
            parse_datetime(r.get("updated_at")),
        ),
    },
    {
        "name": "study_records",
        "file": "study_records.json",
        "columns": ["id","user_id","title","content","created_at","updated_at"],
        "transform": lambda r: (
            r.get("id"), r.get("user_id"), r.get("title"), r.get("content"),
            parse_datetime(r.get("created_at")), parse_datetime(r.get("updated_at")),
        ),
    },
    {
        "name": "device_status_logs",
        "file": "device_status_logs.json",
        "columns": ["id","device_id","payload","recorded_at"],
        "transform": lambda r: (
            r["id"], r["device_id"],
            json_val(r.get("payload")),
            parse_datetime(r.get("recorded_at")),
        ),
    },
]


def insert_batch(cursor, table_name, columns, rows):
    placeholders = ", ".join(["%s"] * len(columns))
    col_names = ", ".join(columns)
    sql = f"INSERT INTO `{table_name}` ({col_names}) VALUES ({placeholders})"
    cursor.executemany(sql, rows)


def import_table(conn, table_info):
    name = table_info["name"]
    path = BASE_DIR / table_info["file"]
    transform = table_info["transform"]
    columns = table_info["columns"]

    if not path.exists():
        print(f"  [跳过] 文件不存在: {path.name}")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        print(f"  [跳过] 无数据: {path.name}")
        return

    rows = [transform(r) for r in data]

    with conn.cursor() as cur:
        for i in range(0, len(rows), BATCH_SIZE):
            batch = rows[i:i + BATCH_SIZE]
            insert_batch(cur, name, columns, batch)
        conn.commit()

    print(f"  [完成] {name}: 导入 {len(rows)} 条")


def main():
    print(f"连接 MySQL: {DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}")
    conn = pymysql.connect(**DB_CONFIG)

    try:
        for tbl in TABLES:
            import_table(conn, tbl)
        print("\n全部导入完成。")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
