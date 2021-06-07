"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
 

提示：

1 <= prices.length <= 105
0 <= prices[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

题解: https://leetcode-cn.com/circle/article/qiAgHn/
"""
from typing import List


class SolutionK:
    def maxProfit(self, prices: List[int], k: int):
        """
        dp[i][k][0/1]: i 第几天, k 最多k次交易, 0/1第i天没有持有/持有股票

        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + price[i]) # 1. 今天什么都没做，和昨天保持一致(昨天结束时也是没有卖，且已经到了k) 2. 今天卖了(昨天结束时必然持有股票)
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - price[i]) # 1. 今天什么都没做，和昨天保持一致(昨天结束时卖了，且已经到了k) 2. 今天买入(昨天结束时必然没有持有股票)

        dp[-1][k][0] = 0
        dp[-1][k][1] = -infinity

        dp[i][0][0] = 0
        dp[i][0][1] = -infinity
        """
        dp = []
        for i in range(len(prices)):
            tmp = []
            for j in range(k + 1):
                if i == 0 and j == 1:
                    tmp.append([0, -prices[i]])
                else:
                    tmp.append([0, float('-inf')])
            dp.append(tmp)

        for i in range(1, len(prices)):
            for j in range(1, k + 1):
                for state in [0, 1]:
                    if state == 0:
                        dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                    elif state == 1:
                        dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[-1][k][0]


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        dp = []
        for i in range(len(prices)):
            tmp = []
            for j in range(3):
                if i == 0:
                    tmp.append([0, -prices[i]])
                else:
                    tmp.append([0, float('-inf')])
            dp.append(tmp)
        print('i j price')
        print(0, 0, prices[0], dp[0][0][0], dp[0][0][1])
        print(0, 1, prices[0], dp[0][1][0], dp[0][1][1])
        for i in range(1, len(prices)):
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])
            dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])
            # for j in range(1, 3):
            #     dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
            #     dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
            #     print(i, j, prices[i], dp[i][j][0], dp[i][j][1])

        return dp[-1][2][0]

    def max_profit(self, prices: List[int]) -> int:
        one_time0 = 0
        one_time1 = -prices[0]
        two_times0 = 0
        two_times1 = -prices[0]
        for i in range(1, len(prices)):
            one_time0 = max(one_time0, one_time1 + prices[i])
            one_time1 = max(one_time1, -prices[i])
            two_times0 = max(two_times0, two_times1 + prices[i])
            two_times1 = max(two_times1, one_time0 - prices[i])
            # dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            # dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])
            # dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])
            # dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])

        return two_times0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0][0] = 0
        dp[i][0][1] = -infinity

        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
        dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i]) -> max(dp[i-1][1][1], - prices[i])
        """
        # dp = []
        # for i in range(len(prices)):
        #     dp.append([0, 0])
        #
        # dp[0][1] = -prices[0]
        #
        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #     dp[i][1] = max(dp[i-1][1], - prices[i])
        # return dp[-1][0]

        p0 = 0
        p1 = -prices[0]
        print(0, prices[0], p0, p1)
        for i in range(1, len(prices)):
            p0 = max(p0, p1 + prices[i])
            p1 = max(p1, -prices[i])
            print(i, prices[i], p0, p1)
        return p0


if __name__ == '__main__':
    # s = Solution()
    # prices = [7, 1, 5, 3, 6, 4]
    # print(s.maxProfit(prices))
    # s = SolutionK()
    # prices = [3, 3, 5, 0, 0, 3, 1, 4]
    # print(s.maxProfit(prices, 2))
    s = Solution2()
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    # prices = [1, 2, 3, 4, 5]
    print(s.max_profit(prices))
