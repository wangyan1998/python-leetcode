"""
@File    : FindDuplicate.py
@Time    : 2022/3/6 9:18
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定一个包含n + 1 个整数的数组nums ，其数字都在[1, n]范围内（包括 1 和 n），
# 可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，返回这个重复的数 。
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。


from typing import List


class FindDuplicate:
    # 排序
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
        return 0

    # 二分查找
    def findDuplicate1(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 1, n
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            cnt = 0
            for i in range(n):
                if nums[i] <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans
