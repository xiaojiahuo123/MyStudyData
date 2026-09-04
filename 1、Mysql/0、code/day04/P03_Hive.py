"""
    该案例演示了python连接hive数据源
"""
from impala.dbapi import connect

# 建立与 Hive 的连接
conn = connect(
    host='192.168.10.150',
    port=10000,  # Impala 默认端口
    database='default',
    auth_mechanism='PLAIN'  # 认证方式，根据实际情况修改
)

# 创建游标对象
cursor = conn.cursor()

# 执行 SQL 查询语句
query = "SELECT * FROM stu LIMIT 10"
cursor.execute(query)

# 获取查询结果
results = cursor.fetchall()

# 打印查询结果
for row in results:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()
