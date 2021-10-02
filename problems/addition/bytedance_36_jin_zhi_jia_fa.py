"""
题目描述
36进制由0-9，a-z，共36个字符表示。

要求按照加法规则计算出任意两个36进制正整数的和，如1b + 2x = 48  （解释：47+105=152）

要求：不允许使用先将36进制数字整体转为10进制，相加后再转回为36进制的做法
"""


class Solution:
    NUMBER = list('0123456789abcdefghijklmnopqrstuvwxyz')

    def add(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        ret = []
        while i >= 0 or j >= 0 or carry:
            a = self.get_num(num1, i)
            b = self.get_num(num2, j)
            # print(a, b)
            tmp = a + b + carry
            if tmp >= 36:
                carry = 1
                tmp -= 36
            else:
                carry = 0
            ret.append(self.NUMBER[tmp])
            i -= 1
            j -= 1
        return ''.join(ret)[::-1]

    def get_num(self, num: str, index: int) -> int:
        # print(num[index])
        if index < 0:
            return 0
        if num[index].isalpha():
            a = ord(num[index]) - ord('a') + 10
        else:
            a = int(num[index])
        return a


if __name__ == '__main__':
    s = Solution()
    num1 = '1b'
    num2 = '2x'
    print(s.add(num1, num2))
