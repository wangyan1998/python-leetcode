"""
@File    : PlatesBetweenCandles.py
@Time    : 2022/3/8 10:15
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


class PlateBetweenCandles:
    # 对于每一个询问，我们只需要找到给定区间内最左侧和最右侧的两个蜡烛，这样两个蜡烛
    # 之间的所有盘子都是符合条件的。
    # 对于寻找蜡烛，我们可以预处理区间内每个位置左侧的第一个蜡烛和右侧的第一个蜡烛。这样区间左端点
    # left[i]右侧的第一个蜡烛即为区间最左侧的蜡烛，区间右端点 right[i]左侧的第一个蜡烛即为区间
    # 最右侧的蜡烛。对于计算盘子数量，我们可以计算盘子数量的前缀和preSum。
    # 假设找到的两蜡烛的位置分别为 x 和 y，那么两位置之间的盘子数量即为
    # preSum[y]−preSum[x−1]
    def plateBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        preSum, sum = [0] * n, 0
        left, l = [0] * n, -1
        for i, ch in enumerate(s):
            if ch == '*':
                sum += 1
            else:
                l = i
            preSum[i] = sum
            left[i] = l

        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r

        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if x >= 0 and y >= 0 and x < y:
                ans[i] = preSum[y] - preSum[x]
        return ans
