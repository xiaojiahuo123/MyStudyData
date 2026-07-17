"""
210. 课程表 II (Course Schedule II)

难度：medium

题目描述：
现在你总共有 numCourses 门课需要选，返回你为了学完所有课程所安排的学习顺序。

示例 1：numCourses = 2, prerequisites = [[1,0]] → [0,1]
示例 2：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] → [0,2,1,3]

链接：https://leetcode.cn/problems/course-schedule-ii/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.findOrder(2, [[1,0]]) == [0,1]
    result = s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    assert set(result) == {0,1,2,3}
    assert result.index(0) < result.index(1)
    assert result.index(0) < result.index(2)
    assert result.index(1) < result.index(3)
    assert result.index(2) < result.index(3)
    print("全部通过")



if __name__ == "__main__":
    test()
