"""
128. 最长连续序列
中等
相关标签
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


提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List

"""
计算以每个数为起点的最长连续序列的长度，取最大的那个
不做优化，需要O(n^2),即外圈便利一遍，然后内圈再检查x+1, x+2,...是否在序列中
优化一下, 如果当前数x，它的前一个数x-1也在序列中，就不用检查x了，只需要检查x-1即可
set(nums)，把序列转换成集合，减少遍历次数，同时查询变成O(1)
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ret = 0
        for num in num_set:
            if num - 1 in num_set:
                continue
            current_length = 1
            current_num = num
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            ret = max(ret, current_length)
        return ret


if __name__ == '__main__':
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    s = Solution()
    ret = s.longestConsecutive(nums)
    print(ret)
