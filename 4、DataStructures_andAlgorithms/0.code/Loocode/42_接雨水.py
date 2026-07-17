"""
42. 接雨水 (Trapping Rain Water)

难度：hard

题目描述：
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：height = [0,1,0,2,1,0,1,3,2,1,2,1] → 6
示例 2：height = [4,2,0,3,2,5] → 9

链接：https://leetcode.cn/problems/trapping-rain-water/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert s.trap([4,2,0,3,2,5]) == 9
    print("全部通过")



if __name__ == "__main__":
    test()
