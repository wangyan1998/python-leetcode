"""
@File    : MaxCoins.py
@Time    : 2022/3/7 9:14
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组nums中。
# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得nums[i - 1] * nums[i] * nums[i + 1]
# 枚硬币。这里的 i - 1 和 i + 1 代表和i相邻的两个气球的序号。如果 i - 1或 i + 1 超出
# 了数组的边界，那么就当它是一个数字为 1 的气球。
# 求所能获得硬币的最大数量。
# n == nums.length
# 1 <= n <= 500
# 0 <= nums[i] <= 100
from typing import List


class MaxCoins:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [0] * (n + 2)
        for i in range(1, n + 1):
            val[i] = nums[i - 1]
        val[0] = val[n + 1] = 1
        rec = [[-1] * (n + 2) for _ in range(n + 2)]

        def solve(left, right):
            if left >= right - 1:
                return 0
            if rec[left][right] != -1:
                return rec[left][right]
            for i in range(left + 1, right):
                sum = val[left] * val[i] * val[right]
                sum += solve(left, i) + solve(i, right)
                rec[left][right] = max(rec[left][right], sum)
            return rec[left][right]

        return solve(0, n + 1)
