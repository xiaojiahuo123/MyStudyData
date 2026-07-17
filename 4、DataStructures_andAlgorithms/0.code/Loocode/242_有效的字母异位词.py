"""
242. 有效的字母异位词 (Valid Anagram)

难度：easy

题目描述：
给定两个字符串 s 和 t，判断 t 是否是 s 的字母异位词。

示例 1：s = "anagram", t = "nagaram" → true
示例 2：s = "rat", t = "car" → false

链接：https://leetcode.cn/problems/valid-anagram/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") == True
    assert s.isAnagram("rat", "car") == False
    print("全部通过")



if __name__ == "__main__":
    test()
