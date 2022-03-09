"""
@File    : CanPartition.py
@Time    : 2022/3/9 10:28
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，
# 使得两个子集的元素和相等。
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
from typing import List


class CanPartition:
    # 动态规划，可以转换成0-1背包问题
    # 如果n<2，或者和为奇数，或者最大值大于和的一半，肯定是false
    # 如果和为偶数，令target=sum/2
    # 设dp[i][j]为从数组的[0,j]下标范围内选取若干个正整数，是否存在一种方案使得选取的正整数和正好为j
    # 转移方程：
    # 如果j>=nums[i],nums[i]可以选择，可以不选
    # （1）若选择nums[i],dp[i][j]=dp[i-1][j-nums]
    # (2)若不选nums[i],dp[i][j]=dp[i-1][j]
    # 如果j<nums[i]，那一定不会选nums[i]
    # 此时dp[i][j]=dp[i][j-1]
    # 边界条件：
    # 对于dp[i][0]=True
    # 对于dp[0][nums[0]]=True
    # 最后返回dp[n-1][target]
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        maxNum = max(nums)
        if maxNum > target:
            return False
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][target]
