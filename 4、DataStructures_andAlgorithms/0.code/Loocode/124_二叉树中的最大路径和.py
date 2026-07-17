"""
124. 二叉树中的最大路径和 (Binary Tree Maximum Path Sum)

难度：hard

题目描述：
给你一个二叉树的根节点 root，返回其最大路径和。路径可以不经过根节点。

示例 1：root = [1,2,3] → 6
示例 2：root = [-10,9,20,null,null,15,7] → 42

链接：https://leetcode.cn/problems/binary-tree-maximum-path-sum/
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
    assert s.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6
    assert s.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 42
    print("全部通过")



if __name__ == "__main__":
    test()
