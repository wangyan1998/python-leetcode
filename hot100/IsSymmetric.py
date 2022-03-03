"""
@File    : IsSymmetric.py
@Time    : 2022/2/22 18:02
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
from tool.TreeNode import TreeNode


class IsSymmetric:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p: TreeNode, q: TreeNode):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)

        return check(root, root)
