"""
48. 旋转图像
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。



示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
示例 2：


输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
示例 3：

输入：matrix = [[1]]
输出：[[1]]
示例 4：

输入：matrix = [[1,2],[3,4]]
输出：[[3,1],[4,2]]


提示：

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
通过次数210,853提交次数286,898

tag: 数组 数学 矩阵

# 先水平翻转，再对角线翻转
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        left, top = 0, 0
        right, bottom = n - 1, n - 1
        tmp = [0] * (n - 1)  # TODO 这里可以优化，直接用matrix内部的元素作为tmp,比如说第一行
        while left <= right:
            # (top, left) -> (top, right)
            for row in range(bottom - top):
                tmp[row] = matrix[row + top][right]
                matrix[row + top][right] = matrix[top][row + left]
            # print(f"tmp {tmp}")
            # print(f"matrix {matrix}")
            # (top, right) -> (bottom, right)
            for col in range(right - left):
                matrix[bottom][right - col], tmp[col] = tmp[col], matrix[bottom][right - col]
            # print(f"tmp {tmp}")
            # print(f"matrix {matrix}")
            # (bottom, right) -> (bottom, left)
            for row in range(bottom - top):
                matrix[bottom - row][left], tmp[row] = tmp[row], matrix[bottom - row][left]
            # print(f"tmp {tmp}")
            # print(f"matrix {matrix}")
            # (bottom, left) -> (top, left)
            for col in range(right - left):
                matrix[top][col + left], tmp[col] = tmp[col], matrix[top][col + left]
            # print(f"tmp {tmp}")
            # print(f"matrix {matrix}")
            # print("=====" * 10)
            # update top, bottom, left, right
            top += 1
            left += 1
            bottom -= 1
            right -= 1


if __name__ == '__main__':
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s = Solution()
    s.rotate(matrix)
    print(matrix)

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(matrix)
    print(matrix)

    matrix = [[1]]
    s.rotate(matrix)
    print(matrix)

    matrix = [[1, 2], [3, 4]]
    s.rotate(matrix)
    print(matrix)
