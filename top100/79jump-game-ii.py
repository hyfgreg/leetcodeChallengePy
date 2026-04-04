"""45. 跳跃游戏 II
中等
相关标签
premium lock icon
相关企业
给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。

每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：

0 <= j <= nums[i] 且
i + j < n
返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。



示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2


提示:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
题目保证可以到达 n - 1

面试中遇到过这道题?
1/5
是
否
通过次数
1,226,476/2.7M
通过率
45.7%
相关标签
贪心
数组
动态规划
"""

from typing import List


class Solution:
    def jumpDPslow(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n] * n
        dp[0] = 0
        for i in range(n):
            for j in range(nums[i]):
                if i + j + 1 < n:
                    dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)
                else:
                    break
        return dp[-1]

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_pos, end, step = 0, 0, 0
        for i in range(n - 1):
            if i <= max_pos:
                max_pos = max(max_pos, i + nums[i])
                # end是上一个起跳点所能到达的mas_pos, 那么就在[last_jump, max_pos]内，选一个跳的最远的，即新的max_pos，跳过去
                if end == i:
                    end = max_pos
                    step += 1
        return step


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    # nums = [2, 3, 0, 1, 4]
    solu = Solution()
    print(solu.jump(nums))
