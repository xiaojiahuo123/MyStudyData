"""
82. 删除排序链表中的重复元素 II (Remove Duplicates from Sorted List II)

难度：medium

题目描述：
给定一个已排序的链表，删除所有含有重复数字的节点，只保留原始链表中没有重复出现的数字。

示例 1：head = [1,2,3,3,4,4,5] → [1,2,5]
示例 2：head = [1,1,1,2,3] → [2,3]

链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
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
    assert to_list(s.deleteDuplicates(to_linked([1,2,3,3,4,4,5]))) == [1,2,5]
    assert to_list(s.deleteDuplicates(to_linked([1,1,1,2,3]))) == [2,3]
    print("全部通过")



if __name__ == "__main__":
    test()
