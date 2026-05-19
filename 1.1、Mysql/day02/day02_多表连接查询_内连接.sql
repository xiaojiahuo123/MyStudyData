# 数据准备
CREATE TABLE a(
   aid INT,
   aname VARCHAR(10)
);

CREATE TABLE b(
   bid INT,
   bname VARCHAR(10)
);

INSERT INTO a VALUES(1,'aaaa'),(2,'bbbb'),(3,'cccc');
INSERT INTO b VALUES(4,'aaaa'),(2,'bbbb'),(3,'cccc');

SELECT aid,aname FROM a
UNION ALL
SELECT bid,bname FROM b;

-- 查询所有员工编号,员工姓名,员工的部门名称
SELECT 
	emp.empno,
	emp.ename,
	dept.dname 
FROM 
	emp,
	dept 
WHERE 
	emp.deptno = dept.deptno
-- 内连接(inner join  on)
SELECT 
	e.empno,
	e.ename,
	d.dname 
FROM 
	emp e INNER JOIN dept d 
ON 
	e.deptno = d.deptno






