"""
@File    : SearchRange.py
@Time    : 2022/2/16 11:36
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回[-1, -1]。
# 进阶：
# 你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？


class SearchRange:
    # 使用两次二分查找找到两个边界
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if (mid == 0 or nums[mid - 1] != target) and nums[mid] == target:
                res[0] = mid
                break
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if (mid == len(nums) - 1 or nums[mid + 1] != target) and nums[mid] == target:
                res[1] = mid
                break
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return res
