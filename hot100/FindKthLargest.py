"""
@File    : FindKthLargest.py
@Time    : 2022/3/4 10:12
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。


from typing import List


class FindKthLargest:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        return nums[n - k]
