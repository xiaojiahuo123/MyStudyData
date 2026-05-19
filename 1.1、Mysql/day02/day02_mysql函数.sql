-- 扩展
-- 分支查询
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

-- 去除重复数据
-- 查询员工工资(月薪情况:去除重复数据)
SELECT DISTINCT sal FROM emp;

-- ifnull()练习
-- 查询员工年薪(sal*12+comm)
SELECT empno,ename,sal*12+IFNULL(comm,0) FROM emp;

-- 函数练习
SELECT SYSDATE();
SELECT CURTIME();
SELECT WEEK(SYSDATE());
SELECT WEEKDAY(SYSDATE())+1;

SELECT ename,hiredate FROM emp 
WHERE hiredate 
BETWEEN STR_TO_DATE('1980-1-1', '%Y-%m-%d') 
AND STR_TO_DATE('1980-12-31', '%Y-%m-%d')

-- 字符串函数
SELECT CONCAT_WS('_','hello','world');
SELECT SUBSTRING('helloworld',6,5);
SELECT RIGHT('helloworld',5);
SELECT LEFT('helloworld',5);

-- 数值函数
SELECT CEIL(2.5);
SELECT FLOOR(2.5);
SELECT RAND();
-- 获取四位随机数
SELECT FLOOR(RAND()*10000);

SELECT RIGHT(RAND(),6);

SELECT VERSION();

-- mysql8版本窗口函数
SELECT empno,AVG(sal) OVER()  FROM  emp;





