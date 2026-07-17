"""
150. 逆波兰表达式求值 (Evaluate Reverse Polish Notation)

难度：medium

题目描述：
给你一个字符串数组 tokens，表示一个根据逆波兰表示法表示的算术表达式。返回该表达式的值。

示例 1：tokens = ["2","1","+","3","*"] → 9
示例 2：tokens = ["4","13","5","/","+"] → 6

链接：https://leetcode.cn/problems/evaluate-reverse-polish-notation/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.evalRPN(["2","1","+","3","*"]) == 9
    assert s.evalRPN(["4","13","5","/","+"]) == 6
    assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
    print("全部通过")



if __name__ == "__main__":
    test()
