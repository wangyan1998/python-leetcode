"""
@File    : MaxSlidingWindow.py
@Time    : 2022/3/4 17:37
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。

import heapq
from typing import List


class MaxSlidingWindow:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        # python中默认的优先队列是小根堆
        heapq.heapify(q)
        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans
