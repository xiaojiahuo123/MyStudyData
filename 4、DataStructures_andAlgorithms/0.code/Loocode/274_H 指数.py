"""
274. H 指数 (H-Index)

难度：medium

题目描述：
给你一个整数数组 citations，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。

示例 1：citations = [3,0,6,1,5] → 3
示例 2：citations = [1,3,1] → 1

约束：n == citations.length, 1 <= n <= 5000, 0 <= citations[i] <= 1000

链接：https://leetcode.cn/problems/h-index/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.hIndex([3,0,6,1,5]) == 3
    assert s.hIndex([1,3,1]) == 1
    assert s.hIndex([100]) == 1
    print("全部通过")



if __name__ == "__main__":
    test()
