"""
122. 买卖股票的最佳时机 II (Best Time to Buy and Sell Stock II)

难度：medium

题目描述：
给你一个整数数组 prices，其中 prices[i] 表示某支股票第 i 天的价格。在每一天，你可以决定是否购买和/或出售股票。返回 你能获得的最大利润。

示例 1：prices = [7,1,5,3,6,4] → 7
示例 2：prices = [1,2,3,4,5] → 4
示例 3：prices = [7,6,4,3,1] → 0

约束：1 <= prices.length <= 3 * 10^4, 0 <= prices[i] <= 10^4

链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.maxProfit([7,1,5,3,6,4]) == 7
    assert s.maxProfit([1,2,3,4,5]) == 4
    assert s.maxProfit([7,6,4,3,1]) == 0
    print("全部通过")



if __name__ == "__main__":
    test()
