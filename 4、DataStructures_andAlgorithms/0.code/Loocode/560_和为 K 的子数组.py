"""
560. 和为 K 的子数组 (Subarray Sum Equals K)

难度：medium

题目描述：
给你一个整数数组 nums 和一个整数 k，请你统计并返回该数组中和为 k 的子数组的个数。

示例 1：nums = [1,1,1], k = 2 → 2
示例 2：nums = [1,2,3], k = 3 → 2

链接：https://leetcode.cn/problems/subarray-sum-equals-k/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.subarraySum([1,1,1], 2) == 2
    assert s.subarraySum([1,2,3], 3) == 2
    assert s.subarraySum([1], 0) == 0
    print("全部通过")



if __name__ == "__main__":
    test()
