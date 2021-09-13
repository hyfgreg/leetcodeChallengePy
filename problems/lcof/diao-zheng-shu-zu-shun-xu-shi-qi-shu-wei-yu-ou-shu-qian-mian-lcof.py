"""
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。



示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。


提示：

0 <= nums.length <= 50000
1 <= nums[i] <= 10000
通过次数183,927提交次数286,227

tag: 数组 双指针 排序
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 == 1:
                left += 1
            while right > left and nums[right] % 2 == 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    print(s.exchange(nums))
    nums = [1, 3, 5]
    print(s.exchange(nums))
    nums = [2, 4, 6]
    print(s.exchange(nums))
