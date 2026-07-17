"""
383. 赎金信 (Ransom Note)

难度：easy

题目描述：
给你两个字符串 ransomNote 和 magazine，判断 ransomNote 能不能由 magazine 里面的字符构成。

示例 1：ransomNote = "a", magazine = "b" → false
示例 2：ransomNote = "aa", magazine = "ab" → false
示例 3：ransomNote = "aa", magazine = "aab" → true

链接：https://leetcode.cn/problems/ransom-note/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.canConstruct("a", "b") == False
    assert s.canConstruct("aa", "ab") == False
    assert s.canConstruct("aa", "aab") == True
    print("全部通过")



if __name__ == "__main__":
    test()
