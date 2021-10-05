"""
329. 矩阵中的最长递增路径
给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。



示例 1：


输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4
解释：最长递增路径为 [1, 2, 6, 9]。
示例 2：


输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
示例 3：

输入：matrix = [[1]]
输出：1


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
通过次数56,237提交次数115,823
tag: 深度优先搜索 广度优先搜索 图 拓扑排序 记忆化搜索 动态规划
背诵，这里的memo很巧妙，重点就是这个，memo的每个值保存了经过该点的有效路径的长度
另外，如果搜索到这个点时，该点的memo值>0表示该点已经被搜索过了，直接掠过就可以
"""
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == n == 1:
            return 1

        # memo = [[False for _ in range(n)] for i in range(m)]
        ans = 0

        def dfs(x, y):
            nonlocal memo, ans
            # print(f"x {x} y {y} matrix[x][y] {matrix[x][y]}")
            # print(f"memo {memo}")
            # print(f"curr {curr}")
            if memo[x][y] > 0:
                return memo[x][y]
            memo[x][y] += 1
            for (dx, dy) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_x = x + dx
                new_y = y + dy
                if (0 <= new_x < m) and (0 <= new_y < n) and (matrix[x][y] < matrix[new_x][new_y]):
                    memo[x][y] = max(memo[x][y], dfs(new_x, new_y) + 1)
            return memo[x][y]

        memo = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        # print(ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    print(s.longestIncreasingPath(matrix))
