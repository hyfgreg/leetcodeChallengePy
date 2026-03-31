"""200. 岛屿数量
中等
相关标签
premium lock icon
相关企业
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。



示例 1：

输入：grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
输出：1
示例 2：

输入：grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
输出：3


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'

面试中遇到过这道题?
1/5
是
否
通过次数
1,338,854/2.1M
通过率
63.9%
相关标签
深度优先搜索
广度优先搜索
并查集
数组
矩阵
"""

from typing import List
from queue import Queue


class Solution:
    def dfs(self, grid: List[List[str]]) -> int:
        def _dfs(i, j):
            if i >= len(grid) or i < 0:
                return
            if j >= len(grid[i]) or j < 0:
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                _dfs(i + 1, j)
                _dfs(i - 1, j)
                _dfs(i, j + 1)
                _dfs(i, j - 1)

        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        if not cols:
            return 0
        count = 0
        print(grid)
        for i in range(rows):
            for j in range(cols):
                print(i, j, grid[i][j], grid)
                if grid[i][j] == "1":
                    _dfs(i, j)
                    count += 1
        return count

    def bfs(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        if not cols:
            return 0
        q = Queue()
        island = 0
        for i in range(rows):
            for j in range(cols):
                print(i, j, grid)
                if grid[i][j] == "1":
                    q.put((i, j))
                    island += 1
                    while q.qsize() > 0:
                        x, y = q.get()
                        print("get", x, y)
                        if x < 0 or x >= rows:
                            continue
                        if y < 0 or y >= cols:
                            continue
                        if grid[x][y] == "1":
                            grid[x][y] = "0"
                            print("set", x, y, 0)
                            q.put((x - 1, y))
                            q.put((x + 1, y))
                            q.put((x, y - 1))
                            q.put((x, y + 1))
                    print("after", grid)
                print("=====" * 10)
        return island

    def numIslands(self, grid: List[List[str]]) -> int:
        return self.bfs(grid)


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    grid = [["1", "0", "1", "1", "0", "1", "1"]]
    solu = Solution()
    print(solu.numIslands(grid))
