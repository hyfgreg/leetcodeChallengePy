"""20. 有效的括号
简单
相关标签
premium lock icon
相关企业
提示
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。


示例 1：

输入：s = "()"

输出：true

示例 2：

输入：s = "()[]{}"

输出：true

示例 3：

输入：s = "(]"

输出：false

示例 4：

输入：s = "([])"

输出：true

示例 5：

输入：s = "([)]"

输出：false



提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

面试中遇到过这道题?
1/5
是
否
通过次数
2,514,954/5.5M
通过率
45.5%
相关标签
栈
字符串
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        h = {"(": ")", "[": "]", "{": "}"}
        for b in s:
            if not stk:
                stk.append(b)
            elif stk[-1] in h and h[stk[-1]] == b:
                stk.pop()
            elif stk[-1] in h and b not in h and h[stk[-1]] != b:
                return False
            else:
                stk.append(b)
        return not stk
