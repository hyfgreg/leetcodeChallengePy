"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

通过次数476,993提交次数623,455

tag: 树 深度优先搜索 广度优先搜索 二叉树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        height = 0

        def dfs(root, depth):
            nonlocal height
            if not root:
                return
            depth += 1
            if root.left is None and root.right is None:
                if depth > height:
                    height = depth
                return
            dfs(root.left, depth)
            dfs(root.right, depth)
            return

        dfs(root, 0)
        return height


from collections import deque


class SolutionBFS:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque()
        q.appendleft(root)
        depth = 0
        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                root = q.pop()
                if root.left:
                    q.appendleft(root.left)
                if root.right:
                    q.appendleft(root.right)
        return depth
