"""
@File    : Search.py
@Time    : 2022/2/15 17:07
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
# 使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ...,
#        nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3
# 处经旋转后可能变为[4,5,6,7,0,1,2] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，
# 则返回它的下标，否则返回-1。



class Search:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high - low) // 2 + low
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] < target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target and target < nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
