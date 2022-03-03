"""
@File    : SortColors.py
@Time    : 2022/2/20 17:20
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定一个包含红色、白色和蓝色、共n个元素的数组nums，原地对它们进行排序，使得相同颜色的元素相邻，
# 并按照红色、白色、蓝色顺序排列。
# 我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。
# 必须在不使用库的sort函数的情况下解决这个问题。

from typing import List


class SortColors:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        if n < 2:
            return
        p, q, i = 0, n - 1, 0
        while i <= q:
            if nums[i] == 0:
                nums[i] = nums[p]
                nums[p] = 0
                p += 1
            if nums[i] == 2:
                nums[i] = nums[q]
                nums[q] = 2
                q -= 1
                if nums[i] != 1:
                    i -= 1
            i += 1
