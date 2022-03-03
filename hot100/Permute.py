"""
@File    : Permute.py
@Time    : 2022/2/18 14:00
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同
from typing import List


class Permute:
    # 回溯方法，本题可以可以等价于给定一个长为n的一维数组，将nums中的数填入进去，每个数只能用一次
    # 每次填入的位置是first,填入的范围是没用过的数，我们通过交换将用过的数放在nums[0,first]中，
    # 将没用过的数放在nums[first+1:],然后进行回溯。如果first==n,说明得到一个排列，然后将交换复原
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return res

    # 标记数组的回溯实现全排列
    def permute1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        visit = [False] * n
        cur = []

        def backtrack(pos=0):
            if pos == n:
                res.append(list(cur))
            for i in range(n):
                if visit[i] is False:
                    cur.append(nums[i])
                    visit[i] = True
                    backtrack(pos + 1)
                    cur.remove(nums[i])
                    visit[i] = False

        backtrack()
        return res
