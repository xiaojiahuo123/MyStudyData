"""
49. 字母异位词分组 (Group Anagrams)

难度：medium

题目描述：
给你一个字符串数组，请你将字母异位词组合在一起。

示例 1：strs = ["eat","tea","tan","ate","nat","bat"] → [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2：strs = [""] → [[""]]
示例 3：strs = ["a"] → [["a"]]

链接：https://leetcode.cn/problems/group-anagrams/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    result = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    result_sorted = sorted([sorted(x) for x in result])
    expected = sorted([sorted(x) for x in [["bat"],["nat","tan"],["ate","eat","tea"]]])
    assert result_sorted == expected
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"])[0] == ["a"]
    print("全部通过")



if __name__ == "__main__":
    test()
