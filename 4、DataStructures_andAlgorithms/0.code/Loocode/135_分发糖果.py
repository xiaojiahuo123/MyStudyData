"""
135. 分发糖果 (Candy)

难度：hard

题目描述：
n 个孩子站成一排。给你一个整数数组 ratings，表示每个孩子的评分。你需要给每个孩子分发糖果，规则：每个孩子至少分配到 1 个糖果；相邻两个孩子评分更高的孩子会获得更多的糖果。返回需要准备的最少糖果数目。

示例 1：ratings = [1,0,2] → 5
示例 2：ratings = [1,2,2] → 4

链接：https://leetcode.cn/problems/candy/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.candy([1,0,2]) == 5
    assert s.candy([1,2,2]) == 4
    print("全部通过")



if __name__ == "__main__":
    test()
