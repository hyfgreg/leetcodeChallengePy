"""
104. 二叉树的最大深度
已解答
简单
相关标签
premium lock icon
相关企业
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。



示例 1：





输入：root = [3,9,20,null,null,15,7]
输出：3
示例 2：

输入：root = [1,null,2]
输出：2


提示：

树中节点的数量在 [0, 104] 区间内。
-100 <= Node.val <= 100

面试中遇到过这道题?
1/5
是
否
通过次数
1,978,105/2.5M
通过率
79.0%
相关标签
树
深度优先搜索
广度优先搜索
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


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def maxDepthWide(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 1
        q = Queue()
        q.put((root, 1))
        node: TreeNode
        height: int
        while q.qsize() > 0:
            node, height = q.get()
            if node.left:
                q.put((node.left, height + 1))
            if node.right:
                q.put((node.right, height + 1))
            if q.qsize() == 0:
                ans = height
        return ans
