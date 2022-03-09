"""
@File    : Rob1.py
@Time    : 2022/3/7 16:13
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为root。
# 除了root之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明
# 的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接
# 相连的房子在同一天晚上被打劫 ，房屋将自动报警。
# 给定二叉树的root。返回在不触动警报的情况下，小偷能够盗取的最高金额。
# 树的节点数在 [1, 10^4] 范围内
# 0 <= Node.val <= 10^4
from tool.TreeNode import TreeNode


class Rob1:
    # 动态规划
    def rob(self, root: TreeNode) -> int:
        f = dict()
        g = dict()

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            a, b, c, d = 0, 0, 0, 0
            if node.left in f:
                a = f[node.left]
            if node.right in f:
                b = f[node.right]
            if node.left in g:
                c = g[node.left]
            if node.right in g:
                d = g[node.right]
            f[node] = node.val + c + d
            g[node] = max(a, c) + max(b, d)

        dfs(root)
        return max(f[root], g[root])
