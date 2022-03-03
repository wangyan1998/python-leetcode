"""
@File    : LRUCache.py
@Time    : 2022/2/28 16:08
@Author  : Wang
@Software: PyCharm
@Email   : usebywang@bupt.edu.cn
"""
# 请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# (1).LRUCache(int capacity) 以 正整数 作为容量capacity 初始化 LRU 缓存
# (2).int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# (3).void put(int key, int value)如果关键字key 已经存在，则变更其数据值value ；
#    如果不存在，则向缓存中插入该组key-value 。如果插入操作导致关键字数量超过capacity ,
# 则应该逐出最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
import collections


class LRUCache(collections.OrderedDict):

    def __init__(self, capactity: int):
        super.__init__()
        self.capactity = capactity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capactity:
            self.popitem(last=False)
