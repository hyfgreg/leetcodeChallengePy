"""
239. 滑动窗口最大值
困难
相关标签
premium lock icon
相关企业
提示
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。



示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]


提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

面试中遇到过这道题?
1/5
是
否
通过次数
1,124,594/2.2M
通过率
50.1%
相关标签
队列
数组
滑动窗口
单调队列
堆（优先队列）
"""

from typing import List
from collections import deque


class MaxHeap:
    """
    parent: idx
    left: 2 * idx + 1
    right: 2 * idx + 2

    child: idx
    parent: (idx - 1) // 2
    """

    def __init__(self):
        self.heap = []

    def _go_up(self, idx):
        while idx:
            parent = (idx - 1) // 2
            if self.heap[parent][0] < self.heap[idx][0]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break

    def _go_down(self, idx):
        n = len(self.heap)
        while idx < len(self.heap):
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n and right < n:
                left_val = self.heap[left][0]
                right_val = self.heap[right][0]
                next_val = left_val if left_val > right_val else right_val
                next_idx = left if left_val > right_val else right
            elif left < n:
                left_val = self.heap[left][0]
                next_val = left_val
                next_idx = left
            else:
                break
            if self.heap[idx][0] < next_val:
                self.heap[idx], self.heap[next_idx] = (
                    self.heap[next_idx],
                    self.heap[idx],
                )
                idx = next_idx
            else:
                break

    def push(self, val):
        self.heap.append(val)
        self._go_up(len(self.heap) - 1)

    def pop(self):
        val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._go_down(0)
        return val

    def peek(self):
        return self.heap[0]

    def size(self):
        return self.__len__()

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


"""
还有个有意思的分块处理
"""


class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefixMax, suffixMax = [0] * n, [0] * n
        for i in range(n):
            if i % k == 0:
                prefixMax[i] = nums[i]
            else:
                prefixMax[i] = max(prefixMax[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                suffixMax[i] = nums[i]
            else:
                suffixMax[i] = max(suffixMax[i + 1], nums[i])

        ans = [max(suffixMax[i], prefixMax[i + k - 1]) for i in range(n - k + 1)]
        return ans


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        heap = MaxHeap()
        for i in range(k):
            heap.push((nums[i], i))
        ret.append(heap.peek()[0])

        for i in range(k, len(nums)):  # 此时i是窗口最后一个
            heap.push((nums[i], i))
            while (
                heap.peek()[1] <= i - k
            ):  # 如果最大值的索引不在窗口内，窗口:[i-k+1,...,i]
                heap.pop()
            ret.append(heap.peek()[0])
        return ret

    """
    这个解法的意思是，新来的比队尾前面的猛，那队尾就不要了，队列里的索引是递增的，能力是递减的，队列头是最厉害的且最老的
    """

    def maxSlidingWindowDeque(self, nums: List[int], k: int) -> List[int]:
        ret = []
        q = deque()
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        ret.append(nums[q[0]])

        for i in range(k, len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ret.append(nums[q[0]])
        return ret


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    heap = MaxHeap()
    for i, n in enumerate(nums):
        if len(heap) < 3:
            heap.push((n, i))
        if len(heap) == 3:
            print(heap.pop())
