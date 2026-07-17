"""
221. 最大正方形 (Maximal Square)

难度：medium

题目描述：
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] → 4

链接：https://leetcode.cn/problems/maximal-square/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4
    assert s.maximalSquare([["0"]]) == 0
    assert s.maximalSquare([["1"]]) == 1
    print("全部通过")



if __name__ == "__main__":
    test()
