"""131. 分割回文串
中等
相关标签
premium lock icon
相关企业
给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。



示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]


提示：

1 <= s.length <= 16
s 仅由小写英文字母组成

面试中遇到过这道题?
1/5
是
否
通过次数
759,633/1M
通过率
75.1%
相关标签
字符串
动态规划
回溯
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and (f[i + 1][j - 1])
        ret = []
        tmp = []
        sub_tmp = []

        def dfs(depth):
            nonlocal ret, tmp, sub_tmp
            # print(depth, sub_tmp, tmp)
            if depth == len(s):
                if sub_tmp and sub_tmp == sub_tmp[::-1]:
                    tmp.append("".join(sub_tmp))
                    ret.append(tmp)
                elif not sub_tmp and tmp:
                    ret.append(tmp)
                return

            if not sub_tmp:
                sub_tmp.append(s[depth])
                dfs(depth + 1)
            elif f[depth - len(sub_tmp)][depth - 1]:
                tmp_size = len(tmp)
                sub_tmp_size = len(sub_tmp)
                tmp.append("".join(sub_tmp))
                sub_tmp = [s[depth]]
                dfs(depth + 1)
                tmp = tmp[:tmp_size]
                sub_tmp = list(s[depth - sub_tmp_size : depth])
                sub_tmp.append(s[depth])
                dfs(depth + 1)
            else:
                sub_tmp.append(s[depth])
                dfs(depth + 1)

        dfs(0)
        return ret

    def partition_dp(self, s):
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and (f[i + 1][j - 1])
        tmp = []
        ret = []

        def dfs(i):
            if i == n:
                ret.append(tmp[:])
                return
            for j in range(i, n):
                if f[i][j]:
                    tmp.append(s[i : j + 1])
                    dfs(j + 1)
                    tmp.pop()

        dfs(0)
        return ret


if __name__ == "__main__":
    s = "aab"
    solu = Solution()
    print(solu.partition_dp(s))
