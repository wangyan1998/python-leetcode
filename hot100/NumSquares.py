"""
@File    : NumSquares.py
@Time    : 2022/3/5 11:13
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，
# 其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。


class NumSquares:
    def numSquares(self, n: int) -> int:
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            minn = float('inf')
            while j * j <= i:
                minn = min(minn, f[i - j * j])
                j += 1
            f[i] = 1 + minn
        return f[n]
