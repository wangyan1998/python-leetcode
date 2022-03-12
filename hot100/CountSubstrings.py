"""
@File    : CountSubstrings.py
@Time    : 2022/3/12 10:46
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
# 回文字符串 是正着读和倒过来读一样的字符串。
# 子字符串 是字符串中的由连续字符组成的一个序列。
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。


class CountSubstrings:
    def countSubstrings(s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for p in range(n):
            dp[p][p] = True
            res += 1
        for i in range(2, n + 1):
            for j in range(n):
                k = j + i - 1
                if k < n:
                    if i > 2:
                        dp[j][k] = dp[j + 1][k - 1] and s[j] == s[k]
                    else:
                        dp[j][k] = s[j] == s[k]
                    if dp[j][k] is True:
                        res += 1
                else:
                    break
        return res

