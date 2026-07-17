"""
11. 盛最多水的容器 (Container With Most Water)

难度：medium

题目描述：
给定一个长度为 n 的整数数组 height。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。返回容器可以储存的最大水量。

示例 1：height = [1,8,6,2,5,4,8,3,7] → 49
示例 2：height = [1,1] → 1

链接：https://leetcode.cn/problems/container-with-most-water/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert s.maxArea([1,1]) == 1
    print("全部通过")



if __name__ == "__main__":
    test()
