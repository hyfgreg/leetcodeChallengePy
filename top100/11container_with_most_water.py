"""
11. 盛最多水的容器
中等
相关标签
相关企业
提示
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。



示例 1：



输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1


提示：

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ret = 0
        for i in range(len(height) - 1):
            if i > 0 and height[i] <= height[i - 1]:
                continue
            for j in range(i + 1, len(height)):
                ret = max(ret, min(height[i], height[j]) * (j - i))
        return ret

    """
    难点在于证明贪心的正确性, 谁小就移动谁
    area = min(x,y) * l
    area2 = min(x1, y) * (l-1)
    """

    def maxArea2(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        ret = 0
        left = 0
        right = len(height) - 1
        while left < right:
            ret = max(ret, min(height[left], height[right]) * (right - left))
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return ret


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea2(height))
