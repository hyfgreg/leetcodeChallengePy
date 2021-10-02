"""
123. 买卖股票的最佳时机 III
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



示例 1:

输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2：

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
示例 4：

输入：prices = [1]
输出：0


提示：

1 <= prices.length <= 105
0 <= prices[i] <= 105
通过次数131,619提交次数245,489

tag: 数组 动态规划
背诵，主要是buy2的初始值的设定，按照题目的意思，是可以在一天内，买了卖xN的
"""
from typing import List


class Solution:
    def maxProfitOld(self, prices: List[int]) -> int:
        dp = [[[0, 0] for _ in range(2)] for _ in range(len(prices))]
        dp[0][0][1] = -prices[0]
        dp[0][1][1] = -prices[0]
        for i in range(1, len(prices)):
            # 交易1次
            dp[i][0][0] = max(dp[i - 1][0][0], prices[i] + dp[i - 1][0][1])  # 未持有
            dp[i][0][1] = max(dp[i - 1][0][1], -prices[i])  # 持有

            # 交易2次
            dp[i][1][0] = max(dp[i - 1][1][0], prices[i] + dp[i - 1][1][1])
            dp[i][1][1] = max(dp[i - 1][1][1], -prices[i] + dp[i - 1][0][0])
        return dp[-1][1][0]

    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0
        for i in range(1, len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, prices[i] + buy1)
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, prices[i] + buy2)
        return sell2


if __name__ == '__main__':
    s = Solution()
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(s.maxProfit(prices))
    prices = [1, 2, 3, 4, 5]
    print(s.maxProfit(prices))
