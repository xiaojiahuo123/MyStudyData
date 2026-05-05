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

![](.\image\image-20241227101748001.png)

## 2.3 Mysql服务连接

![](.\image\image-20241227105011725.png)

### 2.3.1 客户端

- Navicate
- **SQLyog**

### 2.3.2 命令行

- mysql自带命令行

- window命令行: mysql -u用户名   -p密码

  ![](.\image\image-20241227102317268.png)

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

> ```mysql
> create database 数据库名称; //创建新数据库
> ```
>
> ```MYSQL
> create database if not exists 数据库名称; //创建数据库前查询该库应该不存在
> //如果要避免自己新建的数据库已经存在，则：
> ```
>
> ```mysql
> CREATE DATABASE IF NOT EXISTS MySqlStudy_one;
> ```
>
> ```mysql
> CREATE DATABASE  数据库名 CHARACTER SET 字符集(utf8mb4) COLLATE  排序规则(utf8mb4_0900_ai_ci)； 
> ```
>
> 

### 4.1.2 查询数据库

> ```mysql
> #查看当前数据库服务器中的所有数据库
> **show databases;**
> 
> #查看前面创建的mydb2数据库的定义信息
> **show  create  database mydb2;**
> 
> #查看当前使用的数据库
> **select database();**
> 
> #查看指定库下所有表
> **SHOW TABLES FROM 数据库名;**
> ```
>
> 

### 4.1.3 修改数据库

> ```mysql
> alter database  数据库名称 character set 字符集 collate 排序规则
> ```
>
> 

### 4.1.4 删除数据库

> ```mysql
> drop database [if exists] 数据库名称
> ```
>
> 

### 4.1.5 切换数据库

> ```mysql
> use 数据库名称
> ```
>
> 

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

![image-20241227114938942](.\image\image-20241227114938942.png)

### 4.2.2 Mysql运算符

- - ```mysql
    算术运算符:不等于
    
    - !=
    - <>
    ```
  
    

## 4.3 操作数据库表

### 4.3.1 创建表

> ```mysql
> create table  表名(
> 
> ​	列名  数据类型  [约束],
> 
> ​	列名  数据类型  [约束],
> 
> ​	列名  数据类型  [约束]
> 
> )
> ```
>
> 

### 4.3.2 查看表

> ```mysql
> show tables from 数据库  #查询当前数据库中所有表
> 
> desc[describe] 表名: 查询表结构
> ```
>
> 

### 4.3.3 修改表

- ```mysql
  - 修改表中列
  
    - 添加一列:alter table 表名 add 新列名  新类型  [first|after  列名]
    - 修改表中的列类型: alter table 表名 modify  列名  新类型
    - 删除表中的列:alter table 表名  drop 列名
    - 修改列名:alter table 表名  change 原列名  新列名   新列名类型 
  
  - 修改表名
  
    > alter table 原表名 rename 新表名
  ```

  


### 4.3.4 删除表

> ```mysql
> drop table 表名
> ```
>
> 

# 5. Mysql客户端工具

## 5.1 Navicate

## 5.2 SQLyog

> 安装路径:非中文

![image-20241227142941631](.\image\image-20241227142941631.png)

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

  

## 7.3 单表分组查询(重点)

## 7.4 单表排序查询(重点)

## 7.5 单表分页查询(重点)

## 7.6 单表查询执行顺序

## 7.7 多表查询(见10)

# 8. 约束

# 9. 表与表之间关系

# 10. 多表连接查询(重点)

# 11. 事务(重点)

# 12. 权限管理(DCL)

# 13. 数据库备份