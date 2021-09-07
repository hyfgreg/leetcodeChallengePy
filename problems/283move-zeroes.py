"""
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
通过次数464,166提交次数726,278

tag: 数组 双指针
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        FUCK slow!!!
        Do not return anything, modify nums in-place instead.
        """

        for zero in range(len(nums)):
            if nums[zero] == 0:
                p = zero + 1
                while p < len(nums) and nums[p] == 0:
                    p += 1
                if p == len(nums):
                    return
                nums[zero], nums[p] = nums[p], nums[zero]

    def moveZeroes2(self, nums: List[int]) -> None:
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print(nums)
