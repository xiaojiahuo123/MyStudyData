# MySQL day01 实操练习题

> 复习范围：`1、Mysql/0、code/day01/day01.md` 的基础语句，以及 `1、Mysql/1、doc/day01.md` 的 DDL、DML 和运算符内容。
> 使用建议：先把下面的题目自己写一遍，全部写完后，再对照《day01-实操练习题-答案.md》检查，不要提前偷看答案哦～

## 一、数据库（库）的基本操作

### 1. 查看所有数据库
写出查看当前 MySQL 服务器所有数据库的语句。

```sql
-- 在这里写你的 SQL
SHOW DATABASES;
-- 运行及如果如下
+--------------------+
| Database           |
+--------------------+
| atguigu            |
| day01              |
| information_schema |
| myemployees        |
| mysql              |
| mysqlstudy_001     |
| performance_schema |
| sys                |
| test               |
+--------------------+

```

### 2. 创建数据库
直接创建一个名为 `mydb` 的数据库。

```sql
mysql> create database if not exists mydb;
Query OK, 1 row affected (0.02 sec)

```

### 3. 使用数据库
进入（使用）`mydb` 数据库。

```sql
USE mydb;

```

### 4. 安全创建数据库
用 `if not exists` 再创建一次 `mydb`，要求库已存在时也不报错。

```sql
上面最开始创建的时候就是使用的 if not exists确保原本不存在数据据mydb

```

### 5. 查看建库语句
查看 `mydb` 数据库的创建语句。

```sql

show database mydb;
```

### 6. 修改库的字符集
把 `mydb` 库的字符集改为 `utf8mb4`，校对规则改为 `utf8mb4_general_ci`。

```sql
alter database mydb character set utf8mb4 collate utf8mb4_general_ci

```

### 7. 删除数据库
直接删除 `mydb` 数据库。

```sql
drop database mydb;

```

### 8. 安全删除数据库
用 `if exists` 删除 `mydb`，要求库不存在时也不报错。

```sql
drop database if not exists mydb;

```

## 二、表结构操作（DDL）

> 做第 9 题之前，请先执行：`create database mydb; use mydb;`

### 9. 创建学生表
创建 `student` 表，包含两个字段：`id int`、`name varchar(20)`。

```sql
mysql> create table student(id int,name varchar(20));
Query OK, 0 rows affected (0.05 sec)

```

### 10. 查看库里的所有表
分别用「先 use」和「不 use」两种方式，查看 `mydb` 库里的所有表。

```sql
好的，先use就是提前进入Mydb数据库
mysql> show tables from  mydb;
+----------------+
| Tables_in_mydb |
+----------------+
| student        |
+----------------+
1 row in set (0.04 sec)

mysql> 
```

### 11. 查看表结构
查看 `student` 表的结构。

```sql
mysql> desc student;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int         | YES  |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.04 sec)

```

### 12. 查看建表语句
查看 `student` 表的完整创建语句。

```sql
show create table student;

```

### 13. 创建多字段老师表
创建 `teacher` 表，字段如下表：

| 字段名 | 数据类型 |
|--------|----------|
| tid | int |
| tname | varchar(5) |
| salary | double |
| weight | double(5,2) |
| birthday | date |
| gender | enum('男','女') |
| blood | enum('A','B','AB','O') |
| tel | char(11) |

```sql
mysql> create table if not exists teacher(
    tid int,
    tname varchar(5),
    salary double,
    weight double(5,2),
    birthday date,
    gender enum('男','女'),
    blood enum('A','B','AB','O'),
    tel char(11)
);
Query OK, 0 rows affected (0.05 sec)

```

### 14. 在末尾添加字段
给 `teacher` 表在**末尾**添加字段 `email varchar(100)`。

```sql
mysql> alter table teacher add eamil varchar(20);
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

```

### 15. 在开头添加字段
给 `teacher` 表在**开头**添加字段 `create_time datetime`。

```sql
mysql> alter table teacher add create_time datetime first;
Query OK, 0 rows affected (0.09 sec)
Records: 0  Duplicates: 0  Warnings: 0

```

### 16. 在指定字段后添加字段
在 `tname` 字段**后面**添加 `age tinyint`。

```sql
mysql> alter table teacher add age tinyint after tname;
Query OK, 0 rows affected (0.07 sec)
Records: 0  Duplicates: 0  Warnings: 0


```

### 17. 删除字段
删除 `teacher` 表的 `weight` 字段。

```sql
alter tabl teacher drop weight;

```

### 18. 修改字段类型
把 `tel` 字段的类型从 `char(11)` 改为 `varchar(20)`。

```sql
mysql> alter table teacher moDIFy tel varchar(20);
Query OK, 0 rows affected (0.13 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

### 19. 修改字段名
把 `tname` 字段改名为 `name`，类型改为 `varchar(10)`。

```sql
mysql> alter table teacher change tname name varchar(10);
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

### 20. 移动字段位置
1) 把 `email` 字段移动到表开头；
2) 把 `email` 字段移动到 `name` 字段之后。

```sql

mysql> alter table teacher modify eamil varchar(20) first;
Query OK, 0 rows affected (1.15 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> alter table teacher modify eamil varchar(20) after name;
Query OK, 0 rows affected (0.13 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

### 21. 修改表名
把 `teacher` 表改名为 `teacher_info`。

```sql
mysql> alter table teacher rename teacher_info;
Query OK, 0 rows affected (0.28 sec)

```

### 22. 修改表的字符集
把 `teacher_info` 表的字符集改为 `utf8mb4`，校对规则改为 `utf8mb4_general_ci`。

```sql
mysql> alter table teacher_info character set utf8mb4 collate utf8mb4_general_ci;
Query OK, 0 rows affected (1.07 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

### 23. 删除表
1) 删除 `student` 表；
2) 用 `if exists` 安全删除 `teacher_info` 表。

