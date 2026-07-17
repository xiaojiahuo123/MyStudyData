"""
1143. 最长公共子序列 (Longest Common Subsequence)

难度：medium

题目描述：
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

示例 1：text1 = "abcde", text2 = "ace" → 3
示例 2：text1 = "abc", text2 = "abc" → 3
示例 3：text1 = "abc", text2 = "def" → 0

链接：https://leetcode.cn/problems/longest-common-subsequence/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.longestCommonSubsequence("abcde", "ace") == 3
    assert s.longestCommonSubsequence("abc", "abc") == 3
    assert s.longestCommonSubsequence("abc", "def") == 0
    print("全部通过")



if __name__ == "__main__":
    test()
