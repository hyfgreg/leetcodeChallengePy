"""
128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9


提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
通过次数161,083提交次数296,506

tag: 并查集 数组 哈希表

背诵官方的思路
只有n-1不在set中时，这个n就是一个连续数字的起始，然后不断查找n+1是否在num_set中，直到找完这个连续数字, 之后这个连续数字的其他数字出现时，因为它不是起始位置，忽略之
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        {0:{count: 2, last: 0}, 3:2, 7:6, 2:[1, 1], 5:4, 8:8, 4:3, 6:5, 1: 0}
        """
        if not nums:
            return 0
        num_set = set(nums)
        uf = {}
        for n in num_set:
            if n in uf:
                continue
            else:
                tmp = {"count": 1, "last": None, "next": None, "gone": False}
                if n - 1 in uf:
                    tmp["last"] = n - 1
                    uf[n - 1]["next"] = n
                if n + 1 in uf:
                    uf[n + 1]["last"] = n
                    tmp["next"] = n + 1
                uf[n] = tmp
        length = 0
        for n in num_set:
            data = uf[n]
            if data["gone"]:
                continue
            count = data["count"]
            next = data["next"]
            data["gone"] = True
            while next is not None:
                next_data = uf[next]
                next_data["gone"] = True
                count += next_data["count"]
                next = next_data["next"]
            last = data["last"]
            while last is not None:
                last_data = uf[last]
                last_data["gone"] = True
                count += last_data["count"]
                last = last_data["last"]
            length = max(length, count)
        return length


class SolutionOfficial:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length = 0
        for n in num_set:
            if n - 1 not in num_set:
                current = n
                sub_length = 1
                while current + 1 in num_set:
                    current += 1
                    sub_length += 1
                length = max(length, sub_length)
        return length


if __name__ == '__main__':
    s = Solution()
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(s.longestConsecutive(nums))
    nums = [100, 4, 200, 1, 3, 2]
    print(s.longestConsecutive(nums))
