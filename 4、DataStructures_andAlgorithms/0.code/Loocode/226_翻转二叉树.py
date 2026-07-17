"""
226. 翻转二叉树 (Invert Binary Tree)

难度：easy

题目描述：
给你一棵二叉树的根节点 root，翻转这棵二叉树，并返回其根节点。

示例 1：root = [4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
示例 2：root = [2,1,3] → [2,3,1]

链接：https://leetcode.cn/problems/invert-binary-tree/
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

def tree_to_list(root):
    if not root: return []
    r, q = [], [root]
    while q:
        node = q.pop(0)
        if node: r.append(node.val); q.append(node.left); q.append(node.right)
        else: r.append(None)
    while r and r[-1] is None: r.pop()
    return r

def test():
    s = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    assert tree_to_list(s.invertTree(root)) == [4,7,2,9,6,3,1]
    assert tree_to_list(s.invertTree(TreeNode(2, TreeNode(1), TreeNode(3)))) == [2,3,1]
    print("全部通过")



if __name__ == "__main__":
    test()
