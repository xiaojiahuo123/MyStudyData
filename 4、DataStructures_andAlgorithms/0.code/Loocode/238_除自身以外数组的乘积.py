"""
238. 除自身以外数组的乘积 (Product of Array Except Self)

难度：medium

题目描述：
给你一个整数数组 nums，返回数组 answer，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例 1：nums = [1,2,3,4] → [24,12,8,6]
示例 2：nums = [-1,1,0,-3,3] → [0,0,9,0,0]

约束：2 <= nums.length <= 10^5

链接：https://leetcode.cn/problems/product-of-array-except-self/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
    print("全部通过")



if __name__ == "__main__":
    test()
