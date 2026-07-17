"""
39. 组合总和 (Combination Sum)

难度：medium

题目描述：
给你一个无重复元素的整数数组 candidates 和一个目标整数 target。找出可以使数字和为目标数 target 的所有不同组合。candidates 中的数字可以无限制重复被选取。

示例 1：candidates = [2,3,6,7], target = 7 → [[2,2,3],[7]]
示例 2：candidates = [2,3,5], target = 8 → [[2,2,2,2],[2,3,3],[3,5]]

链接：https://leetcode.cn/problems/combination-sum/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert sorted(s.combinationSum([2,3,6,7], 7)) == sorted([[2,2,3],[7]])
    assert sorted(s.combinationSum([2,3,5], 8)) == sorted([[2,2,2,2],[2,3,3],[3,5]])
    assert s.combinationSum([2], 1) == []
    print("全部通过")



if __name__ == "__main__":
    test()
