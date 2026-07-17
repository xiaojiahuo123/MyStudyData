"""
23. 合并 K 个升序链表 (Merge k Sorted Lists)

难度：hard

题目描述：
给你一个链表数组，每个链表都已按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：lists = [[1,4,5],[1,3,4],[2,6]] → [1,1,2,3,4,4,5,6]
示例 2：lists = [] → []
示例 3：lists = [[]] → []

链接：https://leetcode.cn/problems/merge-k-sorted-lists/
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
    assert to_list(s.mergeKLists([to_linked([1,4,5]), to_linked([1,3,4]), to_linked([2,6])])) == [1,1,2,3,4,4,5,6]
    assert to_list(s.mergeKLists([])) == []
    assert to_list(s.mergeKLists([to_linked([])])) == []
    print("全部通过")



if __name__ == "__main__":
    test()
