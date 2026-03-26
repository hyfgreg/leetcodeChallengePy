"""48. 旋转图像
中等
相关标签
premium lock icon
相关企业
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。



示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
示例 2：


输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


提示：

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000



面试中遇到过这道题?
1/5
是
否
通过次数
956,371/1.2M
通过率
79.3%
相关标签
数组
数学
矩阵
"""

from typing import List

"""
https://cloud.tencent.com/developer/article/1649537
"""

"""
第二种实在记不住啊。。。
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        先转置，再水平翻转
        """
        # 1. 转置
        for i in range(len(matrix)):
            for j in range(len(matrix) - 1, i - 1, -1):
                # print(i, j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 2. 水平翻转
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][len(matrix) - j - 1] = matrix[i][len(matrix) - j - 1], matrix[i][j]

    def rotateswap(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(n // 2):
                temp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

    solu = Solution()
    solu.rotateswap(matrix)
    print(matrix)
