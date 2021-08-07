"""
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。



示例 1：


输入：matrix = [[1,2,3],
               [4,5,6],
               [7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
通过次数173,495提交次数363,781

tag: 数组 矩阵 模拟
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        输入：matrix = [[1,2,3],
                       [4,5,6],
                       [7,8,9]]
        """
        # todo 这种题目要换图，然后手写上行列的移动范围
        ret = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        while left <= right and top <= bottom:
            row, col = top, left
            # (top, left) -> (top, right)
            while col <= right:
                ret.append(matrix[row][col])
                if col == right:
                    break
                col += 1
            # (top+1, right) -> (bottom, right)
            row += 1
            while row <= bottom:
                ret.append(matrix[row][col])
                if row == bottom:
                    break
                row += 1
            col -= 1
            if left < right and top < bottom:
                # (bottom, right - 1) -> (bottom, left)
                while col >= left:
                    ret.append(matrix[row][col])
                    if col == left:
                        break
                    col -= 1
                row -= 1
                while row >= top + 1:
                    # print(f"(row, top) == ({row}, {top})")
                    ret.append(matrix[row][col])
                    if row == top + 1:
                        break
                    row -= 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return ret

if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    # matrix = [[1, 2, 3, 4],
    #           [5, 6, 7, 8],
    #           [9, 10, 11, 12]]
    # matrix = [[3], [6], [9]]
    s = Solution()
    print(s.spiralOrder(matrix))
