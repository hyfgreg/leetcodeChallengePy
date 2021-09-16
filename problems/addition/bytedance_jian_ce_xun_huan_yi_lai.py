"""
循环依赖检测。如，[['A', 'B'], ['B', 'C'], ['C', 'D'], ['B', 'D']] => false，[['A', 'B'], ['B', 'C'], ['C', 'A']] => true（2021.4 字节跳动-幸福里-后端）[2]
手撕代码：小王写了一个makefile，其中有n个编译项编号为0~n-1，他们互相之间有依赖关系。请写一个程序解析依赖，给出一个可行的编译顺序。（2021.03 字节跳动-系统部-后端）[3]

tag: 深度优先搜索 广度优先搜索
背诵，环检测，以及拓扑排序
拓扑排序：
当且仅当一幅有向图是无环图时它才能进行拓扑排序
拓扑排序用的是DFS的逆后序，在递归调用之后将顶点压入栈
"""
from collections import deque
from typing import Tuple, List


class Solution:
    def haveCircularDependency(self, n: int, prerequisites: List[Tuple[int, int]]):
        g = [[] for _ in range(n)]
        indeg = [0 for _ in range(n)]
        res = []
        q = deque()

        for pre in prerequisites:
            v, w = pre[0], pre[1]
            g[v].append(w)
            indeg[w] += 1

        for i in range(n):
            if indeg[i] == 0:
                q.appendleft(i)

        while q:
            v = q.pop()
            res.append(v)
            for w in g[v]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    q.appendleft(w)

        if len(res) == n:
            return res
        else:
            return []

    def check_cycle(self, n, prerequisites):
        g = [[] for _ in range(n)]
        indeg = [0 for _ in range(n)]
        marked = [False for _ in range(n)]
        on_stack = [False for _ in range(n)]
        edge_to = [0 for _ in range(n)]
        res = []
        q = deque()
        cycle = []
        for pre in prerequisites:
            v, w = pre[0], pre[1]
            g[v].append(w)
            # indeg[w] += 1

        def dfs(v):
            nonlocal g, on_stack, marked, edge_to, cycle
            on_stack[v] = True
            marked[v] = True
            for w in g[v]:
                if cycle:
                    return
                if not marked[w]:
                    edge_to[w] = v
                    dfs(w)
                elif on_stack[w]:
                    x = v
                    while x != w:
                        cycle.append(x)
                        x = edge_to[x]
                    cycle.append(w)
                    cycle.append(v)
            on_stack[v] = False

        for v in range(n):
            dfs(v)

        return cycle


if __name__ == '__main__':
    s = Solution()
    n = 5
    prerequisites = [[0, 1], [1, 2], [2, 3], [2, 4]]
    print(s.haveCircularDependency(n, prerequisites))
    print(s.check_cycle(n,prerequisites))
    n = 3
    prerequisites = [[0, 1], [1, 2], [2, 1]]
    print(s.haveCircularDependency(n, prerequisites))
    print(s.check_cycle(n,prerequisites))
