# 1. Mysql概述

## 1.1 为什么使用数据库

- 信息时代数据为王,存储数据安全性及数据交互效率非常重要
- 使用数据库存储数据更安全,数据交互效率更高

## 1.2 数据库类型

### 1.2.1 关系型数据库

> 存储数据方式:数据库 -> 数据表  ->  数据

- Mysql
- Oracle
- SQLServer
- ...

### 1.2.2 非关系型数据库

> 存储数据方式:数据库  ->  数据(Key-Value)

- Redis
- MongoDB
- Hbase
- ...

## 1.3 DB与DBMS

- DB:DataBase直译数据库,数据库只是概念,数据库不能直接存储数据
- DBMS:DataBase Managerment System 直译数据库管理系统,使用数据库管理系统存储-查询-操作数据
  - 注意:程序员口中数据库指的是DBMS

# 2. 安装Mysql

## 2.1 Mysql下载及安装

### 2.1.1 官方网址

> https://dev.mysql.com/downloads/installer/

### 2.1.2 安装Mysql见(文档)

## 2.2 Mysql服务启动

### 2.2.1 linux系统启动mysql服务

- 启动服务:systemctl  start  mysqld
- 关闭服务:systemctl  stop mysqld

### 2.2.2 window启动mysql服务

![image-20241227101748001](01_Mysql.assets\image-20241227101748001.png)

## 2.3 Mysql服务连接

![image-20241227105011725](01_Mysql.assets\image-20241227105011725.png)

### 2.3.1 客户端

- Navicate
- **SQLyog**

### 2.3.2 命令行

- mysql自带命令行

- window命令行: mysql -u用户名   -p密码

  ![image-20241227102317268](01_Mysql.assets\image-20241227102317268.png)

# 3. SQL类型

> SQL：Structure Query Language。（结构化查询语言） 
>
> SQL:本质是操作数据库语言(标准语言-普通话)
>
> - SQL存在方言
> - mysql分页方言:limit
> - oracle分页方言:`ROWNUM` 是 Oracle 中的一个伪列

## 3.1 DDL:Data Definition  Language

- DDL:数据定义语言
- DDL作用:建库,建表,建约束等
  - create、alter、drop

## 3.2 DML:Data Manipulation  Language

- DML:数据操作语言
- DML作用:增,删,改数据
  - insert
  - delete
  - update

## 3.3 DQL:Data Query Language

- **DQL**:数据查询语言
- DQL作用:查询数据
  - selete

## 3.4 DCL:Data Control Language

- DCL:数据控制语言
- DCL作用:grant、revoke。

## 3.5 TCL:Transaction Control Language

- TCL:事务控制语言
- TCL作用:[开启-提交-回顾]事务
  - commit、rollback 。

# 4. DDL详解

## 4.1 操作数据库

### 4.1.1 创建数据库

> **create database 数据库名称**
>
> create database if not exists 数据库名称
>
> CREATE DATABASE  数据库名 CHARACTER SET 字符集(utf8mb4) COLLATE  排序规则(utf8mb4_0900_ai_ci)； 

### 4.1.2 查询数据库

> 查看当前数据库服务器中的所有数据库
>
> **show databases;**
>
> 查看前面创建的mydb2数据库的定义信息
>
> **show  create  database mydb2;**
> 查看当前使用的数据库
> **select database();**
> #查看指定库下所有表
> **SHOW TABLES FROM 数据库名;**

### 4.1.3 修改数据库

> alter database  数据库名称 character set 字符集 collate 排序规则

### 4.1.4 删除数据库

> drop database [if exists] 数据库名称

### 4.1.5 切换数据库

> use 数据库名称

## 4.2 数据类型及运算符

### 4.2.1 Mysql数据类型

