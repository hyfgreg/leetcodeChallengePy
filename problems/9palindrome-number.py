"""
9. 回文数
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。



示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
示例 4：

输入：x = -101
输出：false


提示：

-231 <= x <= 231 - 1


进阶：你能不将整数转为字符串来解决这个问题吗？

tag: 数学
"""


class Solution:
    def isPalindromeMime(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        origin = x
        new_val = 0
        while x > 0:
            tmp = x % 10
            new_val = new_val * 10 + tmp
            x = x // 10
        return origin == new_val

    def isPalindrome(self, x: int) -> bool:
        # 其实只需要对比一半的数字就可以了，如果位数是偶数，则对比两个数是否相等，如果位数是奇数，那么大的数//10==小的数
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        new_val = 0
        while x > new_val:
            new_val = new_val * 10 + x % 10
            x = x // 10
        return x == new_val or x == new_val // 10


if __name__ == '__main__':
    s = Solution()
    x = 121
    print(s.isPalindrome(x))
