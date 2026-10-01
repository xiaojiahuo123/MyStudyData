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
mysqldump -u root -p 密码 mydb student > D:\backup\student.sql
# 一般来说文件夹的路径可能会包含空格，所以最好用双引号包裹路径：
mysqldump -u root -p123456 mydb student > "D:\My Backup Files\student.sql"
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
alter table 旧表名 rename 新表名; #注意是rename 不是rname
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

##### 模糊匹配（LIKE）

- `%` 代表任意个字符
- `_` 代表1个字符，如果2个下划线就代表2个字符

```sql
use atguigu;

-- 查询名字有 冰 字的
select * from t_employee where ename like '%冰%';

-- 查询名字以 雨 结尾的
select * from t_employee where ename like '%雨';

-- 查询名字以 李 开头的
select * from t_employee where ename like '李%';

-- 查询名字有 红 这个字，但是 红 的前面只能有1个字
select * from t_employee where ename like '_红%';

-- 查询当前MySQL数据库的字符集情况
show variables like '%character%';
```

#### 数据类型

##### 数值类型

###### 整数类型

| 类型 | 字节数 | 有符号范围 | 无符号范围 |
|------|--------|-----------|-----------|
| TINYINT | 1 | -128 ~ 127 | 0 ~ 255 |
| SMALLINT | 2 | -32768 ~ 32767 | 0 ~ 65535 |
| MEDIUMINT | 3 | -8388608 ~ 8388607 | 0 ~ 16777215 |
| INT | 4 | -2147483648 ~ 2147483647 | 0 ~ 4294967295 |
| BIGINT | 8 | -9223372036854775808 ~ 9223372036854775807 | 0 ~ 18446744073709551615 |

对于整数类型，MySQL 还支持在类型名称后面加小括号 (M)，M 表示显示宽度，取值范围是 (0, 255)。`int(M)` 这个 M 只有在字段属性中指定了 `unsigned`（无符号）和 `zerofill`（零填充）的情况下才有意义：当整数值不够 M 位时，用 0 填充；超过 M 位但没超过该类型的取值范围时，按实际位数存储；当 M 宽度超过该数据类型可存储的最大宽度时，也是以实际存储范围为准。

MySQL 8 之前，int 没有指定 (M)，默认显示 (11)。从 MySQL 8.0.17 开始，整数数据类型不推荐使用显示宽度属性。

```sql
-- 创建表
create table t_int(
    i1 int,
    i2 int(2) -- 没有unsigned zerofill，(2)没有意义
);
-- 查看表结构
desc t_int;

-- 创建表
create table t_int2(
    i1 int,
    i2 int(2) unsigned zerofill
);
-- 查看表结构
desc t_int2;
-- 添加数据
insert into t_int2 values(1234,1234);
insert into t_int2 values(1,1);
-- 查询数据（i2不够2位时用0填充显示）
select * from t_int2;
-- 把小数赋值给整数类型的字段时，会截断小数部分，考虑四舍五入
insert into t_int2 values(1.5,1.5);
select * from t_int2;
```

###### 浮点数类型

MySQL 中使用浮点数和定点数来表示小数。浮点数有两种类型：单精度浮点数（**FLOAT**）和双精度浮点数（**DOUBLE**），定点数只有 DECIMAL。

浮点数和定点数都可以用 (M, D) 来表示：
- M 是精度，表示该值总共显示 M 位，包括整数位和小数位。对于 FLOAT 和 DOUBLE 类型，M 取值范围为 0~255；对于 DECIMAL，M 取值范围为 0~65。
- D 是标度，表示小数的位数，取值范围为 0~30，同时必须 <= M。

FLOAT 和 DOUBLE 不指定 (M, D) 时，默认按实际的精度显示。DECIMAL 不指定 (M, D) 时，默认为 (10, 0)，即只保留整数部分。例如 DECIMAL(5,2)，表示该列取值范围是 -999.99 ~ 999.99。如果插入数据的小数部分位数超过 D 位，MySQL 会四舍五入处理；如果插入数据的整数部分位数超过 M-D 位，则会报 Out of range 错误。

DECIMAL 实际是以字符串形式存放的，在对精度要求比较高的时候（如货币、科学数据等）使用 DECIMAL 类型比较好。浮点数相对于定点数的优点是长度一定的情况下能表示更大的数据范围，缺点是会引起精度问题。

```sql
-- 创建表
create table t_double(
    d1 double,
    d2 double(5,2) -- -999.99~999.99
);
-- 查看表结构
desc t_double;
-- 添加数据
insert into t_double values(2.5,2.5);
insert into t_double values(2.5526,2.5526);
insert into t_double values(2.5586,2.5586);
-- 查询数据（小数部分超过D位会四舍五入）
select * from t_double;
-- 添加数据
insert into t_double values(12852.5526,12852.5526);
-- d2字段整数部分超过(5-2=3)位，添加失败

--Double和float的小数直接运算会出现精度丢失的问题，decimal以字符串存储，不存在这个问题

-- 创建表
create table t_decimal(
    d1 decimal, -- 没有指定(M,D)默认是(10,0)
    d2 decimal(5,2)
);
-- 查看表结构
desc t_decimal;
-- 添加数据
insert into t_decimal values(2.5,2.5);
-- 查询数据（d1默认(10,0)，小数被四舍五入为整数）
select * from t_decimal;
```

###### BIT类型

BIT 是一种存储位数据的类型，每个字段的长度可以指定为 1 到 64 位。数据以位流的形式存储，并以字节对齐，即使只存储 1 位，最小存储单元也是 1 字节。

可以使用十六进制、二进制或整数形式插入数据，插入值的位数不能超过定义的位数，否则会报错。查询 BIT 字段时，MySQL 会以二进制格式显示数据，如果需要以整数形式显示，可以使用 BIN() 或 CONV()。

```sql
-- 创建表
create table t_bit(
    b1 bit, -- 没有指定(M)，默认是1位二进制
    b2 bit(4) -- 能够存储4位二进制0000~1111
);
-- 查看表结构
desc t_bit;
-- 添加数据
insert into t_bit values(1,1);
-- 查询数据（以二进制格式显示）
select * from t_bit;
-- 显示二进制值，需要使用bin函数
select bin(b1),bin(b2) from t_bit;
-- 添加数据：2对应二进制10，超过1位，b1存不下
insert into t_bit values(2,2); -- 失败
-- 添加数据
insert into t_bit values(1,8);
-- 以十进制显示
select conv(b1,2,10),conv(b2,2,10) from t_bit;
-- 16的二进制10000，超过4位，b2存不下
insert into t_bit values(1,16); -- 失败
```

##### 字符串类型

###### 定长与变长字符串（CHAR 与 VARCHAR）

**CHAR(M) 为固定长度的字符串**，M 表示最多能存储的字符数，取值范围是 0~255 个字符，如果未指定 (M) 表示只能存储 1 个字符。例如 CHAR(4) 定义了一个固定长度的字符串列，其包含的字符个数最大为 4，如果存储的值少于 4 个字符，右侧将用空格填充以达到指定的长度，查询显示 CHAR 值时，尾部的空格将被删掉。

**VARCHAR(M) 为可变长度的字符串**，M 表示最多能存储的字符数，M 的范围由最长的行的大小（通常是 65535）和使用的字符集确定。例如 utf8mb4 字符编码单个字符最长占用 4 个字节，所以 M 的范围是 [0, 16383]。VARCHAR 类型实际占用的空间为字符串的实际长度加 1 或 2 个字节，这 1 或 2 个字节用于描述字符串值的实际字节数：字符串值在 [0, 255] 个字节范围内额外增加 1 个字节，否则额外增加 2 个字节。**VARCHAR 后面的 M 必须指定。**

例如身份证号、手机号码、QQ号、用户名 username、密码 password、银行卡号等固定长度的文本适合使用 CHAR 类型，而评论、朋友圈、微博等不定长度的文本更适合使用 VARCHAR 类型。

另外，存储引擎对于选择 CHAR 和 VARCHAR 也有影响：
- 对于 MyISAM 存储引擎，最好使用固定长度的数据列代替可变长度的数据列，这样可以使整个表静态化，数据检索更快，用空间换时间。
- 对于 InnoDB 存储引擎，使用可变长度的数据列，因为 InnoDB 数据表的存储格式不分固定长度和可变长度，使用 CHAR 不一定比使用 VARCHAR 更好，但由于 VARCHAR 按照实际长度存储，比较节省空间，对磁盘 I/O 和数据存储总量比较好。

```sql
drop table if exists t_char;
create table t_char (
    c1 char,     -- 默认只能存1个字符
    c2 char(3)   -- 最多存3个字符
);
insert into t_char values('男','女'); -- 成功
insert into t_char values('尚硅谷','尚硅谷'); -- 失败，c1只能存1个字符
insert into t_char values('男','尚硅谷'); -- 成功
select * from t_char;

drop table if exists t_char;
create table t_char (
    c1 varchar -- 错误，VARCHAR必须指定(M)
);

create table t_char (
    c1 varchar(3) -- 最多不超过3个字符，指的是字符数，不是字节数
);
insert into t_char values('尚硅谷'); -- 成功
insert into t_char values('尚硅谷真好'); -- 失败，超过3个字符
select * from t_char;

-- 在utf8mb4字符集下，varchar(65535)报错，字符串过长
create table t_char (
    name varchar(65535)
);
```

###### 文本类型（TEXT系列）

| 类型 | 最大长度 | 说明 |
|------|---------|------|
| TINYTEXT | 255字节 | 微型文本 |
| TEXT | 64KB（65535字节） | 长文本 |
| MEDIUMTEXT | 16MB | 中等长度文本 |
| LONGTEXT | 4GB | 极大文本 |

TEXT 系列类型用于存储较长的字符串，不需要指定长度。超过 VARCHAR 上限的长文本（如文章内容、评论内容）适合使用 TEXT 类型。

###### 枚举与集合（ENUM 与 SET）

有时候我们需要在固定的几个值范围内选择一个或多个，就需要使用 ENUM 枚举类型和 SET 集合类型。比如性别只有"男"或"女"；上下班交通方式可以有"地铁"、"公交"、"出租车"、"自行车"、"步行"等。

枚举和集合类型字段声明的语法格式如下：

```sql
字段名 ENUM(值1,值2,值3)
字段名 SET(值1,值2,值3)
```

- ENUM 类型的字段在赋值时，只能在指定的枚举列表中取值，而且一次只能取一个。枚举列表最多可以有 65535 个成员。ENUM 值在内部用整数表示，每个枚举值均有一个索引值，MySQL 存储的就是这个索引编号。
- SET 类型的字段在赋值时，可从定义的值列表中选择 1 个或多个值的组合。SET 列最多可以有 64 个成员。SET 值在内部也用整数表示，分别是 1、2、4、8……都是 2 的 n 次方值，因为这些整数值对应的二进制都是只有 1 位是 1，其余是 0。

```sql
drop table if exists t_enum;
create table t_enum (
    gender enum('男','女'),
    hobby set('睡觉','打游戏','运动','写代码')
);
desc t_enum;
insert into t_enum values('男','睡觉,打游戏'); -- 成功
insert into t_enum values('男,女','睡觉,打游戏'); -- 失败，enum一次只能取一个
insert into t_enum values('妖','睡觉,打游戏'); -- 失败，不在枚举列表中
insert into t_enum values('男','睡觉,打游戏,吃饭'); -- 失败，'吃饭'不在set列表中
select * from t_enum;
-- 也可以按索引号插入：enum的索引从1开始，set按位计算
insert into t_enum values(2, 2); -- gender为'女'，hobby为'打游戏'(2)
select * from t_enum;
insert into t_enum values(1, 5); -- 5(0101)是1(0001)、4(0100)的组合
select * from t_enum;
insert into t_enum values(1, 7); -- 7(0111)是1(0001)、2(0010)、4(0100)的组合
select * from t_enum;
```

###### 二进制类型（BINARY 与 VARBINARY）

BINARY 和 VARBINARY 类似于 CHAR 和 VARCHAR，只是它们存储的是二进制字符串。

- BINARY(M) 为固定长度的二进制字符串，M 表示最多能存储的字节数，取值范围是 0~255 个字节，如果未指定 (M) 表示只能存储 1 个字节。例如 BINARY(8) 最多能存储 8 个字节，如果字段值不足 (M) 个字节，将在右边填充 '\0' 以补齐指定长度。
- VARBINARY(M) 为可变长度的二进制字符串，M 表示最多能存储的字节数，总字节数不能超过行的字节长度限制 65535，另外还需要 1 或 2 个字节来存储数据的字节数。VARBINARY 和 VARCHAR 一样必须指定 (M)，否则报错。

##### 日期时间类型

| 类型 | 格式 | 示例 | 说明 |
|------|------|------|------|
| YEAR | YYYY | 2022 | 年份信息，取值范围 1901~2155 |
| DATE | YYYY-MM-DD | 2022-02-04 | 年月日 |
| TIME | HH:MM:SS | 10:08:08 | 时分秒 |
| DATETIME | YYYY-MM-DD HH:MM:SS | 2022-02-04 10:08:08 | 年月日时分秒 |
| TIMESTAMP | YYYY-MM-DD HH:MM:SS | 2022-02-04 10:08:08 | 时间戳，与DATETIME类似 |

- 如果仅仅是表示年份信息，可以只使用 YEAR 类型，更节省空间。YEAR 允许的值范围是 1901~2155。YEAR 还有 "YY" 2 位数字的形式，值是 00~69 表示 2000~2069 年，值是 70~99 表示 1970~1999 年，从 MySQL 5.5.27 开始，2 位格式的 YEAR 已经不推荐使用。0 年如果是整数 0 添加，则是 0000 年；如果是日期/字符串的 '0' 添加，则是 2000 年。
- 如果需要经常插入或更新日期时间为系统日期时间，通常使用 TIMESTAMP 类型。TIMESTAMP 与 DATETIME 的区别：TIMESTAMP 的取值范围小，只支持 1970-01-01 00:00:01 UTC 至 2038-01-19 03:14:07 UTC 范围内的日期时间值（UTC 是世界标准时间），并且 TIMESTAMP 在存储时会将当前时区的日期时间值转换为 UTC 存储，检索时再转换回当前时区的日期时间值，对多时区更友好。而 DATETIME 只能反映出插入时当地的时区，其他时区的人查看数据必然会有误差。另外，TIMESTAMP 的属性受 MySQL 版本和服务器 SQLMode 的影响很大。

