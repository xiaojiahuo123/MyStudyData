"""
208. 实现 Trie (前缀树) (Implement Trie (Prefix Tree))

难度：medium

题目描述：
实现一个 Trie，支持 insert、search 和 startsWith 操作。

示例：输入 ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
      [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]] → [null, null, true, false, true, null, true]

链接：https://leetcode.cn/problems/implement-trie-prefix-tree/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    t = Solution()
    t.insert("apple")
    assert t.search("apple") == True
    assert t.search("app") == False
    assert t.startsWith("app") == True
    t.insert("app")
    assert t.search("app") == True
    print("全部通过")



if __name__ == "__main__":
    test()
