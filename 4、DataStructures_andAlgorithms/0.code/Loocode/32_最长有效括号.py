"""
32. 最长有效括号 (Longest Valid Parentheses)

难度：hard

题目描述：
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：s = "(()" → 2
示例 2：s = ")()())" → 4
示例 3：s = "" → 0

链接：https://leetcode.cn/problems/longest-valid-parentheses/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.longestValidParentheses("(()") == 2
    assert s.longestValidParentheses(")()())") == 4
    assert s.longestValidParentheses("") == 0
    print("全部通过")



if __name__ == "__main__":
    test()
