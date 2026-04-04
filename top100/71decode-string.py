"""394. 字符串解码
中等
相关标签
premium lock icon
相关企业
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

测试用例保证输出的长度不会超过 105。



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


提示：

1 <= s.length <= 30
s 由小写英文字母、数字和方括号 '[]' 组成
s 保证是一个 有效 的输入。
s 中所有整数的取值范围为 [1, 300]

面试中遇到过这道题?
1/5
是
否
通过次数
610,852/994.3K
通过率
61.4%
相关标签
栈
递归
字符串
"""


class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i: int) -> tuple[int, list[str]]:
            nonlocal s
            if i >= len(s):
                return i, []
            ret = []
            factor = None
            while i < len(s):
                if s[i].isdigit():
                    if factor is None:
                        factor = int(s[i])
                    else:
                        factor = factor * 10 + int(s[i])
                elif s[i] == "[":
                    i, tmp = decode(i + 1)
                    if factor is None:
                        factor = 1
                    ret.extend(factor * tmp)
                    factor = None
                elif s[i] == "]":
                    break
                else:
                    ret.append(s[i])
                i += 1
            return i, ret

        _, ret = decode(0)
        # print(ret)
        return "".join(ret)

    def decodeStringStack(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                # pop alpha
                curr = ""
                while stack and stack[-1] != "[":
                    curr = stack.pop() + curr
                stack.pop()  # pop [
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * curr)
            else:
                stack.append(c)
        return "".join(stack)


if __name__ == "__main__":
    s = "3[a]2[bc]"
    # s = "3[a2[c]]"
    s = "10[abc]3[cd]xyz"
    solu = Solution()
    print(solu.decodeStringStack(s))
