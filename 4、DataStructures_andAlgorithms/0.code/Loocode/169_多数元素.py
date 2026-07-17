"""
169. 多数元素 (Majority Element)

难度：easy

题目描述：
给定一个大小为 n 的数组 nums，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

示例 1：nums = [3,2,3] → 3
示例 2：nums = [2,2,1,1,1,2,2] → 2

约束：n == nums.length, 1 <= n <= 5 * 10^4

链接：https://leetcode.cn/problems/majority-element/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.majorityElement([3,2,3]) == 3
    assert s.majorityElement([2,2,1,1,1,2,2]) == 2
    print("全部通过")



if __name__ == "__main__":
    test()
