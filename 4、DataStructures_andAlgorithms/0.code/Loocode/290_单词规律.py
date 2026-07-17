"""
290. 单词规律 (Word Pattern)

难度：easy

题目描述：
给定一种规律 pattern 和一个字符串 s，判断 s 是否遵循相同的规律。

示例 1：pattern = "abba", s = "dog cat cat dog" → true
示例 2：pattern = "abba", s = "dog cat cat fish" → false
示例 3：pattern = "aaaa", s = "dog cat cat dog" → false

链接：https://leetcode.cn/problems/word-pattern/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.wordPattern("abba", "dog cat cat dog") == True
    assert s.wordPattern("abba", "dog cat cat fish") == False
    assert s.wordPattern("aaaa", "dog cat cat dog") == False
    assert s.wordPattern("abba", "dog dog dog dog") == False
    print("全部通过")



if __name__ == "__main__":
    test()
