"""51. N 皇后
困难
相关标签
premium lock icon
相关企业
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。



示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]


提示：

1 <= n <= 9

面试中遇到过这道题?
1/5
是
否
通过次数
667,412/885K
通过率
75.4%
相关标签
数组
回溯
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ret = []
        tmp = []
        cols = set()
        digs = set()
        udigs = set()

        def dfs(i):
            if i == n:
                ret.append(tmp[:])
                return
            for j in range(n):
                if j in cols:
                    continue
                if i - j in digs:
                    continue
                if i + j in udigs:
                    continue
                cols.add(j)
                digs.add(i - j)
                udigs.add(i + j)
                line = ["."] * n
                line[j] = "Q"
                tmp.append("".join(line))
                dfs(i + 1)
                tmp.pop()
                cols.remove(j)
                digs.remove(i - j)
                udigs.remove(i + j)

        dfs(0)

        return ret


if __name__ == "__main__":
    solu = Solution()
    print(solu.solveNQueens(4))
