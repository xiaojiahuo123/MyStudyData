"""
130. 被围绕的区域 (Surrounded Regions)

难度：medium

题目描述：
给你一个 m x n 的矩阵 board，由若干字符 'X' 和 'O' 组成，捕获所有被围绕的区域。

示例：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]] → [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

链接：https://leetcode.cn/problems/surrounded-regions/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    board1 = [list("XXXX"),list("XOOX"),list("XXOX"),list("XOXX")]
    s.solve(board1)
    assert board1 == [list("XXXX"),list("XXXX"),list("XXXX"),list("XOXX")]
    print("全部通过")



if __name__ == "__main__":
    test()
