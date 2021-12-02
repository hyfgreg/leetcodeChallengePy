# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from typing import Optional, List

M = 4


class Node:
    def __init__(self, k):
        self.m = k
        self.children: List[Optional[Entry]] = [None for _ in range(M)]


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
        self.n += 1
        if not u:
            return
        t = Node(2)
        t.children[0] = Entry(self.root.children[0].key, None, self.root)
        t.children[1] = Entry(u.children[0].key, None, u)
        self.root = t
        self.height += 1

    def insert(self, h: Node, key, val, ht) -> Optional[Node]:
        t = Entry(key, val, None)
        if ht == 0:
            for jj in range(h.m):
                if self.less(key, h.children[jj].key):
                    j = jj
                    break
            else:
                j = h.m
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
        # print(j)
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

    def __str__(self):
        return self._to_string(self.root, self.height, "")

    def _to_string(self, h: Node, ht: int, indent: str):
        ret = []
        # print("ht", ht)
        if ht == 0:
            for child in h.children[:h.m]:
                ret.append(f"{indent}{child.key} {child.val}\n")
        else:
            for index, child in enumerate(h.children[:h.m]):
                if index > 0:
                    ret.append(f"{indent}({child.key})\n")
                ret.append(self._to_string(child.next, ht - 1, indent + " " * 4))
        return "".join(ret)


if __name__ == '__main__':
    st = BTree()

    # st.put("www.cs.princeton.edu", "128.112.136.12")
    # st.put("www.cs.princeton.edu", "128.112.136.11")
    # st.put("www.princeton.edu", "128.112.128.15")
    # st.put("www.yale.edu", "130.132.143.21")
    # st.put("www.simpsons.com", "209.052.165.60")
    # st.put("www.apple.com", "17.112.152.32")
    # st.put("www.amazon.com", "207.171.182.16")
    # st.put("www.ebay.com", "66.135.192.87")
    # st.put("www.cnn.com", "64.236.16.20")
    # st.put("www.google.com", "216.239.41.99")
    # st.put("www.nytimes.com", "199.239.136.200")
    # st.put("www.microsoft.com", "207.126.99.140")
    # st.put("www.dell.com", "143.166.224.230")
    # st.put("www.slashdot.org", "66.35.250.151")
    # st.put("www.espn.com", "199.181.135.201")
    # st.put("www.weather.com", "63.111.66.11")
    # st.put("www.yahoo.com", "216.109.118.65")

    st.put("A", 1)
    st.put("B", 1)
    st.put("C", 1)
    st.put("E", 1)
    st.put("F", 1)
    st.put("H", 1)
    st.put("I", 1)
    st.put("J", 1)
    st.put("K", 1)
    st.put("M", 1)
    st.put("N", 1)
    st.put("O", 1)
    st.put("P", 1)
    st.put("Q", 1)
    st.put("R", 1)
    st.put("T", 1)
    st.put("U", 1)
    st.put("W", 1)
    st.put("X", 1)

    print(st)
