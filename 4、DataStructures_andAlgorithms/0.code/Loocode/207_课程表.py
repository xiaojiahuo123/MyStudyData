"""
207. 课程表 (Course Schedule)

难度：medium

题目描述：
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1。在选修某些课程之前需要一些先修课程。判断是否可能完成所有课程的学习。

示例 1：numCourses = 2, prerequisites = [[1,0]] → true
示例 2：numCourses = 2, prerequisites = [[1,0],[0,1]] → false

链接：https://leetcode.cn/problems/course-schedule/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.canFinish(2, [[1,0]]) == True
    assert s.canFinish(2, [[1,0],[0,1]]) == False
    print("全部通过")



if __name__ == "__main__":
    test()
