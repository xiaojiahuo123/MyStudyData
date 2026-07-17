"""
125. 验证回文串 (Valid Palindrome)

难度：easy

题目描述：
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样，则可以认为该短语是一个回文串。

示例 1：s = "A man, a plan, a canal: Panama" → true
示例 2：s = "race a car" → false

链接：https://leetcode.cn/problems/valid-palindrome/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("race a car") == False
    assert s.isPalindrome(" ") == True
    print("全部通过")



if __name__ == "__main__":
    test()