```sql
drop table if exists t_date;
create table t_date (
    d1 datetime,
    d2 timestamp
);
insert into t_date values('2021-9-2 14:45:52','2021-9-2 14:45:52');
select * from t_date;
-- 修改当前的时区
set time_zone = '+2:00';
-- 格式错误（年月日时分秒位数不够）
insert into t_date values('202192144552','202192144552');
-- 紧凑格式可以
insert into t_date values('20210902144552','20210902144552');
-- 其他分隔符也可以
insert into t_date values('2021&9&2 14%45%52','2021#9#2 14@45@52');
select * from t_date;

drop table if exists t_date;
create table t_date (
    d year
);
insert into t_date values(2021),(85),(22),(69),(0),('0');
select * from t_date;
```

##### 其他类型

###### JSON类型

在 MySQL 5.7 之前，如果需要存储 JSON 数据只能使用 VARCHAR 或 TEXT 字符串类型。从 5.7.8 版本之后开始支持 JSON 数据类型。

###### 空间类型

MySQL 空间类型扩展支持地理特征的生成、存储和分析。这里的地理特征表示世界上具有位置的任何东西，可以是一个实体（例如一座山），可以是空间（例如一座办公楼），也可以是一个可定义的位置（例如一个十字路口）等等。现在的应用程序开发中空间数据的存储越来越多，例如钉钉的打卡位置是否在办公区域范围内、滴滴打车的位置和路线等。MySQL 提供了非常丰富的空间函数以支持各种空间数据的查询和处理。

MySQL 中使用 Geometry（几何）来表示所有地理特征，指一个点或点的集合，代表世界上任何具有位置的事物。MySQL 的空间数据类型（Spatial Data Type）对应于 OpenGIS 类，包括 GEOMETRY、POINT、LINESTRING、POLYGON 等单值类型，以及 MULTIPOINT、MULTILINESTRING、MULTIPOLYGON、GEOMETRYCOLLECTION 等存放不同几何值的集合类型。

#### MySQL系统预定义函数

函数：代表一个独立的可复用的功能。MySQL中的函数必须有返回值，参数可以有可以没有。

MySQL中函数分为：

1. 系统预定义函数：MySQL数据库管理软件提供的函数，直接用就可以，任何数据库都可以用公共的函数。
   - 单行函数：表示会对表中的每一行记录分别计算，有n行得到还是n行结果。如数学函数、字符串函数、日期时间函数、条件判断函数、窗口函数等。
   - 分组函数：或者又称为聚合函数，多行函数，表示会对表中的多行记录一起做一个"运算"，得到一个结果。如求平均值的avg，求最大值的max，求最小值的min，求总和sum，求个数的count等。
2. 用户自定义函数：由开发人员自己定义的，通过CREATE FUNCTION语句定义，是属于某个数据库的对象。

##### 预置函数重点牢记

> 下面的详细表格太多，不需要全部记住。先把这张精简清单记牢，其余函数用到时再回来查。
> 运行案例前先执行 `use atguigu;`，例子基于 `t_employee` 表（字段有 `ename`、`salary`、`gender`、`email`、`tel`、`commission_pct`、`birthday`、`hiredate`、`work_place` 等）。

###### 分组函数（必背，最高频）

| 函数 | 作用 |
|------|------|
| `count(*)` | 统计行数（`count(字段)` 会忽略 NULL） |
| `sum(字段)` | 求和 |
| `avg(字段)` | 平均值 |
| `max(字段)` / `min(字段)` | 最大值 / 最小值 |

**分组函数使用案例：**

```sql
use atguigu;

-- 员工总人数
select count(*) from t_employee;

-- 有奖金的人数（commission_pct 为 NULL 的不算）
select count(commission_pct) from t_employee;

-- 所有人薪资总和
select sum(salary) from t_employee;

-- 平均薪资
select avg(salary) from t_employee;

-- 最高薪资、最低薪资
select max(salary), min(salary) from t_employee;
```

###### 字符串函数（重点）

| 函数 | 作用 |
|------|------|
| `concat(s1,s2,...)` | 拼接字符串 |
| `concat_ws(分隔符,s1,s2,...)` | 用分隔符拼接 |
| `upper(s)` / `lower(s)` | 转大写 / 小写 |
| `char_length(s)` | 字符个数（推荐，按字符算） |
| `length(s)` | 字节数（和字符集有关） |
| `substring(s,start,len)` | 截取子串（位置从 1 开始） |
| `left(s,n)` / `right(s,n)` | 取左边 / 右边 n 个字符 |
| `trim(s)` | 去两端空格 |
| `replace(s,a,b)` | 把 s 中的 a 全部换成 b |

**字符串函数使用案例：**

```sql
-- 拼接：姓名 + 电话
select concat(ename, '的电话是', tel) from t_employee;

-- 带分隔符拼接
select concat_ws('-', ename, tel) from t_employee;

-- 转大小写
select upper('hello'), lower('HELLO');

-- 字符数 vs 字节数（中文时最容易看出区别）
select ename, char_length(ename) as 字符数, length(ename) as 字节数
from t_employee;

-- 截取邮箱 @ 前面的用户名
select email, substring(email, 1, position('@' in email) - 1) as 邮箱前缀
from t_employee;
#POSITION 用来查找一个字符串在另一个字符串中第一次出现的位置,语法：POSITION(子字符串 IN 字符串)
#比如上面的查询，返回的就是第一次出现的位置，- 1就是截取掉出现之前的字符

-- 取左边 1 个字符、右边 2 个字符
select ename, left(ename,1), right(ename,2) from t_employee;

-- 去两端空格
select trim('   hello   ');

-- 替换：把 work_place 里的逗号换成斜杠
select work_place, replace(work_place, ',', '/') from t_employee;
```

###### 日期时间函数（重点）

| 函数 | 作用 |
|------|------|
| `now()` | 当前日期时间 |
| `curdate()` | 当前日期 |
| `curtime()` | 当前时间 |
| `year(d)` / `month(d)` / `day(d)` | 取年 / 月 / 日 |
| `date_format(d,格式)` | 按格式显示日期（如 `'%Y-%m-%d'`） |
| `datediff(d1,d2)` | 两个日期相差的天数 |

**日期时间函数使用案例：**

```sql
-- 当前日期时间、日期、时间
select now(), curdate(), curtime();

-- 取出年、月、日
select birthday, year(birthday), month(birthday), day(birthday)
from t_employee;

-- 格式化日期
select birthday, date_format(birthday, '%Y年%m月%d日') from t_employee;

-- 距离今天入职多少天
select ename, hiredate, datediff(curdate(), hiredate) as 入职天数
from t_employee;
```

###### 数值函数（重点）

| 函数 | 作用 |
|------|------|
| `round(x)` / `round(x,n)` | 四舍五入（可保留 n 位小数） |
| `ceil(x)` / `floor(x)` | 向上 / 向下取整 |
| `abs(x)` | 绝对值 |
| `mod(x,y)` | 取余（等价 `%`） |
| `truncate(x,n)` | 截断到 n 位小数（不四舍五入） |

**数值函数使用案例：**

```sql
-- 四舍五入（保留 2 位小数）
select round(3.567, 2);   -- 3.57

-- 向上取整、向下取整
select ceil(3.1), floor(3.9);   -- 4, 3

-- 绝对值
select abs(-5);   -- 5

-- 取余
select mod(10, 3);   -- 1

-- 截断（不四舍五入，保留 2 位）
select truncate(3.567, 2);   -- 3.56

-- 给薪资保留 2 位小数
select salary, round(salary, 2) from t_employee;
```

###### 条件判断函数（重点）

| 函数 | 作用 |
|------|------|
| `if(条件,值1,值2)` | 条件成立返回值1，否则值2 |
| `ifnull(字段,默认值)` | 字段为 NULL 时返回默认值 |
| `case when ... then ... else ... end` | 多条件判断，实际项目很常用 |

**条件判断函数使用案例：**

```sql
-- if：薪资 > 20000 显示高薪，否则正常
select ename, salary, if(salary > 20000, '高薪', '正常') as 薪资水平
from t_employee;

-- ifnull：奖金比例是 NULL 时按 0 算（避免计算结果变 NULL）
select ename, salary,
       salary + salary * ifnull(commission_pct, 0) as 实发工资
from t_employee;

-- case when：按薪资分等级
select ename, salary,
  case
    when salary > 20000 then '高'
    when salary > 10000 then '中'
    else '低'
  end as 等级
from t_employee;
```

###### 系统信息函数（会认即可）

| 函数 | 作用 |
|------|------|
| `database()` | 当前数据库名 |
| `version()` | MySQL 版本 |
| `user()` | 当前登录用户 |

**系统信息函数使用案例：**

```sql
select database();   -- 当前在哪个库
select version();    -- MySQL 版本
select user();       -- 当前登录用户
```

###### 加密函数（了解）

| 函数 | 作用 |
|------|------|
| `md5(s)` | 返回 s 的 MD5 值（登录密码常用） |

**加密函数使用案例：**

```sql
select md5('123456');   -- 密码加密（登录功能常用）
```

###### 窗口函数

| 函数 | 作用 |
|------|------|
| `row_number()` | 每行按顺序编号：1,2,3,4 |
| `rank()` | 排名，重复值并列且跳过序号：1,1,3 |
| `dense_rank()` | 排名，重复值并列但不跳过序号：1,1,2 |
| `lag(字段)` / `lead(字段)` | 取当前行的前一行 / 后一行的值 |

**窗口函数先看一眼（不用现在会）：**

```sql
-- 给员工薪资从高到低排个名，先感受一下写法
select ename, salary,
       row_number() over(order by salary desc) as 排名
from t_employee;
```

> 详细语法和案例见下方「窗口函数」章节，等学完 `group by`、`order by` 再回来学。

> 记忆顺序：先分组函数，再字符串 / 日期 / 数值；条件判断会写 `if`、`ifnull` 和 `case when` 就够。窗口函数是第二阶段重点；JSON 函数、空间函数先了解即可，用到再查。

##### 常用数学函数

| 函数 | 说明 |
|------|------|
| abs(x) | 绝对值 |
| ceil(x) | 向上取整 |
| floor(x) | 向下取整 |
| mod(x,y) | x模y |
| rand() | 返回0~1的随机值 |
| round(x,y) | 返回参数x的四舍五入的有y位的小数的值 |
| truncate(x,y) | 返回数字x截断为y位小数的结果 |
| format(x,y) | 强制保留小数点后y位，整数部分超过三位的时候以逗号分割，并且返回的结果是文本类型 |
| sqrt(x) | x的平方根 |
| pow(x,y) | x的y次方 |

```sql
use atguigu;
-- 在t_employee表中查询员工无故旷工一天扣多少钱
-- 分别使用ceil,floor,round,truncate函数
-- 假设本月工作日总天数是22天
-- 旷工一天扣的钱=salary/22
select
    ename,
    salary/22,
    ceil(salary/22),
    floor(salary/22),
    round(salary/22,2),
    truncate(salary/22,2)
from t_employee;
-- 查询公司平均薪资，并对平均薪资
-- 分别使用ceil,floor,round,truncate函数
select
    avg(salary),
    ceil(avg(salary)),
    floor(avg(salary)),
    round(avg(salary),2),
    truncate(avg(salary),2)
from t_employee;

重点需要记住的数学函数：AVG()求平均值 ABS()绝对值，MAX/MIN最大最小值，SUM()求和，COUNT()统计行数
select count(*) from t_employee;
```

##### 常用字符串函数

| 函数 | 说明 |
|------|------|
| concat(s1,s2,…) | 拼接字符串 |
| concat_ws(a,s1,s2,…) | 在字符串间加上a拼接字符串 |
| char_length(s) | s的字符数 |
| length(s) | s的字节数，与字符集有关 |
| locate(s,str) 或 instr(str,s) | 返回s在str中的开始位置 |
| upper(s) 或 ucase(s) | 所有字母转大写 |
| lower(s) 或 lcase(s) | 所有字母转小写 |
| left(s,n) | 返回最左边的n个字符 |
| right(s,n) | 返回最右边的n个字符 |
| lpad(str,len,pad) | 用pad从左边填充str直到长度达到len |
| rpad(str,len,pad) | 用pad从右边填充str直到长度达到len |
| ltrim(s) | 去掉s左侧空格 |
| rtrim(s) | 去掉s右侧空格 |
| trim(s) | 去掉s两侧空格 |
| trim([both] s from str) | 去掉str两侧的s |
| trim([leading] s from str) | 去掉str左侧的s |
| trim([trailing] s from str) | 去掉str右侧的s |
| insert(str,index,len,instr) | str从index位置开始的len个字符替换为instr |
| replace(str,a,b) | str中的a全部替换为b |
| repeat(s,n) | 返回s重复n次的结果 |
| reverse(s) | 反转字符串 |
| strcmp(s1,s2) | 比较s1,s2 |
| substring(str,index,len) | str从index位置截取len个字符 |
| substring_index(str,分隔符,count) | 如果count是正数，那么从左往右数，截取第n个分隔符的左边的全部内容。例如，substring_index("www.atguigu.com",".",1)是"www"。如果count是负数，那么从右边开始数，截取第n个分隔符右边的所有内容。例如，substring_index("www.atguigu.com",".",-1)是"com" |

