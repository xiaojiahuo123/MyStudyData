"""
98. 验证二叉搜索树 (Validate Binary Search Tree)

难度：medium

题目描述：
给你一个二叉树的根节点 root，判断其是否是一个有效的二叉搜索树。

示例 1：root = [2,1,3] → true
示例 2：root = [5,1,4,null,null,3,6] → false

链接：https://leetcode.cn/problems/validate-binary-search-tree/
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
    assert s.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))) == True
    assert s.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))) == False
    print("全部通过")



if __name__ == "__main__":
    test()
