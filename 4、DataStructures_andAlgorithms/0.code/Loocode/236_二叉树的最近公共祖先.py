"""
236. 二叉树的最近公共祖先 (Lowest Common Ancestor of a Binary Tree)

难度：medium

题目描述：
给定一个二叉树，找到该树中两个指定节点的最近公共祖先。

示例 1：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 → 3
示例 2：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 → 5

链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
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
    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
    p, q = root.left, root.right
    assert s.lowestCommonAncestor(root, p, q).val == 3
    assert s.lowestCommonAncestor(root, p, root.left.right).val == 5
    print("全部通过")



if __name__ == "__main__":
    test()
