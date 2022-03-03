"""
@File    : Rob.py
@Time    : 2022/3/1 17:43
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素
# 就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃
# 到的最高金额。
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

from typing import List


class Rob:
    # 典型的动态规划的题目
    # 转移方程为：dp[i]=max(dp[i-2]+nums[i],dp[i-1])
    # 边界值为：dp[0]=nums[0],dp[1]=max(nums[0],nums[1])
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[size - 1]
