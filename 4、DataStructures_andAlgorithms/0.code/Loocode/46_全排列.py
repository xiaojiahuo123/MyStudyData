"""
46. 全排列 (Permutations)

难度：medium

题目描述：
给定一个不含重复数字的数组 nums，返回其所有可能的全排列。

示例 1：nums = [1,2,3] → [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：nums = [0,1] → [[0,1],[1,0]]
示例 3：nums = [1] → [[1]]

链接：https://leetcode.cn/problems/permutations/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert sorted([sorted(x) for x in s.permute([1,2,3])]) == sorted([sorted(x) for x in [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]])
    assert sorted([sorted(x) for x in s.permute([0,1])]) == sorted([sorted(x) for x in [[0,1],[1,0]]])
    assert s.permute([1]) == [[1]]
    print("全部通过")



if __name__ == "__main__":
    test()
