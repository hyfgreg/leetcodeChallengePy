"""
代码
测试用例
测试用例
测试结果
5. 最长回文子串
中等
相关标签
premium lock icon
相关企业
提示
给你一个字符串 s，找到 s 中最长的 回文 子串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成

面试中遇到过这道题?
1/5
是
否
通过次数
2,329,224/5.7M
通过率
40.7%
相关标签
双指针
字符串
动态规划
"""

"""
dp[i][j]是回文子串
    dp[i+1][j-1]是回文子串 and s[i] == s[j]
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = s[0]
        for i in range(n):
            dp[i][i] = True
        # print(dp)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                print(i, j, s[i], s[j], f"dp[{i+1}][{j-1}]", dp[i + 1][j - 1])
                if s[i] == s[j] and (j == i + 1 or j == i + 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > len(ans):
                        ans = s[i : j + 1]
                # print(i, j, dp)
        return ans


if __name__ == "__main__":
    solu = Solution()
    s = "babad"
    # s = "cbbd"
    print(solu.longestPalindrome(s))
