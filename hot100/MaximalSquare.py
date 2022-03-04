"""
@File    : MaximalSquare.py
@Time    : 2022/3/4 10:56
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] 为 '0' 或 '1'


class MaximalSquare:
    # 动态规划题目，使用dp[i][j]表示以(i,j)为右下角且只包含1的正方形的边长最大值，选择其中最大的
    # 转移方程：
    # 如果该位置是0，dp[i][j]=0,不可能组成正方形
    # 如果该位置是1，dp[i][j]的值由其上方、左方、左上方的相邻位置决定：
    #     dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
    # 边界条件：
    # 如果i=0或者j=0，且该位置为‘1’，dp[i][j]=1
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        maxSquare = maxSide * maxSide
        return maxSquare
