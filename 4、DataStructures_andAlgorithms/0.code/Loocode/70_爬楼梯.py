"""
70. 爬楼梯 (Climbing Stairs)

难度：easy

题目描述：
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶？

示例 1：n = 2 → 2
示例 2：n = 3 → 3

链接：https://leetcode.cn/problems/climbing-stairs/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(1) == 1
    assert s.climbStairs(10) == 89
    print("全部通过")



if __name__ == "__main__":
    test()
