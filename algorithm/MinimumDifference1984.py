"""
@File    : MinimumDifference1984.py
@Time    : 2022/2/11 9:34
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


# 给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。
# 从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。
# 返回可能的 最小差值 。


class MinimumDifference1984:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[len(nums) - 1] - nums[0]
        i = k - 1
        while i < len(nums):
            res = min(res, nums[i] - nums[i - k + 1])
            i += 1
        return res

    def minimumDiffernece1(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
