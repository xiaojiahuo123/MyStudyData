"""
198. 打家劫舍 (House Robber)

难度：medium

题目描述：
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金。相邻的房屋装有相互连通的防盗系统。给定一个代表每个房屋存放金额的数组，计算你在不触动警报装置的情况下能够偷窃到的最高金额。

示例 1：nums = [1,2,3,1] → 4
示例 2：nums = [2,7,9,3,1] → 12

链接：https://leetcode.cn/problems/house-robber/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.rob([1,2,3,1]) == 4
    assert s.rob([2,7,9,3,1]) == 12
    assert s.rob([2,1,1,2]) == 4
    print("全部通过")



if __name__ == "__main__":
    test()
