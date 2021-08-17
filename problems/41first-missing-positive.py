"""
41. 缺失的第一个正数
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。


示例 1：

输入：nums = [1,2,0]
输出：3
示例 2：

输入：nums = [3,4,-1,1]
输出：2
示例 3：

输入：nums = [7,8,9,11,12]
输出：1


提示：

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
通过次数153,521提交次数367,385

tag: 数组 哈希表
背诵
O(1)访问数据：
1. 哈希表
2. 数组通过下标
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        h = {}
        for i in nums:
            if i > 0:
                h[i] = [i]
        for i in range(1, len(nums) + 1):
            if i not in h:
                return i
        return len(nums) + 1

    def firstMissingPositive2(self, nums: List[int]) -> int:
        big_number = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = big_number
        for i, n in enumerate(nums):
            n = abs(n)
            if n < big_number:
                nums[n - 1] = -abs(nums[n - 1])

        for i, n in enumerate(nums):
            if 0 < n < big_number:
                return i + 1
        return big_number

    def firstMissingPositiveSwap(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            while 1 <= nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length+1
