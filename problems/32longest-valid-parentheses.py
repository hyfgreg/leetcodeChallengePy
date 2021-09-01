"""
32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。



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
通过次数182,179提交次数512,415

tag: 栈 字符串 动态规划
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        dp[i] 表示下标i字符结尾的最长有效括号长度, 如果s[i] == "(": dp[i] = 0
        有效的子串一定在")"处结尾
        :param s:
        :return:
        """
        if not s:
            return 0
        dp = [0] * len(s)
        i = 1
        max_len = 0
        while i < len(s):
            if s[i] == ")" and s[i - 1] == "(":
                # ......()
                # 上一个有效字串(如果存在)的长度再加上一个新括号的长度
                dp[i] = dp[i - 2] + 2 if i > 1 else 2
            elif s[i] == ")" and s[i - 1] == ")":
                # ......))
                # 如果s[i]是一个连续括号的结尾，那么s[i-1]一定是一个更短的连续字串的结尾, dp[i-1] > 0
                # 那么s[i-dp[i-1]-1]是上一个字串的再上一个字符，如果这个字符是(，那么与s[i]再加上中间的字串，构成一个新的字串
                # 这里注意， 如果dp[i - 1] == 0，那么s[i - dp[i - 1] -1] == s[i - 1] == ")"，以下的if是不生效的
                if i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    # 中间的字串长度+两边的括号的长度
                    dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2 if i - dp[i - 2] - 2 > 0 else dp[i - 1] + 2
            max_len = max(max_len, dp[i])
            i += 1
        return max_len


if __name__ == '__main__':
    so = Solution()
    s = ")()())"
    print(so.longestValidParentheses(s))
    s = "(()"
    print(so.longestValidParentheses(s))
    s = "()(()"
    print(so.longestValidParentheses(s))
