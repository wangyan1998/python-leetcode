"""
@File    : GetIntersectionNode.py
@Time    : 2022/3/1 16:39
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。
# 如果两个链表不存在相交节点，返回 null 。
from tool.ListNode import ListNode


class GetIntersectionNode:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n1, n2 = 0, 0
        temp1, temp2 = headA, headB
        while temp1:
            n1 += 1
            temp1 = temp1.next
        while temp2:
            n2 += 1
            temp2 = temp2.next
        temp1, temp2 = headA, headB
        if n2 > n1:
            x = n2 - n1
            for i in range(x):
                temp2 = temp2.next
            while temp2 != temp1:
                temp2 = temp2.next
                temp1 = temp1.next
        else:
            x = n1 - n2
            for i in range(x):
                temp1 = temp1.next
            while temp2 != temp1:
                temp2 = temp2.next
                temp1 = temp1.next
        return temp1
