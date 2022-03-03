"""
@File    : ReverseList.py
@Time    : 2022/3/1 21:51
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
from tool.ListNode import ListNode


class ReverseList:
    def reverseList(self, head: ListNode):
        if head is None or head.next is None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return newHead