- 数值型

  | 类型             | 大小                                     | 范围（有符号）                                   | 范围（无符/负号）           | 用途           |
  | ---------------- | ---------------------------------------- | ------------------------------------------------ | --------------------------- | -------------- |
  | [INT/INTEGER]()  | 4 字节                                   | (-2147483648，2147 483 647)                      | (0，4294967 295)            | 整数值         |
  | [TINYINT]()      | 1 字节                                   | (-128，127)                                      | (0，255)                    | 整数值         |
  | [SMALLINT]()     | 2 字节                                   | (-32768，32767)                                  | (0，65535)                  | 整数值         |
  | [MEDIUMINT]()    | 3 字节                                   | (-8388608，8388607)                              | (0，16777215)               | 整数值         |
  | [BIGINT]()       | 8 字节                                   | (-2^63,2^63-1)                                   | (0，2^64)                   | 整数值         |
  | [DOUBLE(M,D)]()  | 8个字节，M表示长度，D表示小数位数（4,2） | 同上，受M和D的约束   DOUBLE(16,2) -999.99-999.99 | 同上，受M和D的约束，M最大16 | 双精度浮点数值 |
  | [DECIMAL(M,D)]() | 16个字节，DECIMAL(M,D)                   | 依赖于M和D的值，M最大值为65                      | 依赖于M和D的值，M最大值为65 | 小数值         |

- 字符型

  | 类型        | 大小        | 用途                              |
  | ----------- | ----------- | --------------------------------- |
  | [CHAR]()    | 0-255字符   | 定长字符串  char(10) 10个字符     |
  | [VARCHAR]() | 0-65535字节 | 变长字符串  varchar(10)  10个字符 |

- 日期型

  | 类型          | 大小  | 格式                  | 范围                                                         | 用途                     |
  | ------------- | :---- | --------------------- | ------------------------------------------------------------ | ------------------------ |
  | [DATE]()      | 3字节 | YYYY-MM-DD            | 1000-01-01/9999-12-31  '2022-03-21'                          | 日期值                   |
  | [TIME]()      | 3字节 | HH:MM:SS              | '-838:59:59'/'838:59:59'  '17:24:20'                         | 时间值或持续时间         |
  | [YEAR]()      | 1字节 | YYYY                  | 1901/2155  ‘1990’  1990                                      | 年份值                   |
  | [DATETIME]()  | 8字节 | YYYY-MM-DD HH:MM:SS   | 1000-01-01 00:00:00/9999-12-31 23:59:59                      | 混合日期和时间值         |
  | [TIMESTAMP]() | 4字节 | YYYY-MM-DD HH：MM：SS | 1970-01-01 00:00:00/2038 结束时间是第 **2147483647** 秒北京时间 **2038-1-19 11:14:07**，格林尼治时间 2038年1月19日 凌晨 03:14:07 | 混合日期和时间值，时间戳 |

- 其他型

  | 类型     | 成员数 | 用途                            |
  | -------- | ------ | ------------------------------- |
  | [Enum]() | 65535  | 定义多个可选值,每次只能选择一个 |
  | [Set]()  | 64     | 定义多个可选值,每次可以选择多个 |

![image-20241227114938942](01_Mysql.assets\image-20241227114938942.png)

### 4.2.2 Mysql运算符

- 算术运算符:不等于
  - !=
  - <>

## 4.3 操作数据库表

### 4.3.1 创建表

> create table  表名(
>
> ​	列名  数据类型  [约束],
>
> ​	列名  数据类型  [约束],
>
> ​	列名  数据类型  [约束]
>
> )

### 4.3.2 查看表

> show tables from 数据库  #查询当前数据库中所有表
>
> desc[describe] 表名: 查询表结构

### 4.3.3 修改表

- 修改表中列

  - 添加一列:alter table 表名 add 新列名  新类型  [first|after  列名]
  - 修改表中的列类型: alter table 表名 modify  列名  新类型
  - 删除表中的列:alter table 表名  drop 列名
  - 修改列名:alter table 表名  change 原列名  新列名   新列名类型 

- 修改表名

  > alter table 原表名 rename 新表名

### 4.3.4 删除表

> drop table 表名

# 5. Mysql客户端工具

## 5.1 Navicate

## 5.2 SQLyog

> 安装路径:非中文

![image-20241227142941631](01_Mysql.assets\image-20241227142941631.png)

# 6. DML详解(重点)

> SQL语法
>
> - mysql中不区分大小写,一般语法推荐使用大写,库名表名列名等推荐使用小写
> - 插入数据时,非数值型都需要使用""或''括起来
>   - 推荐使用''

## 6.1 新增数据

```sql
create table t_emp(
    id int,
    name varchar(100),
    gender varchar(10),
    birthday date,
    salary double(10,2),
    entry_date date,
    resume text
);
```

