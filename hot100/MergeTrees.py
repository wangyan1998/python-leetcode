"""
@File    : MergeTrees.py
@Time    : 2022/3/12 11:12
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你两棵二叉树： root1 和 root2 。
# 想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。
# 你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点
# 的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。
# 返回合并后的二叉树。
# 注意: 合并过程必须从两个树的根节点开始。


from tool.TreeNode import TreeNode


class MergeTrees:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged
