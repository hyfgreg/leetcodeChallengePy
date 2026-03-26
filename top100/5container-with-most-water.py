"""
11. 盛最多水的容器
已解答
中等
相关标签
premium lock icon
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

面试中遇到过这道题?
1/5
是
否
通过次数
2,107,755/3.4M
通过率
61.7%
相关标签
贪心
数组
双指针
"""

from typing import List

"""
一句话概括：我们left++和right--都是为了尝试取到更多的水，如果短的板不动的话，取到的水永远不会比上次多。
"""
class Solution:
    def maxAreaViolent(self, height: List[int]) -> int:
        m = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                m = max(m, (j - i) * min(height[i], height[j]))
        return m

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        m = 0

        while left < right:
            m = max(m, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return m


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea(height))
