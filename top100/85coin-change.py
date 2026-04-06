"""322. 零钱兑换
中等
相关标签
premium lock icon
相关企业
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。



示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0


提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

面试中遇到过这道题?
1/5
是
否
通过次数
1,356,186/2.6M
通过率
52.8%
相关标签
广度优先搜索
数组
动态规划
"""

from typing import List

"""
dp[i] = 1 + min(dp[i-j]) for j in coins
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            minn = float("inf")
            for c in coins:
                if c > i:
                    continue
                elif c == i:
                    minn = 0
                elif dp[i - c] != -1:
                    minn = min(dp[i - c], minn)
            if minn == float("inf"):
                dp[i] = -1
            else:
                dp[i] = 1 + minn
        # print(dp)
        return dp[-1]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    # coins = [2]
    # amount = 3
    solu = Solution()
    print(solu.coinChange(coins, amount))
