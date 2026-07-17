"""
205. 同构字符串 (Isomorphic Strings)

难度：easy

题目描述：
给定两个字符串 s 和 t，判断它们是否是同构的。

示例 1：s = "egg", t = "add" → true
示例 2：s = "foo", t = "bar" → false
示例 3：s = "paper", t = "title" → true

链接：https://leetcode.cn/problems/isomorphic-strings/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.isIsomorphic("egg", "add") == True
    assert s.isIsomorphic("foo", "bar") == False
    assert s.isIsomorphic("paper", "title") == True
    assert s.isIsomorphic("badc", "baba") == False
    print("全部通过")



if __name__ == "__main__":
    test()
