"""
64. 最小路径和 (Minimum Path Sum)

难度：medium

题目描述：
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

示例 1：grid = [[1,3,1],[1,5,1],[4,2,1]] → 7
示例 2：grid = [[1,2,3],[4,5,6]] → 12

链接：https://leetcode.cn/problems/minimum-path-sum/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7
    assert s.minPathSum([[1,2,3],[4,5,6]]) == 12
    print("全部通过")



if __name__ == "__main__":
    test()
