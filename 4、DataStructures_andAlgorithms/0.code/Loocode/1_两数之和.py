"""
1. 两数之和 (Two Sum)

难度：easy

题目描述：
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。

示例 1：nums = [2,7,11,15], target = 9 → [0,1]
示例 2：nums = [3,2,4], target = 6 → [1,2]
示例 3：nums = [3,3], target = 6 → [0,1]

链接：https://leetcode.cn/problems/two-sum/
"""

from typing import List, Optional


class Solution:
    def solve(self,nums: List[int],target: int) -> List[int]:
        # TODO: 请在这里实现你的解法
        index1,index2 = 0,0
        # for i,s in enumerate(nums):
            
        pass


def test():
    s = Solution()
    assert s.twoSum([2,7,11,15], 9) == [0,1]
    assert s.twoSum([3,2,4], 6) == [1,2]
    assert s.twoSum([3,3], 6) == [0,1]
    print("全部通过")



if __name__ == "__main__":
    test()
