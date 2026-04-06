"""118. 杨辉三角
简单
相关标签
premium lock icon
相关企业
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。





示例 1:

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例 2:

输入: numRows = 1
输出: [[1]]


提示:

1 <= numRows <= 30

面试中遇到过这道题?
1/5
是
否
通过次数
836,799/1.1M
通过率
78.0%
相关标签
数组
动态规划
"""

from typing import List

"""
dp[1] = [[1]]
dp[2] = [[1,2,1]]
dp[i][j] = dp[i-1][j-1] + dp[i-1][j] j-1 <0 -> 0 j >= n -> 0
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        dp = [[1]]
        for i in range(1, numRows):
            dp.append([0] * (i + 1))
            for j in range(i + 1):
                left = dp[i - 1][j - 1] if j >= 1 else 0
                right = dp[i - 1][j] if j < i else 0
                dp[i][j] = left + right
        return dp

if __name__ == "__main__":
    solu = Solution()
    print(solu.generate(5))