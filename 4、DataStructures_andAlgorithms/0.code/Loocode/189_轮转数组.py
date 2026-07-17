"""
189. 轮转数组 (Rotate Array)

难度：medium

题目描述：
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1：nums = [1,2,3,4,5,6,7], k = 3 → [5,6,7,1,2,3,4]
示例 2：nums = [-1,-100,3,99], k = 2 → [3,99,-1,-100]

约束：1 <= nums.length <= 10^5, -2^31 <= nums[i] <= 2^31 - 1, 0 <= k <= 10^5

链接：https://leetcode.cn/problems/rotate-array/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    nums1 = [1,2,3,4,5,6,7]; s.rotate(nums1, 3); assert nums1 == [5,6,7,1,2,3,4]
    nums2 = [-1,-100,3,99]; s.rotate(nums2, 2); assert nums2 == [3,99,-1,-100]
    print("全部通过")



if __name__ == "__main__":
    test()
