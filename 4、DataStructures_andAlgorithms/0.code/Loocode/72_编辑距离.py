"""
72. 编辑距离 (Edit Distance)

难度：medium

题目描述：
给你两个单词 word1 和 word2，请返回将 word1 转换成 word2 所使用的最少操作数。你可以进行插入、删除、替换一个字符的操作。

示例 1：word1 = "horse", word2 = "ros" → 3
示例 2：word1 = "intention", word2 = "execution" → 5

链接：https://leetcode.cn/problems/edit-distance/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.minDistance("horse", "ros") == 3
    assert s.minDistance("intention", "execution") == 5
    assert s.minDistance("", "a") == 1
    print("全部通过")



if __name__ == "__main__":
    test()
