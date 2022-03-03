"""
@File    : MinStack.py
@Time    : 2022/3/1 16:18
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 实现 MinStack 类:
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。


import math


# 辅助栈实现
class MinStack:
    def __init__(self):
        self.a = []
        self.b = [math.inf]

    def push(self, val: int) -> None:
        self.a.append(val)
        self.b.append(min(val, self.b[-1]))

    def pop(self) -> None:
        self.a.pop()
        self.b.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.b[-1]
