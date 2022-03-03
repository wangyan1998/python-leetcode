"""
@File    : MaxPathSum.py
@Time    : 2022/2/23 16:06
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
# 同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

from typing import Optional

from tool.TreeNode import TreeNode


class MaxPathSum:
    def __init__(self):
        self.maxPath = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            maxp = node.val + left + right
            self.maxPath = max(self.maxPath, maxp)
            return node.val + max(left, right)

        dfs(root)
        return self.maxPath
