"""287. 寻找重复数
中等
相关标签
premium lock icon
相关企业
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。



示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3
示例 3 :

输入：nums = [3,3,3,3,3]
输出：3




提示：

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次


进阶：

如何证明 nums 中至少存在一个重复的数字?
你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？

面试中遇到过这道题?
1/5
是
否
通过次数
629,298/931.8K
通过率
67.5%
相关标签
位运算
数组
双指针
二分查找
"""

from typing import List

"""
解法一：快慢指针（弗洛伊德判圈法）

核心思想
将数组索引 0..n 看作节点，nums[i] 看作节点 i 指向的下一个节点（即 i -> nums[i]）。因为所有 nums[i] 都在 1..n 范围内，所以从 0 出发，沿着指针移动，一定不会越界。又因为存在重复数，意味着至少有两个不同的索引 i 和 j 满足 nums[i] == nums[j]，那么在链表中就会形成环，环的入口就是重复的那个数。

为什么环的入口就是重复数？

假设重复数为 target，那么至少有两个节点指向 target（因为 target 出现在至少两个位置）。而 target 本身也指向某个位置（因为 nums[target] 存在）。这样，从 0 出发走到 target 后，就会进入一个环，环的起点正是 target。

算法步骤
使用快慢指针 slow 和 fast，初始都指向 0。

移动指针：slow = nums[slow]（每次走一步），fast = nums[nums[fast]]（每次走两步）。

当 slow == fast 时，说明相遇，此时它们位于环中的某个位置。

将 slow 重置为 0，fast 保持在相遇点。然后两个指针每次各走一步，再次相遇的位置就是环的入口，即重复数。


解法二：二分查找（基于鸽笼原理）
核心思想
在区间 [1, n] 内二分查找，对于每个中间值 mid，统计数组中小于等于 mid 的元素个数 cnt。根据鸽笼原理，如果 cnt > mid，说明重复数在 [1, mid] 内；否则在 [mid+1, n] 内。

算法步骤
初始化 left = 1, right = n。

当 left < right 时：

mid = (left + right) // 2

统计 nums 中 <= mid 的元素个数 cnt

若 cnt > mid：right = mid

否则：left = mid + 1

返回 left（或 right）。

def findDuplicate(nums: List[int]) -> int:
    left, right = 1, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        cnt = sum(1 for x in nums if x <= mid)
        if cnt > mid:
            right = mid
        else:
            left = mid + 1
    return left
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        # 第一阶段：找到快慢指针相遇点
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # 第二阶段：找到环的入口
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
