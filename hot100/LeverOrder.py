"""
@File    : LeverOrder.py
@Time    : 2022/2/22 18:24
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
import collections
from queue import Queue
from typing import List

from tool.TreeNode import TreeNode


class LevelOrder:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = []
        queue.append(root)
        while len(queue) > 0:
            cur = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                cur.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res.append(cur)
        return res
