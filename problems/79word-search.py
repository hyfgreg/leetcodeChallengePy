"""
79. 单词搜索
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



示例 1：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
示例 3：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false


提示：

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成

tag:
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_set = set(list(word))
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] not in word_set:
                    visited[i][j] = True
                    continue
                if board[i][j] != word[0]:
                    continue

                res = self.dfs(i, j, m, n, board, visited, word, word_set)
                if res:
                    return True
        return False

    def dfs(self, i, j, m, n, board, visited, word, word_set):
        # print(word)
        if visited[i][j]:
            return False
        if board[i][j] not in word_set:
            visited[i][j] = True
            return False
        if board[i][j] != word[0]:
            return False
        if len(word) == 1:
            return True
        visited[i][j] = True
        for [di, dj] in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < m and 0 <= new_j < n:
                res = self.dfs(new_i, new_j, m, n, board, visited, word[1:], word_set)
                if res:
                    return True
        visited[i][j] = False
        return False


if __name__ == '__main__':
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(s.exist(board, word))
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    print(s.exist(board, word))
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    print(s.exist(board, word))
