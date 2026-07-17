"""
21. 合并两个有序链表 (Merge Two Sorted Lists)

难度：easy

题目描述：
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：list1 = [1,2,4], list2 = [1,3,4] → [1,1,2,3,4,4]
示例 2：list1 = [], list2 = [] → []
示例 3：list1 = [], list2 = [0] → [0]

链接：https://leetcode.cn/problems/merge-two-sorted-lists/
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
    assert to_list(s.mergeTwoLists(to_linked([1,2,4]), to_linked([1,3,4]))) == [1,1,2,3,4,4]
    assert to_list(s.mergeTwoLists(to_linked([]), to_linked([]))) == []
    assert to_list(s.mergeTwoLists(to_linked([]), to_linked([0]))) == [0]
    print("全部通过")



if __name__ == "__main__":
    test()
