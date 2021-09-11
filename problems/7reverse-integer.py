"""
7. 整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。


示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0


提示：

-231 <= x <= 231 - 1
通过次数819,476提交次数2,318,598

tag: 数学
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        maximum = 2 ** 31 - 1
        negative = 1
        if x < 0:
            negative = -1
            x = abs(x)
        tmp = []
        while x > 0:
            value = x % 10
            x = x // 10
            if not tmp and value == 0:
                continue
            tmp.append(value)
        val = 0
        for i in tmp:
            tmp = val * 10 + i
            if tmp > maximum and not negative:
                return 0
            elif tmp > maximum + 1 and negative:
                return 0
            if tmp < val:
                return 0
            val = tmp
        return negative * val


if __name__ == '__main__':
    s = Solution()
    x = 123
    print(s.reverse(x))
    x = 1534236469
    print(s.reverse(x))
