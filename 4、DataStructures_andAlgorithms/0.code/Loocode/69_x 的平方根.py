"""
69. x 的平方根 (Sqrt(x))

难度：easy

题目描述：
给你一个非负整数 x，计算并返回 x 的算术平方根。由于返回类型是整数，结果只保留整数部分，小数部分将被舍去。

示例 1：x = 4 → 2
示例 2：x = 8 → 2

链接：https://leetcode.cn/problems/sqrtx/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.mySqrt(4) == 2
    assert s.mySqrt(8) == 2
    assert s.mySqrt(0) == 0
    assert s.mySqrt(1) == 1
    print("全部通过")



if __name__ == "__main__":
    test()
