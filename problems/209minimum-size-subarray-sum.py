"""
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。



示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0


提示：

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105


进阶：

如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
通过次数185,382提交次数394,124

tag: 数组 二分查找 前缀和 滑动窗口 双指针
"""
import bisect
from typing import List


class Solution:
    MAX = float('inf')

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left, right = 0, 0
        tmp = 0
        res = self.MAX
        for right in range(len(nums)):
            # print(f"left {left} right {right}")
            if nums[right] >= target:
                return 1
            tmp += nums[right]
            # print("_sum", _sum)
            if tmp >= target:
                while tmp >= target:
                    res = min(res, right - left + 1)
                    tmp -= nums[left]
                    left += 1
                    # print("haha", _sum, left)
            # print("-----" * 10)
        if res == self.MAX:
            return 0
        return res


class SolutionOfficial:
    """
    背诵这个二分查找的逻辑，淦
    我们申请一个临时数组 sums，其中 sums[i] 表示的是原数组 nums 前 i 个元素的和，题中说了 “给定一个含有 n 个 正整数 的数组”，既然是正整数，
    那么相加的和会越来越大，也就是sums数组中的元素是递增的。我们只需要找到 sums[k]-sums[j]>=s，那么 k-j 就是满足的连续子数组，但不一定是最小的，
    所以我们要继续找，直到找到最小的为止。怎么找呢，我们可以使用两个 for 循环来枚举，但这又和第一种暴力求解一样了，所以我们可以换种思路，
    求 sums[k]-sums[j]>=s 我们可以求 sums[j]+s<=sums[k]，那这样就好办了，因为数组sums中的元素是递增的，也就是排序的，
    我们只需要求出 sum[j]+s 的值，然后使用二分法查找即可找到这个 k。
    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        print("nums", nums)
        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])
        print("sums", sums)

        for i in range(1, n + 1):
            print("i", i)
            target = s + sums[i - 1]
            print("target", target)
            bound = bisect.bisect_left(sums, target)
            print("bound", bound)
            if bound != len(sums):
                print("update ans")
                ans = min(ans, bound - (i - 1))
                print("ans", ans)
            print("=====" * 10)
        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    s = SolutionOfficial()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(s.minSubArrayLen(target, nums))
    target = 11
    nums = [1, 2, 3, 4, 5]
    print(s.minSubArrayLen(target, nums))
