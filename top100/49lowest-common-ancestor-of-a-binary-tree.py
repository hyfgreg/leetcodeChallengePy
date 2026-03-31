"""236. 二叉树的最近公共祖先
中等
相关标签
premium lock icon
相关企业
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”



示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1


提示：

树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。

面试中遇到过这道题?
1/5
是
否
通过次数
1,195,566/1.6M
通过率
74.9%
相关标签
树
深度优先搜索
二叉树
"""

from typing import Optional
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)

    @classmethod
    def build_bfs(cls, lists: list[int]) -> Optional["TreeNode"]:
        if not lists:
            return None
        root = cls(lists[0])
        q = Queue()
        q.put(root)
        depth = 1
        prev = None
        while True:
            start = depth * 2 - 1
            end = depth * 2
            for i, num in enumerate(lists[start : end + 1]):
                if i % 2 == 0:
                    prev = q.get_nowait()
                    if num is not None:
                        prev.left = TreeNode(num)
                        q.put(prev.left)
                elif num is not None:
                    prev.right = TreeNode(num)  # type: ignore
                    q.put(prev.right)
            if end >= len(lists):
                break
            depth += 1

        return root

    @classmethod
    def walk_bfs(cls, root):
        if not root:
            return []
        ret = []
        q = [root]
        while q:
            tmp = []
            for node in q:
                if node and (node.left or node.right):
                    tmp.append(node.left if node else None)
                    tmp.append(node.right if node else None)

                ret.append(node.val if node else None)
            q = tmp
        if ret[-1] is None:
            ret = ret[:-1]
        return ret


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        path_p = []
        path_q = []

        def dfs(node):
            if not node:
                return
            print(node)
            if path_p and path_p[-1] == p and path_q and path_q[-1] == q:
                return
            if not path_p or path_p[-1] != p:
                path_p.append(node)
            if not path_q or path_q[-1] != q:
                path_q.append(node)
            dfs(node.left)
            dfs(node.right)
            if path_p and path_p[-1] != p:
                print("pop p", path_p)
                path_p.pop()
            if path_q and path_q[-1] != q:
                print("pop q", path_q)
                path_q.pop()

     

        dfs(root)
        print([_.val for _ in path_p])
        print([_.val for _ in path_q])
        ret = root
        for i, j in zip(path_p, path_q):
            if i == j:
                ret = i
            if i == p or j == q:
                break
        return ret


if __name__ == "__main__":
    lists = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = TreeNode.build_bfs(lists)
    solu = Solution()
    print(solu.lowestCommonAncestor(root, root.left, root.left.right.right))
