"""124. 二叉树中的最大路径和
困难
相关标签
premium lock icon
相关企业
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。



示例 1：


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


提示：

树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000

面试中遇到过这道题?
1/5
是
否
通过次数
707,411/1.5M
通过率
47.9%
相关标签
树
深度优先搜索
动态规划
二叉树
"""

from typing import Optional
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ret = float("-inf")

        def dfs(node):
            nonlocal ret
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            ret = max(
                ret,
                node.val,
                left_max + node.val,
                right_max + node.val,
                left_max + right_max + node.val,
            )
            return max(left_max + node.val, right_max + node.val, node.val)

        dfs(root)
        return ret


if __name__ == "__main__":
    lists = [-10, 9, 20, None, None, 15, 7]
    root = TreeNode.build_bfs(lists)
    solu = Solution()
    print(solu.maxPathSum(root))
