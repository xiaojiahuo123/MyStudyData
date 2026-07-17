"""
399. 除法求值 (Evaluate Division)

难度：medium

题目描述：
给你一个变量对数组 equations 和一个实数数组 values，其中 equations[i] = [Ai, Bi] 且 values[i] 表示 Ai / Bi = values[i]。返回能由给定 equations 推导出的 queries[j] = [Cj, Dj] 的答案。

示例：equations = [["a","b"],["b","c"]], values = [2.0,3.0],
      queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]] → [6.00000,0.50000,-1.00000,1.00000,-1.00000]

链接：https://leetcode.cn/problems/evaluate-division/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    eq = [["a","b"],["b","c"]]
    val = [2.0, 3.0]
    q = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    assert s.calcEquation(eq, val, q) == [6.0, 0.5, -1.0, 1.0, -1.0]
    print("全部通过")



if __name__ == "__main__":
    test()
