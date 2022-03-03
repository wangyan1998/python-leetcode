"""
@File    : MaxProduct.py
@Time    : 2022/3/1 14:49
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个整数数组 nums，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），
# 并返回该子数组所对应的乘积。
# 测试用例的答案是一个32-位整数。
# 子数组 是数组的连续子序列。
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# nums 的任何前缀或后缀的乘积都 保证是一个 32-位 整数
from typing import List


class MaxProduct:
    # 这道题和最大子序和有点相似，虽然都是动态规划问题，其实大有不同
    # 最大子序和的思路是dp[i]=max(dp[i-1]*nums[i],nums[i]),因为加法只需要考虑前一个元素对子序和的
    # 影响
    # 而乘积不一样，乘积需要考虑正负号问题，异号越乘越小，同号越乘越大
    # 对于以当前元素结尾的子序列，最大连续乘积并不一定来自于前一个dp[i-1],因为如果当前是负数，那么我们希望
    # 动态规划的dp[i-1]应该也是负数，而且越小越好，如果当前元素是正数，我们希望dp[i-1]也是正数，而且越大
    # 越好
    # 因此，我们有：
    # maxdp[i]=max(maxdp[i-1]*nums[i],mindp[i-1]*nums[i],nums[i])
    # mindp[i]=min(maxdp[i-1]*nums[i],mindp[i-1]*nums[i],nums[i])
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxF = list(nums)
        minF = list(nums)
        for i in range(1, n):
            maxF[i] = max(maxF[i - 1] * nums[i], minF[i - 1] * nums[i], nums[i])
            minF[i] = min(minF[i - 1] * nums[i], maxF[i - 1] * nums[i], nums[i])
        ans = maxF[0]
        for i in range(1, n):
            ans = max(ans, maxF[i])
        return ans
