"""42. 接雨水
已解答
困难
相关标签
premium lock icon
相关企业
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9


提示：

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

面试中遇到过这道题?
1/5
是
否
通过次数
1,704,781/2.6M
通过率
65.9%
相关标签
栈
数组
双指针
动态规划
单调栈
"""

from typing import List

"""
两年过去了，我的思路竟然是一模一样的。。。
双指针的思路：
维护两个变量
leftMax：左指针及其左边的最高柱子高度，当左指针右移时更新
rightMax：右指针及其右边的最高柱子高度，当右指针左移时更新
因为木桶效应，存水量取决于短的柱子
所以当 leftMax<rightMax 时，左指针指向的柱子的存水量只取决于leftMax，即使左指针右边有还没遍历到的更高的柱子也没有影响，存水量 ans+=leftMax-heigth[left]，左指针右移，left++
右指针同理
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        left, right = 0, 1
        ret = 0
        tmp = 0
        # print("height", height)
        while right < len(height):
            if height[left] <= height[right]:
                # print("left", left, "right", right, "tmp", tmp, ret)
                ret += tmp
                tmp = 0
                left = right
                right += 1
                # print("left", left, "right", right, "tmp", tmp, ret)

            else:
                # print("aaa", "left", left, "right", right, "tmp", tmp)
                # print(height, height[left], height[right])
                tmp += height[left] - height[right]
                right += 1
                # print("bbb", "left", left, "right", right, "tmp", tmp)
        if tmp:
            ret += self.trap(height[left:][::-1])
        return ret


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    print(s.trap(height))