```sql
-- 添加单条数据
insert into 表名(列名1,列名2,列名3...)  values(数值1,数值2,数值3...)

-- 添加多条数据
insert into 表名(列名1,列名2,列名3...)  values(数值1,数值2,数值3...),(数值1,数值2,数值3...),(数值1,数值2,数值3...);
```

## 6.2 修改数据

```sql
update 表名 set 列名 = 更新值,列名2 = 更新值2,...  [where 条件]
```

## 6.3 删除数据

```sql
delete from 表名 where 条件
```

# 7. DQL详解(重点)

## 7.1 单表普通查询

```sql
select 列名列表  from 表名
-- as关键字:为表或列定义别名,案例如下:
SELECT emp.id AS '员工编号',`name`,gender,birthday,salary,entry_date,`resume` FROM t_emp  emp;
-- 查询所有员工编号,员工姓名,员工薪资
SELECT id AS '员工编号',`name` '员工姓名',salary '员工薪资' FROM t_emp  emp;
```

## 7.2 单表条件查询

### 7.2.1 扩展运算符

> 范围运算符
>
> - 连续范围:between  and
> - 非连续范围:in
>
> 非空运算符
>
> - 判断空值:is null
> - 判断非空:is not null
>
> 不等于
>
> - !=
> - <>:推荐使用

### 7.2.2 案例

```sql

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
```

### 7.2.3 模糊查询

- 通配符

  - _:匹配**单个任意**字符
  - %:匹配**n个(n>=0)任意**字符

- 案例

  ```sql
  -- 查询员工姓名中包含i
  SELECT * FROM t_emp WHERE `name` LIKE '%i%' ;
  
  -- 查询员工姓名以'z'开头
  SELECT * FROM t_emp WHERE `name` LIKE 'z%' ;
  SELECT * FROM t_emp WHERE `name` LIKE 'z_' ;
  
  -- 查询员工姓'张'的员工信息
  SELECT * FROM t_emp WHERE `name` LIKE '张%' ;
  
  ```


### 7.2.4 分支条件查询

```sql
-- 查询员工工资,显示工资等级(sal>=4000:A   sal>=3000:B  sal>=2000:C sal<2000:D)

SELECT 
	empno,
	ename,
	CASE
		WHEN sal >= 4000 THEN 'A'
		WHEN sal >= 3000 THEN 'B'
		WHEN sal >= 2000 THEN 'C'
		ELSE 'D'
	END AS '工资等级'
FROM 
	emp
```

### 7.2.4 字段控制查询

- 去除重复数据

  ```sql
  -- 去除重复数据
  -- 查询员工工资(月薪情况:去除重复数据)
  SELECT DISTINCT sal FROM emp;
  ```

- ifnull()函数应用

  ```sql
  -- ifnull()练习
  -- 查询员工年薪(sal*12+comm)
  SELECT empno,ename,sal*12+IFNULL(comm,0) FROM emp;
  ```

## 7.3 单表分组查询(重点)

### 7.3.1 聚合函数

| 聚合函数 | 说明                     |
| -------- | ------------------------ |
| SUM()    | 求所有行中单列结果的总和 |
| AVG()    | 平均值                   |
| MAX()    | 最大值                   |
| MIN()    | 最小值  null当做0        |
| COUNT()  | 求总数  null不计数       |

### 7.3.2 分组查询

> 语法: group  by  列名(分组)  having  条件(分组)
>
> ```sql
> select  列名列表
> from  表名
> where 条件
> group by 列名
> having 条件(分组后)
> ```
>
> 作用: 查询条件中包含"各个","每个"等字样时,使用分组查询

- 分组查询案例

  ```sql
  -- 查询各部门的平均工资
  SELECT deptno '部门编号',AVG(sal) AS '平均工资'
  FROM emp
  WHERE 1=1
  GROUP BY deptno
  
  -- 查询各个部门、各个岗位的人数
  SELECT deptno '部门编号',COUNT(sal) AS '部门人数'
  FROM emp
  WHERE 1=1
  GROUP BY deptno,job
  ```

  

![]()

- 分组中条件

  - where:解决普通条件

  - having:解决聚合函数作为条件

    - 案例

      ```sql
      -- 查询工资总和大于9000的部门编号以及工资和
      SELECT deptno,SUM(sal)
      FROM emp
      WHERE 1=1
      GROUP BY deptno
      HAVING SUM(sal) > 9000
      ```

      

    ![image-20241228102201271](01_Mysql.assets\image-20241228102201271.png)

