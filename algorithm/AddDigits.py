"""
@File    : AddDigits.py
@Time    : 2022/3/3 9:00
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

class AddDigits:
    def addDigits(self, num: int) -> int:
        while num > 9:
            res = 0
            while num != 0:
                res += num % 10
                num = num // 10
            num = res
        return num
