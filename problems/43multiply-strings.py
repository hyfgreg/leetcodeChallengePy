"""
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
通过次数164,858提交次数367,239

tag: 数学 字符串 模拟
"""
from itertools import zip_longest


class Solution:
    i2s = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    s2i = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        ret = '0'
        for i, n in enumerate(num1[::-1]):
            tmp = self.numbers_time_number(num2, n)
            tmp += '0' * i
            ret = self.numbers_add_numbers(tmp, ret)
        return ret

    def numbers_time_number(self, numbers: str, number: str) -> str:
        if number == '0':
            return '0'
        ret = ['0'] * (len(numbers) + 1)
        length = len(ret)
        carry = '0'
        for i, n in enumerate(numbers[::-1]):
            ret[length - i - 1], new_carry = self.number_times_number(n, number)
            ret[length - i - 1], tmp_new_carry = self.number_add_number(ret[length - i - 1], carry)
            carry = self.number_add_number(new_carry, tmp_new_carry)[0]
        ret[0] = carry
        if ret[0] == '0':
            return ''.join(ret[1:])
        return ''.join(ret)

    def number_times_number(self, num1: str, num2: str) -> (str, str):
        nums1, nums2 = self.s2i[num1], self.s2i[num2]
        ret = nums1 * nums2
        if ret < 10:
            return self.i2s[ret], '0'
        return self.i2s[ret % 10], self.i2s[ret // 10]

    def numbers_add_numbers(self, num1: str, num2: str) -> str:
        ret = ['0'] * (max(len(num1), len(num2)) + 1)
        length = len(ret)
        carry = '0'
        for i, (n1, n2) in enumerate(zip_longest(num1[::-1], num2[::-1])):
            if n1 and n2:
                ret[length - i - 1], new_carry = self.number_add_number(n1, n2)
                ret[length - i - 1], tmp_new_carry = self.number_add_number(ret[length - i - 1], carry)
                if tmp_new_carry != '0':
                    new_carry = tmp_new_carry
                carry = new_carry
            elif n1:
                ret[length - i - 1], new_carry = self.number_add_number(carry, n1)
                carry = new_carry
            elif n2:
                ret[length - i - 1], new_carry = self.number_add_number(n2, carry)
                carry = new_carry
        ret[0] = carry
        if ret[0] == '0':
            return ''.join(ret[1:])
        return ''.join(ret)

    def number_add_number(self, num1: str, num2: str) -> (str, str):
        nums1, nums2 = self.s2i[num1], self.s2i[num2]
        ret = nums1 + nums2
        if ret < 10:
            return self.i2s[ret], '0'
        return self.i2s[ret - 10], '1'


class SolutionOfficial:
    # 背诵
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        ansArr = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                ansArr[i + j + 1] += x * int(num2[j])

        for i in range(m + n - 1, 0, -1):
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] %= 10

        index = 1 if ansArr[0] == 0 else 0
        ans = "".join(str(x) for x in ansArr[index:])
        return ans


if __name__ == '__main__':
    s = Solution()
    nums1 = "123"
    nums2 = "456"
    print(s.multiply(nums1, nums2))
