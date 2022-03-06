"""
@File    : LengthOfLIS.py
@Time    : 2022/3/6 16:56
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而
# 不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
from typing import List


class LengthOfLIS:
    # 典型的动态规划
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        res = 0
        for i in range(1, n):
            maxNum = 0
            for j in range(i):

                if nums[j] < nums[i]:
                    maxNum = max(maxNum, dp[j])
            dp[i] = maxNum + 1
            res = max(dp[i], res)
        return res
