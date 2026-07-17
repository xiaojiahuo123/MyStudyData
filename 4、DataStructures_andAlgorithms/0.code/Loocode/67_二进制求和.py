"""
67. 二进制求和 (Add Binary)

难度：easy

题目描述：
给你两个二进制字符串 a 和 b，以二进制字符串的形式返回它们的和。

示例 1：a = "11", b = "1" → "100"
示例 2：a = "1010", b = "1011" → 10101

链接：https://leetcode.cn/problems/add-binary/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"
    print("全部通过")



if __name__ == "__main__":
    test()
