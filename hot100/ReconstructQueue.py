"""
@File    : ReconstructQueue.py
@Time    : 2022/3/9 10:20
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。
# 每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
# 请你重新构造并返回输入数组people 所表示的队列。返回的队列应该格式化为数组 queue ，
# 其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。


from typing import List


class ReconstructQueue:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        n = len(people)
        ans = list()
        for person in people:
            ans[person[1]:person[1]] = [person]
        return ans
