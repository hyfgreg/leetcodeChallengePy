"""
给定两个字符串形式的非负整数num1 和num2，计算它们的和。



提示：

num1 和num2的长度都小于 5100
num1 和num2 都只包含数字0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库，也不能直接将输入的字符串转换为整数形式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_length = len(num1)
        num2_length = len(num2)
        length = max(num1_length, num2_length)
        # print(length)
        num1 = num1[::-1]
        num2 = num2[::-1]
        ret = ['0'] * (length + 1)
        i = 0
        flag = 0
        zero = ord('0')
        while i < length:
            # print('i', i)
            first = ord(num1[i]) - zero if i < num1_length else 0
            second = ord(num2[i]) - zero if i < num2_length else 0
            _sum = first + second + flag
            # print('sum', _sum)
            ans = chr(_sum % 10 + zero) if _sum >= 10 else chr(_sum + zero)
            # print('ans', ans)
            ret[i] = ans
            flag = _sum // 10
            # print('flag', flag)
            i += 1
        if flag:
            ret[i] = '1'
        ret = ret[::-1]
        if ret[0] == '0':
            ret = ret[1:]
        return ''.join(ret)


if __name__ == '__main__':
    a = '123'
    b = '123'
    s = Solution()
    print(s.addStrings(a, b))
