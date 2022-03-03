"""
@File    : IsValid.py
@Time    : 2022/2/13 15:27
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


class IsValid:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack
