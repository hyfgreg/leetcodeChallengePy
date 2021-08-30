"""
322. 零钱兑换
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
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2


提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
通过次数286,612提交次数647,280

tag: 广度优先搜索 数组 二叉树
"""
from typing import List


class Solution:
    dp = []

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        tmp = None
        for i in range(1, amount + 1):
            for c in coins:
                if i == c:
                    tmp = 0
                elif i - c > 0 and dp[i - c] != -1:
                    if tmp is None or tmp > dp[i - c]:
                        tmp = dp[i - c]
            if tmp is not None:
                dp[i] = tmp + 1
            tmp = None
            # print(f"i {i}, dp {dp}")
        return dp[amount]

    def coinChangeDFS(self, coins: List[int], amount: int) -> int:
        self.dp = [-2] * (amount + 1)
        self.dp[0] = 0
        return self.dfs(coins, amount)

    def dfs(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if self.dp[amount] != -2:
            return self.dp[amount]
        for c in coins:
            ret = self.dfs(coins, amount - c)
            if ret >= 0:
                if self.dp[amount] < 0 or self.dp[amount] > ret + 1:
                    self.dp[amount] = ret + 1
        if self.dp[amount] == -2:
            self.dp[amount] = -1
        return self.dp[amount]


if __name__ == '__main__':
    # coins = [1, 2, 5]
    # amount = 11
    s = Solution()
    # print(s.coinChangeDFS(coins, amount))
    # coins = [2]
    # amount = 3
    # print(s.coinChangeDFS(coins, amount))
    coins = [186, 419, 83, 408]
    amount = 6249
    print(s.coinChange(coins, amount))
    print(s.coinChangeDFS(coins, amount))
