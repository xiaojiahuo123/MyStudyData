"""
3. 无重复字符的最长子串 (Longest Substring Without Repeating Characters)

难度：medium

题目描述：
给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。

示例 1：s = "abcabcbb" → 3
示例 2：s = "bbbbb" → 1
示例 3：s = "pwwkew" → 3

链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring(" ") == 1
    print("全部通过")



if __name__ == "__main__":
    test()
