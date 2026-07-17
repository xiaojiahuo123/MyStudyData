"""
86. 分隔链表 (Partition List)

难度：medium

题目描述：
给你一个链表的头节点 head 和一个特定值 x，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。

示例 1：head = [1,4,3,2,5,2], x = 3 → [1,2,2,4,3,5]
示例 2：head = [2,1], x = 2 → [1,2]

链接：https://leetcode.cn/problems/partition-list/
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
    assert to_list(s.partition(to_linked([1,4,3,2,5,2]), 3)) == [1,2,2,4,3,5]
    assert to_list(s.partition(to_linked([2,1]), 2)) == [1,2]
    print("全部通过")



if __name__ == "__main__":
    test()
