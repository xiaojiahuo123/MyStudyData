```sql
-- 查看所有的数据库
show databases;

-- 创建 atguigu 数据库
create database atguigu;

-- 使用 atguigudb 数据库
use atguigu;

-- 删除 atguigudb 数据库
drop database atguigu;

-- 创建表并避免有重名提前检查
create database if not exists atguigu;

-- 查看 atguigu 库的所有表格，要求前面有 use 语句
use atguigu;
show tables;
-- 或
show tables from atguigu;

-- 创建学生表，用逗号分割每个字段
create table student(
id int,
name varchar(20)
);

-- 查看表结构
desc student;

;
-- 添加两条记录到学生表中
insert into student values(1,'张三');
insert into student values(2,'李四');

-- 查看学生表数据
select * from student;

-- 删除学生表
drop table student;

-- 导入数据
source 需导入的sql文件路径;

-- 导出数据
mysqldump -u 用户名 -p 密码 数据库名 表名 > 脚本名.sql;
```

![]()![.\images\Snipaste_2026-07-30_20-47-18.png)