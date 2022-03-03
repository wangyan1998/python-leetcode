"""
@File    : NumTrees.py
@Time    : 2022/2/22 16:41
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？
# 返回满足题意的二叉搜索树的种数。
# 1 <= n <= 19
class NumTrees:
    # 动态规划：给定一个有序序列1,2...n,可以遍历每一个数字i作为树根，将1~i-1作为左子树
    # 将i+1~n作为右子树，按照同样的方式递归构建二叉搜索树。因此原问题可以分解成两个规模较小
    # 的子问题，并且子问题可以复用，因为它只和树的结点个数有关
    # 可以定义两个函数：
    # 1.G(n)，长度为n的序列能构成的不同二叉搜索树的个数
    # 2.F(i,n):以i为根，序列长度为n的不同二叉搜索树个数（1<=i<=n）
    # G(n)就是我们需要求解的函数。
    # G(n)=sum{i=1->n}F(i,n),边界G(0)=1,G(1)=1
    # 而对于F，F(i,n)=G(i-1)*G(n-i)
    # 综上：G(n)=sum{i=1->n}G(i-1)*G(n-i)
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]
