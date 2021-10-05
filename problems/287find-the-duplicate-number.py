"""
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。



示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3
示例 3：

输入：nums = [1,1]
输出：1
示例 4：

输入：nums = [1,1,2]
输出：1


提示：

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次


进阶：

如何证明 nums 中至少存在一个重复的数字?
你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
通过次数178,994提交次数271,235

背诵， 知识点包括，二分查找，循环链表查找入口
tag: 位运算 数组 双指针 二分查找
"""
from typing import List


class Solution:
    def findDuplicateBisect(self, nums: List[int]) -> int:
        # 二分查找
        # 性质，假设target是重复的数字，定义cnt[i]是小于等于i的数字的个数，对于[1,target-1], cnt[i] <= i, 对于[target, n]
        # cnt[i] > i
        n = len(nums)
        left = 1
        right = n - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            # print("left %d, right, %d, mid %d, cnt %d" % (left, right, mid, cnt))
            if cnt <= mid:
                # ans = mid
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans

    def findDuplicate(self, nums: List[int]) -> int:
        """
        循环链表，floyd方法
                 __
        -------/    \
               \ __ /
        假设，环外长度为a，第一次相遇时，slow指针在环内的行走距离为b，环的另一部分的长度为c
        fast指针的行走距离
        a + n(b+c) + b
        slow指针的行走距离
        a+b
        => a + n(b+c) +b = 2(a+b)
        => a = c + (n-1)(b+c)
        将快指针重新指向起点，然后和slow指针一起每次走一个，相遇点就是入环点
        """
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # print(f"slow {slow}, fast {fast}")
            if slow == fast:
                ptr = 0
                while True:
                    ptr = nums[ptr]
                    slow = nums[slow]
                    if ptr == slow:
                        return ptr


if __name__ == '__main__':
    s = Solution()
    nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    print(s.findDuplicate(nums))
