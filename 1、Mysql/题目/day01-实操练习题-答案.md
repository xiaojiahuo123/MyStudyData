# MySQL day01 实操练习题 —— 答案版

> 配套题目：《day01-实操练习题.md》
> 答案仅供参考，SQL 大小写不敏感，能跑通、结果正确即可。

## 一、数据库（库）的基本操作

### 1. 查看所有数据库
```sql
-- 查看所有的数据库
show databases;
```

### 2. 创建数据库
```sql
-- 创建 mydb 数据库
create database mydb;
```

### 3. 使用数据库
```sql
-- 使用 mydb 数据库
use mydb;
```

### 4. 安全创建数据库
```sql
-- 库已存在时不会报错
create database if not exists mydb;
```

### 5. 查看建库语句
```sql
show create database mydb;
```

### 6. 修改库的字符集
```sql
alter database mydb character set utf8mb4 collate utf8mb4_general_ci;
```

### 7. 删除数据库
```sql
drop database mydb;
```

### 8. 安全删除数据库
```sql
drop database if exists mydb;
```

## 二、表结构操作（DDL）

### 9. 创建学生表
```sql
create table student(
id int,
name varchar(20)
);
```

### 10. 查看库里的所有表
```sql
-- 方式一：先 use，再 show tables
use mydb;
show tables;

-- 方式二：直接 from 指定库
show tables from mydb;
```

### 11. 查看表结构
```sql
desc student;
```

### 12. 查看建表语句
```sql
show create table student;
```

### 13. 创建多字段老师表
```sql
create table teacher(
tid int,
tname varchar(5),
salary double,
weight double(5,2),
birthday date,
gender enum('男','女'),
blood enum('A','B','AB','O'),
tel char(11)
);
```

### 14. 在末尾添加字段
```sql
-- 默认就在表末尾添加
alter table teacher add email varchar(100);
```

### 15. 在开头添加字段
```sql
alter table teacher add create_time datetime first;
```

### 16. 在指定字段后添加字段
```sql
alter table teacher add age tinyint after tname;
```

### 17. 删除字段
```sql
alter table teacher drop weight;
```

### 18. 修改字段类型
```sql
alter table teacher modify tel varchar(20);
```

### 19. 修改字段名
```sql
-- change 旧字段名 新字段名 新类型；类型必须写
alter table teacher change tname name varchar(10);
```

### 20. 移动字段位置
```sql
-- 移到表开头
alter table teacher modify email varchar(100) first;

-- 移到 name 之后
alter table teacher modify email varchar(100) after name;
```

### 21. 修改表名
```sql
alter table teacher rename teacher_info;
-- 或
rename table teacher to teacher_info;
```

### 22. 修改表的字符集
```sql
alter table teacher_info character set utf8mb4 collate utf8mb4_general_ci;
```

### 23. 删除表
```sql
drop table student;

-- 安全删除，表不存在也不报错
drop table if exists teacher_info;
```

## 三、数据增删改（DML）

### 24. 插入两条记录
```sql
insert into student values(1,'张三');
insert into student values(2,'李四');
```

### 25. 一条语句插入多条记录
```sql
insert into student values
(3,'王五'),
(4,'赵六'),
(5,'孙七');
```

### 26. 只插入指定字段
```sql
-- 只插入 id，name 会为 null
insert into student(id) values(6);
```

### 27. 修改部分数据
```sql
update student set name = '张三丰' where id = 1;
```

### 28. 修改所有数据
```sql
-- 没有 where，会修改所有行
update student set name = '同学';
```

### 29. 删除指定数据
```sql
delete from student where id = 2;
```

### 30. 清空表数据（保留表结构）
```sql
delete from student;
```

### 31. 截断表
```sql
truncate student;
```

### 32. delete 与 truncate 的区别
- `delete` 是一条一条删除记录，效率较低；在事务中提交前可以回滚。
- `truncate` 相当于 drop 掉整张表再新建，效率更高；在事务中也不能回滚。
- 两者都会清空数据、保留表结构。

## 四、查询（DQL）

### 33. 查询常量、表达式、函数
```sql
select 1;      -- 结果 1
select 9/2;    -- 结果 4.5000
select now();  -- 结果 当前日期时间
```

### 34. 查询所有字段
```sql
select * from student;
```

### 35. 查询指定字段
```sql
select name, salary from teacher_info;
```

### 36. 条件查询
```sql
select * from student where id > 2;
```

### 37. 使用别名
```sql
select id as 编号, name as 姓名 from student;
-- 中文别名加不加引号都行；带空格要用引号
-- select id as 编号, name "姓 名" from student;
```

## 五、运算符专项

### 38. 算术运算
```sql
select 10+3;      -- 13
select 10-3;      -- 7
select 10*3;      -- 30
select 10/3;      -- 3.3333
select 10 div 3;  -- 3
select 10%3;      -- 1
select -10;       -- -10
```

### 39. 比较运算
```sql
select 1=1;                 -- 1
select null<=>null;         -- 1
select 1!=2;                -- 1
select 1<2;                 -- 1
select 5 between 1 and 10;  -- 1
select 'a' in ('a','b');    -- 1
```

### 40. 逻辑运算
```sql
select 1 and 1;   -- 1
select 1 or 0;    -- 1
select not 1;     -- 0
select 1 xor 0;   -- 1
```

### 41. 位运算
```sql
select 5 & 3;   -- 1
select 5 | 3;   -- 7
select 5 ^ 3;   -- 6
select ~5;      -- -6
select 5 << 1;  -- 10
select 5 >> 1;  -- 2
```

### 42. 运算符优先级排序
从高到低：`( )` > `* /` > `+ -` > `NOT` > `AND` > `OR` > `:=`

## 六、导入与导出

### 43. 导入 SQL 文件
```sql
source D:/data/student.sql;
```

### 44. 导出数据
```bash
mysqldump -u root -p mydb student > student.sql;
```
> 注意：`-p` 后可以不直接写密码，回车后再输入更安全；路径带空格时用引号包起来。

## 七、改错题

① `show table;`
错误：少了复数 `s`，应为 `show tables;`。

② create table 中两个字段之间少了逗号，应为：
```sql
create table student(
id int,
name varchar(20)
);
```

③ `alter table teacher change name username;`
错误：`change` 必须同时写新数据类型，应为：
```sql
alter table teacher change name username varchar(10);
```

④ `delete from student;`
这不是语法错误，但会删除 `student` 表**所有数据**，只保留表结构。执行前要确认是否真的想清空。
