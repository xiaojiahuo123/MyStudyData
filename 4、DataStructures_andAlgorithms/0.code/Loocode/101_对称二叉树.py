"""
101. 对称二叉树 (Symmetric Tree)

难度：easy

题目描述：
给你一个二叉树的根节点 root，检查它是否轴对称。

示例 1：root = [1,2,2,3,4,4,3] → true
示例 2：root = [1,2,2,null,3,null,3] → false

链接：https://leetcode.cn/problems/symmetric-tree/
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
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert s.isSymmetric(root) == True
    root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert s.isSymmetric(root2) == False
    print("全部通过")



if __name__ == "__main__":
    test()
