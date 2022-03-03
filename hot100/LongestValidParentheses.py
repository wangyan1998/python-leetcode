"""
@File    : LongestValidParentheses.py
@Time    : 2022/2/15 14:14
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

class LongestValidParentheses:
    def longestValidParentheses(self, s: str):
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        for i in range(len(s)):
            # i-dp[i-1]-1是与当前)对称的位置
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        return max(dp)
