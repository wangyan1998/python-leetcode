"""
@File    : DetectCycle.py
@Time    : 2022/2/28 8:36
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 给定一个链表的头节点head，返回链表开始入环的第一个节点。如果链表无环，则返回null。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表
# 示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从
# 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅
# 是为了标识链表的实际情况。
# 不允许修改 链表。


from tool.ListNode import ListNode


class DetectCycle:
    def detectCycle(self, head: ListNode) -> ListNode:
        pre = head
        setnode = set()
        while pre:
            if setnode.__contains__(pre):
                return pre
            else:
                setnode.add(pre)
                pre = pre.next
        return None
