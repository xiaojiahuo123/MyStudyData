"""
104. 二叉树的最大深度 (Maximum Depth of Binary Tree)

难度：easy

题目描述：
给定一个二叉树 root，返回其最大深度。最大深度是指从根节点到最远叶子节点的最长路径上的节点数。

示例 1：root = [3,9,20,null,null,15,7] → 3
示例 2：root = [1,null,2] → 2

链接：https://leetcode.cn/problems/maximum-depth-of-binary-tree/
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
    assert s.maxDepth(root) == 3
    assert s.maxDepth(TreeNode(1, None, TreeNode(2))) == 2
    assert s.maxDepth(None) == 0
    print("全部通过")



if __name__ == "__main__":
    test()
