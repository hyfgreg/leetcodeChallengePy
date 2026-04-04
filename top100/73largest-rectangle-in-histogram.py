"""84. 柱状图中最大的矩形
困难
相关标签
premium lock icon
相关企业
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。



示例 1:



输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：



输入： heights = [2,4]
输出： 4


提示：

1 <= heights.length <=105
0 <= heights[i] <= 104

面试中遇到过这道题?
1/5
是
否
通过次数
662,801/1.3M
通过率
49.2%
相关标签
栈
数组
单调栈
"""

from typing import List

"""
思路: 计算以每一根柱子为高时的最大面积，最大的那个就是
如何计算呢？
1. 以我为高
2. 左右两边的必须比我低
3. 找到左右最近的那个比我高的，然后就可以算了
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                right[j] = i
            stack.append(i)
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                left[j] = i
            stack.append(i)

        # print(heights)

        # print(left)
        # print(right)

        return max([(right[i] - left[i] - 1) * heights[i] for i in range(n)])


if __name__ == "__main__":
    heights = [3, 5, 5, 2, 5, 5, 6, 6, 4, 4, 1, 1, 2, 5, 5, 6, 6, 4, 1, 3]
    heights = [2, 1, 5, 6, 2, 3]

    solu = Solution()
    print(solu.largestRectangleArea(heights))
