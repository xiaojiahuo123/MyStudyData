"""
543. 二叉树的直径 (Diameter of Binary Tree)

难度：easy

题目描述：
给你一棵二叉树的根节点，返回该树的直径。二叉树的直径是指树中任意两个节点之间最长路径的长度。

示例 1：root = [1,2,3,4,5] → 3
示例 2：root = [1,2] → 1

链接：https://leetcode.cn/problems/diameter-of-binary-tree/
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
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert s.diameterOfBinaryTree(root) == 3
    assert s.diameterOfBinaryTree(TreeNode(1, TreeNode(2))) == 1
    print("全部通过")



if __name__ == "__main__":
    test()
