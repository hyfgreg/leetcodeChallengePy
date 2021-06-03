"""
tag: 堆 分治算法

215. 数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""
from typing import List


class MaxPQ:
    def __init__(self, nums: List[int]):
        self.nums: List[None or int] = [None] * (len(nums) + 1)
        self.count = 0
        for n in nums:
            self.count += 1
            self.nums[self.count] = n
            self.swim(self.count)

    def less(self, i, j):
        return self.nums[i] < self.nums[j]

    def exchange(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def swim(self, index: int):
        while index > 1 and self.less(index // 2, index):
            self.exchange(index // 2, index)
            index = index // 2

    def sink(self, index: int):
        while 2 * index <= self.count:
            next = 2 * index
            if next < self.count and self.less(next, next + 1):
                next += 1
            if self.less(index, next):
                self.exchange(index, next)
                index = next
            else:
                break

    def del_max(self):
        if self.count == 0:
            raise Exception("empty pq")

        old_max = self.nums[1]
        self.exchange(1, self.count)
        self.nums[self.count] = None
        self.count -= 1
        self.sink(1)

        return old_max


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        本质是排序，然后再取第K个，可以考虑用优先队列
        """
        maxpq = MaxPQ(nums)
        while True:
            k -= 1
            a = maxpq.del_max()
            if k == 0:
                return a


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    maxpq = MaxPQ(nums)
    for i in range(9):
        print(maxpq.del_max())