```sql
use atguigu;
-- 在t_employee表中查询员工姓名ename和电话tel
-- 并使用concat函数，concat_ws函数
select concat(ename,tel),concat_ws('-',ename,tel) from t_employee;
-- 在t_employee表中查询薪资高于15000的男员工姓名
-- 并把姓名处理成 张xx 的样式
-- left(s,n)函数表示取字符串s最左边的n个字符
-- 而rpad(str,len,pad)函数表示在字符串str的右边填充pad使得字符串长度达到len
select rpad(left(ename,1),3,'x'),salary
from t_employee
where salary>15000 and gender='男';
-- 在t_employee表中查询薪资高于10000的男员工姓名，姓名包含的字符数和占用的字节数
select ename,char_length(ename) as 占用字符数,length(ename) as 占用字节数量
from t_employee
where salary>10000 and gender='男';
-- 在t_employee表中查询薪资高于10000的男员工姓名和邮箱email
-- 并把邮箱名 @ 字符之前的字符串截取出来
-- MySQL中substring函数截取字符串，位置从1开始
select ename,email,substring(email,1,position('@' in email)-1)
from t_employee
where salary>10000 and gender='男';
-- trim()默认是去掉前后空白符
select trim('    hello   world   ');
select concat('[',trim('    hello   world   '),']');
-- 去掉前后的 &
select trim(both '&' from '&&&&hello   world&&&&');
select trim(leading '&' from '&&&&hello   world&&&&');
select trim(trailing '&' from '&&&&hello   world&&&&');
```

##### 日期时间函数

| 函数 | 说明 |
|------|------|
| curdate() 或 current_date() | 当前系统日期 |
| curtime() 或 current_time() | 当前系统时间 |
| now() 或 sysdate() 或 current_timestamp() 或 localtime() 或 localtimestamp() | 当前系统日期时间 |
| utc_date() 或 utc_time() | 当前UTC日期值/时间值 |
| unix_timestamp(date) | UNIX时间戳 |
| year(date)/month(date)/day(date)/hour(time)/minute(time)/second(time) | 取年/月/日/小时/分钟/秒 |
| extract(type from date) | 从日期中提取一部分值 |
| dayofmonth(date) | 一月中第几天 |
| dayofyear(date) | 一年中第几天 |
| week(date) 或 weekofyear(date) | 一年中的第几周 |
| dayofweek(date) | 返回周几，周日是1，周一是2，…周六是7 |
| weekday(date) | 返回周几，周一是0，周二是1，…周日是6 |
| dayname(date) | 返回星期，Monday,Tuesday,…Sunday |
| monthname(date) | 返回月份，January,… |
| datediff(date1,date2) | date1-date2的日期间隔 |
| timediff(time1,time2) | time1-time2的时间间隔 |
| date_add(date,interval expr type) 或 adddate/date_sub/subdate | 返回与给定日期相差interval时间段的日期 |
| addtime(time,expr)/subtime(time,expr) | 返回给定时间加上/减去expr的时间值 |
| date_format(datetime,fmt) | 按照字符串fmt格式化日期datetime值 |
| time_format(time,fmt) | 按照字符串fmt格式化时间time值 |
| str_to_date(str,fmt) | 按照字符串fmt将str解析为一个日期 |
| get_format(val_type,format_type) | 返回日期时间字符串的显示格式 |

函数中日期时间类型说明：

| 参数类型 | 说明 | 参数类型 | 说明 |
|---------|------|---------|------|
| YEAR | 年 | YEAR_MONTH | 年月 |
| MONTH | 月 | DAY_HOUR | 日时 |
| DAY | 日 | DAY_MINUTE | 日时分 |
| HOUR | 小时 | DAY_SECOND | 日时分秒 |
| MINUTE | 分钟 | HOUR_MINUTE | 时分 |
| SECOND | 秒 | HOUR_SECOND | 时分秒 |
| WEEK | 星期 | MINUTE_SECOND | 分秒 |
| QUARTER | 季度 | | |

函数中format参数说明：

| 格式符 | 说明 | 格式符 | 说明 |
|--------|------|--------|------|
| %Y | 4位数字表示年份 | %y | 2位数字表示年份 |
| %M | 月名表示月份（January,…） | %m | 2位数字表示月份（01,02,03,…） |
| %b | 缩写的月名（Jan.,Feb.,…） | %c | 数字表示月份（1,2,3…） |
| %D | 英文后缀表示月中的天数（1st,2nd,3rd,…） | %d | 2位数字表示月中的天数（01,02,…） |
| %e | 数字形式表示月中的天数（1,2,3,…） | %p | AM或PM |
| %H | 2位数字表示小时，24小时制（01,02,03,…） | %h和%I | 2位数字表示小时，12小时制（01,02,03,…） |
| %k | 数字形式的小时，24小时制（1,2,3,…） | %l | 数字表示小时，12小时制（1,2,3,…） |
| %i | 2位数字表示分钟（00,01,02,…） | %S和%s | 2位数字表示秒（00,01,02,…） |
| %T | 时间，24小时制（hh:mm:ss） | %r | 时间，12小时制（hh:mm:ss）后加AM或PM |
| %W | 一周中的星期名称（Sunday,…） | %a | 一周中的星期缩写（Sun.,Mon.,Tues.,…） |
| %w | 以数字表示周中的天数（0=Sunday,1=Monday,…） | %j | 以3位数字表示年中的天数（001,002,…） |
| %U | 以数字表示的年份中的第几周（1,2,3,…），其中Sunday为周中的第1天 | %u | 以数字表示的年份中的第几周（1,2,3,…），其中Monday为周中第1天 |
| %V | 一年中第几周（01~53），周日为每周的第1天，和%X同时使用 | %X | 4位数形式表示该周的年份，周日为每周第1天，和%V同时使用 |
| %v | 一年中第几周（01~53），周一为每周的第1天，和%x同时使用 | %x | 4位数形式表示该周的年份，周一为每周第1天，和%v同时使用 |
| %% | 表示% | | |

GET_FORMAT函数中val_type 和format_type参数说明：

| 值类型 | 格式化类型 | 显示格式字符串 |
|--------|-----------|----------------|
| DATE | EUR | %d.%m.%Y |
| DATE | INTERVAL | %Y%m%d |
| DATE | ISO | %Y-%m-%d |
| DATE | JIS | %Y-%m-%d |
| DATE | USA | %m.%d.%Y |
| TIME | EUR | %H.%i.%s |
| TIME | INTERVAL | %H%i%s |
| TIME | ISO | %H:%i:%s |
| TIME | JIS | %H:%i:%s |
| TIME | USA | %h:%i:%s %p |
| DATETIME | EUR | %Y-%m-%d %H.%i.%s |
| DATETIME | INTERVAL | %Y%m%d %H%i%s |
| DATETIME | ISO | %Y-%m-%d %H:%i:%s |
| DATETIME | JIS | %Y-%m-%d %H:%i:%s |
| DATETIME | USA | %Y-%m-%d %H.%i.%s |

```sql
use atguigu;
-- 获取系统日期。curdate()和current_date()函数都可以获取当前系统日期
select curdate(),current_date();
-- 将日期值 +0
select curdate()+0;
-- 获取系统时间。curtime()和current_time()函数都可以获取当前系统时间
select curtime(),current_time();
-- 将时间值 +0
select curtime()+0;
-- 获取系统日期时间值。current_timestamp(),localtime(),sysdate(),now()
select current_timestamp(),localtime(),sysdate(),now();
-- 获取当前UTC（世界标准时间）日期或时间值
-- 本地时间是根据地球上不同时区所处的位置调整 UTC 得来的
-- 例如，北京时间比UTC时间晚8个小时
-- utc_date(),curdate(),utc_time(),curtime()
select utc_date(),curdate(),utc_time(),curtime();
-- 获取UNIX时间戳
select unix_timestamp(),unix_timestamp("2000-1-1");
-- 获取具体的时间值，比如年、月、日、时、分、秒
-- year(date),month(date),day(date)
-- hour(time),minute(time),second(time)
select year(now()),month(now()),day(now()),
       hour(now()),minute(now()),second(now());
-- 获取日期时间的指定值。extract(type from date/time)函数
select extract(year_month from now());
-- 获取两个日期或时间之间的间隔
-- datediff(date1,date2) 返回两个日期之间间隔的天数
-- timediff(time1,time2) 返回两个时间之间间隔的时分秒
select datediff(now(),"2000-1-1");
select timediff(now(),"2000-1-1 12:00:00");
-- 查询今天距离员工入职的日期间隔天数
select ename,datediff(curdate(),hiredate) from t_employee;
-- 查询现在距离中午放学还有多少时间
select timediff("12:00:00",curtime());
-- 在t_employee表中查询本月生日的员工姓名、生日
select ename,birthday
from t_employee
where month(curdate()) = month(birthday);
-- 查询入职时间超过5年的
select ename,hiredate,datediff(curdate(),hiredate)
from t_employee
where datediff(curdate(),hiredate)>365*5;
```

##### 常用加密函数

| 函数 | 说明 |
|------|------|
| password(str) | 返回字符串str的加密版本，41位长的字符串（MySQL8不再支持） |
| md5(str) | 返回字符串str的md5值，也是一种加密方式 |
| sha(str) | 返回字符串str的sha算法加密字符串，40位十六进制值的密码字符串 |
| sha2(str,hash_length) | 返回字符串str的sha算法加密字符串，密码字符串的长度是hash_length/4。hash_length可以是224、256、384、512、0，其中0等同于256 |

```sql
use atguigu;
-- 当用户需要对数据进行加密时
-- 比如做登录功能时，给用户的密码加密等
select md5('123456'),sha('123456'),sha2('123456',0);
select
    char_length(md5('123456')),
    char_length(sha('123456')),
    char_length(sha2('123456',0));
drop table if exists t_user;
create table t_user(
    id int primary key auto_increment,
    username varchar(20),
    password varchar(100)
);
insert into t_user values(null,"chai",md5("123456"));
select * from t_user where username="chai" and password="123456";
select * from t_user where username="chai" and password=md5("123456");
drop table if exists t_user;
```

##### 常用系统信息函数

| 函数 | 说明 |
|------|------|
| database() | 当前数据库名 |
| version() | 当前数据库版本 |
| user() | 当前登录用户名 |

##### 条件判断函数

| 函数 | 说明 |
|------|------|
| if(a,x,y) | 如果a为真，返回x，否则返回y |
| ifnull(x,y) | 如果x不为空，返回x，否则返回y |
| case when 条件1 then result1 when 条件2 then result2 else resultn end | 依次判断条件，哪个条件满足了，就返回对应的result，所有条件都不满足就返回else的result。如果没有单独的else子句，当所有when后面的条件都不满足时则返回NULL |
| case 表达式 when 常量值1 then 值1 when 常量值2 then 值2 else 值n end | 判断表达式与哪个常量值匹配，找到匹配的就返回对应值，都不匹配就返回else的值。如果没有单独的else子句，当所有when后面的常量值都不匹配时则返回NULL |

```sql
use atguigu;
-- 条件判断函数不是筛选记录的函数
-- 而是根据条件不同显示不同的结果的函数
-- 如果薪资大于20000，显示高薪，否则显示正常
select ename,salary,if(salary>20000,'高薪','正常')
from t_employee;
-- 计算实发工资。实发工资 = 薪资 + 薪资 * 奖金比例
select
    ename,
    salary,
    commission_pct,
    salary + salary * commission_pct as 实发工资
from t_employee;
-- 如果commission_pct是NULL，计算完结果是NULL
select
    ename,
    salary,
    commission_pct,
    salary + salary * ifnull(commission_pct,0) as 实发工资
from t_employee;
-- 查询员工编号，姓名，薪资，等级，等级根据薪资判断
-- 如果薪资大于20000，显示 羡慕级别
-- 如果薪资15000-20000，显示 努力级别
-- 如果薪资10000-15000，显示 平均级别
-- 如果薪资10000以下，显示 保底级别
select eid,ename,salary,
case
    when salary>20000 then '羡慕级别'
    when salary>15000 then '努力级别'
    when salary>10000 then '平均级别'
    else '保底级别'
end as "等级"
from t_employee;
-- 在t_employee表中查询入职7年以上的员工姓名、工作地点、轮岗的工作地点数量情况
-- 计算工作地点的数量可以转换为求work_place中逗号的数量+1
-- work_place中逗号的数量 = work_place的总字符数 - work_place去掉逗号的字符数
-- 使用replace函数去掉work_place中逗号
select work_place,
char_length(work_place)-char_length(replace(work_place,",",""))+1 as 工作地点数量
from t_employee;

select ename,work_place,
case char_length(work_place)-char_length(replace(work_place,",",""))+1
    when 1 then '只在一个地方工作'
    when 2 then '在两个地方来回奔波'
    when 3 then '在三个地方流动'
    else '频繁出差'
end as "工作地点数量情况"
from t_employee
where datediff(curdate(),hiredate)>365*7;
```

##### 其他函数

从5.7.8版本之后开始支持JSON数据类型，并提供了操作JSON类型数据的相关函数。MySQL还提供了非常丰富的空间函数以支持各种空间数据的查询和处理。这两类函数暂时不讲，如果项目中有用到查询API使用。

##### 分组函数

分组函数有合并计算过程。调用完分组函数后，结果的行数变少，可能得到一行，可能得到少数几行。

常用的分组函数：

| 函数 | 说明 |
|------|------|
| avg(x) | 平均值 |
| sum(x) | 求和 |
| max(x) | 最大值 |
| min(x) | 最小值 |
| count(x) | 计数 |

```sql
use atguigu;
-- 统计t_employee表的员工的数量
select count(*) from t_employee;
select count(1) from t_employee;
select count(eid) from t_employee;
select count(commission_pct) from t_employee;
/*
count(*)或count(常量值)：都是统计实际的行数
count(字段/表达式)：统计时忽略NULL值
*/
-- 找出t_employee表中最高的薪资值
select max(salary) from t_employee;
-- 找出t_employee表中最低的薪资值
select min(salary) from t_employee;
-- 统计t_employee表中平均薪资值
select avg(salary) from t_employee;
-- 统计所有人的薪资总和
select sum(salary) from t_employee;
select sum(salary+salary*ifnull(commission_pct,0)) from t_employee;
-- 找出年龄最小、最大的员工的出生日期
select min(birthday),max(birthday) from t_employee;
-- 查询最新入职的员工的入职日期
select max(hiredate) from t_employee;
-- 分组函数一般和group by子句结合在一起使用，例如
-- 查询每一个部门的平均薪资
select did,round(avg(salary),2)
from t_employee
group by did;
```

