"""
295. 数据流的中位数 (Find Median from Data Stream)

难度：hard

题目描述：
中位数是有序整数列表中间的数。设计一个支持以下两种操作的数据结构：
- void addNum(int num) 从数据流中添加一个整数到数据结构中
- double findMedian() 返回目前所有元素的中位数

链接：https://leetcode.cn/problems/find-median-from-data-stream/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    mf = Solution()
    mf.addNum(1); mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
    print("全部通过")



if __name__ == "__main__":
    test()
