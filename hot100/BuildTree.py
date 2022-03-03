"""
@File    : BuildTree.py
@Time    : 2022/2/23 14:47
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定两个整数数组preorder 和 inorder，其中preorder 是二叉树的先序遍历，
# inorder是同一棵树的中序遍历，请构造二叉树并返回其根节点。


from typing import List

from tool.TreeNode import TreeNode


class BuildTree:
    # 关于二叉树的题目很多都是用递归解决的，根本原因还是二叉树和其左子树右子树有相同的结构
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        map = dict()
        n = len(inorder)
        for i in range(n):
            map[inorder[i]] = i

        def build(pl, pr, il, ir):
            if pl > pr:
                return None
            proot = preorder[pl]
            idx = map[proot]
            size = idx - il
            root = TreeNode()
            root.__init__(proot)
            root.left = build(pl + 1, pl + size, il, idx - 1)
            root.right = build(pl + size + 1, pr, idx + 1, ir)
            return root

        return build(0, n - 1, 0, n - 1)
