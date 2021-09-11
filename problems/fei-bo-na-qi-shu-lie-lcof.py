"""
剑指 Offer 10- I. 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
f(2) = f(1) + f(0) = 1
f(3) = f(2) + f(1) = 2
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。



示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5


提示：

0 <= n <= 100
通过次数252,249提交次数701,688

tag: 记忆化搜索 数学 动态规划
"""
from functools import lru_cache


class Solution:

    @lru_cache
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        MOD = 10 ** 9 + 7
        p, q, r = 0, 0, 1
        for _ in range(2, n + 1):
            p = q
            q = r
            r = (p + q) % MOD
        return r


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        print(i, s.fib(i))
