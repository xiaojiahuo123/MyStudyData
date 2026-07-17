"""
199. 二叉树的右视图 (Binary Tree Right Side View)

难度：medium

题目描述：
给定一个二叉树的根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1：root = [1,2,3,null,5,null,4] → [1,3,4]
示例 2：root = [1,null,3] → [1,3]
示例 3：root = [] → []

链接：https://leetcode.cn/problems/binary-tree-right-side-view/
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
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert s.rightSideView(root) == [1,3,4]
    assert s.rightSideView(TreeNode(1, None, TreeNode(3))) == [1,3]
    assert s.rightSideView(None) == []
    print("全部通过")



if __name__ == "__main__":
    test()
