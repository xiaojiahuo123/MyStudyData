"""
    该案例演示了python操作MySQL数据库
"""
import pymysql
# 获取连接
def get_connection():
    try:
        conn = pymysql.connect(
            host='192.168.10.150',
            port=3306,
            user='root',
            password='123456',
            database='atguigu',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except:
        print("获取连接的时候发生了异常")

# 从数据库表中查询数据
def select_data(conn):
    # 创建游标对象
    my_cursor = conn.cursor()

    # 执行sql语句
    sql = "select * from t_department"
    my_cursor.execute(sql)

    # 获取查询结果
    results = my_cursor.fetchall()

    for row in results:
        print(row)
    my_cursor.close()

def insert_data(conn):
    my_c = conn.cursor()
    sql = "insert into t_department values (10,'test','testtest')"
    my_c.execute(sql)
    # 提交事务
    conn.commit()
    my_c.close()

def delete_data(conn):
    my_c = conn.cursor()
    sql = "delete from t_department where did=10"
    my_c.execute(sql)
    # 提交事务
    conn.commit()
    my_c.close()

def update_data(conn):
    my_c = conn.cursor()
    sql = "update t_department set dname='dev' where did=10"
    my_c.execute(sql)
    # 提交事务
    conn.commit()
    my_c.close()

if __name__ == '__main__':
    conn = get_connection()
    # insert_data(conn)
    # update_data(conn)
    delete_data(conn)
    select_data(conn)
    conn.close()