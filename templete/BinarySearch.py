"""
@File    : templete.py
@Time    : 2022/3/13 11:31
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


def binarySearch(arr, x):
    if len(arr) == 0:
        return -1
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
    return -1


def binarySearchLeftBound(arr, x):
    if len(arr) == 0:
        return -1
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            r = mid - 1
        elif arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
    if l <= len(arr) - 1 and arr[l] == x:
        return l
    return -1


def binarySearchRightBound(arr, x):
    if len(arr) == 0:
        return -1
    l, r = 0, len(arr)
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            l = mid + 1
        elif arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
    if r >= 0 and arr[r] == x:
        return r
    return -1


arr = [1, 2, 2, 2, 3, 4, 5, 8]
print(binarySearch(arr, 5))
print(binarySearch(arr, 6))
print(binarySearchLeftBound(arr, 2))
print(binarySearchRightBound(arr, 2))