## 7.4 单表排序查询(重点)

> 语法: order  by  列名  asc(升序)|desc(降序)
>
> 作用: 排序
>
> 案例
>
> ```sql
> -- 查询所有学生记录，按年龄升序排序
> SELECT sid,sname,age,gender 
> FROM stu
> ORDER BY age ASC
> 
> -- 查询所有雇员，按月薪降序排序，如果月薪相同时，按编号升序排序
> SELECT * 
> FROM emp
> ORDER BY sal DESC,empno ASC
> ```

## 7.5 单表分页查询(重点)

### 7.5.1 为什么分页

- 提高用户体验度
- 减低服务器压力

### 7.5.2 如何实现分页

> - 分页实现是方言,不同数据库有不同实现方式
>
> - mysql数据库分页
>
>   - limit  n,m
>   - n:查询起始下标,下标从0开始
>   - m:每页显示条数
>
> - 案例
>
>   ```sql
>   -- 分页查询(每页显示5条)
>   SELECT * FROM stu
>   -- 第一页
>   SELECT * FROM stu LIMIT 0,5
>   -- 第2页
>   SELECT * FROM stu LIMIT 5,5
>   -- 第3页
>   SELECT * FROM stu LIMIT 10,5
>   ```

## 7.6 单表查询执行顺序

### 7.6.1 单表查询语法

> select 列名列表
>
> from 表名
>
> where 条件
>
> group by  列名(分组)
>
> having 条件(分组后)
>
> order  by   列名(排序)    [asc|desc降序]
>
> limit  n,m

### 7.6.2 查询顺序

```sql
版本一
[4]select 列名列表
[1]from 表名
[2]where 条件
[3]group by  列名(分组)
[5]having 条件(分组后)
[6]order  by   列名(排序)    [asc|desc降序]
[7]limit  n,m
版本二(AI)
[5]select 列名列表
[1]from 表名
[2]where 条件
[3]group by  列名(分组)
[4]having 条件(分组后)
[6]order  by   列名(排序)    [asc|desc降序]
[7]limit  n,m
```

![image-20241228111841009](01_Mysql.assets\image-20241228111841009.png)

## 7.7  函数扩展

### 7.7.1 时间函数

| 获取当前时间函数   | 描述                                   |
| ------------------ | :------------------------------------- |
| SYSDATE() \| NOW() | 当前系统时间（日、月、年、时、分、秒） |
| CURDATE()          | 获取当前日期                           |
| CURTIME()          | 获取当前时间                           |

| 提取时间数据  | 描述                                |
| ------------- | :---------------------------------- |
| WEEK(DATE)    | 获取指定日期为一年中的第几周        |
| YEAR(DATE)    | 获取指定日期的年份                  |
| HOUR(TIME)    | 获取指定时间的小时值                |
| MINUTE(TIME)  | 获取时间的分钟值                    |
| WEEKDAY(date) | 注意，周1是0，周2是1，。。。周日是6 |
| QUARTER(date) | 返回日期对应的季度，范围为1～4      |

| 时间运算函数                      | 描述                              |
| --------------------------------- | :-------------------------------- |
| DATEDIFF(DATE1,DATE2)             | 获取DATE1 和 DATE2 之间相隔的天数 |
| ADDDATE(date,INTERVAL expr  type) | 计算DATE 加上 N 个单位后的日期    |
| SUBDATE(date,INTERVAL expr  type) | 计算DATE 减去 N 天后的日期        |

| 时间格式函数          | 描述                          |
| --------------------- | :---------------------------- |
| DATE_FORMAT(date,fmt) | 按照字符串fmt格式化日期date值 |

