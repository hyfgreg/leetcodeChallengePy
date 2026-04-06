"""198. 打家劫舍
中等
相关标签
premium lock icon
相关企业
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。



示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400

面试中遇到过这道题?
1/5
是
否
通过次数
1,563,322/2.8M
通过率
56.4%
相关标签
数组
动态规划
"""

from typing import List

"""
dp[i] 截止第i个邻居，能偷到的最多的钱，要注意，第i个邻居不一定被偷
dp[0] = nums[0]
dp[1] = max(ans, nums[1])
i >= 2:
dp[i] = max(ans, nums[i] + dp[i-2])
ans = max(ans, dp[i])

dp[i] = max(nums[i]+dp[i-2], dp[i-1]) 这个才是更好的
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

    def robeasy(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        a, b = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            a, b = b, max(b, nums[i] + a)
        return b


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    nums = [2, 7, 9, 3, 1]
    # nums = [2, 1, 1, 2]
    solu = Solution()
    print(solu.robeasy(nums))
