"""238. 除了自身以外数组的乘积
中等
相关标签
premium lock icon
相关企业
提示
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。



示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]


提示：

2 <= nums.length <= 105
-30 <= nums[i] <= 30
输入 保证 数组 answer[i] 在  32 位 整数范围内


进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）


面试中遇到过这道题?
1/5
是
否
通过次数
954,946/1.2M
通过率
77.9%
相关标签
数组
前缀和
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        for n in nums:
            prefix.append(prefix[-1] * n)
        for n in nums[::-1]:
            suffix.append(suffix[-1] * n)
        ret = []
        n = len(nums)
        for i in range(n):
            ret.append(prefix[i] * suffix[n - i - 1])
        return ret

    def productExceptSelfO1(self, nums: List[int]) -> List[int]:
        answer = [1]
        for n in nums[:-1]:
            answer.append(answer[-1]* n)
        n = len(nums)
        r = 1
        for i in range(n - 1, -1, -1):
            answer[i] = (answer[i]) * r
            r *= nums[i]
        return answer


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solu = Solution()
    print(solu.productExceptSelfO1(nums))
