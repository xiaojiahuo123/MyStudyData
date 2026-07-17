"""
75. 颜色分类 (Sort Colors)

难度：medium

题目描述：
给定一个包含红色、白色和蓝色共 n 个元素的数组 nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。使用整数 0、1 和 2 分别表示红色、白色和蓝色。

示例 1：nums = [2,0,2,1,1,0] → [0,0,1,1,2,2]
示例 2：nums = [2,0,1] → [0,1,2]

链接：https://leetcode.cn/problems/sort-colors/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    nums1 = [2,0,2,1,1,0]; s.sortColors(nums1); assert nums1 == [0,0,1,1,2,2]
    nums2 = [2,0,1]; s.sortColors(nums2); assert nums2 == [0,1,2]
    print("全部通过")



if __name__ == "__main__":
    test()
