"""
@File    : SimplifiedFractions1447.py
@Time    : 2022/2/10 10:20
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from math import gcd
from typing import List


# 给你一个整数n,请你返回所有0到1之间（不包括0和1）满足分母小于等于n的最简分数.分数可以以任意顺序返回。
class SimplifiedFractions1447:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f"{j}/{i}" for i in range(2, n + 1) for j in range(1, i) if gcd(i, j) == 1]
