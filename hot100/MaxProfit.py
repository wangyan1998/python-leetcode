"""
@File    : MaxProfit.py
@Time    : 2022/2/23 16:03
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


class MaxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        res = 0
        n = len(prices)
        for i in range(n):
            minp = min(prices[i], minp)
            res = max(res, prices[i] - minp)
        return res
