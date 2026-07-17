"""
62. 不同路径 (Unique Paths)

难度：medium

题目描述：
一个机器人位于 m x n 网格的左上角。机器人每次只能向下或向右移动一步。问总共有多少条不同的路径。

示例 1：m = 3, n = 7 → 28
示例 2：m = 3, n = 2 → 3

链接：https://leetcode.cn/problems/unique-paths/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3
    assert s.uniquePaths(7, 3) == 28
    assert s.uniquePaths(3, 3) == 6
    print("全部通过")



if __name__ == "__main__":
    test()
