"""34. 在排序数组中查找元素的第一个和最后一个位置
中等
相关标签
premium lock icon
相关企业
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。



示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]


提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109

面试中遇到过这道题?
1/5
是
否
通过次数
1,486,866/3.2M
通过率
46.5%
相关标签
数组
二分查找
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                # print(left, mid, right)
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # print(left, " ",right)
            return left

        start = search(nums, target)
        if start >= len(nums) or nums[start] != target:
            return [-1, -1]
        end = search(nums, target + 1)
        return [start, end - 1]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 4
    solu = Solution()
    print(solu.searchRange(nums, target))
