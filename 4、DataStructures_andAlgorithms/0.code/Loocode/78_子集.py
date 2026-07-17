"""
78. 子集 (Subsets)

难度：medium

题目描述：
给你一个整数数组 nums，数组中的元素互不相同。返回该数组所有可能的子集。

示例 1：nums = [1,2,3] → [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：nums = [0] → [[],[0]]

链接：https://leetcode.cn/problems/subsets/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    result = s.subsets([1,2,3])
    result_sorted = sorted([sorted(x) for x in result])
    expected = sorted([sorted(x) for x in [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]])
    assert result_sorted == expected
    assert sorted([sorted(x) for x in s.subsets([0])]) == sorted([[], [0]])
    print("全部通过")



if __name__ == "__main__":
    test()
