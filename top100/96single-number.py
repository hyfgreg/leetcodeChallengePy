"""

代码
测试用例
测试用例
测试结果
136. 只出现一次的数字
简单
相关标签
premium lock icon
相关企业
提示
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。



示例 1 ：

输入：nums = [2,2,1]

输出：1

示例 2 ：

输入：nums = [4,1,2,1,2]

输出：4

示例 3 ：

输入：nums = [1]

输出：1



提示：

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
除了某个元素只出现一次以外，其余每个元素均出现两次。

面试中遇到过这道题?
1/5
是
否
通过次数
1,449,493/1.9M
通过率
76.6%
相关标签
位运算
数组
"""

from typing import List

"""
他妈的的，异或
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for n in nums:
            single ^= n
        return single
