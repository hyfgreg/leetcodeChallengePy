"""
283. 移动零
简单
相关标签
相关企业
提示
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。



示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]


提示:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


进阶：你能尽量减少完成的操作次数吗？
"""
from typing import List


class MySolution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        a = []
        for num in nums:
            if num != 0:
                a.append(num)
        if len(a) == len(nums):
            return
        for i, b in enumerate(a):
            nums[i] = b
        for i in range(len(a), len(nums)):
            nums[i] = 0


"""
一次遍历
这里参考了快速排序的思想，快速排序首先要确定一个待分割的元素做中间点 x，然后把所有小于等于 x 的元素放到 x 的左边，大于 x 的元素放到其右边。
这里我们可以用 0 当做这个中间点，把不等于 0(注意题目没说不能有负数)的放到中间点的左边，等于 0 的放到其右边。
这的中间点就是 0 本身，所以实现起来比快速排序简单很多，我们使用两个指针 i 和 j，只要 nums[i]!=0，我们就交换 nums[i] 和 nums[j]

作者：王尼玛
链接：https://leetcode.cn/problems/move-zeroes/solutions/90229/dong-hua-yan-shi-283yi-dong-ling-by-wang_ni_ma/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                print(i, j, nums)
                continue
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
            print(i, j, nums)


if __name__ == '__main__':
    # nums = [0, 1, 0, 3, 12]
    nums = [1, 0, 0, 0, 0, 0, 3, 12, 13, 14, 15, 0, 0, 0, 16, 17, 18]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)
