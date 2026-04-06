"""152. 乘积最大子数组
中等
相关标签
premium lock icon
相关企业
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

请注意，一个只包含一个元素的数组的乘积是这个元素的值。



示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


提示:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
nums 的任何子数组的乘积都 保证 是一个 32-位 整数

面试中遇到过这道题?
1/5
是
否
通过次数
730,716/1.7M
通过率
44.2%
相关标签
数组
动态规划
"""

from typing import List

"""
因为有负数的加入，所以不能只维护最大dp，还要维护一个最小dp，因为如果dp_min[i-1]<0, nums[i] <0, 负负得正可能更大

dp_max[i] = max( nums[i],                // 单独 nums[i]
                 nums[i] * dp_max[i-1],  // 与前面的最大乘积相乘
                 nums[i] * dp_min[i-1] ) // 与前面的最小乘积相乘（针对负数情况）

dp_min[i] = min( nums[i],
                 nums[i] * dp_max[i-1],
                 nums[i] * dp_min[i-1] )
注意看，i只和i-1有关，所以可以把内存占用优化到O(1)
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n
        dp_max[0] = dp_min[0] = nums[0]
        for i in range(1, n):
            dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
        # print(dp_max)
        # print(dp_min)
        return max(dp_max)

    def maxProductnolist(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = cur_max = cur_min = nums[0]
        for i in range(1, n):
            prev_max, prev_min = cur_max, cur_min
            cur_max = max(nums[i], prev_max * nums[i], prev_min * nums[i])
            cur_min = min(nums[i], prev_max * nums[i], prev_min * nums[i])
            ans = max(cur_max, ans)

        # print(dp_max)
        # print(dp_min)
        return ans


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    solu = Solution()
    print(solu.maxProduct(nums))
