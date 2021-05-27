# -*- coding: utf-8 -*-
import copy
import random
import typing
import attr


@attr.s
class SortBase:
    def sort(self, a: list):
        raise NotImplementedError

    def less(self, v: any, w: any) -> bool:
        return v < w

    def exch(self, a, i: int, j: int) -> None:
        a[i], a[j] = a[j], a[i]

    def show(self, a: list) -> None:
        print(a)

    def is_sorted(self, a: list) -> bool:
        i = 0
        j = 1
        while i < len(a) and j < len(a):
            if self.less(a[j], a[i]):
                return False
            i += 1
            j += 1
        return True


@attr.s
class Insertion(SortBase):
    def sort(self, a: list):
        length = len(a)
        for i in range(1, length):
            for j in range(i, 0, -1):
                if self.less(a[j], a[j - 1]):
                    self.exch(a, j, j - 1)
                else:
                    break


@attr.s
class Merge(SortBase):
    def sort(self, a: list):
        pass


@attr.s
class Shell(SortBase):
    def sort(self, a: list):
        length = len(a)
        h = 1
        while h < length // 3:
            h = 3 * h + 1
        while h >= 1:
            for i in range(h, length):
                for j in range(i, 0, -h):
                    if self.less(a[j], a[j - h]):
                        self.exch(a, j, j - h)
                    else:
                        break
            h = h // 3


@attr.s
class Merge(SortBase):
    aux = attr.ib(type='list', default=attr.Factory(list))

    def sort(self, a: list):
        self.aux = a[:]
        self._sort(self.aux, a, 0, len(a))
        # a = self.aux

    def _merge(self, a, aux, lo, mid, hi):
        # self.aux = a[:]
        i = lo
        j = mid
        for k in range(lo, hi):
            if i >= mid:
                a[k] = aux[j]
                j += 1
            elif j >= hi:
                a[k] = aux[i]
                i += 1
            elif self.less(aux[j], aux[i]):
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1

    def _sort(self, a: list, aux: list, lo: int, hi: int):
        if hi - lo <= 1:
            return
        mid = lo + (hi - lo) // 2
        self._sort(aux, a, lo, mid)
        self._sort(aux, a, mid, hi)
        self._merge(aux, a, lo, mid, hi)


@attr.s
class Quick(SortBase):
    def sort(self, a: list):
        self._sort(a, 0, len(a))

    def _sort(self, a: list, lo: int, hi: int):
        if hi - lo <= 1:
            return
        mid = self._partition(a, lo, hi)
        # print(lo,mid, hi)
        self._sort(a, lo, mid)
        self._sort(a, mid + 1, hi)

    def _partition(self, a: list, lo: int, hi: int):
        mid = lo + (hi - lo) // 2
        self.exch(a, lo, mid)
        i = lo + 1
        j = hi - 1
        while True:
            while i < hi and self.less(a[i], a[lo]):
                i += 1
            while j > lo and self.less(a[lo], a[j]):
                j -= 1
            if j <= i:
                break
            self.exch(a, i, j)
        self.exch(a, lo, j)
        return j


if __name__ == '__main__':
    a = list(range(100))
    random.shuffle(a)
    print(a)
    # s = Insertion()
    # s.sort(a)
    # assert s.is_sorted(a)
    # print(a)
    # s = Shell()
    # s.sort(a)
    # assert s.is_sorted(a)
    # print(a)
    # s = Merge()
    # s.sort(a)
    # assert s.is_sorted(a)
    # print(a)
    # print(s.aux)
    s = Quick()
    s.sort(a)
    # assert s.is_sorted(a)
    print(a)
