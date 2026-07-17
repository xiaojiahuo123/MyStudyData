"""
373. 查找和最小的 K 对数字 (Find K Pairs with Smallest Sums)

难度：medium

题目描述：
给定两个以升序排列的整数数组 nums1 和 nums2，以及一个整数 k。返回和最小的 k 对数字。

示例 1：nums1 = [1,7,11], nums2 = [2,4,6], k = 3 → [[1,2],[1,4],[1,6]]
示例 2：nums1 = [1,1,2], nums2 = [1,2,3], k = 2 → [[1,1],[1,1]]

链接：https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.kSmallestPairs([1,7,11], [2,4,6], 3) == [[1,2],[1,4],[1,6]]
    assert s.kSmallestPairs([1,1,2], [1,2,3], 2) == [[1,1],[1,1]]
    assert s.kSmallestPairs([1,2], [3], 3) == [[1,3],[2,3]]
    print("全部通过")



if __name__ == "__main__":
    test()
