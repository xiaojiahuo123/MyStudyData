"""
48. 旋转图像 (Rotate Image)

难度：medium

题目描述：
给定一个 n x n 的矩阵 matrix，将它顺时针旋转 90 度。你必须在原地旋转。

示例 1：matrix = [[1,2,3],[4,5,6],[7,8,9]] → [[7,4,1],[8,5,2],[9,6,3]]
示例 2：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] → [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

链接：https://leetcode.cn/problems/rotate-image/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(m1)
    assert m1 == [[7,4,1],[8,5,2],[9,6,3]]
    m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    s.rotate(m2)
    assert m2 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print("全部通过")



if __name__ == "__main__":
    test()
