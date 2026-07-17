"""
133. 克隆图 (Clone Graph)

难度：medium

题目描述：
给你无向连通图中一个节点的引用，请你返回该图的深拷贝。

示例 1：adjList = [[2,4],[1,3],[2,4],[1,3]] → [[2,4],[1,3],[2,4],[1,3]]
示例 2：adjList = [[]] → [[]]
示例 3：adjList = [] → []

链接：https://leetcode.cn/problems/clone-graph/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def test():
    s = Solution()
    n1 = Node(1); n2 = Node(2); n3 = Node(3); n4 = Node(4)
    n1.neighbors = [n2,n4]; n2.neighbors = [n1,n3]; n3.neighbors = [n2,n4]; n4.neighbors = [n1,n3]
    clone = s.cloneGraph(n1)
    assert clone is not None
    assert clone.val == 1
    assert len(clone.neighbors) == 2
    print("全部通过")



if __name__ == "__main__":
    test()
