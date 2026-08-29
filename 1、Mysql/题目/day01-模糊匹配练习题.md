# MySQL day01 模糊匹配（LIKE）实操练习

> 对应笔记：`1、Mysql/1、doc/day01.md` 最后的「模糊匹配（LIKE）」部分
> 先记住两个通配符：`%` 代表任意个字符（可以是 0 个），`_` 代表恰好 1 个字符

## 准备数据

先执行下面这段，建好练习用的表和测试数据：

```sql
create database if not exists mydb;
use mydb;

create table if not exists employee(
    id int,
    ename varchar(20)
);

insert into employee values
(1,'李冰'),
(2,'王冰冰'),
(3,'冰红茶'),
(4,'刘雨'),
(5,'张雨雨'),
(6,'李四'),
(7,'红孩儿'),
(8,'小红'),
(9,'李红'),
(10,'红'),
(11,'张三丰'),
(12,'李');
```

> 小技巧：每做完一题，先 `select * from employee;` 看看完整数据，再对照你的查询结果。

## 题目

### 1. 名字中包含「冰」字
查询名字里包含「冰」字的员工。

```sql
-- 你的答案
mysql> select * from employee where ename like '%冰%';
+----+--------+
| id | ename  |
+----+--------+
|  1 | 李冰   |
|  2 | 王冰冰 |
|  3 | 冰红茶 |
+----+--------+
3 rows in set (0.09 sec)

```

### 2. 名字以「雨」结尾
查询名字以「雨」结尾的员工。

```sql
mysql> select * from employee where ename like '%雨';
+----+--------+
| id | ename  |
+----+--------+
|  4 | 刘雨   |
|  5 | 张雨雨 |
+----+--------+
2 rows in set (0.11 sec)
```

### 3. 名字以「李」开头
查询名字以「李」开头的员工。

```sql
mysql> select * from employee where ename like '李%';
+----+-------+
| id | ename |
+----+-------+
|  1 | 李冰  |
|  6 | 李四  |
|  9 | 李红  |
| 12 | 李    |
+----+-------+
4 rows in set (0.08 sec)

```

### 4. 「红」前面只有一个字
查询名字中「红」字前面**只有一个字**的员工。

```sql
mysql> select * from employee where ename like '_红';
+----+-------+
| id | ename |
+----+-------+
|  8 | 小红  |
|  9 | 李红  |
+----+-------+
2 rows in set (0.11 sec)
```

### 5. 名字恰好两个字
查询名字恰好是**两个字**的员工。

```sql
mysql> select * from employee where ename like '__';
+----+-------+
| id | ename |
+----+-------+
|  1 | 李冰  |
|  4 | 刘雨  |
|  6 | 李四  |
|  8 | 小红  |
|  9 | 李红  |
+----+-------+
5 rows in set (0.08 sec)
```

### 6. 名字不以「李」开头
查询名字**不**以「李」开头的员工。

```sql
mysql> SELECT * FROM employee WHERE ename NOT LIKE '李%';
+----+--------+
| id | ename  |
+----+--------+
|  2 | 王冰冰 |
|  3 | 冰红茶 |
|  4 | 刘雨   |
|  5 | 张雨雨 |
|  7 | 红孩儿 |
|  8 | 小红   |
| 10 | 红     |
| 11 | 张三丰 |
+----+--------+
8 rows in set (0.09 sec)

```

### 7. 包含「冰」或「雨」
查询名字中包含「冰」**或者**「雨」的员工。

```sql

mysql> SELECT * FROM employee WHERE (ename LIKE '%冰%' OR ename LIKE '%雨%');
+----+--------+
| id | ename  |
+----+--------+
|  1 | 李冰   |
|  2 | 王冰冰 |
|  3 | 冰红茶 |
|  4 | 刘雨   |
|  5 | 张雨雨 |
+----+--------+
5 rows in set (0.11 sec)

```

### 8. 第二个字是「冰」
查询名字的**第二个字是「冰」**的员工。

```sql
mysql> SELECT * FROM employee WHERE ename LIKE '_冰%';
+----+--------+
| id | ename  |
+----+--------+
|  1 | 李冰   |
|  2 | 王冰冰 |
+----+--------+
2 rows in set (0.13 sec)
```

### 9. 李姓且只有两个字
查询姓「李」并且名字恰好**两个字**的员工。

```sql


mysql> SELECT * FROM employee WHERE ename LIKE '李_';
+----+-------+
| id | ename |
+----+-------+
|  1 | 李冰  |
|  6 | 李四  |
|  9 | 李红  |
+----+-------+
3 rows in set (0.10 sec)
```

### 10. 用模糊匹配查系统变量
查询当前 MySQL 中所有名字里带 `character` 的系统变量。

```sql
show variables like '%character%';
```

## 挑战题（选做）

如果名字里真的含有 `%` 或 `_` 这两个符号本身，直接把它们写在 like 里会被当成通配符。请写出：

1. 查询名字中包含下划线 `_` 的员工；
2. 查询名字中包含百分号 `%` 的员工。

> 你的答案：反引号？

## 📝 订正（第 4 题和挑战题）

### 第 4 题：`_红` 要改成 `_红%`
你写的 `_红` 在这份数据里结果碰巧对，但它要求「红是最后一个字」。题目只要求「红前面有 1 个字」，后面可以还有字，所以更严谨的写法是：

```sql
select * from employee where ename like '_红%';
```

### 挑战题：用 ESCAPE 转义，不是反引号
当 `_`、`%` 要当作普通字符时，用 `ESCAPE` 指定转义字符：

```sql
-- 查包含下划线 _ 的名字：! 是转义符，!_ 表示普通下划线
select * from employee where ename like '%!_%' escape '!';

-- 查包含百分号 % 的名字：!% 表示普通百分号
select * from employee where ename like '%!%%' escape '!';
```

> 可以自己插两条数据验证：`insert into employee values (13,'a_b'), (14,'a%b');`

> 第 10 题你已经自己改成 `show variables like '%character%';` 了，正确 ✅


