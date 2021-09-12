"""
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。



示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
通过次数178,511提交次数424,264

tag: 数组 动态规划
背诵
因为有负负得正的情况，所以要考虑当前的最大值和最小值

因为这里的定义并不满足「最优子结构」。具体地讲，如果 a={5,6,−3,4,−3}，那么此时 fmax
对应的序列是{5,30,−3,4,−3}，按照前面的算法我们可以得到答案为 3030，即前两个数的乘积，而实际上答案应该是全体数字的乘积。我们来想一想问题出在哪里呢？问题出在最后一个 -3−3 所对应的fmax
的值既不是 -3−3，也不是 4×−3，而是5×30×(−3)×4×(−3)。所以我们得到了一个结论：当前位置的最优解未必是由前一个位置的最优解转移得到的。
我们可以根据正负性进行分类讨论。
考虑当前位置如果是一个负数的话，那么我们希望以它前一个位置结尾的某个段的积也是个负数，这样就可以负负得正，并且我们希望这个积尽可能「负得更多」，即尽可能小。如果当前位置是一个正数的话，我们更希望以它前一个位置结尾的某个段的积也是个正数，并且希望它尽可能地大。于是这里我们可以再维护一个 f_{\min}(i)f 
min
 (i)，它表示以第 ii 个元素结尾的乘积最小子数组的乘积，那么我们可以得到这样的动态规划转移方程：
fmax(i) = max(fmax(i-1)*ai, fmin(i-1)*ai, ai)
fmin(i) = min(fmax(i-1)*ai, fmin(i-1)*ai, ai)
它代表第 i 个元素结尾的乘积最大子数组的乘积 fmax(i)，可以考虑把 ai加入第i−1 个元素结尾的乘积最大或最小的子数组的乘积中，二者加上 ai ，三者取大，就是第 i 个元素结尾的乘积最大子数组的乘积。
第 i 个元素结尾的乘积最小子数组的乘积 fmin(i)同理。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/maximum-product-subarray/solution/cheng-ji-zui-da-zi-shu-zu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxProductOld(self, nums: List[int]) -> int:
        MAX = 0
        MIN = 1
        dp = []
        for i in range(len(nums)):
            tmp = [0, 0]
            dp.append(tmp)
        dp[0][MAX] = nums[0]
        dp[0][MIN] = nums[0]
        res = dp[0][MAX]
        # print(0, nums[0], dp[0])
        for i in range(1, len(nums)):
            dp[i][MAX] = max(dp[i - 1][MAX] * nums[i], dp[i - 1][MIN] * nums[i], nums[i])
            dp[i][MIN] = min(dp[i - 1][MAX] * nums[i], dp[i - 1][MIN] * nums[i], nums[i])
            # print(i, nums[i], dp[i])
            # print(dp)
            res = max(*dp[i], res)
        return res

    def maxProduct(self, nums: List[int]) -> int:
        max_val = nums[0]
        min_val = nums[0]
        res = max_val
        for i in range(1, len(nums)):
            tmp_max = max_val
            max_val = max(tmp_max * nums[i], min_val * nums[i], nums[i])
            min_val = min(tmp_max * nums[i], min_val * nums[i], nums[i])
            # print(i, nums[i], dp[i])
            # print(dp)
            res = max(max_val, min_val, res)
        return res


if __name__ == '__main__':
    s = Solution()
    # nums = [2, 3, -2, 4]
    # print(s.maxProduct(nums))
    # nums = [-2, 0, -1]
    # print(s.maxProduct(nums))
    # nums = [-2,3,-4]
    # print(s.maxProduct(nums))
    nums = [2, -5, -2, -4, 3]
    print(s.maxProduct(nums))
