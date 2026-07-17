"""
4. 寻找两个正序数组的中位数 (Median of Two Sorted Arrays)

难度：hard

题目描述：
给定两个大小分别为 m 和 n 的正序数组 nums1 和 nums2，请你找出并返回这两个正序数组的中位数。算法的时间复杂度应该为 O(log (m+n))。

示例 1：nums1 = [1,3], nums2 = [2] → 2.00000
示例 2：nums1 = [1,2], nums2 = [3,4] → 2.50000

链接：https://leetcode.cn/problems/median-of-two-sorted-arrays/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.findMedianSortedArrays([1,3], [2]) == 2.0
    assert s.findMedianSortedArrays([1,2], [3,4]) == 2.5
    print("全部通过")



if __name__ == "__main__":
    test()
