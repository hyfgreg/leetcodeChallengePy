"""74. 搜索二维矩阵
中等
相关标签
premium lock icon
相关企业
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。



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

面试中遇到过这道题?
1/5
是
否
通过次数
726,125/1.4M
通过率
52.5%
相关标签
数组
二分查找
矩阵
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if not rows:
            return False
        cols = len(matrix[0])
        if not cols:
            return False

        left, right = 0, rows * cols - 1
        while left <= right:
            #print(left, right)
            mid = left + (right - left) // 2
            #print(mid)
            i = mid // cols
            j = mid % cols
            #print(i, j)
            p#rint("=====")
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == "__main__":
    solu = Solution()
    print(solu.searchMatrix([[1, 1]], 2))
