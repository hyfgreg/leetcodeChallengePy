"""416. 分割等和子集
中等
相关标签
premium lock icon
相关企业
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。



示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。


提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100

面试中遇到过这道题?
1/5
是
否
通过次数
974,310/1.8M
通过率
54.1%
相关标签
数组
动态规划
"""

from typing import List

"""
dp[i][j] = dp[i-1][j]  or  (j >= nums[i-1] and dp[i-1][j - nums[i-1]])

i 表示考虑前 i 个元素（0-indexed 下标 0 ~ i-1）
j 表示当前需要凑出的和
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]  # 不选i
                if j >= num:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - num]  # 尝试选i
            if dp[i][target]:
                return True
        return dp[-1][-1]

    def canPartition1D(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
            if dp[target]:
                return True
        return dp[target]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    nums = [1, 2, 3, 10]
    solu = Solution()
    print(solu.canPartition(nums))
