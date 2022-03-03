"""
@File    : ReverseOnlyLetters.py
@Time    : 2022/2/23 9:54
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个字符串 s ，根据下述规则反转字符串：
# 所有非英文字母保留在原有位置。
# 所有英文字母（小写或大写）位置反转。
# 返回反转后的 s 。

class ReverseOnlyLetters:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = []
        n = len(s)
        res = ''
        for i in range(n):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
                stack.append(s[i])
        for i in range(n):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
                res += stack.pop()
            else:
                res += s[i]
        return res
