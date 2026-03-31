"""994. 腐烂的橘子
中等
相关标签
premium lock icon
相关企业
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。



示例 1：



输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
示例 3：

输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] 仅为 0、1 或 2

面试中遇到过这道题?
1/5
是
否
通过次数
436,455/786.7K
通过率
55.5%
相关标签
资深工程师
广度优先搜索
数组
矩阵
第 124 场周赛
"""

from queue import Queue
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        if not cols:
            return 0
        q = Queue()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.put((i, j, 0))
                    while not q.empty():
                        x, y, t = q.get()
                        for a, b in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                            if 0 <= a < rows and 0 <= b < cols:
                                if grid[a][b] == 1 or (
                                    grid[a][b] < 0 and -grid[a][b] > t + 1
                                ):
                                    grid[a][b] = -(t + 1)  # 记录腐烂时间，加一个负号
                                    q.put((a, b, t + 1))
        t = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
                elif grid[i][j] < 0:
                    t = max(-grid[i][j], t)
        return t


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    # grid = [[0, 2]]
    solu = Solution()
    print(solu.orangesRotting(grid))
