# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from typing import Optional, List

M = 4


class Node:
    def __init__(self, k):
        self.m = k
        self.children: List[Optional[Entry]] = [None for _ in range(k)]


class Entry:
    def __init__(self, key, val, next: Optional[Node] = None):
        self.key = key
        self.val = val
        self.next = next


class BTree:
    def __init__(self):
        self.root = Node(0)
        self.n = 0
        self.height = 0

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.n

    def get_height(self):
        return self.height

    def search(self, x: Node, key, ht):
        children = x.children
        if ht == 0:
            for child in children:
                if self.eq(key, child.key):
                    return child.val

        for j in range(x.m):
            if j + 1 == x.m or self.less(key, children[j + 1].key):
                return self.search(children[j].next, key, ht - 1)

        return None

    def put(self, key, val):
        if key is None:
            raise Exception("invalid key")
        u = self.insert(self.root, key, val, self.height)
        if not u:
            return
        self.n += 1
        t = Node(2)
        t.children[0] = Entry(self.root.children[0].key, None, self.root)
        t.children[1] = Entry(u.children[0].key, None, u)
        self.root = t
        self.height += 1

    def insert(self, h: Node, key, val, ht) -> Optional[Node]:
        t = Entry(key, val, None)
        j = 0
        if ht == 0:
            for jj in range(h.m):
                if self.less(key, h.children[jj].val):
                    j = jj
                    break
            else:
                j = h.m - 1
        else:
            for jj in range(h.m):
                if jj + 1 == h.m or self.less(key, h.children[jj + 1].key):
                    u = self.insert(h.children[jj].next, key, val, ht - 1)
                    if not u:
                        return None
                    t.key = u.children[0].key
                    t.val = None
                    t.next = u
                    j = jj
                    j += 1
                    break
            else:
                j = h.m

        for i in range(h.m, j, -1):
            h.children[i] = h.children[i - 1]
        h.children[j] = t
        h.m += 1
        if h.m < M: return None
        return self.split(h)

    def split(self, h: Node) -> Node:
        t = Node(M // 2)
        h.m = M // 2
        for j in range(M // 2):
            t.children[j] = h.children[M // 2 + j]
        return t

    def less(self, k1, k2):
        return k1 < k2

    def eq(self, k1, k2):
        return k1 == k2
