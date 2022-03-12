"""
@File    : SubarraySum.py
@Time    : 2022/3/12 11:37
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
from typing import List


class SubarraySum:
    # 前缀和加哈希表
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        d = dict()
        n = len(nums)
        sum = 0
        d[0] = 1
        for i in range(n):
            sum += nums[i]
            dif = sum - k
            if dif in d:
                res += d[dif]
            if sum in d:
                d[sum] += 1
            else:
                d[sum] = 1
        return res
