"""
226. 翻转二叉树
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
通过次数289,091提交次数367,052

tag: 树 深度优先搜索 广度优先搜索 二叉树
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.bfs(root)
        return root

    def dfs(self, root: TreeNode):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.dfs(root.left)
        self.dfs(root.right)

    def bfs(self, root: TreeNode):
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            sz = len(q)
            for _ in range(sz):
                node = q.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

