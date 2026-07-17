"""
10. 正则表达式匹配 (Regular Expression Matching)

难度：hard

题目描述：
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

示例 1：s = "aa", p = "a" → false
示例 2：s = "aa", p = "a*" → true
示例 3：s = "ab", p = ".*" → true

链接：https://leetcode.cn/problems/regular-expression-matching/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.isMatch("aa", "a") == False
    assert s.isMatch("aa", "a*") == True
    assert s.isMatch("ab", ".*") == True
    assert s.isMatch("aab", "c*a*b") == True
    assert s.isMatch("mississippi", "mis*is*p*.") == False
    print("全部通过")



if __name__ == "__main__":
    test()
