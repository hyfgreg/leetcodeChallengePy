"""
72. 编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

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
通过次数160,215提交次数261,893

tag: 字符串 动态规划
背诵
"""


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         n = len(word1)
#         m = len(word2)
#
#         # 有一个字符串为空串
#         if n * m == 0:
#             return n + m
#
#         # DP 数组
#         D = [[0] * (m + 1) for _ in range(n + 1)]
#
#         # 边界状态初始化
#         for i in range(n + 1):
#             D[i][0] = i
#         for j in range(m + 1):
#             D[0][j] = j
#
#         # 计算所有 DP 值
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 left = D[i - 1][j] + 1
#                 down = D[i][j - 1] + 1
#                 left_down = D[i - 1][j - 1]
#                 if word1[i - 1] != word2[j - 1]:
#                     left_down += 1
#                 D[i][j] = min(left, down, left_down)
#
#         return D[n][m]

# dp[i][j] word1前i个字符到word2前j个字符的距离
# dp[i][j-1] -> dp[i][j], 知道了i -> j-1的距离A，那么i->j的距离为A+1
# dp[i-1][j] -> dp[i][j], 知道了i-1 -> j的距离B，那么i->j的距离为B+1
# dp[i-1][j] -> dp[i][j], 知道了i-1 -> j-1的距离C
#   如果word1第i个字符==word2的第j个字符(word1[i] == word2[j]), 那么dp[i][j] = dp[i-1][j-1]
#   如果word1第i个字符!=word2的第j个字符(word1[i] != word2[j]), 那么dp[i][j] = dp[i-1][j-1] + 1

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m * n == 0:
            return m + n

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # print(f"(i, j) == ({i}, {j})")
                # print(f"dp[{i - 1}][{j}]=={dp[i - 1][j]}")
                # print(f"dp[{i}][{j - 1}]=={dp[i][j - 1]}")
                # print(f"dp[{i - 1}][{j - 1}]=={dp[i - 1][j - 1]}")
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
                # print(f"dp[{i}][{j}]=={dp[i][j]}")
                # print("=====" * 10)
        return dp[m][n]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    s = Solution()
    print(s.minDistance(word1, word2))
