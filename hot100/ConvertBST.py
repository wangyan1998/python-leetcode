"""
@File    : ConvertBST.py
@Time    : 2022/3/12 12:13
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
# 使每个节点 node的新值等于原树中大于或等于node.val的值之和。
# 提醒一下，二叉搜索树满足下列约束条件：
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。


from typing import Optional

from tool.TreeNode import TreeNode


class ConvertBST:
    def convertBST(self, root: Optional[TreeNode]) -> TreeNode:
        tnode = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            for node in tnode:
                node.val += root.val
            tnode.append(root)
            postorder(root.right)

        postorder(root)
        return root