##### 窗口函数

###### 核心概念

窗口函数也叫OLAP函数（Online Analytical Processing，联机分析处理），可以对数据进行实时分析处理。窗口函数是每条记录都会分析，有几条记录执行完还是几条，因此也属于单行函数。

**窗口函数 vs GROUP BY 的区别**：GROUP BY 会把多行"合并"成一行，窗口函数保留每一行。

```
原始数据：
部门    姓名    薪资
IT      张三    10000
IT      李四    12000
HR      王五    8000

GROUP BY 部门 → 结果只有2行（IT平均11000，HR平均8000）
窗口函数   → 结果还是3行，每行都能看到部门平均值
```

**窗口 = 你看数据的"视角范围"**

###### 语法格式

```sql
函数名(参数列表) OVER(
    [PARTITION BY column]    -- 按什么分组（可选）
    [ORDER BY column]        -- 按什么排序（可选）
    [ROWS BETWEEN <start> AND <end>]  -- 计算范围（可选）
)
```

**记忆口诀**：`函数 + OVER(分组 + 排序 + 范围)`

OVER关键字用来指定窗口函数的窗口范围。如果OVER后面是空`()`，则表示SELECT语句筛选的所有行是一个窗口。OVER后面的`()`支持以下语法来设置窗口范围：
- `PARTITION BY`：一个窗口范围还可以分为多个区域。按照哪些字段进行分区/分组，窗口函数在不同的分组上分别处理分析
- `ORDER BY`：按照哪些字段进行排序，窗口函数将按照排序后结果进行分析处理
- `ROWS/RANGE BETWEEN <start> AND <end>`：在计算窗口函数时，指定哪些行/值将被包含在计算范围内，`<start>`和`<end>`用于定义窗口范围：
  - `UNBOUNDED PRECEDING`：窗口从分区的第一行开始
  - `n PRECEDING`：当前行之前的n行
  - `CURRENT ROW`：当前行
  - `n FOLLOWING`：当前行之后的n行
  - `UNBOUNDED FOLLOWING`：窗口到分区的最后一行

**PARTITION BY 的作用**：按字段分组后，每个组内独立计算排名（从1重新开始）。

```
原始数据：
部门    姓名    薪资
IT      李四    12000
IT      张三    10000
HR      王五    8000

PARTITION BY 部门 ORDER BY 薪资 DESC 的执行过程：

第1步：按部门分成两个独立的"窗口"
  窗口1 (IT部门)：李四12000, 张三10000
  窗口2 (HR部门)：王五8000

第2步：每个窗口内独立排名
  窗口1 (IT部门)：李四→排名1, 张三→排名2
  窗口2 (HR部门)：王五→排名1（重新从1开始）

第3步：合并结果
  IT    李四  12000   1
  IT    张三  10000   2
  HR    王五  8000    1  ← 不是3，因为这是新的组
```

**对比有无 PARTITION BY**：
```sql
-- 有分组：每个部门独立排名
ROW_NUMBER() OVER(PARTITION BY 部门 ORDER BY 薪资 DESC)
-- 结果：1, 2, 1

-- 无分组：全公司统一排名
ROW_NUMBER() OVER(ORDER BY 薪资 DESC)
-- 结果：1, 2, 3
```

###### 窗口函数分类

| 分类 | 函数 | 说明 | 使用场景 |
|------|------|------|----------|
| 排名函数 | `ROW_NUMBER()` | 顺序编号，永远不重复：1,2,3,4 | 排名、分页 |
| | `RANK()` | 并列排名，跳过重复序号：1,1,3 | 有并列的排名 |
| | `DENSE_RANK()` | 并列排名，不跳过序号：1,1,2 | 有并列的排名 |
| 偏移函数 | `LAG(字段, n)` | 取当前行的前n行的值 | 环比、同比 |
| | `LEAD(字段, n)` | 取当前行的后n行的值 | 环比、同比 |
| 聚合窗口函数 | `SUM() OVER()` | 累计求和 | 累计销售额 |
| | `AVG() OVER()` | 移动平均 | 移动平均值 |
| | `COUNT() OVER()` | 累计计数 | 累计数量 |
| | `MAX()/MIN() OVER()` | 组内最大/最小值 | 组内极值 |
| 首尾函数 | `FIRST_VALUE()` | 窗口中第一个值 | 取首条记录 |
| | `LAST_VALUE()` | 窗口中最后一个值 | 取末条记录 |

**排名函数对比**：
```sql
-- 假设薪资：10000, 10000, 8000, 6000
ROW_NUMBER()  → 1, 2, 3, 4  （永远不重复）
RANK()        → 1, 1, 3, 4  （并列跳号）
DENSE_RANK()  → 1, 1, 2, 3  （并列不跳号）
```

###### 基础示例

```sql
use atguigu;

-- 给所有员工按薪资从高到低排序（全公司统一排名）
SELECT
    ename,
    salary,
    ROW_NUMBER() OVER(ORDER BY salary DESC) AS rn
FROM t_employee;

-- 在t_employee表中查询薪资在[8000,10000]之间的员工姓名和薪资并给每一行记录编序号
select row_number() over() as rn,ename,salary
from t_employee
where salary between 8000 and 10000;
```

###### 分组排名示例

```sql
-- 在t_employee表中查询女员工姓名，部门编号，薪资
-- 查询结果按照部门编号分组后再按薪资升序排列
-- 并分别使用row_number()、rank()、dense_rank()三个序号函数给每一行记录编序号
select ename,did,salary,gender,
row_number() over(partition by did order by salary) as "row_num",
rank() over(partition by did order by salary) as "rank_num",
dense_rank() over(partition by did order by salary) as "ds_rank_num"
from t_employee where gender='女';

-- 或使用window给窗口指定别名（MySQL 8.0+支持）
select ename,did,salary,
row_number() over w as "row_num",
rank() over w as "rank_num",
dense_rank() over w as "ds_rank_num"
from t_employee where gender='女'
window w as(partition by did order by salary);
```

###### 聚合窗口函数示例

```sql
-- 计算每一个部门的平均薪资与全公司的平均薪资的差值
-- PARTITION BY did：按部门分组，计算每个部门的平均薪资
-- 无PARTITION BY：计算全公司的平均薪资
select distinct
    did,
    avg(salary) over(partition by did) as 部门平均薪资,
    avg(salary) over() as 公司平均薪资,
    round(avg(salary) over(partition by did) - avg(salary) over(), 2) as 差值
from t_employee;
```

###### 常见业务场景

**场景1：取每组前N名**

```sql
-- 在t_employee表中查询每个部门薪资排名前3的员工姓名，部门编号，薪资值
# WHERE 不能使用窗口函数的别名窗口函数是在 SELECT 阶段计算的，而 WHERE 在 SELECT 之前执行，所以 WHERE test_one=1 会报错。需要用子查询包一层：

  SELECT * FROM (
      SELECT ename, salary,
             ROW_NUMBER() OVER(PARTITION BY did ORDER BY salary DESC) AS test_one
      FROM emp
  ) t #  MySQL 要求子查询必须有一个别名，否则会报错
  WHERE test_one = 1;
  #执行顺序
  #FROM → WHERE → SELECT → ORDER BY
  #窗口函数在 SELECT 阶段才计算，WHERE 阶段它还不存在，所以不能直接用。用子查询包一层后，外层的 WHERE 就能识别 test_one 了。


---
select temp.*
from (
    select ename, did, salary,
    dense_rank() over(partition by did order by salary desc) as "排名"
    from t_employee
) temp
where temp.排名 <= 3;

-- 在t_employee表中查询全公司薪资排名前3的员工姓名，部门编号，薪资值
select temp.*
from (
    select ename, did, salary,
    dense_rank() over(order by salary desc) as "排名"
    from t_employee
) temp
where temp.排名 <= 3;
```

**场景2：取每组最低N名**

```sql
-- 在t_employee表中查询每个部门最低3个薪资值的女员工姓名，部门编号，薪资值
select temp.*
from (
    select ename, did, salary,
    rank() over(partition by did order by salary) as "排名"
    from t_employee
    where gender='女'
) temp
where temp.排名 <= 3;
```

**场景3：偏移函数（LAG/LEAD）**

```sql
-- 查找薪资排名的上一位、下一位、首位、末位
select
    ename,
    salary,
    lag(ename,1,'-') over(order by salary) as '上一位姓名',
    lag(salary,1,0) over(order by salary) as '上一位薪资',
    lead(ename) over(order by salary) as '下一位姓名',
    lead(salary) over(order by salary) as '下一位薪资',
    first_value(salary) over(order by salary) as '首位薪资',
    last_value(ename) over(order by salary rows between unbounded preceding and unbounded following) as '末位姓名'
from t_employee;
```

###### 实战场景总结

| 场景 | 推荐函数 | 示例 |
|------|----------|------|
| 排名（第几名）| `ROW_NUMBER` / `RANK` / `DENSE_RANK` | 每个部门薪资排名 |
| 环比/同比 | `LAG` / `LEAD` | 本月销售额 vs 上月销售额 |
| 累计求和 | `SUM() OVER(ORDER BY ...)` | 累计销售额 |
| 移动平均 | `AVG() OVER(ROWS BETWEEN ...)` | 最近3天平均销售额 |
| 组内占比 | `SUM() OVER(PARTITION BY ...)` | 部门薪资占公司比例 |
| 取每组第一 | `ROW_NUMBER` + 子查询筛选 | 每个部门薪资最高的人 |

#### MySQL关联查询

##### 什么是关联查询

关联查询：两个或更多个表一起查询。

前提条件：这些一起查询的表之间是有关系的（一对一、一对多），它们之间一定是有关联字段，这个关联字段可能建立了外键，也可能没有建立外键。

比如：员工表和部门表，这两个表依靠"部门编号"进行关联。

##### 关联查询的几种情况

- 凡是联合查询的两个表，必须有"关联字段"。关联字段是逻辑意义一样，数据类型一样，名字可以一样也可以不一样的两个字段。比如：t_employee（A表）中did和t_department（B表）中的did。
- 关联字段其实就是"可以"建外键的字段。当然联合查询不要求一定建外键。
- 关联查询必须写关联条件，关联条件的个数 = n – 1，n是联合查询的表的数量：
  - 2个表一起联合查询，关联条件数量是1，
  - 3个表一起联合查询，关联条件数量是2，
  - 4个表一起联合查询，关联条件数量是3，
  - 否则就会出现笛卡尔积现象。
- 关联条件可以用on子句编写，也可以写到where中，但是建议用on单独编写，这样可读性更好。每一个join后面都要加on子句。

```sql
A inner|left|right join B on 关联条件
A inner|left|right join B on 关联条件 inner|left|right join C on 关联条件
```

下面所有案例的背景说明：t_employee 看成A表，t_department 看成B表。此时 t_employee（A表）中的李红和周洲的 did 是 NULL，没有对应部门；t_department（B表）中的测试部，没有对应员工。

##### 内连接

内连接的结果是 **A∩B**，会排除没有部门的员工，也会排除没有员工的部门。

```sql
use atguigu;

-- 查询所有员工的姓名，部门编号，部门名称
-- 员工的姓名在t_employee（A表）
-- 部门的编号在t_employee（A表）和t_department（B表）都有
-- 部门名称在t_department（B表）
-- 所以需要联合两个表一起查询
select ename,did,dname
from t_employee inner join t_department;
-- 上述sql报错
-- did在两个表中都有，名字相同，不知道取哪个表中字段
-- 有可能存在两个表都有did，但是did的意义不同的情况
-- 为了避免这种情况，需要在编写sql的时候，明确指出是用哪个表的did
select ename,t_department.did,dname
from t_employee inner join t_department;
-- 上述sql语法对，结果不对
-- 出现 笛卡尔积 现象， A表记录*B表记录
select ename,t_department.did,dname
from t_employee inner join t_department
on t_employee.did = t_department.did;

select *
from t_employee inner join t_department
on t_employee.did = t_department.did;

-- 查询部门编号为1的女员工的姓名、部门编号、部门名称、薪资等情况
select ename,gender,t_department.did,dname,salary
from t_employee inner join t_department 
on t_employee.did = t_department.did
where t_department.did = 1 and gender = '女';

-- 查询部门编号为1的员工姓名、部门编号、部门名称、薪资、职位编号、职位名称等情况
select ename,gender,t_department.did,dname,salary,job_id,jname
from t_employee
inner join t_department on t_employee.did = t_department.did
inner join t_job on t_employee.job_id = t_job.jid
where t_department.did = 1;
```

##### 左连接

左连接的结果是 **A**（包括 A-A∩B），即保留左表的所有记录，包括没有指定部门的员工。

```sql
use atguigu;

-- 查询所有员工，包括没有指定部门的员工，他们的姓名、薪资、部门编号、部门名称
select ename,salary,t_department.did,dname
from t_employee left join t_department
on t_employee.did = t_department.did;
-- 查询的结果是A

-- 查询没有部门的员工信息
select ename,salary,t_department.did,dname
from t_employee left join t_department
on t_employee.did = t_department.did
where t_employee.did is null;
-- 查询的结果是A-A∩B
-- 此时的where条件，建议写子表的关联字段is null，这样更准确一点
-- 如果要建外键，它们之间有子表和父表的角色，写子表的关联字段is null
-- 因为父表中这个字段一般是主键，不会为null
```

##### 右连接

右连接的结果是 **B**（包括 B-A∩B），即保留右表的所有记录，包括没有对应员工的部门。

```sql
use atguigu;

-- 查询所有部门，包括没有对应员工的部门，他们的姓名、薪资、部门编号、部门名称
select ename,salary,t_department.did,dname
from t_employee right join t_department
on t_employee.did = t_department.did;
-- 查询的结果是B

-- 查询没有员工部门的信息
select ename,salary,t_department.did,dname
from t_employee right join t_department
on t_employee.did = t_department.did
where t_employee.did is null;
-- 查询的结果是B-A∩B

-- 查询所有员工，包括没有指定部门的员工，他们的姓名、薪资、部门编号、部门名称
-- 把A表和B表换个位置，右连接也能实现左连接的效果
select ename,salary,t_department.did,dname
from t_department right join t_employee
on t_employee.did = t_department.did;
-- 查询的结果是A

-- 查询没有部门的员工信息
select ename,salary,t_department.did,dname
from t_department right join t_employee
on t_employee.did = t_department.did
where t_employee.did is null;
-- 查询的结果是A-A∩B
```

##### union合并查询

MySQL中没有直接的全外连接 full join，但可以通过 left join 和 right join 结合 union 实现 A∪B 的效果。

union结果：**A∪B** 或 **A∪B-A∩B = A-A∩B ∪ B-A∩B**。

union合并时要注意：
- 两个表要查询的结果字段是一样的（列数、类型一致）
- union all 表示直接合并结果，保留重复的记录
- union 表示合并结果时，去重
- 要实现A∪B的结果，那么必须是合并查询A表结果和查询B表结果的select语句
- 要实现A∪B-A∩B的结果，那么必须是合并查询A-A∩B结果和查询B-A∩B的select语句

```sql
use atguigu;

-- 查询所有员工和所有部门，包括没有指定部门的员工和没有分配员工的部门
select *
from t_employee left join t_department
on t_employee.did=t_department.did
union
select *
from t_employee right join t_department
on t_employee.did=t_department.did;
-- 以下union会报错，两个select语句的列数是不同的
select * from t_employee
union
select * from t_department;

-- 查询那些没有分配部门的员工和没有指定员工的部门，即A表和B表在对方那里找不到对应记录的数据
select *
from t_employee left join t_department
on t_employee.did = t_department.did
where t_employee.did is null
union
select *
from t_employee RIGHT join t_department
on t_employee.did = t_department.did
where t_employee.did is null;
```

##### 自连接

自连接是物理上是一张表，逻辑上是两张表。

t_employee表中mid表示员工的领导的编号，即该员工领导的员工编号。例如eid为3的员工邓超远，他的mid是7，表示他的领导是员工编号为7的员工。mid的取值范围受到eid字段的限制，mid的值选择必须是eid现有值范围。

```sql
use atguigu;

-- 查询每一个员工的编号、名字、薪资和他领导的编号、姓名、薪资
select
    emp.eid,emp.ename,emp.salary,
    mgr.eid,mgr.ename,mgr.salary
from t_employee as emp inner join t_employee as mgr
on emp.mid = mgr.eid;
-- 把t_employee当成两张表，通过取别名的方式
-- t_employee as emp 把员工表 当成员工表
-- t_employee as mgr 把员工表 当成存储领导信息的领导表
-- emp.mid = mgr.eid; 员工表的领导编号就是领导表的员工编号
```

##### select的七个字句

七个子句顺序：

| 顺序 | 子句 | 作用 |
|------|------|------|
| 1 | from | 从哪些表中筛选数据 |
| 2 | join on | 多表关联查询 |
| 3 | where | 从表中筛选数据的条件 |
| 4 | group by | 分组依据 |
| 5 | having | 在分组结果中再次筛选 |
| 6 | order by | 排序 |
| 7 | limit | 分页 |

###### from

```sql
select * from t_employee;
```

###### join on

join on 的关联条件不止可以写等值条件，也可以写非等值条件。

```sql
use atguigu;
-- 查询员工信息，并显示薪资比该员工薪资2倍还高的领导的姓名和薪资
select temp1.*,temp2.ename,temp2.salary
from t_employee as temp1
join t_employee as temp2
on temp2.salary > temp1.salary*2;
```

###### where

```sql
use atguigu;
select * from t_employee
where salary>10000;
```

###### group by

```sql
# GROUP BY 不是排序，是分组。它把相同的值合并成一组，然后对每组做聚合计算
use atguigu;
-- 查询每一个部门的平均薪资
select did,round(avg(salary),2)
from t_employee
group by did;
-- 查询每一个部门的平均薪资，显示部门编号，部门的名称，该部门的平均薪资
select t_department.did,dname,round(avg(salary),2)
from t_department left join t_employee
on t_department.did = t_employee.did
group by t_department.did;
-- 查询每一个部门的平均薪资，显示部门编号，部门的名称，该部门的平均薪资
-- 要求，如果没有员工的部门，平均薪资不显示null，显示0
select t_department.did,dname,ifnull(round(avg(salary),2),0)
from t_department left join t_employee
on t_department.did = t_employee.did
group by t_department.did;
```

with rollup合计：

```sql
use atguigu;
-- 按照部门统计人数
select did,count(*)
from t_employee
group by did;
-- 按照部门统计人数，并合计总数
select did,count(*)
from t_employee
group by did with rollup;

select
    ifnull(did,'合计') as "部门编号",
    count(*) as "人数"
from t_employee
group by did with rollup;
```

多字段分组：

```sql
use atguigu;
-- 按照不同的部门，不同的职位，分别统计男和女的员工人数
select did,job_id,gender,count(*)
from t_employee 
group by did,job_id,gender;
```

分组统计时，select后字段列表的问题：

```sql
use atguigu;
-- 分组统计时，select后面只写和分组统计有关的字段
-- 其他无关字段不要出现，否则会引起歧义
select eid,ename,did,count(*)
from t_employee
group by did;
-- eid,ename此时不应该出现在select后面
select did,count(*)
from t_employee
group by did;
```

###### having

having子句后面也写条件。
- where是对原表中的记录的筛选。where后面不能出现分组函数。
- having是对统计结果（分组函数计算后）的筛选。having后面能出现分组函数。

```sql
use atguigu;
-- 查询每一个部门的女员工的平均薪资，显示部门编号，部门的名称，该部门的平均薪资
-- 要求，如果没有员工的部门，平均薪资不显示null，显示0
-- 最后只显示平均薪资高于12000的部门
select t_department.did,dname,ifnull(round(avg(salary),2),0)
from t_department left join t_employee
on t_department.did=t_employee.did
where gender='女'
group by t_department.did
having ifnull(round(avg(salary),2),0)>12000;
-- 查询每一个部门薪资超过10000的男女员工的人数，显示部门编号，部门的名称，性别，人数
-- 只显示人数低于3人的
select t_department.did,dname,gender,count(eid)
from t_employee right join t_department
on t_employee.did=t_department.did
where salary>10000
group by t_department.did,gender
having count(eid)<3;
```

###### order by

asc代表升序，desc代表降序，默认升序。

```sql
use atguigu;
-- 查询员工信息，按照薪资从高到低
select * from t_employee
order by salary desc;
-- 查询每一个部门薪资超过10000的男女员工的人数，显示部门编号，部门的名称，性别，人数
-- 只显示人数低于3人的，按照人数升序排列
select t_department.did,dname,gender,count(eid)
from t_employee
right join t_department
on t_employee.did=t_department.did
where salary>10000
group by t_department.did,gender
having count(eid)<3
order by count(eid);
-- 查询员工的薪资，按照薪资从低到高，薪资相同按照员工编号从高到低
select *
from t_employee
order by salary asc,eid desc;
```

###### limit

limit子句是用于分页显示结果。

limit m,n：
- n：表示最多该页显示几行
- m：表示从第几行开始取记录，第一个行的索引是0
- m = (page-1)*n，page表示第几页

如每页最多显示5条，n=5：
- 第1页，page=1，m = (1-1)*5 = 0; limit 0,5
- 第2页，page=2，m = (2-1)*5 = 5; limit 5,5
- 第3页，page=3，m = (3-1)*5 = 10; limit 10,5

```sql
use atguigu;
-- 查询员工表的数据，分页显示，每页显示5条记录
-- 第1页
select * from t_employee limit 0,5;
-- 第2页
select * from t_employee limit 5,5;
-- 第3页
select * from t_employee limit 10,5;
-- 查询所有的男员工信息，分页显示，每页显示3条，第2页
select *
from t_employee
where gender='男'
limit 3,3;
-- 综合案例：查询每一个编号为偶数的部门，显示部门编号，名称，员工数量
-- 只显示员工数量>=2的结果，按照员工数量升序排列
-- 每页显示2条，显示第1页
select t_department.did,dname,count(eid)
from t_employee
right join t_department
on t_employee.did=t_department.did
where t_department.did%2=0
group by t_department.did
having count(eid)>=2
order by count(eid)
limit 0,2;
```

#### MySQL子查询

##### 什么是子查询

子查询：嵌套在另一个SQL语句中的查询。

select语句可以嵌套在另一个select、update、delete、insert、create等语句中。根据子查询嵌入的位置，分为以下几种情况。在使用子查询的时候需要注意，外层用到的列必须是子查询查询出来的

##### select中嵌套子查询

```sql
use atguigu;
-- 在t_employee表中查询每个人薪资和公司平均薪资的差值
-- 并显示员工薪资和公司平均薪资相差5000元以上的记录
select
    ename as "姓名",
    salary as "薪资",
    round((select avg(salary) from t_employee),2) as "全公司平均薪资",
    round(salary-(select avg(salary) from t_employee),2) as "差值"
from t_employee
where abs(round(salary-(select avg(salary) from t_employee),2))>5000;
-- 在t_employee表中查询每个部门平均薪资和公司平均薪资的差值
select
    did,
    avg(salary),
    avg(salary)-(select avg(salary) from t_employee)
from t_employee
group by did;
-- 使用子查询按薪资大小编号
select
    ename,
    salary,
    (select count(*) from t_employee as temp2 where temp1.salary>temp2.salary) as rk
from t_employee as temp1
order by rk;
```

##### where或having中嵌套子查询

当子查询结果作为外层另一个SQL的过滤条件，通常把子查询嵌入到where或having中。根据子查询结果的情况，分为如下三种情况：

- 当子查询的结果是单列单个值，那么可以直接使用比较运算符，如"<"、"<="、">"、">="、"="、"!="等与子查询结果进行比较
- 当子查询的结果是单列多个值，那么可以使用比较运算符in或not in进行比较
- 当子查询的结果是单列多个值，还可以使用比较运算符，如"<"、"<="、">"、">="、"="、"!="等搭配any、all等关键字与查询结果进行比较

```sql
use atguigu;
-- 在t_employee表中查询薪资最高的员工姓名和薪资
select ename,salary
from t_employee
where salary=(select max(salary) from t_employee);
-- 在t_employee表中查询比全公司平均薪资高的男员工姓名和薪资
select ename,salary
from t_employee
where salary>(select avg(salary) from t_employee) and gender='男';
-- 在t_employee表中查询和 白露，谢吉娜 同一部门的员工姓名和电话
select ename,tel,did
from t_employee
where did in (select did from t_employee where ename='白露' or ename='谢吉娜');
-- in的效果等同于 = any
select ename,tel,did
from t_employee
where did=any(select did from t_employee where ename='白露' or ename='谢吉娜');
-- 在t_employee表中查询薪资比 白露，李诗雨，黄冰茹 三个人的薪资都要高的员工姓名和薪资
select ename,salary
from t_employee
where salary>all(select salary from t_employee where ename in('白露','李诗雨','黄冰茹'));
-- > all的效果等同于 > max
select ename,salary
from t_employee
where salary>(select max(salary) from t_employee where ename in('白露','李诗雨','黄冰茹'));
-- 查询t_employee和t_department表，按部门统计平均工资
-- 显示部门平均工资比全公司的总平均工资高的部门编号、部门名称、部门平均薪资
-- 并按照部门平均薪资升序排列
select t_department.did,dname,avg(salary)
from t_employee
right join t_department
on t_employee.did=t_department.did
group by t_department.did
having avg(salary)>(select avg(salary) from t_employee)
order by avg(salary);
```

##### exists型子查询

exists型子查询也是存在外层select的where子句中，不过它和上面的where型子查询的工作模式不相同，所以这里单独讨论它。

- 如果exists关键字后面的参数是一个任意的子查询，系统将对子查询进行运算以判断它是否返回行，如果至少返回一行，那么exists的结果为true，此时外层查询语句将进行查询；如果子查询没有返回任何行，那么exists的结果为false，此时外层查询语句不进行查询。exists和not exists的结果只取决于是否返回行，而不取决于这些行的内容，所以这个子查询输入列表通常是无关紧要的。
- 如果exists关键字后面的参数是一个关联子查询，即子查询的where条件中包含与外层查询表的关联条件，那么此时将对外层查询表做循环，即在筛选外层查询表的每一条记录时，都看这条记录是否满足子查询的条件，如果满足就再用外层查询的其他where条件对该记录进行筛选，否则就丢弃这行记录。

```sql
use atguigu;
-- exists()中的子查询和外面的查询没有联合的情况下
-- 如果exists()中的子查询没有返回任何行，那么外面的子查询就不查了

-- 查询t_employee表中是否存在部门编号为null的员工
-- 如果存在，查询t_department表的部门编号、部门名称
select * from t_department 
where exists(select * from t_employee where did is null);
-- exists()中的子查询与外面的查询有联合工作的情况下
-- 循环进行把外面查询表的每一行记录的值，代入()中子查询，如果可以查到结果
-- 就留下外面查询的这条记录，否则就舍去

-- 查询t_department表是否存在与t_employee表相同部门编号的记录
-- 如果存在，查询这些部门的编号和名称
select * from t_department
where exists(select * from t_employee where t_employee.did=t_department.did);
-- 查询结果等价于下面的SQL
select distinct t_department.*
from t_department
inner join t_employee
on t_department.did=t_employee.did;
```

##### from中嵌套子查询

当子查询结果是多列的结果时，通常将子查询放到from后面，然后采用给子查询结果取别名的方式，把子查询结果当成一张"动态生成的临时表"使用。

