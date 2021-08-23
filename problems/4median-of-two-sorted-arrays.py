"""
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000


提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

tag: 数组 二分查找 分治

背诵
操！
nums1: 1, 3, 4, 9
nums2: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(log(m+n))

        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        # print(f"left {left}, right {right}")
        left_k = self.get_kth(nums1, 0, m, nums2, 0, n, left)
        # print("=====" * 10)
        right_k = self.get_kth(nums1, 0, m, nums2, 0, n, right)
        return (left_k + right_k) / 2

    def get_kth(self, nums1: List[int], start1: int, end1: int, nums2: List[int], start2: int, end2: int, k: int):
        len1 = end1 - start1
        len2 = end2 - start2
        # print("-----" * 10)
        # print(f"len1 {len1}, len2 {len2}, k {k}")
        if len1 == 0:
            # print(f"len1 == 0 , return nums2[start2 + k - 1] {nums2[start2 + k - 1]}")
            return nums2[start2 + k - 1]
        if len2 == 0:
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])

        k_sub = k // 2
        # print(f"k//2 {k_sub}")
        i = start1 + min(len1, k_sub) - 1
        j = start2 + min(len2, k_sub) - 1
        # print(f"i {i}, j {j}")
        if nums1[i] < nums2[j]:
            return self.get_kth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))
        else:
            return self.get_kth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        # O(log min(m+n))
        # 中位数（又称中值，英语：Median），[统计学] (https://baike.baidu.com/item/统计学/2630438)中的专有名词，
        # 代表一个样本、种群或 [概率分布] (https://baike.baidu.com/item/概率分布/828907)中的一个数值，
        # 其可将数值集合划分为相等的上下两部分。

        对于两个排序数组，把数组A分为i和m-i两部分，把数组B分为j和n-j两部分，如果i,j符合中位数切分，则
        max(A[i-1], B[j-1]) <= min(A[i], B[j])

        又A,B是两个升序数组，则
        A[i-1] <= B[j] and B[j-1]<=A[i]
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        half = (len1 + len2 + 1) // 2
        left, right = 0, len1
        while left <= right:
            i = left + (right - left) // 2
            j = half - i
            if i != 0 and j != len2 and nums1[i - 1] > nums2[j]:
                right = i - 1
            elif i != len1 and j != 0 and nums1[i] < nums2[j - 1]:
                left = i + 1
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (len1 + len2) % 2 == 1:
                    return max_left

                if i == len1:
                    min_right = nums2[j]
                elif j == len2:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                return (max_left + min_right) / 2


def test(nums1: List[int], nums2: List[int]):
    s = Solution2()
    return s.findMedianSortedArrays(nums1, nums2)


if __name__ == '__main__':
    print(test([1, 3], [2]))

    print(test([0, 0], [0, 0]))
    print(test([1, 3, 4, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(test([1], [2, 3, 4, 5, 6]))

    print(test([1, 2], [3, 4]))
