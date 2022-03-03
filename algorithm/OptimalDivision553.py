"""
@File    : OptimalDivision553.py
@Time    : 2022/2/27 18:47
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定一组正整数，相邻的整数之间将会进行浮点除法操作。例如，[2,3,4] -> 2 / 3 / 4 。
# 但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，
# 才能得到最大的结果，并且返回相应的字符串格式的表达式。你的表达式不应该含有冗余的括号。
# 输入数组的长度在 [1, 10] 之间。
# 数组中每个元素的大小都在 [2, 1000] 之间。
# 每个测试用例只有一个最优除法解

from typing import List


class OptimalDivision553:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return str(nums[0]) + '/' + str(nums[1])
        res = ""
        res = res + str(nums[0]) + "/(" + str(nums[1])
        for i in range(2, n):
            res += "/"
            res += str(nums[i])
        res += ")"
        return res
