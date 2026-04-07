"""32. 最长有效括号
困难
相关标签
premium lock icon
相关企业
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。

左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。



示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0


提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'

面试中遇到过这道题?
1/5
是
否
通过次数
716,915/1.7M
通过率
41.8%
相关标签
栈
字符串
动态规划
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        max_len = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

    """
    dp[i], 考虑以s[i]为结尾的有效括号最大数量
    s[i]只能是")"
    状态转移方程:
    1. ..(), s[i-1] == "(", dp[i] = 2 + (dp[i-2] if i>= 2 else 0)
    2. ..)), s[i-1] == ")", 且s[i-dp[i-1]-1] == "(", 即更前面得有一个配套的"(", dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1]-2] if i>= dp[i-1]+2 else 0) 

    """

    def longestValidParenthesesDP(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        for i, ch in enumerate(s):
            if i >= 1 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = 2 + (dp[i - 2] if i >= 2 else 0)
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = (
                        dp[i - 1]
                        + 2
                        + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 else 0)
                    )
        # print(dp)
        return max(dp)

if __name__ == "__main__":
    s = ")()())"
    solu = Solution()
    print(solu.longestValidParenthesesDP(s))