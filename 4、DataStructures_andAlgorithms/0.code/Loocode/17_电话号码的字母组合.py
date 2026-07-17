"""
17. 电话号码的字母组合 (Letter Combinations of a Phone Number)

难度：medium

题目描述：
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

示例 1：digits = "23" → ["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：digits = "" → []
示例 3：digits = "2" → ["a","b","c"]

链接：https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert sorted(s.letterCombinations("23")) == sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])
    assert s.letterCombinations("") == []
    assert s.letterCombinations("2") == ["a","b","c"]
    print("全部通过")



if __name__ == "__main__":
    test()
