"""
剑指 Offer 62. 圆圈中最后剩下的数字
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
0 1 2 3 4
0 1 3 4
1 3 4
1 3
3


示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2


限制：

1 <= n <= 10^5
1 <= m <= 10^6
通过次数106,339提交次数162,287

tag: 递归 数学
背诵 约瑟夫环
f(n,m) = (f(n-1,m)+m)%n
困的要死
"""


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = list(range(n))
        start = 0
        while True:
            if len(nums) == 1:
                break
            pop_index = (m - 1 + start) % len(nums)
            nums.pop(pop_index)
            if pop_index == len(nums):
                start = 0
            else:
                start = pop_index

        return nums[0]

    def lastRemainingRecur(self, n: int, m: int) -> int:
        if n == 1:
            return 0
        return (self.lastRemainingRecur(n - 1, m) + m) % n

    def lastRemainingIter(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
            # print(x)
        return x


if __name__ == '__main__':
    s = Solution()
    print(s.lastRemainingIter(5, 3))
    print(s.lastRemainingIter(10, 17))
