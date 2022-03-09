"""
@File    : DecodeString.py
@Time    : 2022/3/8 10:58
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""


# 给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。
# 注意 k 保证为正整数。
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像3a或2[4]的输入。


class DecodeString:
    # 采用辅助栈工具进行实现
    # 遍历字符串s中的每个字符c:
    # 如果c为数字，将数字转换成数字multi,用于后续倍数计算
    # 如果c为字母，在res尾部添加c
    # 如果c为[，将multi和res入栈，然后置空置0：用于存储此层内的子字符串及其数目
    # 如果c为]，从栈中取出，进行拼接
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

