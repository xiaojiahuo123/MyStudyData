"""
    该案例演示了python连接redis
"""
import redis

# 创建 Redis 连接对象
r = redis.Redis(
    host='192.168.10.150',  # Redis 服务器主机名
    port=6379,         # Redis 服务器端口号
    db=0               # 使用的数据库编号，默认为 0
)

# 设置一个字符串键值对
# r.set('my_key', 'Hello, Redis!')

# 从 Redis 中获取字符串值
value = r.get('my_key')
if value:
    print(value.decode('utf-8'))  # 解码为字符串
else:
    print('Key not found.')

print("~~~~~~~~~~~~~~~~~~~~~~")
"""


# 设置一个哈希键值对
r.hset('user:1', 'name', 'John')
r.hset('user:1', 'age', 30)

# 获取单个字段的值
name = r.hget('user:1', 'name')
if name:
    print(name.decode('utf-8'))

# 获取整个哈希的所有字段和值
user_info = r.hgetall('user:1')
for field, value in user_info.items():
    print(f'{field.decode("utf-8")}: {value.decode("utf-8")}')
print("~~~~~~~~~~~~~~~~~~~~~~")

# 向列表中添加元素
r.rpush('my_list', 'apple', 'banana', 'cherry')
# 获取列表中的元素
elements = r.lrange('my_list', 0, -1)  # 获取列表的所有元素
for element in elements:
    print(element.decode('utf-8'))
print("~~~~~~~~~~~~~~~~~~~~~~")

# 向集合中添加元素
r.sadd('my_set', 'red', 'green', 'blue')
# 获取集合中的所有元素
members = r.smembers('my_set')
for member in members:
    print(member.decode('utf-8'))
print("~~~~~~~~~~~~~~~~~~~~~~")

# 向有序集合中添加元素
r.zadd('my_sorted_set', {'apple': 1, 'banana': 2, 'cherry': 3})
# 获取有序集合中的元素
elements = r.zrange('my_sorted_set', 0, -1)
for element in elements:
    print(element.decode('utf-8'))
"""
