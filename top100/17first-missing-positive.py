"""41. 缺失的第一个正数
困难
相关标签
premium lock icon
相关企业
提示
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。


示例 1：

输入：nums = [1,2,0]
输出：3
解释：范围 [1,2] 中的数字都在数组中。
示例 2：

输入：nums = [3,4,-1,1]
输出：2
解释：1 在数组中，但 2 没有。
示例 3：

输入：nums = [7,8,9,11,12]
输出：1
解释：最小的正数 1 没有出现。


提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

面试中遇到过这道题?
1/5
是
否
通过次数
731,205/1.5M
通过率
49.1%
相关标签
数组
哈希表
"""

from typing import List

"""
思路：把数字x放到对应的索引上去(x-1)
我觉得swap的方法更符合我的逻辑。。。
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        big = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = big

        # print(nums)
        for i in range(len(nums)):
            idx = abs(nums[i])
            if idx < big and nums[idx - 1] > 0:
                nums[idx - 1] = -nums[idx - 1]
        # print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return big

    def firstMissingPositiveSwap(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # print(nums)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


if __name__ == "__main__":
    nums = [1, 2, 0]
    # nums = [3, 4, -1, 1]
    # nums = [7, 8, 9, 11, 12]
    # nums = [1, 1]
    solu = Solution()
    print(solu.firstMissingPositiveSwap(nums))
