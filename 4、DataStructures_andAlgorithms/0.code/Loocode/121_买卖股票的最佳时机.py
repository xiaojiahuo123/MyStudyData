"""
121. 买卖股票的最佳时机 (Best Time to Buy and Sell Stock)

难度：easy

题目描述：
给定一个数组 prices，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出。返回你所能获取的最大利润。

示例 1：prices = [7,1,5,3,6,4] → 5
示例 2：prices = [7,6,4,3,1] → 0

约束：1 <= prices.length <= 10^5, 0 <= prices[i] <= 10^4

链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.maxProfit([7,1,5,3,6,4]) == 5
    assert s.maxProfit([7,6,4,3,1]) == 0
    print("全部通过")



if __name__ == "__main__":
    test()
