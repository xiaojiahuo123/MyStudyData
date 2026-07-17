"""
115. 不同的子序列 (Distinct Subsequences)

难度：hard

题目描述：
给定一个字符串 s 和一个字符串 t，计算在 s 的子序列中 t 出现的个数。

示例 1：s = "rabbbit", t = "rabbit" → 3
示例 2：s = "babgbag", t = "bag" → 5

链接：https://leetcode.cn/problems/distinct-subsequences/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.numDistinct("rabbbit", "rabbit") == 3
    assert s.numDistinct("babgbag", "bag") == 5
    print("全部通过")



if __name__ == "__main__":
    test()
