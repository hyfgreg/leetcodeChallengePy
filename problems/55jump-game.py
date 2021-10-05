"""
55. 跳跃游戏
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。



示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。


提示：

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105
通过次数328,262提交次数759,069

tag: 贪心 数组 动态规划
"""
from collections import deque
from typing import List


class Solution:
    def canJumpIdiot(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[0] = True
        q = deque()
        q.appendleft(0)
        while q:
            sz = len(q)
            for _ in range(sz):
                index = q.pop()
                step = nums[index]
                # print("index %s,step %s" % (index, step))
                for i in range(1, step + 1):
                    # print("index+i", index + i)
                    candidate = index + i
                    if candidate < len(nums) and not dp[candidate]:
                        dp[candidate] = True
                        q.appendleft(candidate)
                        if dp[-1]:
                            return True
                # print(dp)
        return dp[-1]

    def canJump(self, nums: List[int]) -> bool:
        """
        算法思路：从左往右遍历，不断扩充可跳范围，当可跳范围大于等于数组最大下标时，则返回true，否则，返回false
        """
        n, right = len(nums), 0
        for i in range(n):
            if i <= right:
                right = max(right, i + nums[i])
                if right >= n - 1:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    # nums = [2, 3, 1, 1, 4]
    # print(s.canJump(nums))
    # nums = [3, 2, 1, 0, 4]
    # print(s.canJump(nums))
    # nums = [2, 0, 0]
    # print(s.canJump(nums))
    nums = [3, 0, 8, 2, 0, 0, 1]
    print(s.canJump(nums))
