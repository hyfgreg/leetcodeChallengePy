"""
153. 寻找旋转排序数组中的最小值
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。



示例 1：

输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
示例 2：

输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
示例 3：

输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。


提示：

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 中的所有整数 互不相同
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
通过次数202,396提交次数357,757

tag: 数组 二分查找
逻辑
考虑数组中的最后一个元素 xx：在最小值右侧的元素（不包括最后一个元素本身），它们的值一定都严格小于 xx；
                        而在最小值左侧的元素，它们的值一定都严格大于 xx。
因此，我们可以根据这一条性质，通过二分查找的方法找出最小值。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-5irwp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from typing import List


class SolutionOfficial:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        right = length - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            if nums[left] < nums[mid] < nums[right]:
                return nums[left]
            if nums[left] > nums[right]:
                if nums[mid] < nums[right]:
                    right = mid - 1
                    left += 1
                else:
                    left = mid + 1

        return nums[left]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 4, 5, 1, 2]
    print(s.findMin(nums))
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(s.findMin(nums))
    nums = [11, 13, 15, 17]
    print(s.findMin(nums))
    nums = [13, 15, 17, 11]
    print(s.findMin(nums))
    nums = [1]
    print(s.findMin(nums))
    nums = [8, 0, 1, 2, 4, 5, 6, 7]
    print(s.findMin(nums))
