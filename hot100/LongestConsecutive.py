"""
@File    : LongestConsecutive.py
@Time    : 2022/2/23 17:32
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为O(n) 的算法解决此问题。


from typing import List


class LongestConsecutive:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longlen = 0
        for num in s:
            if num - 1 not in s:
                l = 1
                cur = num
                while cur + 1 in s:
                    l += 1
                    cur += 1
                longlen = max(longlen, l)
        return longlen
