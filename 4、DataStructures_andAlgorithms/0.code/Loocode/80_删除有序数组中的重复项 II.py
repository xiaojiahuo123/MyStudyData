"""
80. 删除有序数组中的重复项 II (Remove Duplicates from Sorted Array II)

难度：medium

题目描述：
给你一个有序数组 nums，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次，返回删除后数组的新长度。

示例 1：nums = [1,1,1,2,2,3] → 5, nums = [1,1,2,2,3,_]
示例 2：nums = [0,0,1,1,1,1,2,3,3] → 7, nums = [0,0,1,1,2,3,3,_,_]

约束：1 <= nums.length <= 3 * 10^4, -10^4 <= nums[i] <= 10^4, nums 已按 升序 排列

链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    nums1 = [1,1,1,2,2,3]
    assert s.removeDuplicates(nums1) == 5
    nums2 = [0,0,1,1,1,1,2,3,3]
    assert s.removeDuplicates(nums2) == 7
    print("全部通过")



if __name__ == "__main__":
    test()
