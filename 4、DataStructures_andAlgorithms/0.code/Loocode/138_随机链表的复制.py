"""
138. 随机链表的复制 (Copy List with Random Pointer)

难度：medium

题目描述：
给你一个长度为 n 的链表，每个节点包含一个额外的随机指针 random。请构造这个链表的深拷贝。

示例 1：head = [[7,null],[13,0],[11,4],[10,2],[1,0]] → [[7,null],[13,0],[11,4],[10,2],[1,0]]

链接：https://leetcode.cn/problems/copy-list-with-random-pointer/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def test():
    s = Solution()
    n1 = Node(1); n2 = Node(10); n3 = Node(11); n4 = Node(13); n5 = Node(7)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5
    n1.random = None; n2.random = n1; n3.random = n5; n4.random = n2; n5.random = None
    clone = s.copyRandomList(n1)
    assert clone is not None
    assert clone.val == 1
    print("全部通过")



if __name__ == "__main__":
    test()