```sql
use atguigu;
-- 当一个查询要基于另一个查询结果来筛选的时候
-- 另一个查询还是多行多列的结果，那么就可以把这个查询结果当成一张临时表
-- 放在from后面进行再次筛选

-- 在t_employee表中，查询每个部门的平均薪资
-- 然后与t_department表联合查询
-- 所有部门的部门编号、部门名称、部门平均薪资
select t_department.did,dname,pingjun
from t_department
left join (select did,avg(salary) as pingjun from t_employee group by did) temp
on t_department.did=temp.did;
-- 在t_employee表中查询每个部门中薪资排名前2的员工姓名、部门编号和薪资
select *
from (
    select
        ename,
        did,
        salary,
        dense_rank() over (partition by did order by salary desc) as paiming
    from t_employee
) temp
where temp.paiming<=2;
```

##### update中嵌套子查询

```sql
use atguigu;
-- 修改t_employee表中部门编号和测试部部门编号相同的员工薪资为原来薪资的1.5倍
update t_employee
set salary = salary * 1.5
where did=(select did from t_department where dname='测试部');
-- 修改t_employee表中did为null的员工信息
-- 将他们的did值修改为测试部的部门编号
-- 这种子查询必须是单个值，否则无法赋值
update t_employee 
set did = (select did from t_department where dname='测试部')
where did is null;
-- 修改t_employee表中李冰冰的薪资值等于孙红梅的薪资值
update t_employee
set salary = (select salary from(select salary from t_employee where ename='孙红梅')temp)
where ename='李冰冰';
-- 当update的表和子查询的表是同一个表时，需要将子查询的结果用临时表的方式表示
-- 即再套一层子查询，使得update和最外层的子查询不是同一张表

-- 修改t_employee表李冰冰的薪资与她所在部门的平均薪资一样
update t_employee
set salary = 
(
    select pingjun
    from 
        (
            select avg(salary) pingjun
            from t_employee
            where did=(
                        select did
                        from t_employee
                        where ename='李冰冰'
                    )
        ) temp
)
where ename='李冰冰';
```

##### delete中嵌套子查询

```sql
use atguigu;
-- 从t_employee表中删除测试部的员工记录
delete from t_employee 
where did = (select did from t_department where dname='测试部');
-- 从t_employee表中删除和李冰冰同一个部门的员工记录
delete from t_employee
where did=(select did from t_employee where ename='李冰冰');
-- 报错，因为删除和子查询是同一张表
delete from t_employee
where did=(select did from (select did from t_employee where ename='李冰冰')temp);
```

##### 使用子查询复制表结构和数据

复制表结构：

```sql
use atguigu;
-- 仅复制表结构，可以用create语句
create table department like t_department;
```

复制一条或多条记录：

```sql
use atguigu;
-- 使用insert语句+子查询，复制数据，此时insert不用写values
insert into department (select * from t_department where did<=3);
```

同时复制表结构和记录：

```sql
use atguigu;
-- 同时复制表结构+数据
create table d_department as (select * from t_department);
-- 如果select后面是部分字段，复制的新表就只有这一部分字段
```

##### 通用表达式（CTE）

通用表达式简称为CTE（Common Table Expressions）。CTE是命名的临时结果集，作用范围是当前语句。CTE可以理解为一个可以复用的子查询，但是和子查询又有区别，一个CTE可以引用其他CTE，CTE还可以是自引用(递归CTE)，也可以在同一查询中多次引用，但子查询不可以。

语法格式：

```sql
with [recursive]
cte_name [(字段名1,字段名2)] as (子查询),
cte_name [(字段名1,字段名2)] as (子查询)
```

通用表达式以with开头，如果with后面加recursive就表示接下来在通用表达式中需要递归引用自己，否则就不递归引用。每一个通用表达式都需要有一个名字，它相当于是子查询结果集的名字。

```sql
use atguigu;
-- 在t_employee表中查询每个人薪资和公司平均薪资的的差值
with
temp as (select round(avg(salary),2) as pingjun from t_employee)
select
    ename as "员工姓名",
    salary as "薪资",
    pingjun "公司平均薪资",
    round(salary - pingjun,2) "差值"
from t_employee,temp
having abs(差值)>5000;
-- 查询薪资低于9000的员工编号，员工姓名，员工薪资，领导编号，领导姓名，领导薪资
with 
emp as (select eid,ename,salary,`mid` from t_employee where salary<9000),
mgr(meid,mename,msalary) as (select eid,ename,salary from t_employee)
select
    eid as "员工编号",
    ename as "员工姓名",
    salary as "员工薪资",
    meid as "领导编号",
    mename as "领导姓名",
    msalary as "领导薪资"
from emp join mgr on emp.mid=mgr.meid;
```

递归CTE：

```sql
use atguigu;
-- 查询eid为21的员工，和他所有领导，直到最高领导
-- 建表，设置多层领导
create table emp as (select eid,ename,salary,tel,`mid` from t_employee where salary<10000);
update emp set mid=19 where eid=21; 
update emp set mid=17 where eid=19; 
update emp set mid=16 where eid=17; 
update emp set mid=15 where eid=16;
update emp set mid=4 where eid=15; 
update emp set mid=null where eid=4;
select * from emp;
with recursive
cte as(
    select eid,ename,`mid`
    from emp
    where eid=21
    union all
    select emp.eid,emp.ename,emp.mid
    from emp join cte
    on emp.eid=cte.mid
    where emp.eid is not null
)
select * from cte;
```

#### MySQL约束

##### 约束的作用

约束是为了保证数据的完整性。数据完整性（Data Integrity）是指数据的精确性（Accuracy）和可靠性（Reliability）。它是应防止数据库中存在不符合语义规定的数据和防止因错误信息的输入输出造成无效操作或错误信息而提出的。

数据的完整性要从以下四个方面考虑：

- 实体完整性（Entity Integrity）：例如，同一个表中，不能存在两条完全相同无法区分的记录
- 域完整性（Domain Integrity）：例如，年龄范围0-120，性别范围"男/女"
- 引用完整性（Referential Integrity）：例如，员工所在部门，在部门表中要能找到这个部门
- 用户自定义完整性（User-defined Integrity）：例如，用户名唯一、密码不能为空等，本部门经理的工资不得高于本部门职工的平均工资的5倍

可以在创建表时规定约束（通过create table语句），或者在表创建之后也可以添加约束（通过alter table语句）。

##### 约束的类型

- 键约束：主键约束、外键约束、唯一键约束
- Not NULL约束：非空约束
- Check约束：检查约束
- Default约束：默认值约束
- 自增是键约束字段的一个额外的属性

##### 表级约束和列级约束

- **表级约束**：不仅要看约束字段当前单元格的数据，还要看其他单元格的数据。键约束和检查约束是表级约束。
- **列级约束**：约束字段只看当前单元格的数据即可，和其他单元格无关。非空约束和默认值约束是列级约束。

所有的表级约束都可以在"information_schema.table_constraints"表中查看。

```sql
select * from information_schema.table_constraints where table_name = '表名';
```

##### 约束和索引

在MySQL中键约束会自动创建索引，提高查询效率。

约束和索引不同：

- 约束是一个逻辑概念，不会占用物理空间
- 索引是一个物理概念，会占用物理空间

例如，字典里面有要求，不能有重复的字（字一样，读音也一样），这是约束。字典里面有"目录"，它可以快速的查找某个字，目录需要占用单独的页，这是索引。

##### 非空约束

`not null`：限定某个字段/某列的值不允许为空。

- 只能某个列单独限定非空，不能组合非空
- 一个表可以有很多列都分别限定了非空

###### 指定非空约束：

```sql
-- 建表时
create table 表名(
    字段名 数据类型 not null,
    字段名 数据类型 not null
);

-- 建表后
alter table 表名 modify 字段名 数据类型 not null;
-- 如果该字段已经有值了，给该字段增加非空约束，要求该字段的值不能有NULL值
-- 否则需要先处理NULL值才能加上非空约束
```

###### 删除非空约束：

```sql
alter table 表名 modify 字段名 数据类型;
-- 如果使用modify修改有非空约束的字段时想要保留非空约束，必须带上not null
-- 否则会在修改时，把非空约束丢掉
```

###### 示例：

```sql
create table not_null_demo(
    id int not null,
    name varchar(20) not null,
    birthday date
);
insert into not_null_demo values(null,null,null);
insert into not_null_demo(id) values(1);
-- 此时name设定了非空约束，但没有指定默认值
-- 如果没赋值只能处理为NULL，违反了非空约束
-- 在insert添加记录时，必须给所有没有指定默认值的非空约束字段赋值
insert into not_null_demo(id,name) values(1,'张三');
insert into not_null_demo(id,name,birthday) values(2,'李四','2000-1-1');
insert into not_null_demo values(3,'王五','2000-2-1');
insert into not_null_demo values(4,'赵六',null);
-- 给birthday字段添加非空约束
alter table not_null_demo modify column birthday date not null;
-- 失败的原因是因为birthday字段现在有NULL值，添加不上非空约束
-- 如果要加，必须先将原来的NULL值修改掉
update not_null_demo set birthday = '2000-5-1' where birthday is null;
alter table not_null_demo modify column birthday date not null;
desc not_null_demo;
-- 删除birthday字段的非空约束
alter table not_null_demo modify column birthday date;
desc not_null_demo;
-- 修改name字段的数据类型为varchar(30)，本来想要保留非空约束的
alter table not_null_demo modify column name varchar(30);
desc not_null_demo;
-- alter没有加not null，会把name字段的非空约束给丢掉
```

##### 唯一键约束

`unique key`：用来限制某列的值或几个字段的值组合不能重复。

- 一个表可以有很多个唯一键约束
- 每一个唯一键约束字段都会自动创建索引
- 唯一键约束允许为空（NULL可以重复）
- 唯一键约束也可以是复合唯一
- 删除唯一键约束的索引来删除唯一键约束，索引名默认是字段名，复合唯一默认是第一个字段名

###### 指定唯一键约束：

```sql
-- 建表时
create table 表名(
    字段名 数据类型 unique key,
    字段名 数据类型 unique key
);
-- 或
create table 表名(
    字段名1 数据类型,
    字段名2 数据类型,
    unique key(字段名1),
    unique key(字段名2)
);

-- 建表后
alter table 表名 add unique (字段名);
```

###### 复合唯一：

```sql
-- 多个字段的组合是唯一
create table 表名(
    字段名1 数据类型,
    字段名2 数据类型,  
    字段名3 数据类型,
    unique key(字段名1,字段名2,字段名3)
);
```

###### 查看唯一键约束：

```sql
desc 表名;
show create table 表名;
show index from 表名; -- 查看表的索引信息
select * from information_schema.table_constraints where table_name = '表名';
```

###### 删除唯一键约束：

```sql
-- 删除唯一键约束需要手动删除对应的索引
alter table 表名 drop index 索引名;
```

###### 示例：

```sql
-- 建表，限定编号、身份证号码和手机号码唯一
drop table if exists emp;
create table emp(
    id int unique key, -- 表示id字段值不能重复
    name varchar(20),
    cardid char(18),
    tel char(11),
    unique key(cardid), -- 表示cardid字段值不能重复
    unique key(tel) -- 表示tel字段值不能重复
);
desc emp;
show create table emp;
-- 添加数据
insert into emp values(1,'张三','25678544522222','13589587585');
insert into emp values(2,'张三','25678544522211','13589587596');
select * from emp;
insert into emp values(3,'李四','25678544522233','13589587596');
-- 手机号码重复，报错
insert into emp values
(3,'李四',null,null),
(4,'王五',null,null);
-- NULL可以重复
select * from emp;
-- 查看emp表的索引
show index from emp;
-- 删除唯一键约束
-- 如果在指定唯一键约束时，没有手动定义名字，默认就是字段名
-- 建议在删除时用show index语句查看一下索引名
-- 删除emp表的cardid的唯一键约束
alter table emp drop index cardid;
show index from emp;
desc emp;
-- 建表后给emp表的cardid增加唯一键约束
alter table emp add unique key(cardid);
desc emp;
show index from emp;

-- 复合唯一，表示两个或更多个字段值的组合唯一，单个字段看不唯一
-- 学生表
drop table if exists stu;
create table stu(
    id int,
    name varchar(20)
);
insert into stu values(1,'张三'),(2,'李四');
select * from stu;
-- 课程表
drop table if exists course;
create table course(
    id int,
    title varchar(50)
);
insert into course values(1,'python'),(2,'mysql');
select * from course;
-- 选课表
drop table if exists course;
create table xuanke(
    xid int unique key, -- xid不能重复
    sid int,
    cid int,
    score int,
    unique key(sid,cid)
    -- 这么写表示sid和cid的组合不能重复
    -- 单独看sid和cid是可以重复的
);
insert into xuanke values
(1,1,1,89),
(2,1,2,96),
(3,2,1,75),
(4,2,2,96);
select * from xuanke;
insert into xuanke values(5,1,1,100); -- sid为1和cid为1组合重复
desc xuanke;
show index from xuanke;
-- 组合唯一键索引名默认是unique key(字段1,字段2)的第一个字段名
-- 删除复合唯一键约束
alter table xuanke drop index sid;
desc xuanke;
show index from xuanke;
```

##### 主键约束

`primary key`：用来唯一的确定一条记录。

- 唯一并且非空
- 一个表最多只能有一个主键约束
- 如果主键是由多列组成，可以使用复合主键
- 主键列会自动创建索引（能够根据主键查询的，就根据主键查询，效率更高），mysql会给每个表的主键列创建索引，会开辟单独的物理空间来存储每一个主键的目录表（Btree结构）。这样可以根据主键快速查询到某一行的记录
- 如果删除主键约束了，主键约束对应的索引就自动删除了

唯一键约束和主键约束区别：

- 唯一键约束一个表可以有好几个，但是主键约束只有一个。
- 唯一键约束本身不带非空限制，如果需要非空，需要单独定义。主键约束不用再定义not null，自身就带非空限制。

###### 指定主键约束：

```sql
-- 建表时
create table 表名(
    字段名 数据类型 primary key,
    字段名 数据类型
); 
-- 或
create table 表名(
    字段名1 数据类型,
    字段名2 数据类型,  
    primary key(字段名1)
);

-- 建表后
alter table 表名 add primary key(字段列表);
-- 字段列表可以是一个字段，也可以是多个字段，如果是多个字段的话，是复合主键
```

