"""
300. 最长递增子序列 (Longest Increasing Subsequence)

难度：medium

题目描述：
给你一个整数数组 nums，找到其中最长严格递增子序列的长度。

示例 1：nums = [10,9,2,5,3,7,101,18] → 4
示例 2：nums = [0,1,0,3,2,3] → 4
示例 3：nums = [7,7,7,7,7,7,7] → 1

链接：https://leetcode.cn/problems/longest-increasing-subsequence/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert s.lengthOfLIS([0,1,0,3,2,3]) == 4
    assert s.lengthOfLIS([7,7,7,7,7,7,7]) == 1
    print("全部通过")



if __name__ == "__main__":
    test()
