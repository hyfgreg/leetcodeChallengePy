"""
70. 爬楼梯
简单
相关标签
premium lock icon
相关企业
提示
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？



示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶


提示：

1 <= n <= 45

面试中遇到过这道题?
1/5
是
否
通过次数
2,159,584/3.9M
通过率
55.7%
相关标签
记忆化
数学
动态规划
"""

"""
dp[i]: 上到第i级台阶有多少种方法
dp[i] = dp[i-1] + dp[i-2]，从上一级跨一步上来，从上两级跨一步上来
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # dp = [0] * n
        # dp[0] = 1
        # dp[1] = 2
        # for i in range(2, n):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[-1]
        # n-2, n-1, n
        p = 1  # 爬1层
        q = 2  # 爬2层
        if n == 1:
            return p
        if n == 2:
            return q
        r = 0
        for _ in range(2, n):
            r = p + q
            p = q
            q = r
        return r


if __name__ == "__main__":
    solu = Solution()
    n = 3
    print(solu.climbStairs(n))
