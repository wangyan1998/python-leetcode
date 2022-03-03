"""
@File    : Trap.py
@Time    : 2022/2/16 21:18
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

class Trap:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0], rightMax[n - 1] = height[0], height[n - 1]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
            j = n - i - 1
            rightMax[j] = max(rightMax[j + 1], height[j])
        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res
