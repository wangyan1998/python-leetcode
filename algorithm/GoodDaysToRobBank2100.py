"""
@File    : GoodDaysToRobBank2100.py
@Time    : 2022/3/6 10:04
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 你和一群强盗准备打劫银行。给你一个下标从 0开始的整数数组security，
# 其中security[i]是第 i天执勤警卫的数量。日子从 0开始编号。同时给你一个整数time。
# 如果第 i天满足以下所有条件，我们称它为一个适合打劫银行的日子：
# 第 i天前和后都分别至少有 time天。
# 第 i天前连续 time天警卫数目都是非递增的。
# 第 i天后连续 time天警卫数目都是非递减的。
# 更正式的，第 i 天是一个合适打劫银行的日子当且仅当：
# security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].
# 请你返回一个数组，包含 所有 适合打劫银行的日子（下标从 0开始）。返回的日子可以 任意顺序排列。

from typing import List


class GoodDaysToRobBank:
    # 动态规划
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
            if security[n - i - 1] <= security[n - i]:
                right[n - i - 1] = right[n - i] + 1
        res = []
        for i in range(n):
            if left[i] >= time and right[i] >= time:
                res.append(i)
        return res