```sql
mysql> drop table if exists student;
Query OK, 0 rows affected (0.41 sec)


mysql> drop table if exists teacher_info;
Query OK, 0 rows affected (0.03 sec)
```

## 三、数据增删改（DML）

> 做下面的题之前，先重建表并切换库：
> `create database mydb; use mydb;`
> `create table student(id int, name varchar(20));`

### 24. 插入两条记录
向 `student` 表插入两条记录：`(1,'张三')`、`(2,'李四')`。

```sql
mysql> insert into student values(1,'张三'),(2,'李四');
Query OK, 2 rows affected (0.62 sec)
Records: 2  Duplicates: 0  Warnings: 0
```

### 25. 一条语句插入多条记录
用**一条** `insert` 语句插入三条记录：`(3,'王五')`、`(4,'赵六')`、`(5,'孙七')`。

```sql
mysql> insert into student values(3,'王五'),(4,'赵六'),(5,'孙七');
Query OK, 3 rows affected (0.02 sec)
Records: 3  Duplicates: 0  Warnings: 0
```

### 26. 只插入指定字段
只给 `student` 表的 `id` 字段插入值 `6`。

```sql

mysql> insert into student(id) values(6);
Query OK, 1 row affected (0.01 sec)
```

### 27. 修改部分数据
把 `student` 表中 `id=1` 的记录的 `name` 改为 `张三丰`。

```sql
mysql> update student set name='张三丰' where id=1;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

### 28. 修改所有数据
把 `student` 表所有记录的 `name` 都改为 `同学`（不加 where）。

```sql
mysql> update student set name='同学';
Query OK, 6 rows affected (0.01 sec)
Rows matched: 6  Changed: 6  Warnings: 0
```

### 29. 删除指定数据
删除 `student` 表中 `id=2` 的记录。

```sql
mysql> delete from student where id=2;
Query OK, 1 row affected (0.02 sec)
```

### 30. 清空表数据（保留表结构）
删除 `student` 表所有数据，但保留表结构。

```sql
mysql> delete from student;
Query OK, 5 rows affected (0.01 sec)
```

### 31. 截断表
用 `truncate` 清空 `student` 表。

```sql

```

### 32. 简答：delete 与 truncate 的区别
写出 `delete from 表名` 和 `truncate 表名` 的主要区别（至少两点）。

> 你的答案：delete是一条一条删除数据，在事务中支持回滚，truncate是将原来的整个表删除再创建一张新的表，不支持回滚




## 四、查询（DQL）

### 33. 查询常量、表达式、函数
分别写出查询常量 `1`、表达式 `9/2`、当前时间函数 `now()` 的语句。

```sql
mysql> select 1;
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.08 sec)

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2026-08-29 14:41:26 |
+---------------------+
1 row in set (0.07 sec)
```

### 34. 查询所有字段
查看 `student` 表的所有数据。

```sql
#上面把这个表的数据清空了

mysql> select * from student;
Empty set
```

### 35. 查询指定字段
只查看 `teacher_info` 表的 `name` 和 `salary` 字段。

```sql


```

### 36. 条件查询
查询 `student` 表中 `id > 2` 的记录。

```sql


```

### 37. 使用别名
查询 `student` 表，把 `id` 显示为「编号」，把 `name` 显示为「姓名」。

```sql


```

## 五、运算符专项

### 38. 算术运算
写出以下表达式的查询语句，并在注释里写出结果：
`10+3`、`10-3`、`10*3`、`10/3`、`10 DIV 3`、`10%3`、`-10`

```sql


```

### 39. 比较运算
写出以下比较的查询语句，并写出结果：
`1=1`、`NULL<=>NULL`、`1!=2`、`1<2`、`5 BETWEEN 1 AND 10`、`'a' IN ('a','b')`

```sql


```

### 40. 逻辑运算
写出以下逻辑运算的查询语句，并写出结果：`1 AND 1`、`1 OR 0`、`NOT 1`、`1 XOR 0`

```sql


```

### 41. 位运算
写出以下位运算的查询语句，并写出结果：`5 & 3`、`5 | 3`、`5 ^ 3`、`~5`、`5 << 1`、`5 >> 1`

```sql


```

### 42. 运算符优先级排序
把下面的运算符按优先级**从高到低**排列：`+ -`、`AND`、`( )`、`NOT`、`* /`、`OR`、`:=`

> 你的答案：




## 六、导入与导出

### 43. 导入 SQL 文件
在 MySQL 客户端里导入一个本地 SQL 脚本文件（写出语句框架即可）。

```sql

source 假设名字是这个.sql
```

### 44. 导出数据
在操作系统命令行里，用 `mysqldump` 把 `mydb` 库的 `student` 表导出为 `student.sql`（写出命令框架即可）。

```bash
mysqldump -u root -p 123456 mydb student > student.sql

```

## 七、改错题

下面每条 SQL 都有问题，请指出错误并写出正确写法。

```sql
-- ① 找出错误
show table;

-- ② 找出错误
create table student(
id int
name varchar(20)
);
少了student 后的values，应该是 create table student values
-- ③ 找出错误
alter table teacher change name username;

-- ④ 陷阱题：这条语句会删除什么？
delete from student;#清空表student 中的所有数据
```

> 你的答案：
>
> ① 查看表的结构应该是desc ＋表名，如：desc teacher
>
> ② 少了student 后的values，应该是 create table student values
>
> ③ 最后面应该加上新的数据类型
>
> ④ 清空表student 中的所有数据
