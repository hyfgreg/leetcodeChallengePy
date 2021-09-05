"""
179. 最大数
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。



示例 1：

输入：nums = [10,2]
输出："210"
示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"
示例 3：

输入：nums = [1]
输出："1"
示例 4：

输入：nums = [10]
输出："10"


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 109
通过次数117,276提交次数286,114

tag: 贪心 字符串 排序
"""
from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
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

        nums.sort(key=cmp_to_key(my_compare), reverse=True)
        # print(nums)
        index = 0
        while nums[index] == 0 and index < len(nums) - 1:
            index += 1
        return ''.join([str(i) for i in nums[index:]])


if __name__ == '__main__':
    s = Solution()
    # nums = [10, 2]
    # print(s.largestNumber(nums))
    # nums = [3, 30, 34, 5, 9]
    # print(s.largestNumber(nums))
    # nums = [34323, 3432]
    # print(s.largestNumber(nums))
    nums = [0]
    print(s.largestNumber(nums))
    nums = [0,0,0]
    print(s.largestNumber(nums))