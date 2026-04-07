"""72. 编辑距离
中等
相关标签
premium lock icon
相关企业
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')


提示：

0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成

面试中遇到过这道题?
1/5
是
否
通过次数
849,066/1.3M
通过率
64.1%
相关标签
字符串
动态规划
"""

"""
我们定义 dp[i][j] 表示 word1 的前 i 个字符转换成 word2 的前 j 个字符所需的最少操作数。

动态规划解法
状态定义
1. i：word1 的前缀长度，取值范围 0..len1

2. j：word2 的前缀长度，取值范围 0..len2

2. dp[i][j]：最小编辑距离

边界条件
1. dp[0][j] = j：空字符串转换成 word2 的前 j 个字符，需要插入 j 次。

2. dp[i][0] = i：word1 的前 i 个字符转换成空字符串，需要删除 i 次。

转移fangcheng
1. word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
2. word1[i-1] != word2[j-1]: dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1] + 1)
    dp[i][j-1] + 1: word1[0:i]变换为word2[0: j-1]后，插入word2[j-1]
    dp[i-1][j] + 1: word1[0:i-1]变换为word2[0:j]后，删除word1[i-1]
    dp[i-1][j-1] + 1: word1[0:i-1]变换为word2[0:j-1]后，把word1[i-1]替换为word2[j-1]
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0] = list(range(n + 1))
        for i in range(1, m + 1):
            dp[i][0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1)
        return dp[-1][-1]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    solu = Solution()
    print(solu.minDistance(word1, word2))
