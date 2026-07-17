"""
502. IPO (IPO)

难度：hard

题目描述：
给你 n 个项目。给定利润数组 profits 和资本数组 capitals。初始资本为 w。最多只能做 k 个项目。返回最终可以获得的最大资本。

示例 1：k = 2, w = 0, profits = [1,2,3], capitals = [0,1,1] → 4
示例 2：k = 3, w = 0, profits = [1,2,3], capitals = [0,1,2] → 6

链接：https://leetcode.cn/problems/ipo/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]) == 4
    assert s.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]) == 6
    print("全部通过")



if __name__ == "__main__":
    test()
