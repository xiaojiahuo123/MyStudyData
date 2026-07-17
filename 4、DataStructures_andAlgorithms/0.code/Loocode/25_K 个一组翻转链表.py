"""
25. K 个一组翻转链表 (Reverse Nodes in k-Group)

难度：hard

题目描述：
给你链表的头节点 head，每 k 个节点一组进行翻转，请你返回修改后的链表。

示例 1：head = [1,2,3,4,5], k = 2 → [2,1,4,3,5]
示例 2：head = [1,2,3,4,5], k = 3 → [3,2,1,4,5]

链接：https://leetcode.cn/problems/reverse-nodes-in-k-group/
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
    assert to_list(s.reverseKGroup(to_linked([1,2,3,4,5]), 2)) == [2,1,4,3,5]
    assert to_list(s.reverseKGroup(to_linked([1,2,3,4,5]), 3)) == [3,2,1,4,5]
    print("全部通过")



if __name__ == "__main__":
    test()
