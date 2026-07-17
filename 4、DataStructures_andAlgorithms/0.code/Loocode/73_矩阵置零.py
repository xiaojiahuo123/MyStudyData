"""
73. 矩阵置零 (Set Matrix Zeroes)

难度：medium

题目描述：
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列都设为 0。请使用原地算法。

示例：matrix = [[1,1,1],[1,0,1],[1,1,1]] → [[1,0,1],[0,0,0],[1,0,1]]

链接：https://leetcode.cn/problems/set-matrix-zeroes/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    m1 = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(m1)
    assert m1 == [[1,0,1],[0,0,0],[1,0,1]]
    m2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(m2)
    assert m2 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    print("全部通过")



if __name__ == "__main__":
    test()
