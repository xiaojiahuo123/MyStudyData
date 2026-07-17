"""
79. 单词搜索 (Word Search)

难度：medium

题目描述：
给定一个 m x n 二维字符网格 board 和一个字符串单词 word。如果 word 存在于网格中，返回 true。

示例 1：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED" → true
示例 2：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE" → true
示例 3：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB" → false

链接：https://leetcode.cn/problems/word-search/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert s.exist([row[:] for row in board1], "ABCCED") == True
    assert s.exist([row[:] for row in board1], "SEE") == True
    assert s.exist([row[:] for row in board1], "ABCB") == False
    print("全部通过")



if __name__ == "__main__":
    test()
