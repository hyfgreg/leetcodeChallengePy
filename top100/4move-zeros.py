"""283. 移动零
已解答
简单
相关标签
premium lock icon
相关企业
提示
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。



示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]


提示:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


进阶：你能尽量减少完成的操作次数吗？


面试中遇到过这道题?
1/5
是
否
通过次数
2,264,940/3.5M
通过率
63.8%
相关标签
数组
双指针
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
                print("switch and move", nums, left, right)
            elif nums[left] == nums[right] == 0:
                right += 1
                print("all 0, move right", nums, left, right)
            elif nums[left] != 0:
                left += 1
                if left == right:
                    right += 1


if __name__ == "__main__":
    nums = [1, 1, 0, 1, 0, 3, 12]
    s = Solution()
    print(s.moveZeroes(nums))
