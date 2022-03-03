"""
@File    : SingleNonDuplicate540.py
@Time    : 2022/2/14 10:51
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


# 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
# 请你找出并返回只出现一次的那个数。
# 你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。


class SingleNonDuplicate540:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (high - low) // 2 + low
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    low = mid + 1
                else:
                    high = mid
            else:
                if nums[mid - 1] == nums[mid]:
                    low = mid + 1
                else:
                    high = mid
        return nums[low]
