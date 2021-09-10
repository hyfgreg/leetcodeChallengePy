"""


给你一个整数数组 nums，请你将该数组升序排列。

 

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 

提示：

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

tag: 排序 归并排序
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        self.buffer = [0] * len(nums)
        self.sort(nums, 0, len(nums))
        return nums

    def sort(self, nums: List[int], start: int, end: int):
        if start == end - 1:
            return
        mid = start + (end - start) // 2
        self.sort(nums, start, mid)
        self.sort(nums, mid, end)
        self.merge(nums, start, mid, mid, end)

    def merge(self, nums: List[int], start1, end1, start2, end2):
        # print("merge")
        # print(nums, start1, end1, start2, end2)
        for i in range(start1, end1):
            self.buffer[i] = nums[i]
        for i in range(start2, end2):
            self.buffer[i] = nums[i]
        # print("buffer", self.buffer)
        i, j = start1, start2
        k = min(i, j)
        while i < end1 or j < end2:
            if i < end1 and j < end2:
                if self.buffer[i] < self.buffer[j]:
                    nums[k] = self.buffer[i]
                    i += 1
                else:
                    nums[k] = self.buffer[j]
                    j += 1
            elif i < end1:
                nums[k] = self.buffer[i]
                i += 1
            else:
                nums[k] = self.buffer[j]
                j += 1
            k += 1
        # print(nums)
        # print("=====")


if __name__ == '__main__':
    s = Solution()
    nums = [5, 2, 3, 1]
    print("len nums", len(nums))
    print(s.sortArray(nums))