###### 复合主键：

```sql
create table 表名(
    字段名1 数据类型,
    字段名2 数据类型,  
    字段名3 数据类型,
    primary key(字段名1,字段名2)
);
```

###### 删除主键约束：

```sql
alter table 表名 drop primary key;
```

###### 示例：

```sql
drop database if exists atguigu;
create database atguigu;
use atguigu;
-- 创建员工表
create table emp(
    id int primary key, -- 主键
    ename varchar(20) not null, -- 非空
    cardid char(18) unique key not null, -- 非空且唯一
    tel char(11) unique key, -- 唯一
    address varchar(100)
);
desc emp;
insert into emp values
(1,'张三','524265198235684255','18536955456',null),
(2,'李四','524265198235685255',null,null),
(3,'李四','524265198235685895',null,null);
select * from emp;
insert into emp values(3,'王五','524265198235675895',null,null); -- 主键重复
insert into emp values(null,'王五','524265198235675775',null,null); -- 主键为null
-- 创建一个表，两个字段设置主键，报错
create table xuanke(
    sid int primary key,
    cid int primary key,
    score int
);

-- 复合主键约束
-- 学生表
create table stu(
    id int,
    name varchar(20)
);
insert into stu values(1,'张三'),(2,'李四');
select * from stu;
-- 课程表
create table course(
    id int,
    title varchar(50)
);
insert into course values(1,'python'),(2,'mysql');
select * from course;
-- 选课表
create table xuanke(
    sid int,
    cid int,
    score int,
    primary key(sid,cid) -- 复合主键
);
insert into xuanke values(1,1,96),(2,1,85),(1,2,75),(2,2,45);
insert into xuanke values(1,1,75);
-- 报错，重复主键
-- 查看emp表和xuanke表的索引
show index from emp;
show index from xuanke;
-- 删除xuanke表的主键约束
alter table xuanke drop primary key;
show index from xuanke;
desc xuanke;
-- 删除主键约束时，对应的索引、键约束删除了，但是主键约束自带的非空约束没有删除
-- 如果要去掉的话，需要用删除非空约束的方式，单独删除
-- 建表后增加主键约束
alter table xuanke add primary key(sid,cid);
desc xuanke;
-- 删除emp的主键约束
alter table emp drop primary key;
desc emp;
-- 自动把cardid识别为主键，因为cardid定义了唯一键+非空约束，但是不同于真正的主键
show index from emp;
-- 给emp表的id字段增加主键约束
alter table emp add primary key(id);
show index from emp;
```

##### 自增约束

`auto_increment`：给某个字段自动赋值，这个值如无干扰每次+1。

- 一个表只能有一个自增字段，因为一个表只有一个AUTO_INCREMENT属性记录自增字段值
- 自增字段只能是**key字段，即定义了主键、唯一键等键约束**的字段
- 自增字段应该是数值类型，一般都是整数类型
- 如果自增列指定了0和null，会在当前最大值的基础上自增，如果自增列手动指定了具体值，直接赋值为具体值
- 如果手动修改AUTO_INCREMENT属性值，必须 > 当前自增字段的最大值

###### 指定自增约束：

```sql
-- 建表时
create table 表名(
    字段名 数据类型 primary key auto_increment,
    字段名 数据类型 unique key not null
);

-- 建表后
alter table 表名 modify 字段名 数据类型 auto_increment;
```

###### 删除自增约束：

```sql
alter table 表名 modify 字段名 数据类型;
-- 去掉auto_increment相当于删除
```

###### 示例：

```sql
drop table if exists emp;
create table emp(
    eid int auto_increment,
    ename varchar(20)
);
-- 报错，只能有一个自增字段且需为key字段
create table emp(
    eid int primary key auto_increment,
    ename varchar(20)
);
insert into emp(ename) values('李四'); -- 不给自增字段指定值，也是自增
insert into emp values(null,'张三'); -- 给自增字段赋值NULL，也是自增
insert into emp values(0,'王五');  -- 给自增字段赋值0，也是自增
select * from emp;
insert into emp values(-5,'王五');
insert into emp values(15,'田七');
select * from emp;
-- 当手动给自增字段赋值时
-- 如果这个值大于当前 AUTO_INCREMENT 属性记录的自增值时
-- 会修改 AUTO_INCREMENT 属性值
-- 下次就从这个值基础上自增
-- 建议不要随意修改 AUTO_INCREMENT 的值，让他自动维护
insert into emp values(7, '周八');
select * from emp;
-- 修改emp表 AUTO_INCREMENT 值为8
alter table emp AUTO_INCREMENT = 8;
show create table emp;
-- AUTO_INCREMENT值都不能修改为<当前自增字段最大的值
-- 删除eid字段的自增属性
alter table emp modify column eid int;
desc emp;
-- modify会影响列级约束，默认值、非空等约束
-- 表级约束（主键、唯一键）不受影响
-- 给eid字段的添加自增属性
alter table emp modify column eid int auto_increment;
desc emp;
```

##### 默认值约束

`default`：给某个字段/某列指定默认值，当添加时或修改时，可以使用默认值。

###### 指定默认值约束：

```sql
-- 建表时
create table 表名(
    字段名 数据类型 primary key,
    字段名 数据类型 unique key not null,
    字段名 数据类型 unique key,
    字段名 数据类型 not null default 默认值
);
-- 默认值约束一般不在唯一键和主键列上加

-- 建表后
alter table 表名 modify 字段名 数据类型 default 默认值;
```

###### 删除默认值约束：

```sql
alter table 表名 modify 字段名 数据类型;
-- 如果使用modify修改有默认值约束的字段时想要保留默认值约束，必须带上default 默认值
-- 否则会在修改时，把默认值约束丢掉
```

###### 示例：

```sql
drop table if exists emp;
create table emp(
    eid int primary key,
    ename varchar(20) not null,
    gender enum('男','女') default '男' not null, -- 非空并且有默认值
    address varchar(100) default '不详' -- 可以指定为null
);
insert into emp values(1,'张三'); -- 错误，值的数量和字段的数量不匹配
insert into emp(eid,ename) values(1,'张三');
insert into emp values(2,'李四',default,default);
insert into emp values(3,'王五',default,null);
select * from emp;
-- 删除emp表的address的默认值约束
alter table emp modify column address varchar(100);
desc emp;
-- 给emp表address增加 不详 默认值
alter table emp modify column address varchar(100) default '不详';
desc emp;
```

##### 检查约束

`check`：检查约束用于限制字段中的值的范围。如果对单个字段定义检查约束，那么该字段只允许特定范围的值。如果对一个表定义检查约束，那么此约束会基于行中其他字段的值在特定的字段中对值进行限制。

- 在MySQL 8.0.16版本之前，create table语句支持给单个字段定义检查约束的语法，但是不起作用。
- 在MySQL 8.0.16版本之后，create table语句既支持给单个字段定义列级检查约束，也支持定义表级检查约束。

###### 指定检查约束：

```sql
-- 建表时
create table 表名(
    字段名 数据类型 check(条件), -- 在字段后面直接加检查约束
    字段名 数据类型,
    字段名 数据类型,
    check (条件) enforced -- 可以限定两个字段之间的取值条件
);
-- 如果省略或指定为enforced，则会强制执行约束，不满足约束的数据行不能插入成功
-- 如果写not enforced，则不满足检查约束也没关系

-- 建表后
alter table 表名 add check(条件);
```

###### 删除检查约束：

```sql
alter table 表名 drop check 检查约束名;
```

###### 示例：

```sql
drop table if exists emp;
create table emp(
    id int primary key auto_increment,
    name varchar(20) not null,
    age int check(age>=18), -- 年龄>=18岁
    birthday date not null, -- 出生日期
    hiredate date not null, -- 入职日期
    check(year(hiredate)-year(birthday)>=18) -- 入职时>=18岁
);
insert into emp values(null,'张三',23,'2000-1-1','2021-11-30');
select * from emp;
insert into emp values(null,'张三',8,'2013-1-1','2021-11-30'); -- 不满足条件
insert into emp values(null,'张三',28,'2013-1-1','2021-11-30'); -- 不满足条件
desc emp;
show create table emp;
-- 查看emp表的约束
select * from information_schema.table_constraints where table_name = 'emp';
-- 只能看到主键、唯一键、外键、检查约束
-- 默认值、非空约束这里看不到
-- 删除emp表的age字段的检查约束 emp_chk_1 
-- 删除emp表的hiredate和birthday字段的检查约束 emp_chk_2
alter table emp drop check emp_chk_1;
alter table emp drop check emp_chk_2;
show create table emp;
-- 使用modify给age字段添加检查约束age>=18，不起作用
alter table emp modify age int check(age>=18); -- 语法没问题，但是没有真正起作用
insert into emp values(null,'李四',6,'1998-5-1','2021-1-2'); -- 添加成功，说明检查约束没有起作用
-- 使用add check给age字段添加检查约束age>=18
alter table emp add check(age>=18);
-- 因为表中有违反(age>=18)的数据，必须先处理
select * from emp;
update emp set age = 26 where age<18;
-- 使用add check给age字段添加检查约束age>=18
alter table emp add check(age>=18);
insert into emp values(null,'李四',6,'1998-5-1','2021-1-2');
```

##### 外键约束

`foreign key`：限**定某个表的某个字段的引用完整性，比如：员工表的员工所在部门的选择，必须在部门表能找到对应的部分。**

外键约束会影响性能，效率，所以很多人不愿意加外键约束。

建和不建外键约束有什么区别：

- 建外键约束，操作（创建表、删除表、添加、修改、删除）会受到限制，从语法层面受到限制。例如在员工表中不可能添加一个员工信息，它的部门的值在部门表中找不到。
- 不建外键约束，操作（创建表、删除表、添加、修改、删除）不受限制，要保证数据的引用完整性，只能依靠程序员的自觉，或者是在程序中进行限定。例如在员工表中，可以添加一个员工的信息，它的部门指定为一个完全不存在的部门。

主表和从表/父表和子表：

- 主表（父表）：被引用的表，被参考的表
- 从表（子表）：引用别人的表，参考别人的表

例如员工表与部门表。员工表的员工所在部门这个字段的值要参考部门表，部门表是主表，员工表是从表。例如学生表、课程表、选课表。选课表的学生和课程要分别参考学生表和课程表，学生表和课程表是主表，选课表是从表。

外键约束的特点：

- 在从表中指定外键约束，并且一个表可以建立多个外键约束
- 创建表时就指定外键约束的话，先创建主表，再创建从表
- 删表时，先删从表（或先删除外键约束），再删除主表。或者先解除关系，再各自删除
- 从表的外键列，必须引用/参考主表的键列（主键或唯一键），因为被依赖/被参考的值必须是唯一的
- 从表的外键列的数据类型，要与主表被参考/被引用的列的数据类型一致，并且逻辑意义一致。例如都是表示部门编号，都是int类型
- 外键列也会自动建立索引（根据外键查询效率更快）
- **外键约束删除后索引不会自动删除，如果要删除对应的索引，必须手动删除**

指定外键约束：

```sql
-- 建表时
create table 主表(
    字段1 数据类型 primary key,
    字段2 数据类型
);

create table 从表(
    字段1 数据类型 primary key,
    字段2 数据类型,
    foreign key (从表的某个字段) references 主表(被参考字段)
);
-- (从表的某个字段)的数据类型必须与主表(被参考字段)的数据类型一致，逻辑意义也一样
-- (从表的某个字段)的字段名可以与主表(被参考字段)的字段名不同

-- 建表后
alter table 从表 add foreign key (从表的字段) references 主表(被引用字段) [on update xx] [on delete xx];
```

查看外键约束：

```sql
desc 从表; -- 可以看到外键约束，但看不到外键约束名
show create table 从表; -- 可以看到外键约束名
select * from information_schema.table_constraints where table_name='表名';
-- information_schema数据库名(系统库)
-- table_constraints表名(专门存储各个表的约束)
```

查看外键字段索引：

```sql
show index from 表名;
```

删除外键约束：

```sql
-- 先查看约束名和删除外键约束
select * from information_schema.table_constraints where table_name='表名';
alter table 从表 drop foreign key 外键约束名;
-- 查看索引名和删除索引
show index from 表名;
alter table 从表 drop index 索引名;
```

示例：

```sql
drop table if exists dept;
create table dept(
    did int primary key auto_increment,
    dname varchar(50) unique key not null
);
drop table if exists emp;
create table emp(
    id int primary key auto_increment,
    name varchar(20) not null,
    departmentid int,
    -- 外键约束只能在字段列表下面单独定义，不能在字段后面直接定义
    foreign key (departmentid) references dept(did)
);
desc dept;
desc emp;
show create table dept;
show create table emp;
-- 查看系统库的约束表
select * from information_schema.table_constraints where table_name='emp';
-- 添加父表数据，没有影响
insert into dept values(null,'财务'),(null,'教学'),(null,'咨询'),(null,'后勤');
select * from dept;
-- 添加子表数据，有影响，受到约束
insert into emp values(null,'张三',1); -- 成功
insert into emp values(null,'李四',1); -- 成功
insert into emp values(null,'王五',2); -- 成功
insert into emp values(null,'赵六',6); -- 失败
-- departmentid=6在父表dept中找不到对应部门
select * from emp;
-- 修改子表的外键字段的信息，有影响，受到约束
update emp set departmentid = 3 where id=1; -- 成功
update emp set departmentid = 6 where id=3; -- 失败
-- departmentid=6在父表dept中找不到对应部门
select * from emp;
-- 修改父表的被引用字段的值，受约束
update dept set did = 6 where did=1; -- 失败
-- did=1的部门被子表引用
update dept set did = 6 where did=4; -- 成功
-- did=4的部门没有被子表引用
select * from dept;
-- 删除父表的记录，受约束
delete from dept where did=6; -- 成功
-- did=6的部门没有被子表引用
delete from dept where did=1; -- 失败
-- did=1的部门被子表引用
-- 删除子表的数据，不受约束
delete from emp where name='王五';
select * from emp;
-- 删除父表，受约束
drop table dept; -- 失败
-- 删除子表，不受约束
drop table emp;

-- 建表后添加外键约束
create table emp(
    id int primary key auto_increment,
    name varchar(20) not null,
    departmentid int
);
-- 给emp表(子表)增加外键约束
alter table emp add foreign key (departmentid) references dept(did);
-- 查看emp的约束信息
select * from information_schema.table_constraints where table_name='emp';
-- 键约束(主键、唯一键、外键)都会自动创建索引
-- 查看emp表的索引
show index from emp;
-- 主键字段索引名是PRIMARY，删除主键时，会自动删除对应索引
-- 唯一键字段索引名是字段名，删除唯一键时，就是通过删除对应的索引方式来删除唯一键约束
-- 外键字段索引名是字段名，删除外键约束时，不会自动删除外键字段的索引，因为它们的命名不一样
-- 删除emp表的departmentid字段的外键约束
alter table emp drop foreign key emp_ibfk_1;
show index from emp;
-- 删除emp表的departmentid字段的索引
alter table emp drop index departmentid;
show index from emp;
```

