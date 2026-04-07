"""
62. 不同路径
中等
相关标签
premium lock icon
相关企业
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？



示例 1：


输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6


提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109

面试中遇到过这道题?
1/5
是
否
通过次数
1,193,754/1.7M
通过率
70.2%
相关标签
数学
动态规划
组合数学
"""

"""
dp[i][j] = dp[i][j-1] + dp[i-1][j] # 向右 + 向下
这里的dp[i]只和同一行前一列和上一行同一列有关系，所以这里可以对空间进行优化
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i][j - 1] if j >= 1 else 0) + (dp[i - 1][j] if i >= 1 else 0)
                # print(i, j, dp)

        # print(dp)
        return dp[-1][-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
                #print(i, j, dp)

        # print(dp)
        return dp[-1]


if __name__ == "__main__":
    solu = Solution()
    print(solu.uniquePaths2(2, 2))
