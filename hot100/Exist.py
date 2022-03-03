"""
@File    : Exist.py
@Time    : 2022/2/22 14:37
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word
# 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格
# 是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


from typing import List


class Exist:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        h, w = len(board), len(board[0])
        visited = set()

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in direction:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            visited.remove((i, j))
            return result

        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        return False
