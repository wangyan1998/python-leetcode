"""
@File    : LuckyNumbers.py
@Time    : 2022/2/15 9:44
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


class LuckyNumbers:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row = [10 ** 5] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                row[i] = min(row[i], matrix[i][j])
                col[j] = max(col[j], matrix[i][j])
        res = []
        for i in range(m):
            for j in range(n):
                if row[i] == col[j]:
                    res.append(row[i])
                    continue
        return res

