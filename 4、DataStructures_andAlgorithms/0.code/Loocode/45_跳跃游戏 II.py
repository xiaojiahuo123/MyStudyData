"""
45. 跳跃游戏 II (Jump Game II)

难度：medium

题目描述：
给定一个长度为 n 的非负整数数组 nums，初始位置为 nums[0]。每个元素代表在该位置可以跳跃的最大长度。到达最后一个下标所需的最小跳跃次数。

示例 1：nums = [2,3,1,1,4] → 2
示例 2：nums = [2,3,0,1,4] → 2

约束：1 <= nums.length <= 10^4, 0 <= nums[i] <= 1000

链接：https://leetcode.cn/problems/jump-game-ii/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.jump([2,3,1,1,4]) == 2
    assert s.jump([2,3,0,1,4]) == 2
    print("全部通过")



if __name__ == "__main__":
    test()
