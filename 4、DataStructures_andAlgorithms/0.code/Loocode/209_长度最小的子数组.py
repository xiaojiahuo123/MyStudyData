"""
209. 长度最小的子数组 (Minimum Size Subarray Sum)

难度：medium

题目描述：
给定一个含有 n 个正整数的数组和一个正整数 target。找出该数组中满足其总和大于等于 target 的长度最小的连续子数组，并返回其长度。

示例 1：target = 7, nums = [2,3,1,2,4,3] → 2
示例 2：target = 4, nums = [1,4,4] → 1
示例 3：target = 11, nums = [1,1,1,1,1,1,1,1] → 0

链接：https://leetcode.cn/problems/minimum-size-subarray-sum/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.minSubArrayLen(7, [2,3,1,2,4,3]) == 2
    assert s.minSubArrayLen(4, [1,4,4]) == 1
    assert s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0
    print("全部通过")



if __name__ == "__main__":
    test()
