"""189. 轮转数组
中等
相关标签
premium lock icon
相关企业
提示
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。



示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]


提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


进阶：

尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？

面试中遇到过这道题?
1/5
是
否
通过次数
1,459,542/3M
通过率
48.0%
相关标签
数组
数学
双指针
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return

        def reverse(left, right):
            nonlocal nums
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - k - 1)
        reverse(len(nums) - k, len(nums) - 1)
        reverse(0, len(nums) - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    # [4,3,2,1,7,6,5]
    # [5,3,2,1,7,6,4]
    # [5,6,2,1,7,3,4]
    # [5,6,7,1,2,3,4]
    k = 3
    solu = Solution()
    solu.rotate(nums,k)
    print(nums)
