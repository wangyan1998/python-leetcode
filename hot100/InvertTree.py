"""
@File    : InvertTree.py
@Time    : 2022/3/4 15:20
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
from tool.TreeNode import TreeNode


class InvertTree:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            if root is None:
                return None
            left = dfs(root.left)
            right = dfs(root.right)
            root.left = right
            root.right = left
            return root

        return dfs(root)
