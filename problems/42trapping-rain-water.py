"""
42. 接雨水
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
0 <= n <= 3 * 104
0 <= height[i] <= 105
通过次数289,892提交次数509,024

tag: 栈 数组 双指针 动态规划 单调栈

淦淦淦
"""
from typing import List


class Solution:
    # 单调栈版本O(N), O(N)
    def trap(self, height: List[int]) -> int:
        ret = 0
        st = []
        for index, h in enumerate(height):
            # print("=====" * 10)
            # print(f"index {index}, h {h}")
            while st and h > height[st[-1]]:
                top = st.pop()
                if not st:
                    break
                left = st[-1]
                width = index - left - 1
                water_height = min(h, height[left]) - height[top]
                ret += width * water_height
                # print(f"width {width}, water_height {water_height}")
            st.append(index)
        return ret


class SolutionDoublePointer:
    # 双指针版本，O(N), O(1)
    # 基于动态规划版本，结合这个题目，非常巧妙
    # 对于每一个格子，water_height都取决于min(leftMax[i], rightMax[i]), 且leftMax从左往右单调递增，rightMax从右往左单调递增
    # 那么可以分别从左边、右边开始，向中间靠拢，然后分别计算leftMax和rightMax
    # 当leftMax<rightMax时，可以直接算出water_height
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        ret = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                ret += left_max - height[left]
                left += 1
            else:
                ret += right_max - height[right]
                right -= 1
        return ret


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = SolutionDoublePointer()
    print(s.trap(height))
