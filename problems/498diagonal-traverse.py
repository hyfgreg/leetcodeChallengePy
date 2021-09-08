"""
498. 对角线遍历
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。



示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释:



说明:

给定矩阵中的元素总数不会超过 100000 。
通过次数41,871提交次数90,393

tag: 数组 矩阵 模拟
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        if m == 0:
            return []
        if m == 1:
            return mat[0]
        n = len(mat[0])
        if n == 0:
            return []
        if n == 1:
            return [i[0] for i in mat]
        i, j = 0, 0
        upper = True
        ret = []
        while True:
            # print(i, j)
            ret.append(mat[i][j])
            if upper:
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1
            if len(ret) == m * n:
                break

            if upper:
                if i < 0 and j < n:
                    i = 0
                    upper = not upper
                elif j == n:
                    i += 2

                    j = n - 1
                    upper = not upper
            else:
                if i < m and j < 0:
                    j = 0
                    upper = not upper
                elif i == m:
                    i = m - 1
                    j += 2
                    upper = not upper

        return ret


if __name__ == '__main__':
    s = Solution()
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(s.findDiagonalOrder(mat))
    mat = [
        [1, 2],
        [3, 4]
    ]
    print(s.findDiagonalOrder(mat))
