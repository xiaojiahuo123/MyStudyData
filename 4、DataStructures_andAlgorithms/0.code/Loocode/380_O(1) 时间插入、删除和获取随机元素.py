"""
380. O(1) 时间插入、删除和获取随机元素 (Insert Delete GetRandom O(1))

难度：medium

题目描述：
实现RandomizedSet类，支持在平均 O(1) 时间下执行 insert、remove 和 getRandom 操作。

示例：输入 ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
      [[], [1], [2], [2], [], [1], [2], []]

链接：https://leetcode.cn/problems/insert-delete-getrandom-o1/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.insert(1) == True
    assert s.remove(2) == False
    assert s.insert(2) == True
    assert s.getRandom() in [1, 2]
    assert s.remove(1) == True
    assert s.insert(2) == False
    assert s.getRandom() == 2
    print("全部通过")



if __name__ == "__main__":
    test()
