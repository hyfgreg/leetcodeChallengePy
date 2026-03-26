"""560. 和为 K 的子数组
中等
相关标签
premium lock icon
相关企业
提示
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。



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

面试中遇到过这道题?
1/5
是
否
通过次数
1,038,577/2.2M
通过率
46.3%
相关标签
数组
哈希表
前缀和
"""

from typing import List
from collections import defaultdict

"""
前缀和 - 前面的某个前缀和 = 这段区间的和
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        pre = 0
        ret = 0
        for n in nums:
            pre += n
            if pre - k in count:
                ret += count[pre - k]
            count[pre] += 1
        return ret


if __name__ == "__main__":
    solu = Solution()
    # nums = [1, 1, -1, 0, 1, -1, -2, -3, 3, 2, 1]
    nums = [1, 2, 3]
    nums = [1, 1, 1]
    print(solu.subarraySum(nums, 2))
