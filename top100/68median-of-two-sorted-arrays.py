"""4. 寻找两个正序数组的中位数
困难
相关标签
premium lock icon
相关企业
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5




提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

面试中遇到过这道题?
1/5
是
否
通过次数
1,471,521/3.3M
通过率
44.5%
相关标签
高级工程师
数组
二分查找
分治
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        inf = float("inf")
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            i = left + (right - left) // 2
            j = (m + n + 1) // 2 - i

            left1 = -inf if i == 0 else nums1[i - 1]
            right1 = inf if i == m else nums1[i]
            left2 = -inf if j == 0 else nums2[j - 1]
            right2 = inf if j == n else nums2[j]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                return max(left1, left2)
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1


if __name__ == "__main__":
    nums1 = [1]
    nums2 = []
    solu = Solution()
    print(solu.findMedianSortedArrays(nums1, nums2))
