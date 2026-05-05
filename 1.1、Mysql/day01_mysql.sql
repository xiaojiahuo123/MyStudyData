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

DELETE FROM t_emp WHERE id = 1004;


-- DQL(select)
-- 单表普通查询
SELECT * FROM t_emp;

SELECT emp.id AS '员工编号',`name`,gender,birthday,salary,entry_date,`resume` FROM t_emp  emp;
-- 查询所有员工编号,员工姓名,员工薪资
SELECT id AS '员工编号',`name` '员工姓名',salary '员工薪资' FROM t_emp  emp;

-- 查询薪资在20000-40000之间员工信息
SELECT * FROM t_emp WHERE salary >= 20000 AND salary <= 40000;

SELECT * FROM t_emp WHERE salary BETWEEN 20000 AND 40000;

-- 查询2025-05-05入职女同志
SELECT * FROM t_emp WHERE entry_date = '2025-05-05' AND gender = '女';

SELECT * FROM t_emp WHERE entry_date = '2025-05-05' OR gender = '女';

-- 查询id=1002,1003,1005的员工信息

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
