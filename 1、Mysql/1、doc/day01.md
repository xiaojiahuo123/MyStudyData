#### DDL数据定义语言

##### 基础语句

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

![](.\images\Snipaste_2026-07-30_20-47-18.png)

新建表需要先添加对应的字段之后，在点击保存，为表命名

##### navicat导出数据表

![]()![Snipaste\_2026-07-30\_20-51-26](.\images\Snipaste_2026-07-30_20-51-26.png)

##### Navicat导出数据库

![](.\images\Snipaste_2026-07-30_20-51-36.png)

##### 修改库编码格式

```sql
alter database 数据库名 character set 字符集名称 collate 字符集对应校对规则;
-- 例如
alter database db01 character set utf8 collate utf8_general_ci;
```

##### 删除库

```sql
drop database 数据库名;
-- drop database test;

-- 删除数据库
drop database if exists atguigu;

-- 查看数据库的创建语句
show create database atguigu;
```

##### 数据表相关

###### 创建表

```sql
create table [if not exists] 表名(
字段名 数据类型, 字段名 数据类型
);

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

-- 查看表的详细定义
show create table teacher;
```

###### 修改表编码

```sql
alter table teacher character set 字符集 collate 校对规则;
-- 例如(character:字符集)
alter table teacher character set utf8mb4 collate utf8mb4_general_ci;
```

###### 修改表的字段-添加字段

```sql
alter table 表名 add 字段名 数据类型; -- 在表末尾添加字段
alter table 表名 add 字段名 数据类型 first; -- 在表开头添加字段
alter table 表名 add 字段名 数据类型 after 另一个字段; -- 在另一个字段后添加
字段
```

###### 删除表字段

```sql
alter table 表名 drop 字段名;
```

###### 修改字段数据类型

```sql
alter table 表名 modify 字段名 新的数据类型;

-- 例：将 name 字段从 varchar(20) 改为 varchar(50)
alter table teacher modify name varchar(50);

-- 例：将 age 字段从 int 改为 tinyint
alter table teacher modify age tinyint;

-- 例：修改字段时同时添加约束
alter table teacher modify email varchar(100) not null;
```

###### 修改字段名

```sql
alter table 表名 change 旧字段名 新字段名 新的数据类型;

-- 例：将 name 字段改名为 username，类型改为 varchar(50)
alter table teacher change name username varchar(50);

-- 例：只改名不改类型（类型必须写，否则报错）
alter table teacher change age age_new int;
```

###### 修改字段位置

```sql
alter table 表名 modify 字段名 数据类型 first; -- 将字段移动到表的开头
alter table 表名 modify 字段名 数据类型 after 另一个字段; -- 将字段移动到表的
另一个字段之后

-- 例：将 email 字段移动到表开头
alter table teacher modify email varchar(100) first;

-- 例：将 email 字段移动到 name 字段之后
alter table teacher modify email varchar(100) after name;
```

###### 修改表名

```sql
alter table 旧表名 rename 新表名;
-- 或者
rename table 旧表名 to 新表名;

-- 例：将 teacher 表改名为 teacher_info
alter table teacher rename teacher_info;

-- 例：使用 rename table 方式
rename table teacher_info to teacher;
```

###### 删除表

```sql
drop table [if exists] 表名;

-- 例：删除 teacher 表
drop table teacher;

-- 例：安全删除（表不存在也不会报错）
drop table if exists teacher;
```

#### DML数据操纵语言

##### 添加

```sql
insert into 表名(字段列表) values(值列表),(值列表),(值列表); 
-- 值列表中的值的顺序、类型、个数必须与字段列表一一对应,示例：

insert into StudyDML values(1,'第一条数据');#主要是要和表的结构一致

-- 插入多条数据
insert into teacher values
(3,'王五','男','1990-01-01',10000,'12345678901'),
(4,'赵六','男','1990-01-01',10000,'12345678901'),
(5,'孙七','男','1990-01-01',10000,'12345678901');

-- 只插入选中的字段
insert into teacher(id,name) values(6,'周八'),(7,'吴九'),(8,'郑十');
```

##### 删除

```sql
#删除多条数据
delete from 表名 where 条件;

-- 示例：删除 id 为 3 的老师
delete from teacher where id = 3;

-- 示例：删除名字为 '李四' 的老师
delete from teacher where name = '李四';

-- 示例：删除工资大于 8000 的老师
delete from teacher where salary > 8000;


#删除所有数据(只保留表的结构)
delete from 表名;

-- 示例：清空 teacher 表所有数据（表结构保留）
delete from teacher;

#截断表
truncate 表名;
```

***delete 是一条一条删除记录的。如果在事务中，事务提交之前支持回滚***

***truncate 是把整个表 drop，新建一张，效率更高。就算在事务中，也无法回滚***

##### 修改

###### 修改部分行的数据

