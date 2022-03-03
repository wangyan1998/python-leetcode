"""
@File    : GenerateParenthesis.py
@Time    : 2022/2/14 14:22
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                res.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right)
                S.pop()

        backtrack([], 0, 0)
        return res
