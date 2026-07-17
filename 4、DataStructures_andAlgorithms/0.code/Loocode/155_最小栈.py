"""
155. 最小栈 (Min Stack)

难度：medium

题目描述：
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

示例：输入 ["MinStack","push","push","push","getMin","pop","top","getMin"]
      [[],[-2],[0],[-3],[],[],[],[]] → [null,null,null,null,-3,null,0,-2]

链接：https://leetcode.cn/problems/min-stack/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    s.push(-2); s.push(0); s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2
    print("全部通过")



if __name__ == "__main__":
    test()
