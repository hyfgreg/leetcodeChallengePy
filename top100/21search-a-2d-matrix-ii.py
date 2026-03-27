"""240. 搜索二维矩阵 II
中等
相关标签
premium lock icon
相关企业
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

面试中遇到过这道题?
1/5
是
否
通过次数
812,234/1.4M
通过率
57.0%
相关标签
数组
二分查找
分治
矩阵
"""

from typing import List

"""
Z字形查找很有意思！！！从右上角开始，比全部数字大就下一行，比那个数字小就往左边走一列，直到行走完或者列走完
"""
class Solution:

    def searchMatrixZ(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def biserach(nums: List[int]):
            nonlocal target
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True, mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            if right == -1:
                # 此时这一行/一列都比target大
                return False, -1
            return False, left - 1

        # 先按行找
        r = 0
        while r < len(matrix):
            find, index = biserach(matrix[r])
            if find:
                return True
            if index == -1:
                return False
            if index < len(matrix):
                cols = [row[index] for row in matrix[r + 1 :]]
                find, _ = biserach(cols)
                if find:
                    return True
            r += 1
        return False

        # # 先按列找
        # find, index = biserach([r[0] for r in matrix])
        # if find:
        #     return True
        # if index != -1:
        #     rows = matrix[index][1:]
        #     find = biserach(rows)[0]
        #     if find:
        #         return True
        # for j in range(len(matrix) - 1, -1, -1):
        #     cols = [r[j] for r in matrix[1:]]
        #     find, _ = biserach(cols)
        #     if find:
        #         return True
        # return False


if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 5
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 20
    solu = Solution()
    for r in matrix:
        for n in r:
            print(n, solu.searchMatrix(matrix, target))
