"""
149. 直线上最多的点数 (Max Points on a Line)

难度：hard

题目描述：
给你一个数组 points，其中 points[i] = [xi, yai] 表示 X-Y 平面上的一个点。返回最多有多少个点在同一条直线上。

示例 1：points = [[1,1],[2,2],[3,3]] → 3
示例 2：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] → 4

链接：https://leetcode.cn/problems/max-points-on-a-line/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.maxPoints([[1,1],[2,2],[3,3]]) == 3
    assert s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4
    print("全部通过")



if __name__ == "__main__":
    test()
