"""
tag: 数组 双指针
给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。

初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1 的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素。



示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]


提示：

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    # 还有一种，把nums2贴到nums1后面然后排序
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = []
        i, j = 0, 0
        while i < m or j < n:
            if i >= m:
                tmp.append(nums2[j])
                j += 1
            elif j >= n:
                tmp.append(nums1[i])
                i += 1
            else:
                n1, n2 = nums1[i], nums2[j]
                if n1 < n2:
                    tmp.append(n1)
                    i += 1
                else:
                    tmp.append(n2)
                    j += 1
        for _ in range(m + n):
            nums1[_] = tmp[_]

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        利用nums1的后部，双指针，从后往前移动，把大的值放在nums1的尾部
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        index = m + n - 1
        while i >= 0 or j >= 0:
            if i < 0:
                nums1[index] = nums2[j]
                j -= 1
                index -= 1
            elif j < 0:
                i -= 1
            else:
                n1, n2 = nums1[i], nums2[j]
                if n1 > n2:
                    nums1[index] = n1
                    i -= 1
                    index -= 1
                else:
                    nums1[index] = n2
                    j -= 1
                    index -= 1


if __name__ == '__main__':
    # nums1 = [1, 2, 3, 0, 0, 0]
    nums1 = [1]
    m = 1
    # nums2 = [2, 5, 6]
    nums2 = []
    n = 0
    s = Solution()
    s.merge2(nums1, m, nums2, n)
    print(nums1)
