"""
34. 在排序数组中查找元素的第一个和最后一个位置 (Find First and Last Position of Element in Sorted Array)

难度：medium

题目描述：
给你一个按非递减顺序排列的整数数组 nums 和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

示例 1：nums = [5,7,7,8,8,10], target = 8 → [3,4]
示例 2：nums = [5,7,7,8,8,10], target = 6 → [-1,-1]
示例 3：nums = [], target = 0 → [-1,-1]

链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.searchRange([5,7,7,8,8,10], 8) == [3,4]
    assert s.searchRange([5,7,7,8,8,10], 6) == [-1,-1]
    assert s.searchRange([], 0) == [-1,-1]
    print("全部通过")



if __name__ == "__main__":
    test()
