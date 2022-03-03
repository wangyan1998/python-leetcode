"""
@File    : MaxArea.py
@Time    : 2022/2/11 9:58
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。
# 在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。
# 找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器。
from typing import List


class MaxArea:
    # 暴力法，会超时
    def maxArea(self, height: List[int]) -> int:
        return max(min(height[i], height[j]) * (j - i) for i in range(len(height)) for j in range(i + 1, len(height)))

    # 双指针：
    # 将双指针分别指向数组的两端，此时容水量是：两个指针中较小的值*指针之间的距离
    # 然后移动双指针中较小的那个，直到两个指针重合，找到最大的容水量
    # 正确性证明：
    # 假设当前左指针和右指针指向的是x和y，假设x<y，同时两指针之间的距离为t
    # 则水容量为：min(x,y)*t=x*t
    # 如果保持左指针不动，向左移动右指针指向y1,此时距离为t1,显然t1<t
    # min(x,y1)<=min(x,y)
    # 如果y1<=y,那么min(x,y1)<=min(x,y)
    # 如果y1>y,那么min(x,y1)=x=min(x,y)
    # 所以：min(x,y1)*t1<min(x,y)*t
    # 也就是说如果移动较大的指针，无论如何移动得到的都比原来的容水量小。也就是说这个左指针固定的情况下，
    # 容水量已经最大了，不可能在随着右指针的移动变化了。所以要移动左指针，或者说每次应该移动指向较小的
    # 数的指针

    def maxArea1(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
