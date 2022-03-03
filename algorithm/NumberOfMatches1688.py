"""
@File    : NumberOfMatches1688.py
@Time    : 2022/1/25 9:16
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


class NumberOfMathes1688:
    def numberOfMatches1688(self, n: int) -> int:
        res = 0
        while n != 1:
            if n % 2 == 0:
                res += n // 2
                n //= 2
            else:
                res += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return res
