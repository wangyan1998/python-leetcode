"""
@File    : CombinationSum.py
@Time    : 2022/2/16 15:55
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个 无重复元素 的整数数组candidates 和一个目标整数target，
# 找出candidates中可以使数字和为目标数target 的 所有不同组合 ，
# 并以列表形式返回。你可以按 任意顺序 返回这些组合。
# candidates 中的同一个数字可以无限制重复被选取 。如果至少一
# 个数字的被选数量不同，则两种组合是不同的。
# 对于给定的输入，保证和为target 的不同组合数少于 150 个。
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都互不相同
# 1 <= target <= 500

from typing import List


class CombinationSum:
    # 典型的回溯法
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(candidates, target):
            if target == 0:
                res.append(list(cur))
            if target < 0:
                return
            for i in range(len(candidates)):
                cur.append(candidates[i])
                backtrack(candidates[i:], target - candidates[i])
                cur.remove(cur[len(cur) - 1])

        backtrack(candidates, target)
        return res
