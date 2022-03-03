"""
@File    : SortList.py
@Time    : 2022/3/1 11:11
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你链表的头结点 head ，请将其按升序排列并返回 排序后的链表 。
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 <= Node.val <= 10^5
from typing import Optional

from tool.ListNode import ListNode


class SortList:
    # 直接把值取出来，进行排序，然后再按顺序把值放回去
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = []
        p = head
        while p:
            num.append(p.val)
            p = p.next
        num.sort()
        p = head
        i = 0
        while p:
            p.val = num[i]
            p = p.next
            i += 1
        return head

    # 递归方法+归并排序，选中中间节点，将链表分成前后两部分，分别对前后两部分进行排序
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head1, head2):
            node = ListNode().__init__(0, None)
            temp, temp1, temp2 = node, head1, head2
            while temp1 and temp2:
                if temp1.val > temp2.val:
                    temp.next = temp2
                    temp2 = temp2.next
                else:
                    temp.next = temp1
                    temp1 = temp1.next
                temp = temp.next
            if temp1 is not None:
                temp.next = temp1
            if temp2 is not None:
                temp.next = temp2
            return node.next

        def sort(head, tail):
            if head is None:
                return head
            elif head.next == tail:
                head.next = None
                return head
            slow, fast = head, head
            while fast != tail:
                slow = slow.next
                fast = fast.next.next
            mid = slow
            list1 = sort(head, mid)
            list2 = sort(mid, tail)
            sorted = merge(list1, list2)
            return sorted

        return sort(head, None)
