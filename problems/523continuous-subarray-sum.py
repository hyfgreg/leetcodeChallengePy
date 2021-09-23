"""
523. 连续的子数组和
给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

子数组大小 至少为 2 ，且
子数组元素总和为 k 的倍数。
如果存在，返回 true ；否则，返回 false 。

如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。



示例 1：

输入：nums = [23,2,4,6,7], k = 6
输出：true
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
示例 2：

输入：nums = [23,2,6,4,7], k = 6
输出：true
解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
示例 3：

输入：nums = [23,2,6,4,7], k = 13
输出：false


提示：

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
通过次数68,391提交次数249,065

tag: 数组 哈希表 数学 前缀和
背诵，思想还是前缀和，这里的trick点在于，子数组和是k的倍数时，则两个前缀和对k求余的余数是相等的，所以只要存余数的索引就行了，然后在余数相等的情况下看索引之差是不是大于1就行
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        table = {0: -1}  # remainder: [index]
        _sum = 0
        for i, num in enumerate(nums):
            _sum += num
            remainder = _sum % k
            if remainder in table and i - table[remainder] > 1:
                return True
            if not remainder in table:
                table[remainder] = i
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [23, 2, 6, 4, 7]
    k = 6
    print(s.checkSubarraySum(nums, k))
