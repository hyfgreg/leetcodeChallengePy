"""
69. x 的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
通过次数356,840提交次数907,915

tag: 数学 二分查找
"""


# 二分版本
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            multiply = mid * mid
            if multiply == x:
                return mid
            elif multiply < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


# 牛顿迭代版本
# todo 理解原理，记笔记，背诵
# todo 手画一下，然后写代码
class SolutionNewton:
    def mySqrt(self, x: int) -> int:
        # todo 实现
        pass


if __name__ == '__main__':
    x = 1
    s = Solution()
    print(s.mySqrt(x))
