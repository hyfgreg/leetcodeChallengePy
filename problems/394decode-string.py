"""
394. 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。



示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
通过次数117,614提交次数213,199

tag: 栈 递归 字符串
"""


class StringInfo:
    def __init__(self, count):
        self.count = count
        self.alpha_list = []

    def add_alpha(self, alpha):
        self.alpha_list.append(alpha)

    def to_string(self):
        return ''.join(self.alpha_list) * self.count

    def __repr__(self):
        return f"{self.count}__{''.join(self.alpha_list)}"


class Solution:
    def decodeString(self, s: str) -> str:
        # if len(s) <= 4:
        #     return s
        ret = []
        stack = []
        i = 0
        si = None
        digit_tmp = []
        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                if si:
                    stack.append(si)
                    si = None
                digit_tmp.append(ch)
            elif ch.isalpha():
                if not si:
                    ret.append(ch)
                else:
                    si.add_alpha(ch)
            elif ch == '[':
                # print(digit_tmp)
                si = StringInfo(int(''.join(digit_tmp)))
                digit_tmp.clear()
            elif ch == ']':
                if si:
                    stack.append(si)
                si = stack.pop()
                if not stack:
                    ret.append(si.to_string())
                    si = None
                else:
                    stack[-1].add_alpha(si.to_string())
                    si = stack.pop()
                # print("stack", stack)
                # print("ret", ret)
            i += 1
            # print(ch)
            # print("si", si)
            # print("stack", stack)
            # print("ret", ret)

        return ''.join(ret)

class SolutionMy:
    # 背诵这个方法，递归练习？
    DIGIT = {'1', '2', '3', '4', '5', '6', '7', '8', '9','0'}

    def __init__(self):
        self.s = None
        self.index = 0

    def decodeString(self, s: str) -> str:
        self.s = s
        self.index = 0
        return self.helper()

    def helper(self) -> str:
        if (self.index == len(self.s) or self.s[self.index] == ']'):
            return ''
        ret = ''
        if self.s[self.index] in self.DIGIT:
            count = self.get_digit()
            self.index += 1 # 跳过[
            string = self.helper()
            ret += count * string
            self.index += 1 # 跳过]
        else:
            ret = self.s[self.index]
            self.index += 1
            ret += self.helper()
        return ret + self.helper()

    def get_digit(self):
        ret = 0
        while self.s[self.index] != '[':
            ret = ret * 10 + int(self.s[self.index])
            self.index += 1
        return ret


if __name__ == '__main__':
    so = Solution()
    # s = "3[a]2[bc]"
    # print(so.decodeString(s))
    # s = "3[a2[c]]"
    # print(so.decodeString(s))
    # s = "2[abc]3[cd]ef"
    # print(so.decodeString(s))
    # s = "abc3[cd]xyz"
    # print(so.decodeString(s))
    # s = "100[leetcode]"
    # print(so.decodeString(s))
    # s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    # print(so.decodeString(s))
    # print("zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")
    # s = "2[a]"
    # print(so.decodeString(s))
    s = "3[a10[bc]]"
    print(so.decodeString(s))
