"""
289. 生命游戏 (Game of Life)

难度：medium

题目描述：
给定一个 m x n 网格，每个细胞处于活(1)或死(0)状态。根据以下规则更新状态：
1. 活细胞周围有 2 或 3 个活细胞则存活
2. 死细胞周围恰好有 3 个活细胞则复活
3. 其他情况死亡/保持死亡

链接：https://leetcode.cn/problems/game-of-life/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    b1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    s.gameOfLife(b1)
    assert b1 == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    b2 = [[1,1],[1,0]]
    s.gameOfLife(b2)
    assert b2 == [[1,1],[1,1]]
    print("全部通过")



if __name__ == "__main__":
    test()
