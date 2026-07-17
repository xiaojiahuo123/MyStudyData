"""
52. N 皇后 II (N-Queens II)

难度：hard

题目描述：
n 皇后问题：在 n×n 的棋盘上放置 n 个皇后，使得它们互不攻击。返回不同的解决方案的数量。

示例 1：n = 4 → 2
示例 2：n = 1 → 1

链接：https://leetcode.cn/problems/n-queens-ii/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.totalNQueens(4) == 2
    assert s.totalNQueens(1) == 1
    print("全部通过")



if __name__ == "__main__":
    test()
