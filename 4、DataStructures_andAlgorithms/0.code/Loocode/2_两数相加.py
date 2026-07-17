"""
2. 两数相加 (Add Two Numbers)

难度：medium

题目描述：
给你两个非空链表，表示两个非负整数。它们每位数字都是按逆序存储的。请将两个数相加，并以相同形式返回一个表示和的链表。

示例 1：l1 = [2,4,3], l2 = [5,6,4] → [7,0,8]
示例 2：l1 = [0], l2 = [0] → [0]
示例 3：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] → [8,9,9,9,0,0,0,1]

链接：https://leetcode.cn/problems/add-two-numbers/
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
    assert to_list(s.addTwoNumbers(to_linked([2,4,3]), to_linked([5,6,4]))) == [7,0,8]
    assert to_list(s.addTwoNumbers(to_linked([0]), to_linked([0]))) == [0]
    assert to_list(s.addTwoNumbers(to_linked([9,9,9,9,9,9,9]), to_linked([9,9,9,9]))) == [8,9,9,9,0,0,0,1]
    print("全部通过")



if __name__ == "__main__":
    test()
