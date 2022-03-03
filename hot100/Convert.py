"""
@File    : Convert.py
@Time    : 2022/2/8 15:37
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行Z 字形排列。
# 比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：
#    P   A   H   N
#    A P L S I I G
#    Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);


class Convert:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        map = dict()
        x = 2 * numRows - 2
        for i in range(len(s)):
            j = i % x
            if j < numRows:
                if j in map:
                    map[j] += s[i]
                else:
                    map[j] = s[i]
            else:
                if x - j in map:
                    map[x - j] += s[i]
                else:
                    map[x - j] = s[i]
        res = ""
        for i in range(numRows):
            res += map.get(i, "")
        return res
