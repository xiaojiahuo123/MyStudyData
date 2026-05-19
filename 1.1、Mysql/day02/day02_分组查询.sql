SELECT * FROM stu;
SELECT * FROM emp;
SELECT * FROM dept;

-- 聚合函数
-- 查询所有员工平均工资
SELECT empno FROM emp;
SELECT AVG(sal) FROM emp;
SELECT MAX(sal) FROM emp;
SELECT MIN(sal) FROM emp;
-- 查询所有员工工资总和
SELECT SUM(sal) FROM emp;
SELECT COUNT(empno) FROM emp;
SELECT COUNT(1) FROM emp;

-- 错误: empno多个数据,无法对应AVG(sal)单个数据
-- SELECT empno,AVG(sal) FROM emp;

-- 分组练习
-- 查询各部门的总人数
SELECT deptno,COUNT(1) 
FROM emp 
WHERE 1=1 
GROUP BY deptno

-- 查询deptno=10的部门总人数
SELECT COUNT(1) FROM emp WHERE deptno=20;

-- 查询所有员工人数
SELECT COUNT(1) FROM emp;

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

SELECT * FROM emp;

-- 查询每个部门的部门编号以及每个部门[工资大于1500的]人数
SELECT deptno '部门编号',COUNT(1) AS '部门人数'
FROM emp
WHERE sal > 1500
GROUP BY deptno

-- 查询工资总和大于9000的部门编号以及工资和
SELECT deptno,SUM(sal) AS sal_sum
FROM emp
WHERE 1=1
GROUP BY deptno
HAVING sal_sum > 9000
ORDER BY deptno
LIMIT n,m





