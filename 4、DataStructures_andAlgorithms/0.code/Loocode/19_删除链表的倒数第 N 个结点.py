"""
19. 删除链表的倒数第 N 个结点 (Remove Nth Node From End of List)

难度：medium

题目描述：
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：head = [1,2,3,4,5], n = 2 → [1,2,3,5]
示例 2：head = [1], n = 1 → []
示例 3：head = [1,2], n = 1 → [1]

链接：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
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
    assert to_list(s.removeNthFromEnd(to_linked([1,2,3,4,5]), 2)) == [1,2,3,5]
    assert to_list(s.removeNthFromEnd(to_linked([1]), 1)) == []
    assert to_list(s.removeNthFromEnd(to_linked([1,2]), 1)) == [1]
    print("全部通过")



if __name__ == "__main__":
    test()
