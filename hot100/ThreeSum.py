"""
@File    : ThreeSum.py
@Time    : 2022/2/11 15:21
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        # 枚举a
        for first in range(n):
            # 需要和上次枚举的a不同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # 对应c的指针初始指向数组最右端
            third = n - 1
            target = -nums[first]
            # 枚举b
            for second in range(first + 1, n):
                # 和上次枚举的b要不同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 要保证b的指针在c的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合,随着b后续增加
                # 就不会有满足a+b+c=0并且b<c的c了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans
