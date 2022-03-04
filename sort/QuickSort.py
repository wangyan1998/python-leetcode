"""
@File    : QuickSort.py
@Time    : 2022/3/4 10:46
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import List


def quicksort(arr: List[int], low: int, high: int):
    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print("排序后的数组:")
for i in range(n):
    print("%d" % arr[i])
