"""543. 二叉树的直径
简单
相关标签
premium lock icon
相关企业
给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。



示例 1：


输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
示例 2：

输入：root = [1,2]
输出：1


提示：

树中节点数目在范围 [1, 104] 内
-100 <= Node.val <= 100

面试中遇到过这道题?
1/5
是
否
通过次数
796,352/1.2M
通过率
64.0%
相关标签
树
深度优先搜索
二叉树
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            l_edges = dfs(node.left)
            r_edges = dfs(node.right)
            if node.left:
                l_edges += 1
            if node.right:
                r_edges += 1
            diameter = max(diameter, l_edges + r_edges)
            return max(l_edges, r_edges)

        dfs(root)
        return diameter
