"""
392. 判断子序列 (Is Subsequence)

难度：easy

题目描述：
给定字符串 s 和 t，判断 s 是否为 t 的子序列。

示例 1：s = "abc", t = "ahbgdc" → true
示例 2：s = "axc", t = "ahbgdc" → false

链接：https://leetcode.cn/problems/is-subsequence/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.isSubsequence("abc", "ahbgdc") == True
    assert s.isSubsequence("axc", "ahbgdc") == False
    assert s.isSubsequence("", "ahbgdc") == True
    print("全部通过")



if __name__ == "__main__":
    test()
