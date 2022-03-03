"""
@File    : AddTwoNumbers.py
@Time    : 2022/2/7 11:13
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from tool.ListNode import ListNode


class AddTwoNumbers:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        carry = 0
        h = None
        t = None
        while l1 is not None or l2 is not None:
            if l1 is not None:
                n1 = l1.val
            else:
                n1 = 0
            if l2 is not None:
                n2 = l2.val
            else:
                n2 = 0
            sum = n1 + n2 + carry
            if h is None:
                h = ListNode()
                h.__init__(sum % 10, None)
                t = h
            else:
                t.next = ListNode()
                t.next.__init__(sum % 10, None)
                t = t.next
            carry = sum // 10
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry != 0:
            t.next = ListNode()
            t.next.__init__(carry, None)
        return h
