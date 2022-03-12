"""
@File    : DailyTemperatures.py
@Time    : 2022/3/12 9:56
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定一个整数数组temperatures，表示每天的温度，返回一个数组answer，其中answer[i]是指在
# 第 i 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用0 来代替。

from typing import List


class DailyTemperatures:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                x = stack.pop()
                res[x] = i - x
            stack.append(i)
        return res
