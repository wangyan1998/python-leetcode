"""
@File    : LowestCommonAncestor.py
@Time    : 2022/3/4 16:39
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，
# 最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽
# 可能大（一个节点也可以是它自己的祖先）。”


from tool.TreeNode import TreeNode


class LowestCommonAncestor:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (root is None) or (root is p or root is q):
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        if l:
            return l
        else:
            return r
