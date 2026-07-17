"""
211. 添加与搜索单词 - 数据结构设计 (Design Add and Search Words Data Structure)

难度：medium

题目描述：
设计一个支持 add 和 search 的数据结构。search 可以搜索文字或正则表达式字符串，字符串中只包含字母 . 或 a-z。"." 表示任何一个字母。

示例：输入 ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
      [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]] → [null,null,null,null,false,true,true,true]

链接：https://leetcode.cn/problems/design-add-and-search-words-data-structure/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    d = Solution()
    d.addWord("bad"); d.addWord("dad"); d.addWord("mad")
    assert d.search("pad") == False
    assert d.search("bad") == True
    assert d.search(".ad") == True
    assert d.search("b..") == True
    print("全部通过")



if __name__ == "__main__":
    test()
