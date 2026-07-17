"""
76. 最小覆盖子串 (Minimum Window Substring)

难度：hard

题目描述：
给你一个字符串 s、一个字符串 t。返回 s 中涵盖 t 所有字符的最小子串。

示例 1：s = "ADOBECODEBANC", t = "ABC" → "BANC"
示例 2：s = "a", t = "a" → "a"
示例 3：s = "a", t = "aa" → (空字符串)

链接：https://leetcode.cn/problems/minimum-window-substring/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("a", "a") == "a"
    assert s.minWindow("a", "aa") == ""
    print("全部通过")



if __name__ == "__main__":
    test()
