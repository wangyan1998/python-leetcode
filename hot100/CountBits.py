"""
@File    : CountBits.py
@Time    : 2022/3/7 20:28
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，
# 返回一个长度为 n + 1 的数组 ans 作为答案。
from typing import List


class CountBits:
    # x&(x-1)表示将x最后一位1变为0。可以循环的进行此操作，指导x变为0
    def countBits(self, n: int) -> List[int]:
        def countOnes(x: int) -> int:
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones += 1
            return ones

        bit = [countOnes(i) for i in range(n + 1)]
        return bit

    def countBits1(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        res[0] = 0
        for i in range(1, n + 1):
            if i % 2 == 1:
                res[i] = res[i - 1] + 1
            else:
                res[i] = res[i // 2]
        return res
