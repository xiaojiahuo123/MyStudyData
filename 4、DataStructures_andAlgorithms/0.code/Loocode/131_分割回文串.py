"""
131. 分割回文串 (Palindrome Partitioning)

难度：medium

题目描述：
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。返回 s 所有可能的分割方案。

示例 1：s = "aab" → [["a","a","b"],["aa","b"]]
示例 2：s = "a" → [["a"]]

链接：https://leetcode.cn/problems/palindrome-partitioning/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.partition("aab") == [["a","a","b"],["aa","b"]]
    assert s.partition("a") == [["a"]]
    print("全部通过")



if __name__ == "__main__":
    test()
