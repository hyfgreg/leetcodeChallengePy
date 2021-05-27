# -*- coding: utf-8 -*-
"""
pq: [None, 2, 5, 7, 8, 10, 12, 13, None, None, None, None, None, None]
qp: [None, None, 1, None, None, 2, None, 3, 4, None, 5, None, 6, 7]
el: [None, None, C, None, None, F, None, H, I, None, K, None, J, L]
     0      1    2   3    4     5  6     7  8  9     10 11    12 13
"""
import random
from typing import List


class IndexMinPQ(object):
    def __init__(self, maxN):
        self.N: int = 0
        self.pq: List[None or int] = [None] * (maxN + 1)
        self.qp: List[None or int] = [None] * (maxN + 1)
        self.elements: List[str or None] = [None] * (maxN + 1)  # 用'A','B','C'...

    def less(self, i, j):
        return self.elements[self.pq[i]] < self.elements[self.pq[j]]

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]], self.qp[self.pq[j]] = self.qp[self.pq[j]], self.qp[self.pq[i]]

    def sink(self, k):
        while 2 * k <= self.N:
            j = 2 * k
            if j < self.N and self.less(j+1, j):
                j += 1
            if self.less(j, k):
                self.exch(j, k)
                k = j
            else:
                break

    def swim(self, k):
        while k > 1 and self.less(k, k // 2):
            self.exch(k, k // 2)
            k = k // 2

    def insert(self, k: int, item: str):
        self.elements[k] = item
        self.N += 1
        self.pq[self.N] = k
        self.qp[k] = self.N
        self.swim(self.N)

    def change(self, k, item):
        self.elements[k] = item
        self.swim(self.qp[k])
        self.sink(self.qp[k])

    def del_min(self):
        a = self.pq[1]
        b = self.elements[a]
        self.exch(1, self.N)
        self.N -= 1
        self.sink(1)
        self.qp[self.pq[self.N + 1]] = None
        self.elements[self.pq[self.N + 1]] = None
        self.pq[self.N + 1] = None
        return a,b

    def __str__(self):
        return '\n'.join([' '.join([str(i) for i in self.pq]), ' '.join([str(i) for i in self.qp]),
                          ' '.join([str(i) for i in self.elements])])

    def is_empty(self):
        return self.N == 0

if __name__ == '__main__':
    a = list('BCDEFGHIJK')
    random.shuffle(a)
    idm = IndexMinPQ(20)
    print(a)
    print('=====' * 20)
    index_set = set()
    _index = None
    for ch in a:
        while True:
            index = random.randint(1, 20)
            if index in index_set:
                continue
            else:
                index_set.add(index)
                break
        if ch == 'H':
            _index = index
        idm.insert(index, ch)
        print(idm)
        print('=====' * 20)

    print(_index, 'H')
    idm.change(_index,'A')

    while not idm.is_empty():
        print(idm.del_min())