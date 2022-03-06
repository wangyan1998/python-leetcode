"""
@File    : Codec.py
@Time    : 2022/3/6 15:02
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""

# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在
# 一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
# 你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格
# 式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
# 树中结点数在范围 [0, 10^4] 内
# -1000 <= Node.val <= 1000
from typing import List

from tool.TreeNode import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        返回该树的前序遍历结果“[1, 2, None, None, 3, 4, None, None, 5, None, None]”
        :type root: TreeNode
        :rtype: str
        """

        def dfs(root):
            if not root: return [None]
            left_t = dfs(root.left)
            right_t = dfs(root.right)
            return [root.val] + left_t + right_t

        return str(dfs(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        由前序遍历的list返回这棵树
        :type data: str
        :rtype: TreeNode
        """
        data_list = eval(data)  # 解析出字符串中的list

        def dfs(data_l):
            root_val = data_list.pop(0)
            if root_val == None:  # 因为data_l中含有0元素所以这里不能用if not root_val
                return None
            root = TreeNode(root_val)
            root.left = dfs(data_l)
            root.right = dfs(data_l)
            return root

        return dfs(data_list)
