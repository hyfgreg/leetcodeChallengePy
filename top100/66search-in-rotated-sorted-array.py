"""33. 搜索旋转排序数组
中等
相关标签
premium lock icon
相关企业
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向左旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。



示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1


提示：

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-104 <= target <= 104

面试中遇到过这道题?
1/5
是
否
通过次数
1,309,966/2.8M
通过率
46.0%
相关标签
数组
二分查找
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            #print(left, mid, right)
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                #print("haha")
                if nums[left] < nums[right]:  # 此时已经是排好序的了
                    right = mid - 1
                elif nums[mid] < nums[left]:  # nums[left] > nums[right-1]
                    left = left + 1
                    right = mid
                else:  # nums[left] > nums[right - 1]
                    #print("gugua")
                    if target < nums[left]:
                        left = left + 1
                    else:
                        right = mid - 1
            else:
                # print("xixi")
                if nums[left] < nums[right]:  # 此时已经是排好序的了
                    left = mid + 1
                elif nums[mid] < nums[left]:  # nums[left] > nums[right-1]
                    if nums[left] > target:
                        left = mid + 1
                    else:
                        # print("yy")
                        right = mid - 1
                else:  # nums[left] > nums[right - 1]
                    left = mid + 1
        return -1


if __name__ == "__main__":
    numss = [
        [3, 4, 5, 6, 7, 0, 1, 2],
        [3, 1],
        [7, 8, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 1],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
    ]

    solu = Solution()
    for nums in numss:
        print(nums)
        for i in nums:
            print(i, solu.search(nums, i))
            print("=====")
