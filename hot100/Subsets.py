"""
@File    : Subsets.py
@Time    : 2022/2/22 10:32
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同
from typing import List


class Subsets:
    # 回溯去重
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)

        def backtrack(i):
            if res.__contains__(cur) is False:
                res.append(list(cur))
            if i == n:
                return
            cur.append(nums[i])
            backtrack(i + 1)
            cur.remove(nums[i])
            backtrack(i + 1)

        backtrack(0)
        return res
