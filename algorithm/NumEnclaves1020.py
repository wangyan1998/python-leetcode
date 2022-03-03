"""
@File    : NumEnclaves1020.py
@Time    : 2022/2/12 14:00
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。


class NumEnclaves:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(grid, row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0 or visited[row][col]:
                return
            visited[row][col] = True
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            dfs(grid, i, 0)
            dfs(grid, i, n - 1)
        for j in range(1, n - 1):
            dfs(grid, 0, j)
            dfs(grid, m - 1, j)
        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 1 and visited[i][j] == False:
                    res += 1
        return res
