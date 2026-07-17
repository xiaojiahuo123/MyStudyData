"""
134. 加油站 (Gas Station)

难度：medium

题目描述：
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。返回绕环路行驶一圈时可以从出发加油站出发的起始加油站编号。

示例 1：gas = [1,2,3,4,5], cost = [3,4,5,1,2] → 3
示例 2：gas = [2,3,4], cost = [3,4,3] → -1

链接：https://leetcode.cn/problems/gas-station/
"""

from typing import List, Optional


class Solution:
    def solve(self):
        # TODO: 请在这里实现你的解法
        pass


def test():
    s = Solution()
    assert s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3
    assert s.canCompleteCircuit([2,3,4], [3,4,3]) == -1
    print("全部通过")



if __name__ == "__main__":
    test()
