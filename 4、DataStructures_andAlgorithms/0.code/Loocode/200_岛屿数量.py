"""
200. 岛屿数量 (Number of Islands)

难度：medium

题目描述：
给你一个由 '1'（陆地）和 '0'（水）组成的二维网格，请你计算网格中岛屿的数量。

示例 1：grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]] → 1
示例 2：grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]] → 3

链接：https://leetcode.cn/problems/number-of-islands/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    g1 = [list("11110"),list("11010"),list("11000"),list("00000")]
    assert s.numIslands(g1) == 1
    g2 = [list("11000"),list("11000"),list("00100"),list("00011")]
    assert s.numIslands(g2) == 3
    print("全部通过")



if __name__ == "__main__":
    test()
