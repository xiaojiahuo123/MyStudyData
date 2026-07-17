"""
74. 搜索二维矩阵 (Search a 2D Matrix)

难度：medium

题目描述：
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。

示例 1：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 → true
示例 2：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 → false

链接：https://leetcode.cn/problems/search-a-2d-matrix/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
    assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False
    print("全部通过")



if __name__ == "__main__":
    test()
