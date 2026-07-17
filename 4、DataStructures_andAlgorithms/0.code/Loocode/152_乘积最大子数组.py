"""
152. 乘积最大子数组 (Maximum Product Subarray)

难度：medium

题目描述：
给你一个整数数组 nums，请你找出数组中乘积最大的非空连续子数组，并返回该子数组所对应的乘积。

示例 1：nums = [2,3,-2,4] → 6
示例 2：nums = [-2,0,-1] → 0

链接：https://leetcode.cn/problems/maximum-product-subarray/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.maxProduct([2,3,-2,4]) == 6
    assert s.maxProduct([-2,0,-1]) == 0
    assert s.maxProduct([-2]) == -2
    print("全部通过")



if __name__ == "__main__":
    test()
