"""
227. 基本计算器 II
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

整数除法仅保留整数部分。



示例 1：

输入：s = "3+2*2"
输出：7
示例 2：

输入：s = " 3/2 "
输出：1
示例 3：

输入：s = " 3+5 / 2 "
输出：5

输入：s = "3+2*2+2/4"
输入：s = "3+2+2+2/4"
输入：s = "3+2*2/3+2/4"

提示：

1 <= s.length <= 3 * 105
s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
s 表示一个 有效表达式
表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
题目数据保证答案是一个 32-bit 整数
通过次数83,369提交次数190,892

tag: 栈 数学 字符串
"""


class Solution:
    def calculate(self, s: str) -> int:
        # print(s)
        NUMBER = 'NUMBER'
        OPERATOR = 'OPERATOR'
        state = NUMBER
        ret = 0
        op_st = []
        num_st = []
        for i in s:
            if i == ' ':
                continue
            if i == '+':
                state = OPERATOR
                if not op_st:
                    op_st.append(i)
                else:
                    v1 = num_st.pop()
                    v2 = num_st.pop()
                    op = op_st.pop()
                    if op == '+':
                        num_st.append(v2 + v1)
                    # elif op == '-':
                    #     num_st.append(v2 - v1)
                    elif op == '*':
                        num_st.append(v2 * v1)
                    else:
                        if v2 < 0:
                            num_st.append(abs(v2) // v1 * (-1))
                        else:
                            num_st.append(v2 // v1)
                    op_st.append(i)
            elif i == '-':
                state = OPERATOR
                if not op_st:
                    op_st.append(i)
                else:
                    v1 = num_st.pop()
                    v2 = num_st.pop()
                    op = op_st.pop()
                    if op == '+':
                        num_st.append(v2 + v1)
                    # elif op == '-':
                    #     num_st.append(v2 - v1)
                    elif op == '*':
                        num_st.append(v2 * v1)
                    else:
                        if v2 < 0:
                            num_st.append(abs(v2) // v1 * (-1))
                        else:
                            num_st.append(v2 // v1)
                    op_st.append(i)
            elif i == '*':
                state = OPERATOR
                if not op_st:
                    op_st.append(i)
                else:
                    if op_st[-1] == '+' or op_st[-1] == '-':
                        op_st.append(i)
                    elif op_st[-1] == '*':
                        op_st.pop()
                        v1 = num_st.pop()
                        v2 = num_st.pop()
                        num_st.append(v2 * v1)
                        op_st.append(i)
                    else:
                        op_st.pop()
                        v1 = num_st.pop()
                        v2 = num_st.pop()
                        if v2 < 0:
                            num_st.append(abs(v2) // v1 * (-1))
                        else:
                            num_st.append(v2 // v1)
                        op_st.append(i)
            elif i == '/':
                state = OPERATOR
                if not op_st:
                    op_st.append(i)
                else:
                    if op_st[-1] == '+' or op_st[-1] == '-':
                        op_st.append(i)
                    elif op_st[-1] == '*':
                        op_st.pop()
                        v1 = num_st.pop()
                        v2 = num_st.pop()
                        num_st.append(v2 * v1)
                        op_st.append(i)
                    else:
                        op_st.pop()
                        v1 = num_st.pop()
                        v2 = num_st.pop()
                        if v2 < 0:
                            num_st.append(abs(v2) // v1 * (-1))
                        else:
                            num_st.append(v2 // v1)
                        op_st.append(i)
            else:
                i = int(i)
                if state == NUMBER:
                    if not num_st:
                        num_st.append(i)
                    else:
                        tmp = num_st.pop()
                        if tmp < 0:
                            num_st.append((abs(tmp) * 10 + i) * (-1))
                        else:
                            num_st.append(tmp * 10 + i)
                else:
                    state = NUMBER
                    num_st.append(i)
                if op_st and op_st[-1] == '-':
                    op_st.pop()
                    num_st[-1] = -1 * num_st[-1]
                    op_st.append('+')

        # print(num_st)
        # print(op_st)

        while op_st:
            v1 = num_st.pop()
            v2 = num_st.pop()
            op = op_st.pop()
            if op == "+":
                num_st.append(v2 + v1)
            # elif op == '-':
            #     num_st.append(v2 - v1)
            elif op == '*':
                num_st.append(v2 * v1)
            else:
                if v2 < 0:
                    num_st.append(abs(v2) // v1 * (-1))
                else:
                    num_st.append(v2 // v1)
        return num_st.pop()


class SolutionOfficial:
    # 背诵 主要是没怎么看，有点懒了当时
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                preSign = s[i]
                num = 0
        return sum(stack)


if __name__ == '__main__':
    s = Solution()
    # ch = "3+2*2+2/4"
    # print(s.calculate(ch))
    # ch = "3+2+2+2/4"
    # print(s.calculate(ch))
    # ch = "3+2*2/3+2/4"
    # print(s.calculate(ch))
    # ch = "3+3*2*2/3+2/4-2+1"
    # print(s.calculate(ch))
    # ch = "1*2-3/4+5*6-7*8+9/10"
    # print(s.calculate(ch))
    ch = "0-2147483647"
    print(s.calculate(ch))
