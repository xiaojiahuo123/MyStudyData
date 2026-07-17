"""
166. 分数到小数 (Fraction to Recurring Decimal)

难度：medium

题目描述：
给定两个整数，分别表示分数的分子和分母，以字符串形式返回小数。如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1：numerator = 1, denominator = 2 → "0.5"
示例 2：numerator = 2, denominator = 1 → "2"
示例 3：numerator = 4, denominator = 333 → 0.(012)

链接：https://leetcode.cn/problems/fraction-to-recurring-decimal/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.fractionToDecimal(1, 2) == "0.5"
    assert s.fractionToDecimal(2, 1) == "2"
    assert s.fractionToDecimal(4, 333) == "0.(012)"
    assert s.fractionToDecimal(1, 6) == "0.1(6)"
    print("全部通过")



if __name__ == "__main__":
    test()
