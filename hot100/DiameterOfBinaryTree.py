"""
@File    : DiameterOfBinaryTree.py
@Time    : 2022/3/12 12:02
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
# 这条路径可能穿过也可能不穿过根结点。
from tool.TreeNode import TreeNode


class DiameterOfBinaryTree:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def getPath(root):
            if not root:
                return 0
            l = getPath(root.left)
            r = getPath(root.right)
            self.ans = max(self.ans, l + r + 1)
            return 1 + max(l, r)

        getPath(root)
        return self.ans
