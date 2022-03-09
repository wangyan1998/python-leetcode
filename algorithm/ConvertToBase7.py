"""
@File    : ConvertToBase7.py
@Time    : 2022/3/7 9:04
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


# 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

class ConvertToBase7:
    def convertToBase(self, num: int) -> str:
        if num == 0:
            return "0"
        n = abs(num)
        res = ""
        while n != 0:
            res += str(n % 7)
            n //= 7
        if num < 0:
            res += "-"
        return res[::-1]
