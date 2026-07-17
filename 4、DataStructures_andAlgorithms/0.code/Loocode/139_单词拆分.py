"""
139. 单词拆分 (Word Break)

难度：medium

题目描述：
给你一个字符串 s 和一个字符串列表 wordDict，判断 s 是否可以被拆分为一个或多个在字典中出现的单词。

示例 1：s = "leetcode", wordDict = ["leet","code"] → true
示例 2：s = "applepenapple", wordDict = ["apple","pen"] → true
示例 3：s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] → false

链接：https://leetcode.cn/problems/word-break/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.wordBreak("leetcode", ["leet","code"]) == True
    assert s.wordBreak("applepenapple", ["apple","pen"]) == True
    assert s.wordBreak("catsandog", ["cats","dog","sand","and","cat"]) == False
    print("全部通过")



if __name__ == "__main__":
    test()
