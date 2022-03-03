"""
@File    : PancakeSort969.py
@Time    : 2022/2/19 18:33
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个整数数组 arr ，请使用 煎饼翻转 完成对数组的排序。
# 一次煎饼翻转的执行过程如下：
# 选择一个整数 k ，1 <= k <= arr.length
# 反转子数组 arr[0...k-1]（下标从 0 开始）
# 例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，
# 得到 arr = [1,2,3,4] 。
# 以数组形式返回能使 arr 有序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转
# 次数在10 * arr.length 范围内的有效答案都将被判断为正确。


from typing import List


class PancakeSort969:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for n in range(len(arr), 1, -1):
            idx = 0
            for i in range(n):
                if arr[i] > arr[idx]:
                    idx = i
            if idx == n - 1:
                continue
            m = idx
            for i in range((m + 1) // 2):
                arr[i], arr[m - i] = arr[m - i], arr[i]
            for i in range(n // 2):
                arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
            res.append(idx + 1)
            res.append(n)
        return res
