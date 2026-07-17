"""
22. 括号生成 (Generate Parentheses)

难度：medium

题目描述：
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

示例 1：n = 3 → ["((()))","(()())","(())()","()(())","()()()"]
示例 2：n = 1 → ["()"]

链接：https://leetcode.cn/problems/generate-parentheses/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert sorted(s.generateParenthesis(3)) == sorted(["((()))","(()())","(())()","()(())","()()()"])
    assert s.generateParenthesis(1) == ["()"]
    print("全部通过")



if __name__ == "__main__":
    test()
