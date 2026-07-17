"""
31. 下一个排列 (Next Permutation)

难度：medium

题目描述：
整数数组的一个排列就是将其所有成员以序列或线性顺序排列。给你一个整数数组 nums，找出 nums 的下一个排列。

示例 1：nums = [1,2,3] → [1,3,2]
示例 2：nums = [3,2,1] → [1,2,3]
示例 3：nums = [1,1,5] → [1,5,1]

链接：https://leetcode.cn/problems/next-permutation/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    nums1 = [1,2,3]; s.nextPermutation(nums1); assert nums1 == [1,3,2]
    nums2 = [3,2,1]; s.nextPermutation(nums2); assert nums2 == [1,2,3]
    nums3 = [1,1,5]; s.nextPermutation(nums3); assert nums3 == [1,5,1]
    print("全部通过")



if __name__ == "__main__":
    test()