设置外键约束等级：

- Cascade方式：在父表上update/delete记录时，同步update/delete子表的匹配记录
- Set null方式：在父表上update/delete记录时，将子表上匹配记录的列设为null，但是要注意子表的外键列不能为not null
- No action方式：如果子表中有匹配的记录,则不允许对父表对应候选键进行update/delete操作
- Restrict方式：同no action，都是立即检查外键约束
- 如果没有指定等级，就相当于Restrict方式。

```sql
-- 创建父表
drop table if exists dept;
create table dept(
    did int primary key auto_increment,
    dname varchar(50) unique key not null
);
insert into dept values(null,'财务'),(null,'教学'),(null,'咨询'),(null,'后勤');
select * from dept;
-- 创建子表
drop table if exists emp;
create table emp(
    id int primary key auto_increment,
    name varchar(20) not null,
    departmentid int,
    foreign key (departmentid) references dept(did) on update cascade on delete set null
    -- on delete set null要求departmentid字段没有not null约束
);
-- 添加子表记录
insert into emp values
(null,'张三',1),
(null,'李四',2),
(null,'王五',1);
select * from emp;
-- 修改父表被引用的did值
update dept set did = 6 where did=1; 
-- 此时did=1的记录被子表引用，可以修改
-- 并且会同时修改子表的departmentid=1的字段值为6，级联修改
select * from dept;
select * from emp;
-- 删除父表被引用的did的记录
delete from dept where did=6;
select * from dept;
select * from emp;
```

#### 事务

##### 事务的特点（ACID）

事务处理：保证所有事务都作为一个工作单元来执行，即使出现了故障，都不能改变这种执行方式。当在一个事务中执行多个操作时，要么所有的事务都被提交(commit)，那么这些修改就永久地保存下来；要么数据库管理系统将放弃所作的所有修改，整个事务回滚(rollback)到最初状态。

事务的 ACID 属性：

| 属性 | 含义 |
|------|------|
| 原子性（Atomicity） | 事务是一个不可分割的工作单位，事务中的操作要么都发生，要么都不发生 |
| 一致性（Consistency） | 事务必须使数据库从一个一致性状态变换到另外一个一致性状态 |
| 隔离性（Isolation） | 一个事务的执行不能被其他事务干扰，并发执行的各个事务之间不能互相干扰 |
| 持久性（Durability） | 一个事务一旦被提交，它对数据库中数据的改变就是永久性的，接下来的其他操作和数据库故障不应该对其有任何影响 |

以"张三给李四转账500"为例理解 ACID（转账前张三、李四余额都是1000）：

- 原子性：成功时张三账号变为500、李四变为1500；失败时张三、李四还是1000，不会出现"只扣了张三的钱、没给李四加钱"的情况
- 一致性：要么两人余额都不变（总和2000），要么张三500、李四1500（总和还是2000）。出现"张三500、李四1000（总和1500）"就是错误结果
- 隔离性：张三要给李四转500、王五也要给李四转500，张三转账是否成功和王五是否转账成功无关
- 持久性：张三给李四转500，一旦成功提交就转账成功，撤不回来了

##### 事务的开启、提交、回滚

MySQL 默认情况下是自动提交事务。每一条语句都是一个独立的事务，一旦成功就提交了。一条语句失败，单独一条语句不生效，其他语句是生效的。

###### 手动提交模式

```sql
-- 开启手动提交事务模式
set autocommit=false;
-- 或
set autocommit=0;
-- 上述语句执行之后，它之后的所有SQL，都需要手动提交才能生效，直到恢复自动提交模式

-- 恢复自动提交模式
set autocommit=true;
-- 或
set autocommit=1;

-- 例如
set autocommit=false; -- 设置当前连接为手动提交模式
update t_employee set salary = 15000 where ename='孙红雷';
commit; -- 提交
-- 如果没有提交，直接关了连接，那么修改不会生效
```

###### 自动提交模式下开启事务

```sql
start transaction; -- 开始事务
update t_employee set salary = 0 where ename='李冰冰';
commit(或 rollback); -- 提交或回滚
-- start transaction ... commit/rollback 中的语句属于手动提交模式，其他的语句仍然是自动提交模式
```

###### DDL语句不支持事务

- DDL：create、drop、alter 等创建库、创建表、删除库、删除表、修改库、修改表结构等语句不支持事务
- 只对 insert、update、delete 语句支持事务
- truncate 不支持事务

##### 事务的隔离级别

数据库事务的隔离性：数据库系统必须具有隔离并发运行各个事务的能力，使它们不会相互影响，避免各种并发问题。一个事务与其他事务隔离的程度称为隔离级别。隔离级别越高，数据一致性就越好，但并发性越弱。

###### 并发问题

| 并发问题 | 说明 |
|---------|------|
| 脏读 | 一个事务读取了另一个事务未提交数据。对于两个事务T1、T2，T1 读取了已经被 T2 更新但还没有被提交的字段。之后若 T2 回滚，T1 读取的内容就是临时且无效的 |
| 不可重复读 | 同一个事务中前后两次读取同一条记录不一样。对于两个事务T1、T2，T1 读取了一个字段，然后 T2 更新/修改了该字段并提交。之后 T1 再次读取同一个字段，值就不同了 |
| 幻读 | 一个事务读取了另一个事务新增、删除的记录情况，记录数不一样，像是出现幻觉。对于两个事务T1、T2，T1 从一个表中读取了一个字段，然后 T2 在该表中插入/删除了一些新的行。之后如果 T1 再次读取同一个表，就会多/少几行 |

###### 四种事务隔离级别

| 隔离级别 | 说明 |
|---------|------|
| read-uncommitted（读未提交） | 允许 A 事务读取其他事务未提交和已提交的数据。会出现脏读、不可重复读、幻读问题 |
| read-committed（读已提交） | 只允许 A 事务读取其他事务已提交的数据。可以避免脏读，但仍然会出现不可重复读、幻读问题 |
| repeatable-read（可重复读） | 确保事务可以多次从一个字段中读取相同的值。在这个事务持续期间，禁止其他事务对这个字段进行更新。可以避免脏读和不可重复读，但是幻读问题仍然存在。注意：MySQL 中使用了 MVCC 多版本控制技术，在这个级别也可以避免幻读 |
| serializable（串行化） | 确保事务可以从一个表中读取相同的行，相同的记录。在这个事务持续期间，禁止其他事务对该表执行插入、更新、删除操作。所有并发问题都可以避免，但性能十分低下 |

> 隔离级别从低到高：read-uncommitted → read-committed → repeatable-read → serializable。级别越高一致性越好、并发性越弱。**MySQL 默认隔离级别是 repeatable-read（可重复读）**。

###### 修改与查看隔离级别

```sql
-- 先更改事务隔离级别，再开启事务
-- 修改隔离级别
set transaction_isolation='隔离级别';
-- 例如
set transaction_isolation='read-committed';

-- 查看隔离级别
select @@transaction_isolation;
```

#### 用户管理

##### 用户管理的目标

###### 登录验证

用户主机IP地址 + 用户名 + 密码三重验证。

- 用户主机IP 是客户端主机的IP，而非 MySQL 服务器的IP
- IP 地址可以是一个明确的IP（例如：192.168.1.25），可以是某个IP段（例如：192.168.1.%），可以是任意IP地址（%）

例如假设 MySQL 服务器的 IP 地址是 192.168.31.152：

| IP写法 | 含义 |
|--------|------|
| `192.168.31.%` | 192.168.31 网段内的客户端都可以连接到 192.168.31.152 机器上的 MySQL 服务 |
| `%` | 任意一台主机的客户端都可以连接到 192.168.31.152 机器上的 MySQL 服务 |
| `192.168.31.23` | 只能从 192.168.31.23 主机的客户端连接到 192.168.31.152 机器上的 MySQL 服务 |

###### 权限管理

权限从大到小分为：

- 全局权限
- 数据库权限
- 数据表权限
- 字段权限
- 存储过程或函数子程序的权限

对用户的操作进行逐级权限验证，如果上一级有这个权限，下一级就不再验证。

##### 用户管理演示

当具有权限管理的用户通过 Navicat 图形界面工具连接 MySQL 服务后，可以按照如下步骤进行用户和权限管理：

1. 步骤1：用户 → 可以选择新建用户，或者对已有用户进行编辑
2. 步骤2：如果要创建新用户，选择"新建用户"按钮，弹出新用户信息填写窗口。用户名和主机文本框必须填写，其他项可以不填写，按照默认值处理。如果密码和再一次输入密码框为空，表示密码为空。如果要设置密码必须保证密码框和再一次输入密码框输入相同字符，并在 Plugin 选择合适的插件 "caching_sha2_password" 或 "mysql_native_password"，默认是 "caching_sha2_password" 插件
3. 步骤3：对已有的用户进行授权操作，或撤销已有用户的授权，可以在权限相关的选项卡中，对相应权限打勾或者取消打勾

#### MySQL8部分新特性

##### 系统表全部为InnoDB表

从 MySQL8.0 开始，mysql 系统表和数据字典表使用 InnoDB 存储引擎，存储在 MySQL 数据目录下的 mysql.ibd 表空间文件中。在 MySQL5.7 之前，这些系统表使用 MyISAM 存储引擎，存储在 MySQL 数据库文件目录下各自的表空间文件中。

```sql
-- 查看系统表类型
SELECT DISTINCT(ENGINE) FROM information_schema.tables;
```

##### 默认字符集为utf8mb4

在 8.0 版本之前，MySQL 默认的字符集为 Latin1，而 8.0 版本默认字符集为 utf8mb4。

- Latin1 是 ISO-8859-1 的别名，有些环境下写作 Latin-1。ISO-8859-1 编码是单字节编码，不支持中文等多字节字符，但向下兼容 ASCII
- MySQL 中 utf8 字符集是 utf8mb3 的别称，使用三个字节编码表示一个字符，自 MySQL4.1 版本被引入，能够支持绝大多数语言的字符，但依然有些字符不能正确编码，如 emoji 表情字符等
- 为此 MySQL5.5 引入了 utf8mb4 字符集。mb4 就是 "mostbyte4" 的意思，专门用来兼容四字节的 Unicode，utf8mb4 编码是 utf8 编码的超集，兼容 utf8，并且能存储 4 字节的表情字符
- 如果原来某些库和表的字符集是 utf8，可以直接修改为 utf8mb4，不需要做其他转换。但是从 utf8mb4 转回 utf8 就会有问题

```sql
-- 查看 MySQL8.0 版本数据库的默认编码
SHOW VARIABLES LIKE 'character_set_database';
```

字符集校对规则是在字符集内用于字符比较和排序的一套规则，比如有的规则区分大小写，有的则无视。校对规则特征：

- 两个不同的字符集不能有相同的校对规则
- 每个字符集有一个默认校对规则
- 校对规则存在命名约定，以其相关的字符集名开始，中间包括一个语言名，并且以 _ci、_cs 或 _bin 结尾。其中 _ci 表示大小写不敏感、_cs 表示大小写敏感、bin 表示直接比较字符的二进制编码，即区分大小写

```sql
-- 查看 utf8mb4 字符集的部分校对规则
SHOW COLLATION LIKE 'utf8mb4_0900%';
```

##### 用户管理（MySQL8的变化）

- 在 MySQL8 之前默认的身份插件是 "mysql_native_password"，即 MySQL 用户的密码使用 PASSWORD 函数进行加密。在 MySQL 8.x 中，默认的身份认证插件是 "caching_sha2_password"，替代了之前的 "mysql_native_password"，PASSWORD 函数被弃用了
- 从 MySQL 5.6.6 版本起，在 mysql.user 表中添加了 "password_expired" 字段，它允许设置密码是否失效。如果 "password_lifetime" 字段值不为 NULL，那么从 MySQL 服务启动时间开始，经过 "password_lifetime" 字段值的时间间隔之后，密码就过期了，即 "password_expired" 字段就为 "Y"。任何密码超期的账号想要连接服务器端进行数据库操作都必须更改密码。MySQL8.0 版本允许数据库管理员手动设置账户密码过期时间
- 从 MySQL8.x 版本开始允许限制重复使用以前的密码
- 在 MySQL8 之前，如果要给多个用户授予相同的角色，需要为每个用户单独授权。在 MySQL8 之后，可以为多个用户赋予统一的角色，然后给角色授权即可，角色可以看成是一些权限的集合，这样就无须为每个用户单独授权。如果角色的权限修改，将会使得该角色下的所有用户的权限都跟着修改，这就非常方便

MySQL 的密码字段变化：

| 版本 | mysql 系统库 user 表的密码字段名 | 说明 |
|------|--------------------------------|------|
| MySQL5.7 之前 | password | 无角色概念 |
| MySQL5.7 | authentication_string | 无角色概念 |
| MySQL8.0 | authentication_string | 新增角色概念，mysql 系统库中有 default_roles 表 |

