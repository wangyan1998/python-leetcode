"""
@File    : IsOneBitCharacter717.py
@Time    : 2022/2/20 9:29
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 有两种特殊字符：
# 第一种字符可以用一个比特0来表示
# 第二种字符可以用两个比特(10或11)来表示、
# 给定一个以 0 结尾的二进制数组bits，如果最后一个字符必须是一位字符，则返回 true 。


from typing import List


class IsOneBitCharacter:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        if i == n - 1:
            return True
        else:
            return False
