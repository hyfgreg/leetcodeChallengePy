"""
695. 岛屿的最大面积
给定一个包含了一些 0 和 1 的非空二维数组 grid 。

一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)



示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。



注意: 给定的矩阵grid 的长度和宽度都不超过 50。

通过次数120,839提交次数182,224

tag: 深度优先搜索 广度优先搜索 并查集 数组 矩阵
"""
from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        visited = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(False)
            visited.append(tmp)

        def bfs(i, j, m, n, grid: List[List[int]]):
            nonlocal visited
            area = 0
            q = deque()
            q.appendleft((i, j))
            while q:
                sz = len(q)
                for i in range(sz):
                    i, j = q.pop()
                    if grid[i][j] == 1 and not visited[i][j]:
                        if i > 0:
                            q.appendleft((i - 1, j))
                        if j > 0:
                            q.appendleft((i, j - 1))
                        if i < m - 1:
                            q.appendleft((i + 1, j))
                        if j < n - 1:
                            q.appendleft((i, j + 1))
                        visited[i][j] = True
                        area += 1
            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(bfs(i, j, m, n, grid), max_area)
        return max_area

    def maxAreaOfIslandDFS(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        visited = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(False)
            visited.append(tmp)

        def dfs(i, j, m, n, grid: List[List[int]]) -> int:
            nonlocal visited
            if grid[i][j] == 0 or visited[i][j]:
                return 0
            area = 1
            visited[i][j] = True
            if i > 0:
                area += dfs(i - 1, j, m, n, grid)
            if j > 0:
                area += dfs(i, j - 1, m, n, grid)
            if i < m - 1:
                area += dfs(i + 1, j, m, n, grid)
            if j < n - 1:
                area += dfs(i, j + 1, m, n, grid)
            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs(i, j, m, n, grid))
        return max_area


if __name__ == '__main__':
    s = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(s.maxAreaOfIslandDFS(grid))
