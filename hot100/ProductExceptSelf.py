"""
@File    : ProductExceptSelf.py
@Time    : 2022/3/4 17:01
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个整数数组nums，返回 数组answer，其中answer[i]等于nums中除nums[i]之外其余各元素的乘积。
# 题目数据 保证 数组nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。
# 请不要使用除法，且在O(n) 时间复杂度内完成此题。
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# 保证 数组nums之中任意元素的全部前缀元素和后缀的乘积都在32 位 整数范围内


from typing import List


class ProductExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left = [0] * n
        right = [0] * n
        left[0], right[n - 1] = 1, 1
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
            right[n - i - 1] = right[n - i] * nums[n - i]
        for i in range(n):
            res[i]=left[i]*right[i]
        return res
