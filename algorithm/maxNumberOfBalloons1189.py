"""
@File    : maxNumberOfBalloons1189.py
@Time    : 2022/2/13 13:20
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from collections import Counter
# 给你一个字符串text，你需要使用 text 中的字母来拼凑尽可能多的单词"balloon"（气球）。
# 字符串text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词"balloon"。


class MaxNumberOfBalloons1189:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(ch for ch in text if ch in "balon")
        cnt['l'] //= 2
        cnt['o'] //= 2
        return min(cnt.values()) if len(cnt) == 5 else 0
