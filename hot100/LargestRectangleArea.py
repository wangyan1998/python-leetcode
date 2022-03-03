"""
@File    : LargestRectangleArea.py
@Time    : 2022/2/22 14:48
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
from typing import List


class LargestRectangleArea:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0
        stack = []
        for i in range(size):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                while len(stack) > 0 and cur_height == heights[stack[-1]]:
                    stack.pop()
                if len(stack) > 0:
                    cur_width = i - stack[-1] - 1
                else:
                    cur_width = i
                res = max(res, cur_height * cur_width)
            stack.append(i)
        while len(stack) > 0 is not None:
            cur_height = heights[stack.pop()]
            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                cur_width = size - stack[-1] - 1
            else:
                cur_width = size
            res = max(res, cur_height * cur_width)
        return res
