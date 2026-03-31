"""79. 单词搜索
中等
相关标签
premium lock icon
相关企业
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



示例 1：


输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCCED"
输出：true
示例 2：


输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE"
输出：true
示例 3：


输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB"
输出：false


提示：

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成


进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？


面试中遇到过这道题?
1/5
是
否
通过次数
871,505/1.7M
通过率
50.8%
相关标签
深度优先搜索
数组
字符串
回溯
矩阵
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        rows = len(board)
        if not rows:
            return False
        cols = len(board[0])
        if not cols:
            return False

        def dfs(i, j, index):
            # print(i, j, board[i][j], word[index], index)
            if board[i][j] != word[index]:
                return False
            if board[i][j] == word[index] and index == len(word) - 1:
                return True
            board[i][j] = ""
            for x, y in [[i + 1, j], [i, j - 1], [i - 1, j], [i, j + 1]]:
                if 0 <= x < rows and 0 <= y < cols and board[x][y] == word[index + 1]:
                    if dfs(x, y, index + 1):
                        return True
            board[i][j] = word[index]
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    res = dfs(i, j, 0)
                    if res:
                        return True

        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    word = "SEE"
    word = "ABCB"
    solu = Solution()
    print(solu.exist(board, word))
