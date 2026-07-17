"""
215. 数组中的第 K 个最大元素 (Kth Largest Element in an Array)

难度：medium

题目描述：
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

示例 1：nums = [3,2,1,5,6,4], k = 2 → 5
示例 2：nums = [3,2,3,1,2,4,5,5,6], k = 4 → 4

链接：https://leetcode.cn/problems/kth-largest-element-in-an-array/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.findKthLargest([3,2,1,5,6,4], 2) == 5
    assert s.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    print("全部通过")



if __name__ == "__main__":
    test()
