"""
684. 冗余连接 (Redundant Connection)

难度：medium

题目描述：
有一棵 n 个节点的树，节点编号为 1 到 n。再给你一条额外的边。找到一条可以删去的多余边，使剩余的边构成一棵 n 个节点的树。

示例 1：edges = [[1,2],[1,3],[2,3]] → [2,3]
示例 2：edges = [[1,2],[2,3],[3,4],[1,4],[1,5]] → [1,4]

链接：https://leetcode.cn/problems/redundant-connection/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.findRedundantConnection([[1,2],[1,3],[2,3]]) == [2,3]
    assert s.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1,4]
    print("全部通过")



if __name__ == "__main__":
    test()
