"""
141. 环形链表 (Linked List Cycle)

难度：easy

题目描述：
给你一个链表的头节点 head，判断链表中是否有环。

示例 1：head = [3,2,0,-4], pos = 1 → true
示例 2：head = [1,2], pos = 0 → true
示例 3：head = [1], pos = -1 → false

链接：https://leetcode.cn/problems/linked-list-cycle/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def test():
    s = Solution()
    n1 = ListNode(3); n2 = ListNode(2); n3 = ListNode(0); n4 = ListNode(-4)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2
    assert s.hasCycle(n1) == True
    n1 = ListNode(1); n2 = ListNode(2); n1.next = n2; n2.next = n1
    assert s.hasCycle(n1) == True
    n1 = ListNode(1)
    assert s.hasCycle(n1) == False
    print("全部通过")



if __name__ == "__main__":
    test()
