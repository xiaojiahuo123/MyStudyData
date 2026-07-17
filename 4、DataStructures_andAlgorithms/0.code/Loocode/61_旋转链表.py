"""
61. 旋转链表 (Rotate List)

难度：medium

题目描述：
给你一个链表的头节点 head，旋转链表，将链表每个节点向右移动 k 个位置。

示例 1：head = [1,2,3,4,5], k = 2 → [4,5,1,2,3]
示例 2：head = [0,1,2], k = 4 → [2,0,1]

链接：https://leetcode.cn/problems/rotate-list/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(node):
    r = []
    while node: r.append(node.val); node = node.next
    return r

def to_linked(lst):
    dummy = ListNode(); cur = dummy
    for v in lst: cur.next = ListNode(v); cur = cur.next
    return dummy.next

def test():
    s = Solution()
    assert to_list(s.rotateRight(to_linked([1,2,3,4,5]), 2)) == [4,5,1,2,3]
    assert to_list(s.rotateRight(to_linked([0,1,2]), 4)) == [2,0,1]
    print("全部通过")



if __name__ == "__main__":
    test()
