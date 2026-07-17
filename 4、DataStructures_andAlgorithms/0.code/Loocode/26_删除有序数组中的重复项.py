"""
26. 删除有序数组中的重复项 (Remove Duplicates from Sorted Array)

难度：easy

题目描述：
给你一个 升序排列 的数组 nums，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

示例 1：nums = [1,1,2] → 2, nums = [1,2,_]
示例 2：nums = [0,0,1,1,1,2,2,3,3,4] → 5, nums = [0,1,2,3,4,_,_,_,_,_]

约束：1 <= nums.length <= 3 * 10^4, -10^4 <= nums[i] <= 10^4, nums 已按 升序 排列

链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    nums1 = [1,1,2]
    assert s.removeDuplicates(nums1) == 2
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    assert s.removeDuplicates(nums2) == 5
    print("全部通过")



if __name__ == "__main__":
    test()
