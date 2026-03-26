"""54. 螺旋矩阵
中等
相关标签
premium lock icon
相关企业
提示
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。



示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

面试中遇到过这道题?
1/5
是
否
通过次数
963,180/1.8M
通过率
55.0%
相关标签
数组
矩阵
模拟
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        rows = len(matrix)
        cols = len(matrix[0])
        count = rows * cols
        round = 0
        i, j = 0, 0
        while True:
            # go right  ➡
            end = cols - round
            while j < end:
                ret.append(matrix[i][j])
                j += 1
            # print("right", ret)
            if len(ret) == count:
                break
            j -= 1
            i += 1

            # go down   ⬇
            end = rows - round
            while i < end:
                ret.append(matrix[i][j])
                i += 1
            # print("down", ret)
            if len(ret) == count:
                break
            i -= 1
            j -= 1

            # go left   ⬅
            end = round
            while j > end - 1:
                ret.append(matrix[i][j])
                j -= 1
            # print("left", ret)
            if len(ret) == count:
                break
            j += 1
            i -= 1

            # go up     ⬆
            end = round
            while i > end:
                ret.append(matrix[i][j])
                i -= 1
            # print("up", ret)
            if len(ret) == count:
                break

            round += 1
            i += 1
            j += 1

        return ret


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # [1,2,3,6,9,8,7,4,5]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    solu = Solution()
    ret = solu.spiralOrder(matrix)
    print("final", ret)
