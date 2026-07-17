"""
35. 搜索插入位置 (Search Insert Position)

难度：easy

题目描述：
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

示例 1：nums = [1,3,5,6], target = 5 → 2
示例 2：nums = [1,3,5,6], target = 2 → 1
示例 3：nums = [1,3,5,6], target = 7 → 4

链接：https://leetcode.cn/problems/search-insert-position/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.searchInsert([1,3,5,6], 5) == 2
    assert s.searchInsert([1,3,5,6], 2) == 1
    assert s.searchInsert([1,3,5,6], 7) == 4
    assert s.searchInsert([1,3,5,6], 0) == 0
    print("全部通过")



if __name__ == "__main__":
    test()
