"""
@File    : RemoveNthFromEnd.py
@Time    : 2022/2/13 14:13
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
from tool.ListNode import ListNode


# 删除链表的倒数第N个节点

class RemoveNthFromEnd:
    def removeNthFromEnd(self, head: ListNode, n: int):
        l = 0
        p = head
        while p != None:
            l += 1
            p = p.next
        idx = l - n
        dummy = ListNode(0, head)
        p = dummy
        for i in range(idx):
            p = p.next
        p.next=p.next.next
        return dummy.next
