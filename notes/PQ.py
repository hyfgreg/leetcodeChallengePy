# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function


class MinPQ:
    Q = []
    N = 0

    def add(self, val):
        self.Q.append(val)
        self.swim(self.N)
        self.N += 1

    def pop(self):
        if self.N == 0:
            raise ValueError("empty PQ")
        self.N -= 1
        self.swap(0, self.N)
        val = self.Q.pop()
        self.sink(0)
        return val

    def sink(self, index):
        left = 2 * index + 1
        while left < self.N:
            right = left + 1
            if right < self.N and self.less(right, left):
                left = right
            if not self.less(left, index):
                break
            self.swap(left, index)
            index = left
            left = 2 * index + 1

    def swim(self, index):
        new_index = (index - 1) // 2
        while index > 0 and self.less(index, new_index):
            self.swap(index, new_index)
            index = new_index
            new_index = (new_index - 1) // 2

    def less(self, p, q):
        return self.Q[p] < self.Q[q]

    def swap(self, p, q):
        self.Q[p], self.Q[q] = self.Q[q], self.Q[p]

    def empty(self):
        return self.N == 0

    def __str__(self):
        return str([i.val for i in self.Q])

if __name__ == '__main__':
    nums = [4, 1, 3, 2, 6, 8, 10]
    pq = MinPQ()
    for n in nums:
        pq.add(n)
    while pq.Q:
        print(pq.pop())
