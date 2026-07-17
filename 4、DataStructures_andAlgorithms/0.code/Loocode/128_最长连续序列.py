"""
128. 最长连续序列 (Longest Consecutive Sequence)

难度：medium

题目描述：
给定一个未排序的整数数组 nums，找出数字连续的最长序列的长度。

示例 1：nums = [100,4,200,1,3,2] → 4
示例 2：nums = [0,3,7,2,5,8,4,6,0,1] → 9

链接：https://leetcode.cn/problems/longest-consecutive-sequence/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.longestConsecutive([100,4,200,1,3,2]) == 4
    assert s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert s.longestConsecutive([]) == 0
    print("全部通过")



if __name__ == "__main__":
    test()
