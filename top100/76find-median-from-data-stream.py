"""295. 数据流的中位数
困难
相关标签
premium lock icon
相关企业
中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder 对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。

示例 1：

输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
提示:

-105 <= num <= 105
在调用 findMedian 之前，数据结构中至少有一个元素
最多 5 * 104 次调用 addNum 和 findMedian

面试中遇到过这道题?
1/5
是
否
通过次数
302,976/512.3K
通过率
59.1%
相关标签
设计
双指针
数据流
排序
堆（优先队列）
"""

"""
手动实现一个最大堆
"""


class HeapQ:
    def __init__(self) -> None:
        self.heap = []

    def _sift_up(self, i) -> None:
        parent = (i - 1) // 2
        while i > 0 and self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent
            parent = (i - 1) // 2

    def _sift_down(self, i) -> None:
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < len(self.heap) and self.heap[largest] < self.heap[left]:
                largest = left

            if right < len(self.heap) and self.heap[largest] < self.heap[right]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

    def push(self, val: int) -> None:
        if not self.heap:
            self.heap.append(val)
            return
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def top(self) -> int:
        return self.heap[0]

    def pop(self) -> int:
        top = self.top()
        n = len(self.heap)
        self.heap[0], self.heap[n - 1] = self.heap[n - 1], self.heap[0]
        self.heap.pop()
        self._sift_down(0)
        return top

    def empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


class MedianFinder:

    def __init__(self):
        self.max_pq = HeapQ()  # 放小的数
        self.min_pq = HeapQ()  # 放大的数

    def addNum(self, num: int) -> None:
        # print("add", num)
        if self.max_pq.empty() or num <= self.max_pq.top():
            # print("to max_pq")
            self.max_pq.push(num)
            # print("max_pq", self.max_pq.heap)
        else:
            self.min_pq.push(-num)
            # print("to min_pq")
            # print("min_pq", self.min_pq.heap)

        # 保证小的数的数量>=大的数的数量，且最多多一个
        if self.max_pq.size() > self.min_pq.size() + 1:
            top = self.max_pq.pop()
            self.min_pq.push(-top)
        elif self.min_pq.size() > self.max_pq.size():
            top = -self.min_pq.pop()
            self.max_pq.push(top)

    def findMedian(self) -> float:
        # print(self.max_pq.heap)
        # print(self.min_pq.heap)
        if (self.max_pq.size() + self.min_pq.size()) % 2 == 0:
            return (self.max_pq.top() - self.min_pq.top()) / 2
        return self.max_pq.top()


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == "__main__":
    import random

    # nums = list(range(10))
    # random.shuffle(nums)
    # pq = HeapQ()
    # nums = [8, 6, 4, 1, 9, 3, 2, 0, 5, 7]
    # print("before", nums)
    # for n in nums:
    #     pq.push(n)
    #     print(n, pq.heap)
    # while pq.heap:
    #     print(pq.pop())
    #     print(pq.heap)

    nums = [8, 6, 4, 1, 9, 3, 2, 0, 5, 7]
    mf = MedianFinder()
    for n in nums:
        print(n)
        mf.addNum(n)
        print(mf.findMedian())
        print("===")
