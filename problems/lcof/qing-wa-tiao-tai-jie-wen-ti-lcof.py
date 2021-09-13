"""
剑指 Offer 10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100
注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/



通过次数187,235提交次数422,969

tag: 记忆化搜索 数学 动态规划
"""
from functools import lru_cache


class Solution:
    @lru_cache
    def numWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        n0 = 1
        n1 = 1
        for i in range(2, n + 1):
            tmp = n1
            n1 = n0 + n1
            n0 = tmp
        return n1 % MOD


if __name__ == '__main__':
    s = Solution()
    print(s.numWays(44))
