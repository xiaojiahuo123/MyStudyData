"""
219. 存在重复元素 II (Contains Duplicate II)

难度：easy

题目描述：
给你一个整数数组 nums 和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums[i] == nums[j] 且 abs(i - j) <= k。

示例 1：nums = [1,2,3,1], k = 3 → true
示例 2：nums = [1,0,1,1], k = 1 → true
示例 3：nums = [1,2,3,1,2,3], k = 2 → false

链接：https://leetcode.cn/problems/contains-duplicate-ii/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.containsNearbyDuplicate([1,2,3,1], 3) == True
    assert s.containsNearbyDuplicate([1,0,1,1], 1) == True
    assert s.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False
    print("全部通过")



if __name__ == "__main__":
    test()