| %Y   | 4位数字表示年份                                             | %y     | 表示两位数字表示年份                                        |
| ---- | ----------------------------------------------------------- | ------ | ----------------------------------------------------------- |
| %M   | 月名表示月份（January,....）                                | %m     | 两位数字表示月份（01,02,03。。。）                          |
| %b   | 缩写的月名（Jan.，Feb.，....）                              | %c     | 数字表示月份（1,2,3,...）                                   |
| %D   | 英文后缀表示月中的天数（1st,2nd,3rd,...）                   | %d     | 两位数字表示月中的天数(01,02...)                            |
| %e   | 数字形式表示月中的天数（1,2,3,4,5.....）                    |        |                                                             |
| %H   | 两位数字表示小数，24小时制（01,02..）                       | %h和%I | 两位数字表示小时，12小时制（01,02..）                       |
| %k   | 数字形式的小时，24小时制(1,2,3)                             | %l     | 数字形式表示小时，12小时制（1,2,3,4....）                   |
| %i   | 两位数字表示分钟（00,01,02）                                | %S和%s | 两位数字表示秒(00,01,02...)                                 |
| %W   | 一周中的星期名称（Sunday...）                               | %a     | 一周中的星期缩写（Sun.，Mon.,Tues.，..）                    |
| %w   | 以数字表示周中的天数(0=Sunday,1=Monday....)                 |        |                                                             |
| %j   | 以3位数字表示年中的天数(001,002...)                         | %U     | 以数字表示年中的第几周，（1,2,3。。）其中Sunday为周中第一天 |
| %u   | 以数字表示年中的第几周，（1,2,3。。）其中Monday为周中第一天 |        |                                                             |
| %T   | 24小时制                                                    | %r     | 12小时制                                                    |
| %p   | AM或PM                                                      | %%     | 表示%                                                       |

### 7.7.2 字符串函数

| 函数                            | 用法                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| CONCAT(S1,S2,......,Sn)         | 连接S1,S2,......,Sn为一个字符串                              |
| CONCAT_WS(s, S1,S2,......,Sn)   | 同CONCAT(s1,s2,...)函数，但是每个字符串之间要加上s           |
| CHAR_LENGTH(s)                  | 返回字符串s的字符数                                          |
| LENGTH(s)                       | 返回字符串s的字节数，和字符集有关                            |
| INSERT(str, index , len, instr) | 将字符串str从第index位置开始，len个字符长的子串替换为字符串instr |
| UPPER(s) 或 UCASE(s)            | 将字符串s的所有字母转成大写字母                              |
| LOWER(s)  或LCASE(s)            | 将字符串s的所有字母转成小写字母                              |
| LEFT(s,n)                       | 返回字符串s最左边的n个字符                                   |
| RIGHT(s,n)                      | 返回字符串s最右边的n个字符                                   |
| LPAD(str, len, pad)             | 用字符串pad对str最左边进行填充，直到str的长度为len个字符     |
| RPAD(str ,len, pad)             | 用字符串pad对str最右边进行填充，直到str的长度为len个字符     |
| LTRIM(s)                        | 去掉字符串s左侧的空格                                        |
| RTRIM(s)                        | 去掉字符串s右侧的空格                                        |
| TRIM(s)                         | 去掉字符串s开始与结尾的空格                                  |
| TRIM(【BOTH 】s1 FROM s)        | 去掉字符串s开始与结尾的s1                                    |
| TRIM(【LEADING】s1 FROM s)      | 去掉字符串s开始处的s1                                        |
| TRIM(【TRAILING】s1 FROM s)     | 去掉字符串s结尾处的s1                                        |
| REPEAT(str, n)                  | 返回str重复n次的结果                                         |
| REPLACE（str, " ", ""）         | 用字符串b替换字符串str中所有出现的字符串a                    |
| STRCMP(s1,s2)                   | 比较字符串s1,s2                                              |
| SUBSTRING(s,index,len)          | 返回从字符串s的index位置其len个字符                          |

### 7.7.3 数值函数

| 函数          | 用法                                 |
| ------------- | ------------------------------------ |
| ABS(x)        | 返回x的绝对值                        |
| CEIL(x)       | 返回大于x的最小整数值                |
| FLOOR(x)      | 返回小于x的最大整数值                |
| MOD(x,y)      | 返回x/y的模                          |
| RAND()        | 返回0~1的随机值                      |
| ROUND(x,y)    | 返回参数x的四舍五入的有y位的小数的值 |
| TRUNCATE(x,y) | 返回数字x截断为y位小数的结果         |
| SQRT(x)       | 返回x的平方根                        |
| POW(x,y)      | 返回x的y次方                         |

### 7.7.4 其他函数

| 函数          | 用法                                    |
| ------------- | --------------------------------------- |
| database()    | 返回当前数据库名                        |
| version()     | 返回当前数据库版本                      |
| user()        | 返回当前登录用户名                      |
| password(str) | 返回字符串str的加密版本，41位长的字符串 |
| md5(str)      | 返回字符串str的md5值，也是一种加密方式  |

