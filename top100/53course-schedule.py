"""207. 课程表
中等
相关标签
premium lock icon
相关企业
提示
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。



示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。


提示：

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
prerequisites[i] 中的所有课程对 互不相同

面试中遇到过这道题?
1/5
是
否
通过次数
732,693/1.3M
通过率
56.9%
相关标签
深度优先搜索
广度优先搜索
图
拓扑排序
"""

from typing import Optional, List
from collections import deque


class Solution:
    def kahn(self, graph: dict) -> bool:
        print(graph)
        indegree = {node: 0 for node in graph}
        for u in graph:
            for v in graph[u]:
                indegree[v] = indegree.get(v, 0) + 1

        q = deque([node for node in indegree if indegree[node] == 0])
        visited_count = 0
        # print(indegree)
        while q:
            node = q.popleft()
            visited_count += 1
            # print("node", node)
            for neibours in graph.get(node, []):
                # print("nei", neibours)
                indegree[neibours] -= 1
                if indegree[neibours] == 0:
                    q.append(neibours)
        # print(visited_count)
        return visited_count == len(graph)

    def dfs(self, graph: dict) -> bool:
        state = {node: 0 for node in graph}
        #print(state)

        def _dfs(node):
            state[node] = 1
            for nei in graph.get(node, []):
                if state[nei] == 1:
                    return False
                if state[nei] == 0:
                    if not _dfs(nei):
                        return False
            state[node] = 2
            return True

        for node in graph:
            if state[node] == 0:
                if not _dfs(node):
                    return False
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = dict()
        for a, b in prerequisites:
            if a not in graph:
                graph[a] = []
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]
        if len(graph) > numCourses:
            return False
        #print(graph)
        return self.dfs(graph)


if __name__ == "__main__":
    solu = Solution()
    numCourses = 2
    prerequisites = [[0, 1]]
    print(solu.canFinish(numCourses, prerequisites))
