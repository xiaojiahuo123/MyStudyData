"""
103. 二叉树的锯齿形层序遍历 (Binary Tree Zigzag Level Order Traversal)

难度：medium

题目描述：
给你二叉树的根节点 root，返回其节点值的锯齿形层序遍历。

示例 1：root = [3,9,20,null,null,15,7] → [[3],[20,9],[15,7]]

链接：https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/
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
    assert s.zigzagLevelOrder(root) == [[3],[20,9],[15,7]]
    assert s.zigzagLevelOrder(TreeNode(1)) == [[1]]
    assert s.zigzagLevelOrder(None) == []
    print("全部通过")



if __name__ == "__main__":
    test()
