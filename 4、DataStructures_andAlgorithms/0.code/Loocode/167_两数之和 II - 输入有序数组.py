"""
167. 两数之和 II - 输入有序数组 (Two Sum II - Input Array Is Sorted)

难度：medium

题目描述：
给你一个下标从 1 开始的整数数组 numbers，已按非递减顺序排列，请你从数组中找出满足相加之和等于目标数 target 的两个数。

示例 1：numbers = [2,7,11,15], target = 9 → [1,2]
示例 2：numbers = [2,3,4], target = 6 → [1,3]

链接：https://leetcode.cn/problems/two-sum-ii---input-array-is-sorted/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.twoSum([2,7,11,15], 9) == [1,2]
    assert s.twoSum([2,3,4], 6) == [1,3]
    assert s.twoSum([-1,0], -1) == [1,2]
    print("全部通过")



if __name__ == "__main__":
    test()
