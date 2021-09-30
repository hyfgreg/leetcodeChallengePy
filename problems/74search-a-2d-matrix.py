"""
74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。


示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
通过次数169,693提交次数368,383

tag: 数组 二分查找 矩阵
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m == n == 1:
            return matrix[0][0] == target

        bottom, top = 0, m - 1
        while bottom <= top:
            mid = bottom + (top - bottom) // 2
            value = matrix[mid][0]
            if value == target:
                return True
            if value > target:
                top = mid - 1
            else:
                bottom = mid + 1
        # print(bottom, top, mid)
        if top == -1:
            top += 1
        nums = matrix[top]
        # print(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # print(left, right, mid)
            value = nums[mid]
            if value == target:
                return True
            if value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13

    # s.searchMatrix(matrix, target)
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(s.searchMatrix(matrix, target))
