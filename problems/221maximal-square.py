"""
221. 最大正方形
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。



示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
示例 2：


输入：matrix = [["0","1"],["1","0"]]
输出：1
示例 3：

输入：matrix = [["0"]]
输出：0


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'
通过次数133,583提交次数281,966

tag: 数组 动态规划 矩阵
"""
import math
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(0)
            dp.append(tmp)
        max_side = 0
        for i in range(m):
            for j in range(n):
                # print(i, j, matrix[i][j])
                if matrix[i][j] == "0":
                    continue
                if i == 0:
                    dp[i][j] = 1
                    max_side = max(max_side, dp[i][j])
                    continue
                if j == 0:
                    dp[i][j] = 1
                    max_side = max(max_side, dp[i][j])
                    continue
                # print("haha")
                if dp[i - 1][j - 1] == 0 or dp[i][j - 1] == 0 or dp[i - 1][j] == 0:
                    dp[i][j] = 1
                else:
                    left_top_side = dp[i - 1][j - 1]
                    left_side = dp[i][j - 1]
                    top_side = dp[i - 1][j]
                    dp[i][j] = 1 + min(left_top_side, left_side, top_side)
                # print(dp)
                max_side = max(max_side, dp[i][j])
        return max_side * max_side


if __name__ == '__main__':
    s = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(s.maximalSquare(matrix))
