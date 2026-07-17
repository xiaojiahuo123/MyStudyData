"""
92. 反转链表 II (Reverse Linked List II)

难度：medium

题目描述：
给你单链表的头指针 head 和两个整数 left 和 right，其中 left <= right。反转从位置 left 到位置 right 的链表节点。

示例 1：head = [1,2,3,4,5], left = 2, right = 4 → [1,4,3,2,5]
示例 2：head = [5], left = 1, right = 1 → [5]

链接：https://leetcode.cn/problems/reverse-linked-list-ii/
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
    assert to_list(s.reverseBetween(to_linked([1,2,3,4,5]), 2, 4)) == [1,4,3,2,5]
    assert to_list(s.reverseBetween(to_linked([5]), 1, 1)) == [5]
    print("全部通过")



if __name__ == "__main__":
    test()
