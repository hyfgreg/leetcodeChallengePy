"""
42. 接雨水
困难
相关标签
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
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # print(height)
        ret = 0
        left = 0
        right = 1
        tmp = 0
        while right < len(height):
            if height[left] <= height[right]:
                # todo compute 容量
                # 移动left， right
                ret += tmp
                # print(left, right, ret)
                left = right
                right += 1
                tmp = 0
                # print("=====" * 10)
            else:
                tmp += abs(height[left] - height[right])
                # print(left, right, tmp)
                right += 1
        if left < right and len(height) > 2:
            # print(left, right)
            new_height = height[left:]
            new_height.reverse()
            ret += self.trap(new_height)
        return ret


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [4, 2, 3]
    s = Solution()
    print(s.trap(height))
