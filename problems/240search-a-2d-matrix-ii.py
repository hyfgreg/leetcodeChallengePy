"""
240. 搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。


示例 1：


输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
示例 2：


输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false


提示：

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
每行的所有元素从左到右升序排列
每列的所有元素从上到下升序排列
-109 <= target <= 109
通过次数160,487提交次数338,257

tag: 数组 二分查找 分治 矩阵
背诵线性的方法，官方题解的方法4，我的可以优化一下，和方法3思路类似
线性的，从左下或者右上开始搜索
左下开始: 大了就往上，小了就往右
"""
from functools import lru_cache

from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # print(matrix)
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        while top <= bottom and left <= right:
            # print(f"top {top}, bottom {bottom}")
            # print(f"left {left}, right {right}")
            row_mid = top + (bottom - top) // 2
            col_mid = left + (right - left) // 2
            # print(f"row_mid {row_mid}, col_mid {col_mid}")
            if matrix[row_mid][col_mid] == target:
                return True
            elif target < matrix[row_mid][col_mid]:
                """
                [
                [1,  2,  3,  4,  5],
                [6,  7,  8,  9,  10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]
              ]
                """
                # if left == right == top == bottom == 0:
                #     break
                # right = col_mid
                # bottom = row_mid
                return self.searchMatrix([row[left:right + 1] for row in matrix[top:row_mid]],
                                         target) or self.searchMatrix(
                    [row[left:col_mid] for row in matrix[row_mid:bottom + 1]], target)
            else:
                # print("haha")
                return self.searchMatrix([row[left:right + 1] for row in matrix[row_mid + 1:bottom + 1]],
                                         target) or self.searchMatrix(
                    [row[col_mid + 1:right + 1] for row in matrix[top:row_mid + 1]],
                    target)

        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 25
    print(s.searchMatrix(matrix, target))
    matrix = [[-1, 3]]
    target = 3
    print(s.searchMatrix(matrix, target))
    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    target = 5
    print(s.searchMatrix(matrix, target))
