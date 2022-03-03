"""
@File    : MergeKLists.py
@Time    : 2022/2/14 14:40
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
from typing import List, Optional

from tool.ListNode import ListNode


class MergeKLists:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            if list2 == None:
                return list1
            elif list1 == None:
                return list2
            elif list1.val < list2.val:
                list1.next = mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = mergeTwoLists(list1, list2.next)
                return list2

        list = None
        for i in range(len(lists)):
            list = mergeTwoLists(lists[i], list)
        return list
