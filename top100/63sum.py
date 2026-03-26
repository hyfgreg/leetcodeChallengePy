"""
15. 三数之和
已解答
中等
相关标签
premium lock icon
相关企业
提示
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。





示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。


提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

面试中遇到过这道题?
1/5
是
否
通过次数
2,848,904/7.1M
通过率
40.3%
相关标签
数组
双指针
排序
"""

"""
这里的关键是
left去重的时候，要和处理过的数字做对比，不然会漏掉一些数
middle和right去重的时候，可以和未处理过的数字对比
以left为锚点，然后退化成双指针找2sum（排好序的）
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:  # type: ignore
        nums.sort()
        ret = []
        for left in range(len(nums) - 2):
            if left > 0 and nums[left - 1] == nums[left]:
                continue
            target = -nums[left]
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                s = nums[middle] + nums[right]
                if s == target:
                    ret.append([nums[left], nums[middle], nums[right]])
                    while middle < right and nums[middle] == nums[middle + 1]:
                        middle += 1
                    while middle < right and nums[right] == nums[right - 1]:
                        right -= 1
                    middle += 1
                    right -= 1
                elif s < target:
                    middle += 1
                else:
                    right -= 1
        return ret


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))
