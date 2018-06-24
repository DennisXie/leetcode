#!/usr/bin/env python
"""
#ref: https://leetcode.com/problems/lru-cache/description/
"""


class Node:
    def __init__(self, data, pprev=None, pnext=None):
        self.data = data
        self.pnext = pnext
        self.pprev = pprev


class List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, data):
        if self.head:
            node = Node(data, None, self.head)
            node.pnext.pprev = node
            self.head = node
        else:
            node = Node(data)
            self.head = node
            self.tail = node
        return node

    def delete_tail(self):
        if self.tail:
            node = self.tail
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.tail
                self.tail = node.pprev
            return node
        else:
            raise Exception('null list')

    def change_to_head(self, node):
        # NOTE: 实际上还需要判断这个node是否在这个链表中
        # NOTE: 或者可以考虑将insert_head的逻辑放进来，那么就不用考虑是否在这个链表中了
        if self.head is node:
            pass
        else:
            if self.tail is node:
                self.tail = node.pprev
            # 修改前一个节点的next指针
            node.pprev.pnext = node.pnext
            # 修改后一个节点的prev指针
            if node.pnext:
                node.pnext.pprev = node.pprev
            # 头指针指向当前node
            self.head.pprev = node
            # ....
            node.pnext = self.head
            node.pprev = None
            self.head = node


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._list = List()
        self._map = dict()
        self._used = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self._map.get(key)
        if node is None:
            return -1
        else:
            self._list.change_to_head(node)
            return node.data[1]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self._map.get(key)
        if node is None:
            node = self._list.insert_head((key, value))
            self._map[key] = node
            if self._used == self._capacity:
                node = self._list.delete_tail()
                del self._map[node.data[0]]
            else:
                self._used += 1
        else:
            self._list.change_to_head(node)
            node.data = (key, value)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

