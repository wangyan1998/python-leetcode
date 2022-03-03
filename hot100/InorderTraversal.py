"""
@File    : InorderTraversal.py
@Time    : 2022/2/22 16:36
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from typing import Optional, List
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
from tool.TreeNode import TreeNode


class InorderTraversal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
