"""
@File    : LetterCombinations.py
@Time    : 2022/2/13 13:29
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


class LetterCombinations:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        if len(digits) == 0:
            return list()

        phoneMap = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv",
                    '9': "wxyz"}
        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
