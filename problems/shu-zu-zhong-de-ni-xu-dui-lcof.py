"""
剑指 Offer 51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。



示例 1:

输入: [7,5,6,4]
输出: 5


限制：

0 <= 数组长度 <= 50000

通过次数98,010提交次数203,440

tag: 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序
背诵 注意逆序对增加的判断时机
"""
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        本质上是一个归并排序
        :param nums:
        :return:
        """
        self.tmp = nums[:]
        return self.merge(nums, 0, len(nums))

    def merge(self, nums: List[int], start, end) -> int:
        # print("start", start, "end", end)
        if end - start <= 1:
            # print("rev_count", 0)
            return 0
        mid = start + (end - start) // 2
        rev_count = self.merge(nums, start, mid) + self.merge(nums, mid, end)
        i, j = start, mid
        k = start
        # print("start", start, "end", end, "before rev_count", rev_count)
        while i < mid and j < end:
            if nums[i] <= nums[j]:
                self.tmp[k] = nums[i]
                i += 1
                # 注意这里，nums[i] <= nums[j]，则对于nums[i]和j之前的数字构成逆序对
                rev_count += (j - mid)
            else:
                # print("add", j - mid + 1, "j", j, "mid", mid)
                # print("two, rev_count", rev_count)
                self.tmp[k] = nums[j]
                j += 1
            k += 1
        # print("i", i, "j", j)
        while i < mid:
            self.tmp[k] = nums[i]
            # 注意这里，nums[i] <= nums[j]，则对于nums[i]和j之前的数字构成逆序对
            rev_count += (j - mid)
            k += 1
            i += 1
        while j < end:
            self.tmp[k] = nums[j]
            k += 1
            j += 1
        nums[start:end] = self.tmp[start:end]
        # print("start", start, "end", end, "rev_count", rev_count)
        # print("nums", nums)
        return rev_count


if __name__ == '__main__':
    s = Solution()
    nums = [7, 5, 6, 4]
    print(s.reversePairs(nums))
    # print(nums)
    nums = [1, 3, 2, 3, 1]
    print(s.reversePairs(nums))
