"""
97. 交错字符串 (Interleaving String)

难度：medium

题目描述：
给定三个字符串 s1、s2、s3，判断 s3 是否由 s1 和 s2 交错组成。

示例 1：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac" → true
示例 2：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc" → false

链接：https://leetcode.cn/problems/interleaving-string/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False
    assert s.isInterleave("", "", "") == True
    print("全部通过")



if __name__ == "__main__":
    test()
