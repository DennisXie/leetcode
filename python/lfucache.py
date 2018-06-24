#!/usr/bin/env python
"""
#ref: https://leetcode.com/problems/lfu-cache/description/
"""
class Data:
    def __init__(self, key, val, f):
        self.key = key
        self.val = val
        self.freq = f


class Node:
    def __init__(self, data, pprev=None, pnext=None):
        self.data = data
        self.pnext = pnext
        self.pprev = pprev


class List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_before(self, inode, node=None):
        """
        @param inode: 将要插入的node
        @param node: 插入到该node之前
        """
        if node:
            inode.pnext = node
            if node.pprev:
                # 插入非队首位置, 或者说node不是头节点时
                node.pprev.pnext = inode
                inode.pprev = node.pprev
                node.pprev = inode
            else:
                # 插入队首位置, 或者说node是头节点时
                inode.pprev = None
                node.pprev = inode
                self.head = inode
        else:
            # 插入队尾
            if self.tail:
                # 队尾有节点, 即不为空链表时
                self.tail.pnext = inode
                inode.pprev = self.tail
                inode.pnext = None
                self.tail = inode
            else:
                # 队尾无节点，即为空链表时
                self.head = inode
                self.tail = inode
        

    def pop(self, node):
        """
        @param node: 需要弹出的节点
        """
        # NOTE: 需要判断这个节点是否在链表中，否则如果传递一个错误的node可以误删节点
        if node:
            if node.pprev is None:
                # 头节点情况
                self.head = node.pnext
            else:
                node.pprev.pnext = node.pnext
            if node.pnext is None:
                # 尾节点情况
                self.tail = node.pprev
            else:
                node.pnext.pprev = node.pprev
            node.pnext = None
            node.pprev = None
            return node
        else:
            raise Exception("null node")

    def __repr__(self):
        s = list()
        p = self.head
        while p:
            s.append(p.data.key)
            p = p.pnext
        return 's={} t={} {}'.format(self.head.data.key, self.tail.data.key, ','.join(map(str, s)))


class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._list = List()
        self._key_map = dict()
        self._freq_map = dict()
        self._used = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self._key_map.get(key)
        if node is None:
            return -1
        else:
            self.change_node_pos(node)
            return node.data.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self._key_map.get(key)
        if self._capacity > 0 and node is None:
            self.try_del_lfu_node()
            data = Data(key, value, 1)
            node = Node(data)
            one_freq_node = self._freq_map.get(1)   # 查找频率为1的首个节点
            self._list.insert_before(node, one_freq_node)
            self._key_map[key] = node
            self._freq_map[1] = node
            self._used += 1
        elif node:
            node.data.val = value
            self.change_node_pos(node)

    def change_node_pos(self, node):
        if self._freq_map[node.data.freq] is node:
            if node.pnext and node.pnext.data.freq == node.data.freq:
                self._freq_map[node.data.freq] = node.pnext
            else:
                del self._freq_map[node.data.freq]
        node = self._list.pop(node)
        node.data.freq += 1
        # 如果没有找到这个频率的首节点那么就插入到队首
        freq_node = self._freq_map.get(node.data.freq, self._list.head)
        self._list.insert_before(node, freq_node)
        self._freq_map[node.data.freq] = node

    def try_del_lfu_node(self):
        if self._used == self._capacity:
            self._used -= 1
            node = self._list.pop(self._list.tail)
            del self._key_map[node.data.key]
            if self._freq_map[node.data.freq] is node:
                # 如果频率最低的最近使用的节点是删除的节点，那么就删除这个f的节点指向
                del self._freq_map[node.data.freq]


if __name__ == "__main__":
    cache = LFUCache(2)
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
    print("----------------------------------")
    s = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    v = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    cache = LFUCache(10)
    for i in range(len(v)):
        print("command {} {}".format(s[i], v[i]))
        if s[i] == "put":
            cache.put(*v[i])
        else:
            print(cache.get(*v[i]))
        print(cache._list)

