"""
239. 滑动窗口最大值 (Sliding Window Maximum)

难度：hard

题目描述：
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到最右侧。返回滑动窗口中的最大值。

示例 1：nums = [1,3,-1,-3,5,3,6,7], k = 3 → [3,3,5,5,6,7]
示例 2：nums = [1], k = 1 → [1]

链接：https://leetcode.cn/problems/sliding-window-maximum/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert s.maxSlidingWindow([1], 1) == [1]
    print("全部通过")



if __name__ == "__main__":
    test()
