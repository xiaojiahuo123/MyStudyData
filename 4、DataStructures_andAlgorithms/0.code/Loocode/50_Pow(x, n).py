"""
50. Pow(x, n) (Pow(x, n))

难度：medium

题目描述：
实现 pow(x, n)，即计算 x 的 n 次幂函数。

示例 1：x = 2.00000, n = 10 → 1024.00000
示例 2：x = 2.10000, n = 3 → 9.26100
示例 3：x = 2.00000, n = -2 → 0.25000

链接：https://leetcode.cn/problems/powx-n/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert abs(s.myPow(2.0, 10) - 1024.0) < 1e-5
    assert abs(s.myPow(2.1, 3) - 9.261) < 1e-5
    assert abs(s.myPow(2.0, -2) - 0.25) < 1e-5
    print("全部通过")



if __name__ == "__main__":
    test()
