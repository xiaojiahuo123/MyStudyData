"""
20. 有效的括号 (Valid Parentheses)

难度：easy

题目描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判断字符串是否有效。

示例 1：s = "()" → true
示例 2：s = "()[]{}" → true
示例 3：s = "(]" → false
示例 4：s = "([)]" → false

链接：https://leetcode.cn/problems/valid-parentheses/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.isValid("()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("(]") == False
    assert s.isValid("([)]") == False
    assert s.isValid("{[]}") == True
    print("全部通过")



if __name__ == "__main__":
    test()
