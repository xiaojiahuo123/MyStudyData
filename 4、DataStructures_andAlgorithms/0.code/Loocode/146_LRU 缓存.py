"""
146. LRU 缓存 (LRU Cache)

难度：medium

题目描述：
请你设计并实现一个满足 LRU (最近最少使用) 缓存约束的数据结构。实现 LRUCache 类：
- LRUCache(int capacity) 以正整数作为容量初始化
- int get(int key) 如果关键字存在则返回值，否则返回 -1
- void put(int key, int value) 更新或插入

链接：https://leetcode.cn/problems/lru-cache/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution(2)
    s.put(1, 1); s.put(2, 2)
    assert s.get(1) == 1
    s.put(3, 3)
    assert s.get(2) == -1
    s.put(4, 4)
    assert s.get(1) == -1
    assert s.get(3) == 3
    assert s.get(4) == 4
    print("全部通过")



if __name__ == "__main__":
    test()
