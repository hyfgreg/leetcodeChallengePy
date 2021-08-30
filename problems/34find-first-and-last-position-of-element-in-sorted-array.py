"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？


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
通过次数321,178提交次数756,582

tag: 数组 二分查找
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        ret = [-1, -1]
        while left <= right:
            if ret[0] != -1 and ret[1] != -1:
                break

            mid = left + (right - left) // 2
            # print(f"left {left} right {right} mid {mid}")
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                # nums[mid] == target
                if ret[1] == -1 and (mid == len(nums) - 1 or nums[mid + 1] != target):
                    ret[1] = mid
                    # print(f"set ret[1] {ret[1]}")
                    left = 0
                    right = mid
                    continue
                elif ret[0] == -1 and (mid == 0 or nums[mid - 1] != target):
                    # print(f"set ret[0] {ret[0]}")
                    ret[0] = mid
                    left = mid
                    right = len(nums) - 1
                    continue

                if ret[0] == -1 and ret[1] != -1:
                    right = mid - 1 if mid > 0 else 0
                elif ret[0] != -1 and ret[1] == -1:
                    left = mid + 1 if mid < len(nums) - 1 else len(nums) - 1
                else:
                    left = mid + 1
        return ret


if __name__ == '__main__':
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(s.searchRange(nums, target))
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(s.searchRange(nums, target))
    nums = []
    target = 0
    print(s.searchRange(nums, target))
    nums = [1]
    target = 1
    print(s.searchRange(nums, target))
    nums = [2, 2]
    target = 2
    print(s.searchRange(nums, target))
    nums = [1, 4]
    target = 4
    print(s.searchRange(nums, target))
