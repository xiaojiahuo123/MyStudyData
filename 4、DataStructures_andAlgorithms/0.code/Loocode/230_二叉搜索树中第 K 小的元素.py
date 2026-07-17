"""
230. 二叉搜索树中第 K 小的元素 (Kth Smallest Element in a BST)

难度：medium

题目描述：
给定一个二叉搜索树的根节点 root 和一个整数 k，请设计一个算法查找其中第 k 个最小元素。

示例 1：root = [3,1,4,null,2], k = 1 → 1
示例 2：root = [5,3,6,2,4,null,null,1], k = 3 → 3

链接：https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
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
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert s.kthSmallest(root, 1) == 1
    root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    assert s.kthSmallest(root2, 3) == 3
    print("全部通过")



if __name__ == "__main__":
    test()
