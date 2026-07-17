"""
637. 二叉树的层平均值 (Average of Levels in Binary Tree)

难度：easy

题目描述：
给定一个非空二叉树的根节点 root，返回每一层节点值的平均值。

示例：root = [3,9,20,null,null,15,7] → [3.00000,14.50000,11.00000]

链接：https://leetcode.cn/problems/average-of-levels-in-binary-tree/
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
    result = s.averageOfLevels(root)
    assert abs(result[0] - 3.0) < 1e-5
    assert abs(result[1] - 14.5) < 1e-5
    assert abs(result[2] - 11.0) < 1e-5
    print("全部通过")



if __name__ == "__main__":
    test()
