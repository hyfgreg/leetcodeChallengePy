"""
662. 二叉树最大宽度
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

示例 1:

输入:

           1
         /   \
        3     2
       / \     \
      5   3     9

输出: 4
解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
示例 2:

输入:

          1
         /
        3
       / \
      5   3

输出: 2
解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
示例 3:

输入:

          1
         / \
        3   2
       /
      5

输出: 2
解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
示例 4:

输入:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
输出: 8
解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
注意: 答案在32位有符号整数的表示范围内。

通过次数27,527提交次数67,597

tag: 树 深度优先搜索 广度优先搜索 二叉树
"""
from collections import deque

# Definition for a binary tree node.
from turtle import width


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        q.appendleft((root, 1))
        width = 1
        while q:
            sz = len(q)
            start = None
            end = None
            for _ in range(sz):
                node, index = q.pop()
                if not start:
                    start = index
                if node:
                    end = index
                if node.left:
                    q.appendleft((node.left, 2 * index))
                if node.right:
                    q.appendleft((node.right, 2 * index + 1))
            width = max(width, end - start + 1)
        return width

    def widthOfBinaryTreeDFS(self, root: TreeNode) -> int:
        # 背诵 深度优先搜索也是可以的，但是没有BFS那么第一反应
        ans = 0
        left = {}

        def dfs(node, depth=0, pos=1):
            nonlocal ans
            if not node:
                return 0
            left.setdefault(depth, pos)
            ans = max(ans, pos - left[depth] + 1)
            dfs(node.left, depth + 1, 2 * pos)
            dfs(node.right, depth + 1, 2 * pos + 1)
        dfs(root)
        return ans
