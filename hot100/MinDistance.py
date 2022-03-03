"""
@File    : MinDistance.py
@Time    : 2022/2/20 9:35
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


# 给你两个单词word1 和word2， 请返回将word1转换成word2 所使用的最少操作数。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成
class MinDistance:
    # 动态规划题目
    # 可以对任意单词进行三种操作：插入一个字符，删除一个字符，替换一个字符
    #  题目给了两个单词，每个单词有三中操作，相应的操作共有6种
    # 6种操作中，A删除和B插入等价，B删除和A插入等价，A替换和B替换等价
    # 所以需要考虑的操作只有三种：A插入，B插入，A替换
    # 拿A=horse和B=ros举例：在A中插入，假设horse到ro的编辑距离为a,那么horse到ros的编辑距离
    # 不会超过a+1;同理，在B中插入，如果hors和ros的编辑距离为b，那么hors和ros的编辑距离不会超过
    # b+1;在修改A时，如果hors到ro的编辑距离为c,那么显然horse到ros的编辑距离不会超过c+1
    # 那么从horse到ros的编辑距离为min(a+1,b+1,c+1)
    # 上述都在单词的末尾进行操作，实际上操作的位置顺序不影响最终结果
    # 如果A为空，从”“到ro的转换需要2次，同理，B为空也是如此。
    # 综上可以用动态规划解决此问题：用dp[i][j]表示A的前i个字母和B的前j个字母之间的编辑距离。
    # 当A和B最后一个字母相同：dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    #
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        # 有一个字符串为空串
        if n * m == 0:
            return n + m
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # 边界状态初始化
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        # 计算所有的dp值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                left_down = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                dp[i][j] = min(left, down, left_down)
        return dp[n][m]
