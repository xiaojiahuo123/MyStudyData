-- 排序练习
-- 查询所有学生记录，按年龄升序排序
SELECT sid,sname,age,gender 
FROM stu
ORDER BY age ASC

-- 查询所有雇员，按月薪降序排序，如果月薪相同时，按编号升序排序
SELECT * 
FROM emp
ORDER BY sal DESC,empno ASC


-- 分页查询(每页显示5条)
SELECT * FROM stu

-- 第一页
SELECT * FROM stu LIMIT 0,5

-- 第2页
SELECT * FROM stu LIMIT 5,5

-- 第3页
SELECT * FROM stu LIMIT 10,5





