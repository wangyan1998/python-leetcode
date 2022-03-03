"""
@File    : LongestPalindrome.py
@Time    : 2022/2/8 15:08
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


# 给你一个字符串 s，找到 s 中最长的回文子串。

# 动态规划，如果s[i+1,j-1]为回文串并且s[i]==s[j]，那么s[i,j]也是回文字符串。特殊情况：长度为1的一定是
# 回文串，长度为2的，如果两个字符相同，则为回文串
class LongestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for L in range(2, n + 1):
            for i in range(n):
                j = i + L - 1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]
