"""
94. 二叉树的中序遍历 (Binary Tree Inorder Traversal)

难度：easy

题目描述：
给定一个二叉树的根节点 root，返回它的中序遍历。

示例 1：root = [1,null,2,3] → [1,3,2]
示例 2：root = [] → []
示例 3：root = [1] → [1]

链接：https://leetcode.cn/problems/binary-tree-inorder-traversal/
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
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert s.inorderTraversal(root) == [1,3,2]
    assert s.inorderTraversal(None) == []
    assert s.inorderTraversal(TreeNode(1)) == [1]
    print("全部通过")



if __name__ == "__main__":
    test()
