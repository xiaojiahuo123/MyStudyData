USE day01;

SELECT * FROM t_students;

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

SELECT * FROM t_emp WHERE id IN (1002,1003,1005);

SELECT * FROM t_emp WHERE gender IS NOT NULL;

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










-- 



-- String sql = "insert into t_emp(emp_id,emp_name) values('','')";