```sql
update 表名 set 字段名 = 值, 字段名 = 值 where 条件; -- 修改满足条件的行
```

###### 修改所有行数据

```sql
update 表名 set 字段名 = 值, 字段名 = 值;-- 修改所有行
```

##### 查询

###### select语句

select 语句是用于查看计算结果、或者查看从数据表中筛选出的数据的。

```sql
select 常量;
select 表达式;
select 函数;
#例如
select 1;
select 9/2;
select now();
```

如果要从数据表中筛选数据，需要加 **from 子句**。`from` 指定数据来源。`字段列表`筛选列。

```sql
select 字段列表 from 表名;
```

如果要从数据表中根据条件筛选数据，需要加 `from` 和 `where` 子句。`where` 筛选行。

```sql
select 字段列表 from 表名 where 条件;
```

使用别名

```sql
select 字段列表 as 别名 from where 条件;
-- 例如
select id as 编号,name "姓 名" from teacher;
```

#### MySQL 运算符汇总

##### 算术运算符

| 运算符 | 含义 | 示例 | 结果 |
|--------|------|------|------|
| `+` | 加法 | `SELECT 10 + 3;` | 13 |
| `-` | 减法 | `SELECT 10 - 3;` | 7 |
| `*` | 乘法 | `SELECT 10 * 3;` | 30 |
| `/` | 除法 | `SELECT 10 / 3;` | 3.3333 |
| `DIV` | 整除 | `SELECT 10 DIV 3;` | 3 |
| `%` 或 `MOD` | 取余 | `SELECT 10 % 3;` | 1 |
| `-`（一元） | 负号 | `SELECT -10;` | -10 |

##### 比较运算符

| 运算符 | 含义 | 示例 | 结果 |
|--------|------|------|------|
| `=` | 等于 | `SELECT 1 = 1;` | 1（真） |
| `<=>` | 安全等于（可比较NULL） | `SELECT NULL <=> NULL;` | 1 |
| `!=` 或 `<>` | 不等于 | `SELECT 1 != 2;` | 1 |
| `<` | 小于 | `SELECT 1 < 2;` | 1 |
| `<=` | 小于等于 | `SELECT 1 <= 2;` | 1 |
| `>` | 大于 | `SELECT 2 > 1;` | 1 |
| `>=` | 大于等于 | `SELECT 2 >= 1;` | 1 |
| `IS NULL` | 是否为空 | `SELECT name IS NULL FROM t;` | 1/0 |
| `IS NOT NULL` | 是否非空 | `SELECT name IS NOT NULL FROM t;` | 1/0 |
| `BETWEEN AND` | 在范围内 | `SELECT 5 BETWEEN 1 AND 10;` | 1 |
| `IN` | 在列表中 | `SELECT 'a' IN ('a','b');` | 1 |
| `NOT IN` | 不在列表中 | `SELECT 'c' NOT IN ('a','b');` | 1 |
| `LIKE` | 模糊匹配 | `SELECT name LIKE '张%';` | 1/0 |
| `REGEXP` | 正则匹配 | `SELECT 'abc' REGEXP '^a';` | 1 |

##### 逻辑运算符

| 运算符 | 含义 | 示例 | 结果 |
|--------|------|------|------|
| `AND` 或 `&&` | 逻辑与 | `SELECT 1 AND 1;` | 1 |
| `OR` 或 `\|\|` | 逻辑或 | `SELECT 1 OR 0;` | 1 |
| `NOT` 或 `!` | 逻辑非 | `SELECT NOT 1;` | 0 |
| `XOR` | 逻辑异或 | `SELECT 1 XOR 0;` | 1 |

##### 位运算符

| 运算符 | 含义 | 示例 | 结果 |
|--------|------|------|------|
| `&` | 按位与 | `SELECT 5 & 3;` | 1 |
| `\|` | 按位或 | `SELECT 5 \| 3;` | 7 |
| `^` | 按位异或 | `SELECT 5 ^ 3;` | 6 |
| `~` | 按位取反 | `SELECT ~5;` | -6 |
| `<<` | 左移 | `SELECT 5 << 1;` | 10 |
| `>>` | 右移 | `SELECT 5 >> 1;` | 2 |

##### 赋值运算符

| 运算符 | 含义 | 示例 |
|--------|------|------|
| `=` | 赋值（SET中） | `SET @x = 10;` |
| `:=` | 赋值（SELECT中） | `SELECT @x := 10;` |

##### 运算符优先级（高到低）

```
1. 括号 ( )
2. 一元运算符 - ! ~
3. * / DIV % MOD
4. + -
5. << >>
6. = <=> < <= > >= != <> IS LIKE REGEXP IN
7. BETWEEN AND CASE WHEN THEN ELSE
8. NOT
9. AND &&
10. XOR
11. OR ||
12. :=
```
