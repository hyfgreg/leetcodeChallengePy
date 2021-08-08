"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成
通过次数670,464提交次数1,918,926

tag: 动态规划 字符串
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        begin = 0
        max_len = 1
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        for L in range(2, len(s) + 1):
            for i in range(len(s) - L + 1):
                # L = j-i+1 => j=L+i-1
                j = L + i - 1
                # i...j， i到j的字串，i > j时不合法，break
                if j < i:
                    break
                # 如果s[i:j+1]是回文字串，那么s[i] == s[j]
                # print(f"L {L} i {i}, j {j}")
                if s[i] == s[j]:
                    if L <= 3:
                        # 1<=L<=3时，必然是回文
                        dp[i][j] = True
                    else:
                        # L > 3时，取决于s[i+1:j]是不是回文
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and L > max_len:
                    begin = i
                    max_len = L
        return s[begin:begin + max_len]


class SolutionExpandAroundCenter:
    def longestPalindrome(self, s: str) -> str:
        """
        dp[i,j] 为真的场景
        1. i == j
        2. j = i+1，且s[i] == s[j]
        3. j > i+1, d[i+1,j-1]为真 且 s[i] == s[j]
        中心扩散法
        for i in [0, len(s)-1]:
            扩展L==1的子串
            扩展L==2的子串
            更新最大的字串
        ...
        :param s: 字符串
        :return:  最大回文子串
        """
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expand(s, i, i)
            left2, right2 = self.expand(s, i, i + 1)
            if right1 - left1 > end - start:
                start = left1
                end = right1
            if right2 - left2 > end - start:
                start = left2
                end = right2
        return s[start:end + 1]

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


if __name__ == '__main__':
    s = "babad"
    s = "cbbd"
    s = "a"
    s = "ac"
    so = SolutionExpandAroundCenter()
    print(so.longestPalindrome(s))
