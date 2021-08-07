"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。


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

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true


提示：

1 <= s.length <= 104

tag: 栈 字符串
"""
parentheses = {
    "{": "}",
    "[": "]",
    "(": ")"
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c in {"}", "]", ")"}:
                if not stack:
                    return False
                left = stack.pop()
                if parentheses[left] == c:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True