"""
有向图，用的是邻接表的表达方式
"""
from typing import List
from collections import deque


# 有向图的表达
class Diagragh:
    def __init__(self, V: int):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]

    def add_edge(self, v: int, w: int):
        self.adj[v].append(w)
        self.E += 1

    def adj_of_vertices(self, v: int) -> List[int]:
        return self.adj[v]

    def reverse(self) -> 'Diagragh':
        R = Diagragh(self.V)
        for v in range(self.V):
            for w in self.adj[v]:
                R.add_edge(w, v)
        return R


# 有向图的DFS，有向图的可达性
# 实际用途可以是垃圾回收
class DirectedDFS:
    def __init__(self, G: 'Diagragh', s: int):
        self.marked = [False for _ in range(G.V)]
        self.dfs(G, s)

    def dfs(self, G: 'Diagragh', v: int):
        self.marked[v] = True
        for w in G.adj_of_vertices(v):
            if not self.marked[w]:
                self.dfs(G, w)

    def is_marked(self, v: int):
        return self.marked[v]


# 检查有向图里面是不是有环
class DirectedCycle:
    def __init__(self, G: 'Diagragh'):
        self.on_stack = [False for _ in range(G.V)]
        self.edge_to = [0 for _ in range(G.V)]
        self.marked = [False for _ in range(G.V)]
        self.cycle = []
        for v in range(G.V):
            self.dfs(G, v)

    def dfs(self, G: 'Diagragh', v: int):
        self.on_stack[v] = True
        self.marked[v] = True
        for w in G.adj_of_vertices(v):
            if self.cycle:
                return
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w)
            elif self.on_stack[w]:
                # 兜兜转转又回来了！
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edge_to[x]
                self.cycle.append(w)
                self.cycle.append(v)
        self.on_stack[v] = False

    def has_cycle(self) -> bool:
        return len(self.cycle) > 0

    def get_cycle(self) -> List[int]:
        return self.cycle


# 基于DFS的顶点排序
# 前序: 在递归调用之前将顶点加入队列queue
# 后序: 在递归调用之后将顶点加入队列queue
# 逆后序: 在递归调用之后将顶点加入栈stack
class DepthFirstOrder:
    def __init__(self, G: 'Diagragh'):
        self.pre = deque()
        self.post = deque()
        self.reversePost = deque()
        self.marked = [False for _ in range(G.V)]
        for v in range(G.V):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G: 'Diagragh', v: int):
        self.marked[v] = True
        self.pre.appendleft(v)
        for w in G.adj_of_vertices(v):
            if not self.marked[w]:
                self.dfs(G, w)
        self.post.appendleft(v)
        self.reversePost.append(v)

    def pre_order(self):
        return self.pre

    def post_order(self):
        return self.post

    def reverse_post_order(self):
        return self.reversePost


class Topological:
    def __init__(self, G: 'Diagragh'):
        cycle_finder = DirectedCycle(G)
        if not cycle_finder.has_cycle():
            dfs = DepthFirstOrder(G)
            self.order = dfs.reverse_post_order()
        else:
            self.order = []

    def get_order(self):
        while self.order:
            yield self.order.pop()


if __name__ == '__main__':
    jobs = """
    Algorithms/Theoretical CS/Databases/Scientific Computing 
    Introduction to CS/Advanced Programming/Algorithms 
    Advanced Programming/Scientific Computing 
    Scientific Computing/Computational Biology 
    Theoretical CS/Computational Biology/Artificial Intelligence 
    Linear Algebra/Theoretical CS 
    Calculus/Linear Algebra
    Artificial Intelligence/Neural Networks/Robotics/Machine Learning 
    Machine Learning/Neural Networks
    """
