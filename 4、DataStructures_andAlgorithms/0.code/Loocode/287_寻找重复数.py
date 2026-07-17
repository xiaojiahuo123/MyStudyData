"""
287. 寻找重复数 (Find the Duplicate Number)

难度：medium

题目描述：
给定一个包含 n + 1 个整数的数组 nums，其数字都在 [1, n] 范围内（包括 1 和 n）。假设 nums 只有 一个重复的整数，返回这个重复的数。

示例 1：nums = [1,3,4,2,2] → 2
示例 2：nums = [3,1,3,4,2] → 3

链接：https://leetcode.cn/problems/find-the-duplicate-number/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.findDuplicate([1,3,4,2,2]) == 2
    assert s.findDuplicate([3,1,3,4,2]) == 3
    print("全部通过")



if __name__ == "__main__":
    test()
