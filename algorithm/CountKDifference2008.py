"""
@File    : CountKDifference2008.py
@Time    : 2022/2/9 10:41
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# //给你一个整数数组nums和一个整数k,请你返回数对(i, j)的数目，满足i<j且|nums[i] - nums[j]| == k。
# //        |x|的值定义为：
# //        如果x >= 0，那么值为x。
# //        如果x < 0，那么值为-x。
from typing import List
from collections import Counter


class CountKDifference:
    def countKDifference(self, nums: List[int], k: int) -> int:
        map = dict()
        res = 0
        for i in range(len(nums)):
            if nums[i] + k in map:
                res += map[nums[i] + k]
            if nums[i] + k in map:
                res += map[nums[i] - k]
            if nums[i] in map:
                map[nums[i]] = map[nums[i]] + 1
            else:
                map[nums[i]] = 1
        return res

    def countKDiffernece1(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = Counter()
        for num in nums:
            res += cnt[num + k] + cnt[num - k]
            cnt[num] += 1
        return res
