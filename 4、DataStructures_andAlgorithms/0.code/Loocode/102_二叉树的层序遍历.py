"""
102. 二叉树的层序遍历 (Binary Tree Level Order Traversal)

难度：medium

题目描述：
给你二叉树的根节点 root，返回其节点值的层序遍历。

示例 1：root = [3,9,20,null,null,15,7] → [[3],[9,20],[15,7]]
示例 2：root = [1] → [[1]]
示例 3：root = [] → []

链接：https://leetcode.cn/problems/binary-tree-level-order-traversal/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test():
    s = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert s.levelOrder(root) == [[3],[9,20],[15,7]]
    assert s.levelOrder(TreeNode(1)) == [[1]]
    assert s.levelOrder(None) == []
    print("全部通过")



if __name__ == "__main__":
    test()
