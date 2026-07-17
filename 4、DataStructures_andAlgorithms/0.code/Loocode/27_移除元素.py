"""
27. 移除元素 (Remove Element)

难度：easy

题目描述：
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

示例 1：nums = [3,2,2,3], val = 3 → 2, nums = [2,2,_,_]
示例 2：nums = [0,1,2,2,3,0,4,2], val = 2 → 5, nums = [0,1,4,0,3,_,_,_]

约束：0 <= nums.length <= 100, 0 <= nums[i] <= 50, 0 <= val <= 100

链接：https://leetcode.cn/problems/remove-element/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    nums1 = [3,2,2,3]
    assert s.removeElement(nums1, 3) == 2
    nums2 = [0,1,2,2,3,0,4,2]
    assert s.removeElement(nums2, 2) == 5
    print("全部通过")



if __name__ == "__main__":
    test()
