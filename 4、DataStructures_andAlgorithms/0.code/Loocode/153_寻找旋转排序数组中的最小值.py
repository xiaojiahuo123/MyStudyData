"""
153. 寻找旋转排序数组中的最小值 (Find Minimum in Rotated Sorted Array)

难度：medium

题目描述：
给你一个元素互不相同的已旋转的排序数组 nums，返回其中的最小元素。

示例 1：nums = [3,4,5,1,2] → 1
示例 2：nums = [4,5,6,7,0,1,2] → 0
示例 3：nums = [11,13,15,17] → 11

链接：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.findMin([3,4,5,1,2]) == 1
    assert s.findMin([4,5,6,7,0,1,2]) == 0
    assert s.findMin([11,13,15,17]) == 11
    print("全部通过")



if __name__ == "__main__":
    test()
