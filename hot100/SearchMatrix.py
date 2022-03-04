"""
@File    : SearchMatrix.py
@Time    : 2022/3/4 17:45
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 编写一个高效的算法来搜索mxn矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9<= matrix[i][j] <= 10^9
# 每行的所有元素从左到右升序排列
# 每列的所有元素从上到下升序排列
# -10^9<= target <= 10^9

from typing import List


class SearchMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i >= 0 and i < m and j >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
