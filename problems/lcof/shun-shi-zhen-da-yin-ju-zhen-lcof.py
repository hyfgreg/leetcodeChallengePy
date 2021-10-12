"""
剑指 Offer 29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。



示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/

通过次数145,917提交次数331,535

tag: 数组 矩阵 模拟
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        (left, top)                 (right, top)



        (left, bottom)              (right, bottom)
        """
        if not matrix:
            return []
        m = len(matrix)
        if m == 1:
            return matrix[0]
        n = len(matrix[0])

        left, top = 0, 0
        bottom, right = m - 1, n - 1
        ret = []
        while left <= right and top <= bottom:

            for num in matrix[top][left:right + 1]:
                ret.append(num)

            for row in matrix[top + 1:bottom + 1]:
                ret.append(row[right])
            if left < right and top < bottom:
                for num in matrix[bottom][right - 1:left:-1]:
                    ret.append(num)

                for row in matrix[bottom:top:-1]:
                    ret.append(row[left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return ret


if __name__ == '__main__':
    s = Solution()
    # matrix = [[1, 2, 3],
    #           [4, 5, 6],
    #           [7, 8, 9]]
    # print(s.spiralOrder(matrix))
    #
    # matrix = [[1, 2, 3, 4],
    #           [5, 6, 7, 8],
    #           [9, 10, 11, 12]]
    #
    # print(s.spiralOrder(matrix))

    matrix = [[7],
              [9],
              [6]]
    print(s.spiralOrder(matrix))
