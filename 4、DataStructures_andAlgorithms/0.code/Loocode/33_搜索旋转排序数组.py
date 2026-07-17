"""
33. 搜索旋转排序数组 (Search in Rotated Sorted Array)

难度：medium

题目描述：
整数数组 nums 按升序排列，数组中的值互不相同。在传递给函数之前，nums 在预先未知的某个下标上进行了旋转。给你一个目标值 target，如果 nums 中存在这个目标值，则返回它的索引，否则返回 -1。

示例 1：nums = [4,5,6,7,0,1,2], target = 0 → 4
示例 2：nums = [4,5,6,7,0,1,2], target = 3 → -1

链接：https://leetcode.cn/problems/search-in-rotated-sorted-array/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.search([4,5,6,7,0,1,2], 0) == 4
    assert s.search([4,5,6,7,0,1,2], 3) == -1
    assert s.search([1], 0) == -1
    print("全部通过")



if __name__ == "__main__":
    test()
