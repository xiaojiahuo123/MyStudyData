"""
136. 只出现一次的数字 (Single Number)

难度：easy

题目描述：
给你一个非空整数数组 nums，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

示例 1：nums = [2,2,1] → 1
示例 2：nums = [4,1,2,1,2] → 4
示例 3：nums = [1] → 1

链接：https://leetcode.cn/problems/single-number/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.singleNumber([2,2,1]) == 1
    assert s.singleNumber([4,1,2,1,2]) == 4
    assert s.singleNumber([1]) == 1
    print("全部通过")



if __name__ == "__main__":
    test()
