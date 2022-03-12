"""
@File    : Postorder.py
@Time    : 2022/3/12 9:50
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""

# 给定一个 n叉树的根节点root，返回 其节点值的 后序遍历 。
# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
from typing import List

from tool.Node import Node


class Postorder:
    def postorder(self, root: Node) -> List[int]:
        res = list()

        def porder(root: Node):
            if root is None:
                return
            for p in root.children:
                porder(p)
            res.append(root.val)

        porder(root)
        return res
