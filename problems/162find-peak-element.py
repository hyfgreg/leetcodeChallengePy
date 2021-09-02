"""
162. 寻找峰值
峰值元素是指其值大于左右相邻值的元素。

给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。



示例 1：

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
示例 2：

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。


提示：

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
对于所有有效的 i 都有 nums[i] != nums[i + 1]


进阶：你可以实现时间复杂度为 O(logN) 的解决方案吗？

通过次数121,002提交次数244,591

tag: 数组 二分查找
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid == left:
                return mid if nums[mid] > nums[mid + 1] else mid + 1
            if mid == right:
                return mid if nums[mid] > nums[mid - 1] else mid - 1
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 1]
    print(s.findPeakElement(nums))
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(s.findPeakElement(nums))
    nums = [1, 2]
    print(s.findPeakElement(nums))
    nums = [2,1]
    print(s.findPeakElement(nums))