### 7.7.5 MYSQL8窗口函数

```sql
-- mysql8版本窗口函数
SELECT empno,AVG(sal) OVER()  FROM  emp;
```

## 7.8 多表查询(见10)

# 8. 约束

## 8.1 实体完整性约束

### 8.1.1 主键约束

> 语法:PRIMARY KEY
>
> 特点: 唯一，标识表中的一行数据，此列的值不可重复，且不能为 NULL

### 8.1.2 唯一约束

> 语法:unique
>
> 特点:唯一，标识表中的一行数据，不可重复，可以为 NULL

### 8.1.3 自动增长列

> 语法:auto_increment
>
> 特点:自动增长,只能为int(整型)类型设置自增,每次增加1

## 8.2 域完整性约束

### 8.2.1 非空约束

> 语法:not null
>
> 特点:设置非空约束的列,不允许为空

### 8.2.2 默认值约束

> 语法:default
>
> 特点:设置默认值列,当列为null时,设置默认值

### 8.2.3 检查约束

> 语法:check
>
> 特点:设置检查约束,案例如下
>
> ```sql
> CREATE TABLE t_teachers(
> 	t_id INT PRIMARY KEY AUTO_INCREMENT,
> 	t_name VARCHAR(20) un`t_emp`,
> 	t_age INT DEFAULT 18,
> 	t_gender CHAR(2),
> 	CHECK(t_gender IN ('男','女'))	
> )
> ```

## 8.3 引用完整性约束（主外键约束）

> 语法：CONSTRAINT 引用名 FOREIGN KEY（列名） REFERENCES 被引用表名(列名)]()
>
> - 语法二:ALTER TABLE 外键表 ADD CONSTRAINT 约束名称 FOREIGN KEY(外键) REFERENCES 主表(主键);
>
> - 详解：FOREIGN KEY 引用外部表的某个列的值，新增数据时，约束此列的值必须是引用表中存在的值。
> - 特点
>   - 主表不能随意删除
>   - 从表不能随意添加&修改

# 9. 表与表之间关系

## 9.1 表之间对应关系

- 一对一

  - 夫妻
  - 国内合法公民与身份证
  - 私人物品

- 一对多

  - 员工与部门
  - 学校与学生
  - 班级与学生

  > 在[多的一方]添加[一的一方]id即可

  ![image-20241228154011780](01_Mysql.assets\image-20241228154011780.png)

- 多对多

  - 学生与老师(尚硅谷)

  - 公交车与乘客

  - ...

    > 多对多表关系中,如何建立表的对应关系?
    >
    > 答:需要创建第三方关联表,案例如下:

    ![image-20241228154832523](01_Mysql.assets\image-20241228154832523.png)

  ![image-20241228153618734](01_Mysql.assets\image-20241228153618734.png)

# 10. 多表连接查询(重点)

## 10.1 纵向连接查询

> 合并结果集:UNION 与 UNION  ALL
>
> - UNION:合并结果集,去除重复数据
> - UNION ALL:合并结果集,不去除重复数据
>
> 案例
>
> ```sql
> CREATE TABLE a(
>    aid INT,
>    aname VARCHAR(10)
> );
> CREATE TABLE b(
>    bid INT,
>    bname VARCHAR(10)
> );
> 
> INSERT INTO a VALUES(1,'aaaa'),(2,'bbbb'),(3,'cccc');
> INSERT INTO b VALUES(4,'aaaa'),(2,'bbbb'),(3,'cccc');
> 
> SELECT aid,aname FROM a
> UNION ALL
> SELECT bid,bname FROM b;
> ```

## 10.2 内连接

> - 语法
>
>   ```sql
>   -- 方式一
>   select 列名列表
>   from t1 inner join t2 
>   on t1.id=t2.id(主外键关系) 
>   -- 方式二
>   select 列名列表
>   from t1,t2 
>   where t1.id=t2.id(主外键关系) 
>   ```
>
> - 特点
>
>   - 内连接查询数据:当主键或外键数据为null时,不能查询该数据(**数据丢失**)

# 11. 事务(重点)

# 12. 权限管理(DCL)

# 13. 数据库备份