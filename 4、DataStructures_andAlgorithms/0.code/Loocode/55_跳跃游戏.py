"""
55. 跳跃游戏 (Jump Game)

难度：medium

题目描述：
给你一个非负整数数组 nums，你最初位于数组的 第一个下标。判断你是否能够到达最后一个下标。

示例 1：nums = [2,3,1,1,4] → true
示例 2：nums = [3,2,1,0,4] → false

约束：1 <= nums.length <= 10^4, 0 <= nums[i] <= 10^5

链接：https://leetcode.cn/problems/jump-game/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.canJump([2,3,1,1,4]) == True
    assert s.canJump([3,2,1,0,4]) == False
    print("全部通过")



if __name__ == "__main__":
    test()
