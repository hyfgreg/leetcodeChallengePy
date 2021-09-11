"""
59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。



示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]


提示：

1 <= n <= 20
通过次数123,184提交次数155,408

tag: 数组 矩阵 模拟
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        (left, top)                  (right top)
        (left bottom)                (right bottom)
        """
        left, right = 0, n
        top, bottom = 0, n
        value = 1
        ret = [[0 for _ in range(n)] for _ in range(n)]
        while left < right and top < bottom:
            # print(f'left {left} right {right} top {top} bottom {bottom}')
            i, j = top, left
            if i == bottom - 1 and j == right - 1:
                ret[i][j] = value
            while j < right - 1:
                ret[i][j] = value
                value += 1
                j += 1
            while i < bottom - 1:
                ret[i][j] = value
                value += 1
                i += 1
            while j > left:
                ret[i][j] = value
                value += 1
                j -= 1
            while i > top:
                ret[i][j] = value
                value += 1
                i -= 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return ret


if __name__ == '__main__':
    s = Solution()
    for n in range(1,11):
        print(s.generateMatrix(n))
