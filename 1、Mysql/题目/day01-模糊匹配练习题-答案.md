# MySQL day01 模糊匹配（LIKE）实操练习 —— 答案版

> 配套题目：《day01-模糊匹配练习题.md》

## 准备数据（同题目版）

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

## 答案

### 1. 名字中包含「冰」字
```sql
select * from employee where ename like '%冰%';
```
结果：id 1、2、3（李冰、王冰冰、冰红茶）

### 2. 名字以「雨」结尾
```sql
select * from employee where ename like '%雨';
```
结果：id 4、5（刘雨、张雨雨）

### 3. 名字以「李」开头
```sql
select * from employee where ename like '李%';
```
结果：id 1、6、9、12（李冰、李四、李红、李）

### 4. 「红」前面只有一个字
```sql
select * from employee where ename like '_红%';
```
结果：id 8、9（小红、李红）
> 注意：`红` 和 `红孩儿` 不符合，因为红前面是 0 个字；`_` 要求恰好 1 个字。

### 5. 名字恰好两个字
```sql
select * from employee where ename like '__';
```
结果：id 1、4、6、8、9（李冰、刘雨、李四、小红、李红）

### 6. 名字不以「李」开头
```sql
select * from employee where ename not like '李%';
```
结果：id 2、3、4、5、7、8、10、11

### 7. 包含「冰」或「雨」
```sql
select * from employee where ename like '%冰%' or ename like '%雨%';
```
结果：id 1、2、3、4、5

### 8. 第二个字是「冰」
```sql
select * from employee where ename like '_冰%';
```
结果：id 1、2（李冰、王冰冰）
> 说明：`_` 先占 1 个字符，所以要求冰前面恰好有 1 个字。

### 9. 李姓且只有两个字
```sql
select * from employee where ename like '李_';
-- 也可以写成
select * from employee where ename like '李%' and ename like '__';
```
结果：id 1、6、9（李冰、李四、李红）

### 10. 用模糊匹配查系统变量
```sql
show variables like '%character%';
```
结果：所有名字里带 character 的变量（如 character_set_server 等）

## 挑战题答案

把 `%` 或 `_` 当普通字符时，要用 `ESCAPE` 指定一个转义字符：

```sql
-- 查包含下划线 _ 的名字：! 是转义符，!_ 表示普通下划线
select * from employee where ename like '%!_%' escape '!';

-- 查包含百分号 % 的名字：!% 表示普通百分号
select * from employee where ename like '%!%%' escape '!';
```

> 提示：本题的测试数据里没有带 `_` 或 `%` 的名字，你可以自己插入两条测试一下。
