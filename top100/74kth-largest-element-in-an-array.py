"""215. 数组中的第K个最大元素
中等
相关标签
premium lock icon
相关企业
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4


提示：

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

面试中遇到过这道题?
1/5
是
否
通过次数
1,654,716/2.7M
通过率
60.2%
相关标签
数组
分治
快速选择
排序
堆（优先队列）
"""

import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k
        left, right = 0, n - 1
        while True:
            index = self.quickselect(nums, left, right)
            if index == target:
                return nums[index]
            if index > target:
                right = index - 1
            else:
                left = index + 1

    def quickselect(self, nums: List[int], l, r) -> int:
        # print("before", nums, l, r)
        p = random.randint(l, r)
        pivot = nums[p]
        # print("use index", p, pivot)
        nums[l], nums[p] = nums[p], nums[l]

        i = l + 1
        j = r
        while True:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1

            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        # print("i", i, "j", j)
        nums[l], nums[j] = nums[j], nums[l]
        # print("after", nums)
        # print("=====")
        return j

    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        def build_heap(nums, n, i):
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            print("n", n, "i", i, "left", left, "right", right)

            if left < n and nums[largest] < nums[left]:
                largest = left

            if right < n and nums[largest] < nums[right]:
                largest = right
            print("i", i, "largest", largest)
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                build_heap(nums, n, largest)  # 向下调整受到影响的子树

        # 建立堆
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            build_heap(nums, n, i)
        print(nums)
        heap_size = n
        for i in range(k):
            print(1, nums)
            nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
            heap_size -= 1
            build_heap(nums, heap_size, 0)
            print(2, nums)
        # print(nums)

        return nums[n - k]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    # nums = [3, 3, 3, 3, 4, 3, 3, 3, 3]
    # k = 2
    # nums = [99, 99]
    # k = 1
    nums = [0, 1, 2, 3, 4, 5, 9999]
    k = 1
    solu = Solution()
    print(solu.findKthLargestHeap(nums, k))
