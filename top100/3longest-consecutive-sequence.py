"""128. 最长连续序列
已解答
中等
相关标签
premium lock icon
相关企业
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
示例 3：

输入：nums = [1,0,1,2]
输出：3


提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109

面试中遇到过这道题?
1/5
是
否
通过次数
1,474,497/3M
通过率
49.1%
相关标签
并查集
数组
哈希表
"""

from typing import List

"""
先去重
判断这个数是不是连续数字的开头数字，如果是，就从这个数字往后面数，直到不在nums中
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        m = 0
        for n in nums:
            if n-1 not in nums:
                current = 1
                cn = n
                while cn + 1 in nums:
                    current += 1
                    cn += 1
                m = max(m, current)
        return m
        


if __name__ == "__main__":
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    s = Solution()
    print(s.longestConsecutive(nums))
