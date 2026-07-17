"""
54. 螺旋矩阵 (Spiral Matrix)

难度：medium

题目描述：
给你一个 m 行 n 列的矩阵 matrix，请按照顺时针螺旋顺序返回矩阵中的所有元素。

示例 1：matrix = [[1,2,3],[4,5,6],[7,8,9]] → [1,2,3,6,9,8,7,4,5]
示例 2：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] → [1,2,3,4,8,12,11,10,9,5,6,7]

链接：https://leetcode.cn/problems/spiral-matrix/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    print("全部通过")



if __name__ == "__main__":
    test()
