"""
@File    : CanFinish.py
@Time    : 2022/3/2 9:53
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 你这个学期必须选修 numCourses 门课程，记为0到numCourses - 1 。
# 在选修某些课程之前需要一些先修课程。 先修课程按数组prerequisites 给出，
# 其中prerequisites[i] = [ai, bi] ，表示如果要学习课程ai 则 必须 先学习课程 bi 。
# 例如，先修课程对[0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false

import collections
from typing import List


class CanFinish:
    def canFinish(self, numCources: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCources
        valid = True

        def dfs(u):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2

        for p in prerequisites:
            edges[p[1]].append(p[0])
        for i in range(numCources):
            if visited[i] == 0 and valid:
                dfs(i)
        return valid
