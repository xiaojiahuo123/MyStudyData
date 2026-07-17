"""
30. 串联所有单词的子串 (Substring with Concatenation of All Words)

难度：hard

题目描述：
给定一个字符串 s 和一个字符串数组 words。找出 s 中恰好可以串联所有 words 中单词的子串的起始索引。

示例 1：s = "barfoothefoobarman", words = ["foo","bar"] → [0,9]
示例 2：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"] → []
示例 3：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"] → [6,9,12]

链接：https://leetcode.cn/problems/substring-with-concatenation-of-all-words/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert sorted(s.findSubstring("barfoothefoobarman", ["foo","bar"])) == sorted([0,9])
    assert s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == []
    assert sorted(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])) == sorted([6,9,12])
    print("全部通过")



if __name__ == "__main__":
    test()
