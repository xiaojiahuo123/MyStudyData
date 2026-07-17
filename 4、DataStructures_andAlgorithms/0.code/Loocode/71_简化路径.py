"""
71. 简化路径 (Simplify Path)

难度：medium

题目描述：
给你一个字符串 path，表示指向某一文件或目录的 Unix 风格绝对路径，请将其转换为更加简洁的规范路径。

示例 1：path = "/home/" → "/home"
示例 2：path = "/../" → "/"
示例 3：path = "/home//foo/" → "/home/foo"
示例 4：path = "/a/./b/../../c/" → /c

链接：https://leetcode.cn/problems/simplify-path/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.simplifyPath("/home/") == "/home"
    assert s.simplifyPath("/../") == "/"
    assert s.simplifyPath("/home//foo/") == "/home/foo"
    assert s.simplifyPath("/a/./b/../../c/") == "/c"
    print("全部通过")



if __name__ == "__main__":
    test()
