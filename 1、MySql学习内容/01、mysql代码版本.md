### day1,创建数据库、数据表、增、删、改、查

```sql
-- windows登录mysql:mysql -u用户名   -p密码
insert -- 增加，插入数据   
delete -- 删除删除
update -- 更新、修改数据
---------------------------------------------------------------------------------------
-- 1. 创建数据库
CREATE DATABASE day01;

-- 2. 创建表
CREATE TABLE t_emp(
    id INT,
    name VARCHAR(100)
);

-- 3. 修改表结构（添加列）
ALTER TABLE t_emp ADD COLUMN salary DOUBLE(10,2);-- 增加一列，salary，数据类型需要是浮点型，10 表示 总长度（整数部分 + 小数部分，不含小数点本身）。2 表示 小数位数，99999999.99（整数部分最多 8 位 + 2 位小数）

ALTER TABLE 表名 MODIFY 字段名 新数据类型 [约束] [FIRST | AFTER 某字段];
-- 在 MySQL 中，使用 MODIFY 时，如果不写出原来的 NOT NULL、DEFAULT 等约束，这些约束会丢失，MODIFY 用于修改列定义，适用于Mysql
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  phone VARCHAR(15)
);
ALTER TABLE users MODIFY phone VARCHAR(20);-- phone 字段类型变为 VARCHAR(20)，原有约束（如果有）会被覆盖，需注意重新指定
ALTER TABLE users MODIFY phone VARCHAR(20) NOT NULL;-- 原来phone允许为空，现在要求不能为空
ALTER TABLE users MODIFY phone VARCHAR(20) AFTER name;-- 把 phone 移到 name 字段之后
ALTER TABLE users MODIFY phone VARCHAR(20) FIRST;-- 移到第一位
ALTER TABLE users MODIFY phone VARCHAR(20) DEFAULT 'N/A'; -- 给 phone 添加默认值 'N/A'
-- 大类型改为小类型（如 VARCHAR(100) 改成 VARCHAR(10)），现有数据超长会导致修改失败
-- 与 CHANGE 的区别：MODIFY 不能修改列名，如果要改列名需用 CHANGE
ALTER TABLE users CHANGE old_name new_name 新类型 ...;


-- 4. 删除表
DROP TABLE t_emp;

-- 5. 删除数据库
DROP DATABASE day01;
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

-- 1. 插入数据
INSERT INTO t_emp(id, name) VALUES(1001, 'zhangsan');

-- 2. 修改数据
UPDATE t_emp SET salary = 20000 WHERE id = 1001;
-- where是条件，语句的意思就是修改id为1001的字段，将salary改为20000

-- 3. 删除数据
DELETE FROM t_emp WHERE id = 1001; -- 删除表中的某个数据
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

-- 1. 查询所有数据
SELECT * FROM t_emp; -- 数据库中单表查询

-- 2. 查询指定列
SELECT id, name FROM t_emp; -- 这个 SQL 语句的作用是：直接查询 t_emp 表中所有行的 id 和 name 这两列数据。

-- 3. 带条件查询
SELECT * FROM t_emp WHERE salary > 10000;

-- 4. 排序查询
SELECT * FROM t_emp ORDER BY salary DESC;
-- ORDER BY 是 SQL 中用来 对查询结果进行排序 的一个子句
SELECT 列名 FROM 表名 ORDER BY 列名 [ASC|DESC]; -- ASC是升序，DESC是降序
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

#1. 授予权限
GRANT SELECT, INSERT ON t_emp TO 'user'@'localhost';
-- 授予用户 user（仅限从本机 localhost 登录）对表 t_emp 进行查询（SELECT）和插入（INSERT）操作的权限
#GRANT：授权关键字。
#SELECT, INSERT：被授予的具体权限。
#SELECT → 允许执行查询（读数据）。
#INSERT → 允许向表中插入新行。（未授予 UPDATE、DELETE 等，用户就只能查和插，无法修改或删除已有数据。）
-- 没有写数据库名（如 mydb.t_emp），此时 MySQL 会使用当前默认数据库。如果执行时未选择数据库，语句会报错。建议写成 数据库名.t_emp 更明确；'user'：用户名。'localhost'：允许连接的来源主机，此处限制只能从本机登录，远程无法使用该账户

#2. 撤销权限
REVOKE INSERT ON t_emp FROM 'user'@'localhost';

#3. 创建用户
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
-- DENTIFIED BY 'password' 设置登录密码为 password
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------


USE day01; -- 切换到day01数数据库

SELECT * FROM t_students; -- 单表查询，在数据库中查询t_students表

CREATE TABLE t_emp(
    id INT,
    NAME VARCHAR(100),
    gender VARCHAR(10),
    birthday DATE,
    salary DOUBLE(10,2),
    entry_date DATE,
    RESUME TEXT
);

SELECT * FROM t_emp;

-- DML(insert  delete  update)
-- 添加数据
INSERT INTO t_emp(id,`name`,gender,birthday,salary,entry_date,`resume`) 
VALUES(1001,'zhangsan','男','2000-01-01',15000,'2025-05-05','简历...');

-- 添加多条数据
INSERT INTO t_emp(id,`name`,gender,birthday,salary,entry_date,`resume`) 
VALUES(1002,'lisi','男','2000-01-01',15000,'2025-05-05','简历...'),
(1003,'wangwu','男','2000-01-01',15000,'2025-05-05','简历...'),
(1004,'zhaoliu','男','2000-01-01',15000,'2025-05-05','简历...'),
(1005,'jiahang','男','2000-01-01',10000,'2025-05-05','简历...'),
(1006,'xiaofei','男','2000-01-01',5000,'2025-05-05','简历...')

-- 修改语句(将晓飞薪资,更为为50000)
UPDATE t_emp SET salary = 20000,entry_date = '2024-01-01' WHERE `name` = 'xiaofei'; 
--WHERE 条件子句，限定只更新满足条件的行
--WHERE `name` = 'xiaofei' 这里的意思也就是只更新表t_emp中姓名为xiaofei的员工信息

DELETE FROM t_emp WHERE id = 1004;


-- DQL(select)
-- 单表普通查询
SELECT * FROM t_emp;

SELECT emp.id AS '员工编号',`name`,gender,birthday,salary,entry_date,`resume` FROM t_emp  emp;
-- AS '员工编号' 的作用：
-- 1. 美化输出 ：让查询结果更容易理解（中文列名），用户看到的是 员工编号 ，但实际查询的还是 id 列的数据
-- 2. 不影响数据 ：原始数据仍然存储在 id 列中
-- 3. 仅在查询时生效 ：别名只在本次查询结果中显示，不会修改表结构
-- 查询所有员工编号,员工姓名,员工薪资
SELECT id AS '员工编号',`name` '员工姓名',salary '员工薪资' FROM t_emp  emp;

-- 查询薪资在20000-40000之间员工信息
SELECT * FROM t_emp WHERE salary >= 20000 AND salary <= 40000;

SELECT * FROM t_emp WHERE salary BETWEEN 20000 AND 40000;
-- BETWEEN ... AND ... 运算符，判断一个值是否落在指定范围内（包含边界），这里等价于salary >= 20000 AND salary <= 40000，但是不能写成salary BETWEEN 40000 AND 20000

-- 查询2025-05-05入职女同志
SELECT * FROM t_emp WHERE entry_date = '2025-05-05' AND gender = '女';

SELECT * FROM t_emp WHERE entry_date = '2025-05-05' OR gender = '女';

-- 查询id=1002,1003,1005的员工信息
-- 1. 等选查询 ：查询多个值的行
-- 2. 包含查询 ：查询包含指定值的行
-- 3. 空值查询 ：查询空值的行
-- 4. 不等于查询 ：查询不等于指定值的行
-- 5. 包含查询 ：查询包含指定值的行
-- 6. 姍缀查询 ：查询以指定值开头的行
-- 7. 后缀查询 ：查询以指定值结尾的行
-- 8. 中间查询 ：查询包含指定值的行
SELECT * FROM t_emp WHERE id=1002 OR id=1003 OR id = 1005;
-- 查询多个值的行
SELECT * FROM t_emp WHERE id IN (1002,1003,1005);

SELECT * FROM t_emp WHERE gender IS NOT NULL;-- 查询年龄不为空的 IS NOT NULL

SELECT * FROM t_emp WHERE birthday = 'null';

-- 查询工资不等于40000的员工信息
SELECT * FROM t_emp WHERE salary != 40000;
SELECT * FROM t_emp WHERE salary <> 40000;

-- 查询员工姓名中包含i
SELECT * FROM t_emp WHERE `name` LIKE '%i%' ;

-- 查询员工姓名以'z'开头
SELECT * FROM t_emp WHERE `name` LIKE 'z%' ;
SELECT * FROM t_emp WHERE `name` LIKE 'z_' ;

-- 查询员工姓'张'的员工信息
SELECT * FROM t_emp WHERE `name` LIKE '张%' ;

-- String sql = "insert into t_emp(emp_id,emp_name) values('','')";

BETWHERE  AND 这是一个连续的范围， in 这是一个不连续的范围，但是 in 可以用来查询多个值
is null 判断空值  IN NOT NULL 判断非空值


- 通配符

  - _:匹配**单个任意**字符
  - %:匹配**n个(n>=0)任意**字符

- 案例
-- 查询员工姓名中包含i
SELECT * FROM t_emp WHERE `name` LIKE '%i%' ;

-- 查询员工姓名以'z'开头
SELECT * FROM t_emp WHERE `name` LIKE 'z%' ;
SELECT * FROM t_emp WHERE `name` LIKE 'z_' ;

-- 查询员工姓'张'的员工信息
SELECT * FROM t_emp WHERE `name` LIKE '张%' ;
```

### linux系统启动mysql服务

- 启动服务:systemctl  start  mysqld
- 关闭服务:systemctl  stop mysqld

### SQL模糊查询示例

!["E:\Code\MyStudyData\1、MySql学习内容\image\屏幕截图 2026-05-18 122423.png"](.\image\myImage20260519001.png)

MySql中的模糊查询，如'S_',是查询S开头的，后面有且仅有一个字符的内容。

### day2