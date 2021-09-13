"""
224. 基本计算器
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。



示例 1：

输入：s = "1 + 1"
输出：2
示例 2：

输入：s = " 2-1 + 2 "
输出：3
示例 3：

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23


提示：

1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式
通过次数69,448提交次数166,100

tag: 栈 递归 字符串 数学
背诵 没有理解官方的意思，自己用的递归还挺好理解的
"""


class Solution:

    def calculate(self, s: str) -> int:
        self.s = s
        self.index = 0
        return self._calculate_recursive()

    def _calculate_recursive(self) -> int:
        ret = 0
        negative = False
        while self.index < len(self.s):
            if self.s[self.index] == '(':
                self.index += 1
                value = self._calculate_recursive()
                if negative:
                    value = -1 * value
                ret += value
            elif self.s[self.index] == ')':
                self.index += 1
                break
            elif self.s[self.index] == '+':
                self.index += 1
                negative = False
                continue
            elif self.s[self.index] == '-':
                negative = True
                self.index += 1
            elif self.s[self.index].isdigit():
                value = self.get_digit()
                if negative:
                    value = -1 * value
                ret += value
            else:
                self.index += 1
        return ret

    def get_digit(self) -> int:
        ret = 0
        while self.index < len(self.s) and self.s[self.index].isdigit():
            ret = ret * 10 + int(self.s[self.index])
            self.index += 1
        return ret


if __name__ == '__main__':
    so = Solution()
    s = "1 + 1"
    print(so.calculate(s))
    s = " 2-1 + 2 "
    print(so.calculate(s))
    s = "(1+(4+5+2)-3)+(6+8)"
    print(so.calculate(s))
