"""
tag 排序 优先队列 堆排序
"""
class MinPQ:
    N = 0
    heap = [None]

    def __init__(self):
        self.N = 0
        self.heap = [None]

    def add(self, val):
        self.heap.append(val)
        self.N += 1
        self.swim(self.N)

    def pop(self):
        if not self.N:
            return None
        self.switch(1, self.N)
        val = self.heap.pop()
        self.N -= 1
        self.sink(1)
        return val

    def top(self):
        if self.N:
            return self.heap[1]
        return None

    def swim(self, i):
        j = i // 2
        while j:
            if self.less(i, j):
                self.switch(i, j)
                i = j
                j = j // 2
            else:
                break

    def sink(self, i):
        j = 2 * i
        while j <= self.N:
            if j + 1 <= self.N and self.less(j + 1, j):
                j = j + 1
            if self.less(j, i):
                self.switch(i, j)
            i = j
            j = 2 * j

    def less(self, i, j):
        return self.heap[i] < self.heap[j]

    def switch(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


if __name__ == '__main__':
    nums = [5, 1, 1, 2, 0, 0]
    s = MinPQ()
    for i in nums:
        s.add(i)
    while True:
        val = s.pop()
        if val is None:
            break
        print(val)
