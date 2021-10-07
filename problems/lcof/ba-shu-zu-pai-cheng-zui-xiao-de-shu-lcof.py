"""
剑指 Offer 45. 把数组排成最小的数
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。



示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"


提示:

0 < nums.length <= 100
说明:

输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
通过次数108,429提交次数193,184

tag
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def my_compare(num1: int, num2: int):
            n1 = str(num1) + str(num2)
            n2 = str(num2) + str(num1)
            n1 = n1.lstrip('0')
            n2 = n2.lstrip('0')
            if len(n1) < len(n2):
                return -1
            if len(n2) < len(n1):
                return 1
            for i, j in zip(n1, n2):
                if i < j:
                    return -1
                elif i > j:
                    return 1
            return 0

        nums.sort(key=cmp_to_key(my_compare))
        # print(nums)
        return ''.join([str(i) for i in nums])


class SolutionOfficial:
    # 背诵这个快排方式
    def minNumber(self, nums: List[int]) -> str:
        def quick_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        strs = [str(num) for num in nums]
        quick_sort(0, len(strs) - 1)
        return ''.join(strs)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(s.minNumber(nums))
