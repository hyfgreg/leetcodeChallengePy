"""437. 路径总和 III
中等
相关标签
premium lock icon
相关企业
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。



示例 1：



输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
示例 2：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3


提示:

二叉树的节点个数的范围是 [0,1000]
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000

面试中遇到过这道题?
1/5
是
否
通过次数
603,378/1.2M
通过率
48.8%
相关标签
树
深度优先搜索
二叉树
"""

import collections
from queue import Queue
from typing import Optional


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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ret = 0

        def dfs(root):
            nonlocal ret, targetSum
            if not root:
                return []
            left_path = dfs(root.left)
            right_path = dfs(root.right)
            for left in left_path:
                if sum(left) + root.val == targetSum:
                    # print(root.val, left)
                    ret += 1
                left.append(root.val)
            for right in right_path:
                if sum(right) + root.val == targetSum:
                    # print(root.val, right)
                    ret += 1
                right.append(root.val)
            if root.val == targetSum:
                ret += 1
            return [[root.val]] + left_path + right_path

        dfs(root)
        return ret

    def pathSumPrefix(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1  # 用于节点的值==targetSum

        def dfs(node, curr):
            """
            curr: 从root到当前node之前的前缀和
            """
            if not node:
                return 0
            # print("node", node.val, "curr", curr, "new_curr", curr + node.val, prefix)
            ret = 0
            curr += node.val  # 计算新的前缀和
            ret += prefix[
                curr - targetSum
            ]  # 前缀和-targetSum 的和是否存在，存在说明存在这样的路径
            prefix[curr] += 1  # 把当前节点的前缀和放入hash
            ret += dfs(node.left, curr)
            ret += dfs(node.right, curr)
            prefix[curr] -= 1  # 当前节点已经遍历完毕，退出当前前缀和
            return ret

        return dfs(root, 0)


if __name__ == "__main__":
    lists = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    root = TreeNode.build_bfs(lists)
    print(TreeNode.walk_bfs(root))

    solu = Solution()
    ret = solu.pathSumPrefix(root, 8)
    print(ret)
