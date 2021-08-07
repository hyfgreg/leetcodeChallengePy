"""
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。



示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
通过次数292,298提交次数532,782

tag: 深度优先搜索 广度优先搜索 并查集 数组 矩阵
"""
from typing import List


# todo 可以不用visited这个set，在访问过一个为"1"的点之后，可以直接把这个点修改为"0"避免再次访问

class Solution:
    N = 0
    visited = set()
    islands = []

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.N = 0
        self.visited = set()
        self.islands = [None] * m * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    self.N += 1
                    self.dfs(i, j, grid, m, n)
        return self.N

    def dfs(self, i, j, grid, rows, cols):
        if i >= rows or j >= cols or i < 0 or j < 0:
            return
        if grid[i][j] == "0":
            return
        if (i, j) in self.visited:
            return
        self.visited.add((i, j))
        self.dfs(i, j + 1, grid, rows, cols)
        self.dfs(i, j - 1, grid, rows, cols)
        self.dfs(i + 1, j, grid, rows, cols)
        self.dfs(i - 1, j, grid, rows, cols)


class SolutionBFS:
    N = 0
    visited = set()
    islands = []

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.N = 0
        self.visited = set()
        self.islands = [None] * m * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    self.bfs(i, j, grid, m, n)
        return self.N

    def bfs(self, i, j, grid, rows, cols):
        self.N += 1
        q = [(i, j)]
        q.append((i, j))
        while q:
            i, j = q.pop()
            self.visited.add((i, j))
            if i + 1 < rows and grid[i + 1][j] == "1" and (i + 1, j) not in self.visited:
                q.append((i + 1, j))
            if i > 0 and grid[i - 1][j] == "1" and (i - 1, j) not in self.visited:
                q.append((i - 1, j))
            if j + 1 < cols and grid[i][j + 1] == "1" and (i, j + 1) not in self.visited:
                q.append((i, j + 1))
            if j > 0 and grid[i][j - 1] == "1" and (i, j - 1) not in self.visited:
                q.append((i, j - 1))


class SolutionUnionFind:
    identity = []
    size = []
    count = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.initUF(grid)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for i, j in [(r, c - 1), (r - 1, c), (r, c + 1), (r + 1, c)]:
                        if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                            self.union(r * n + c, i * n + j)
        return self.count

    def initUF(self, grid):
        self.count = 0
        length = len(grid) * len(grid[0])
        self.identity = [i for i in range(length)]
        self.size = [1] * length
        for row in grid:
            for value in row:
                if value == "1":
                    self.count += 1
        print(self.count)

    def union(self, p, q):
        # print(f"union p {p}, q {q}")
        i = self.find(p)
        j = self.find(q)
        print(f"id[{p}]=={i}, id[{q}] == {j}")
        if i == j:
            print("union return")
            return
        print(f"size[{p}] == {self.size[p]}, size[{q}] == {self.size[q]}")
        if self.size[i] < self.size[j]:
            self.identity[i] = j
            self.size[j] += self.size[i]
            self.identity[p] = j
        else:
            self.identity[j] = i
            self.size[i] += self.size[j]
            self.identity[q] = i
        self.count -= 1

    def find(self, p):
        print(f"p {p}")
        while self.identity[p] != p:
            print(f"identity[{p}]=={self.identity[p]}, p {p}")
            p = self.identity[p]
        return p


if __name__ == '__main__':
    s = SolutionUnionFind()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    # grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]
    # grid = [["1", "1", "1"],
    #         ["0", "1", "0"],
    #         ["1", "1", "1"]]
    # grid = [["1"], ["1"]]
    # grid = [["1", "1", "1", "1", "1", "0", "1", "1", "1", "1"],
    #         ["1", "0", "1", "0", "1", "1", "1", "1", "1", "1"],
    #         ["0", "1", "1", "1", "0", "1", "1", "1", "1", "1"],
    #         ["1", "1", "0", "1", "1", "0", "0", "0", "0", "1"],
    #         ["1", "0", "1", "0", "1", "0", "0", "1", "0", "1"],
    #         ["1", "0", "0", "1", "1", "1", "0", "1", "0", "0"],
    #         ["0", "0", "1", "0", "0", "1", "1", "1", "1", "0"],
    #         ["1", "0", "1", "1", "1", "0", "0", "1", "1", "1"],
    #         ["1", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
    #         ["1", "0", "1", "1", "1", "1", "1", "1", "1", "0"]]
    print(s.numIslands(grid))
