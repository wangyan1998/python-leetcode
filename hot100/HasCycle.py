"""
@File    : HasCycle.py
@Time    : 2022/2/23 18:32
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给你一个链表的头节点 head ，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中
# 的位置（索引从 0 开始）。注意：pos 不作为参数进行传递。仅仅是为了标识链表的实际情况。
# 如果链表中存在环，则返回 true 。 否则，返回 false 。
# 链表中节点的数目范围是 [0, 10^4]
# -10^5 <= Node.val <= 10^5
# pos 为 -1 或者链表中的一个 有效索引 。

from typing import Optional

from tool.ListNode import ListNode


class HasCycle:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        p, q = head, head.next
        while p != q:
            if not q or not q.next:
                return False
            p = p.next
            q = q.next.next

        return True

    # 哈希表
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
