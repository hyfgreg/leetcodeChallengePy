"""
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。



示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25


提示：

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
通过次数214,597提交次数569,791

tag: 递归 数学
背诵，快速幂
在二进制数为1的位做贡献!
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == 1:
            # print("return")
            return x
        negative = n < 0
        n = abs(n)
        ret = 1.0
        while n > 0:
            if n & 1 == 1:
                ret *= x
            x *= x
            n = n >> 1
        return ret if not negative else 1 / ret


if __name__ == '__main__':
    s = Solution()
    x = 2
    n = 9
    print(s.myPow(x, n))
