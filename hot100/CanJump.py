"""
@File    : CanJump.py
@Time    : 2022/2/18 21:50
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标。
# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i] <= 10^5
from typing import List


class CanJump:
    # 思维题：如果x可以到达，那么x+1,x+2,x+3...x+nums[i]必然可以到达，如果能到达的位置左右侧
    # 大于等于数组最右侧，那么数组最后一个位置一定可以到达。
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
