"""
322. 零钱兑换 (Coin Change)

难度：medium

题目描述：
给你一个整数数组 coins 和一个整数 amount。返回凑成总金额所需的最少的硬币个数。如果无法凑成，返回 -1。

示例 1：coins = [1, 2, 5], amount = 11 → 3
示例 2：coins = [2], amount = 3 → -1
示例 3：coins = [1], amount = 0 → 0

链接：https://leetcode.cn/problems/coin-change/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.coinChange([1,2,5], 11) == 3
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([1], 0) == 0
    assert s.coinChange([1,2,5], 100) == 20
    print("全部通过")



if __name__ == "__main__":
    test()
