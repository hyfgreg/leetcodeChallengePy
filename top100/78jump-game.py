"""55. 跳跃游戏
中等
相关标签
premium lock icon
相关企业
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。



示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。


提示：

1 <= nums.length <= 104
0 <= nums[i] <= 105

面试中遇到过这道题?
1/5
是
否
通过次数
1,520,838/3.4M
通过率
44.8%
相关标签
贪心
数组
动态规划
"""

from typing import List

"""

"""


class Solution:
    def canJumpMyself(self, nums: List[int]) -> bool:
        arrived = [False] * len(nums)
        arrived[0] = True
        for i, n in enumerate(nums):
            if not arrived[i]:
                return False
            for j in range(n):
                if i + j + 1 < len(nums):
                    arrived[i + j + 1] = arrived[i]
                    if arrived[-1]:
                        return True
        return arrived[-1]

    """
    用一个rightmost代替arrived，减少空间同时不用遍历就能知道i点能不能到达
    """

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        rightmost = 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
            else:
                return False
        return False

    def canJumpDP(self, nums: list[int]) -> bool:
        """
        dp[i]第截止第i点，所能到达的最远的位置，和上面的rightmost是一个意思
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] >= i:
                dp[i] = max(dp[i - 1], i + nums[i])
            if dp[i] >= n - 1:
                return True
        return dp[n - 1] >= n - 1


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    solu = Solution()
    print(solu.canJumpDP(nums))
