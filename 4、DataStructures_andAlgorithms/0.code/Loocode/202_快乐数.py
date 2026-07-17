"""
202. 快乐数 (Happy Number)

难度：easy

题目描述：
编写一个算法来判断一个数 n 是不是快乐数。快乐数定义：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。

示例 1：n = 19 → true
示例 2：n = 2 → false

链接：https://leetcode.cn/problems/happy-number/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.isHappy(19) == True
    assert s.isHappy(2) == False
    assert s.isHappy(1) == True
    print("全部通过")



if __name__ == "__main__":
    test()
