"""
416. 分割等和子集 (Partition Equal Subset Sum)

难度：medium

题目描述：
给你一个只包含正整数的非空数组 nums。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：nums = [1,5,11,5] → true
示例 2：nums = [1,2,3,5] → false

链接：https://leetcode.cn/problems/partition-equal-subset-sum/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.canPartition([1,5,11,5]) == True
    assert s.canPartition([1,2,3,5]) == False
    assert s.canPartition([1,1]) == True
    print("全部通过")



if __name__ == "__main__":
    test()
