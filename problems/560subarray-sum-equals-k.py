"""
560. 和为 K 的子数组
给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。



示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2


提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
通过次数148,039提交次数331,692

tag: 数组 哈希表 前缀和
背诵，这里有一个概念要记住，前缀和-前缀和=子数组之和
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = {}
        _sum = 0
        count = 0
        table[0] = 1
        for num in nums:
            _sum += num
            if _sum - k in table:
                # print(f"sum {_sum}, num {num}")
                count += table[_sum - k]
            if _sum in table:
                table[_sum] += 1
            else:
                table[_sum] = 1
        return count


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1]
    k = 2
    print(s.subarraySum(nums, k))
    nums = [1, 2, 3]
    k = 3
    print(s.subarraySum(nums, k))
    nums = [1, -1, 0]
    k = 0
    print(s.subarraySum(nums, k))
