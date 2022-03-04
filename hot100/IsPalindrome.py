"""
@File    : IsPalindrome.py
@Time    : 2022/3/4 15:31
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
# 链表中节点数目在范围[1, 10^5] 内
# 0 <= Node.val <= 9
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
from tool.ListNode import ListNode


class IsPalindrome:
    def isPalindrome(self, head: ListNode) -> bool:
        s = ""
        p = head
        while p:
            s += str(p.val)
            p = p.next
        if s == s[::-1]:
            return True
        else:
            return False

    def isPalindrome1(self, head: ListNode) -> bool:
        s = ""
        p = head
        while p:
            s += str(p.val)
            p = p.next
        f, b = 0, len(s) - 1
        while f < b:
            if s[f] != s[b]:
                return False
            f += 1
            b -= 1
        return True
