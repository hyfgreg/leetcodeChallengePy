"""53. 最大子数组和
中等
相关标签
premium lock icon
相关企业
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。



示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23


提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104


进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。


面试中遇到过这道题?
1/5
是
否
通过次数
2,518,545/4.4M
通过率
56.6%
相关标签
数组
分治
动态规划
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        sub_sum = [m]
        for n in nums[1:]:
            sub_sum.append(max(n, sub_sum[-1] + n))
            m = max(m, sub_sum[-1])
        return m


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [5, 4, -1, 7, 8]
    nums = [-1]
    solu = Solution()
    print(solu.maxSubArray(nums))
