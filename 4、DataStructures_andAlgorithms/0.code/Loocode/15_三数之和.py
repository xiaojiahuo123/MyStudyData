"""
15. 三数之和 (3Sum)

难度：medium

题目描述：
给你一个整数数组 nums，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j != k 且 nums[i] + nums[j] + nums[k] == 0。返回所有和为 0 且不重复的三元组。

示例 1：nums = [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]
示例 2：nums = [0,1,1] → []
示例 3：nums = [0,0,0] → [[0,0,0]]

链接：https://leetcode.cn/problems/3sum/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert sorted(s.threeSum([-1,0,1,2,-1,-4])) == sorted([[-1,-1,2],[-1,0,1]])
    assert s.threeSum([0,1,1]) == []
    assert s.threeSum([0,0,0]) == [[0,0,0]]
    print("全部通过")



if __name__ == "__main__":
    test()
