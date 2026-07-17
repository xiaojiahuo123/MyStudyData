"""
188. 买卖股票的最佳时机 IV (Best Time to Buy and Sell Stock IV)

难度：hard

题目描述：
给定一个整数数组 prices 和整数 k，返回你最多可以完成 k 笔交易的最大利润。

示例 1：k = 2, prices = [2,4,1] → 2
示例 2：k = 2, prices = [3,2,6,5,0,3] → 7

链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.maxProfit(2, [2,4,1]) == 2
    assert s.maxProfit(2, [3,2,6,5,0,3]) == 7
    print("全部通过")



if __name__ == "__main__":
    test()
