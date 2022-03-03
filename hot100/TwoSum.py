"""
@File    : TwoSum.py
@Time    : 2022/2/7 11:02
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return []
