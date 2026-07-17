"""
5. 最长回文子串 (Longest Palindromic Substring)

难度：medium

题目描述：
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：s = "babad" → "bab"
示例 2：s = "cbbd" → bb

链接：https://leetcode.cn/problems/longest-palindromic-substring/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.longestPalindrome("babad") in ["bab", "aba"]
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("a") == "a"
    print("全部通过")



if __name__ == "__main__":
    test()
