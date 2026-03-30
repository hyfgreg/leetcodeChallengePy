"""226. 翻转二叉树
简单
相关标签
premium lock icon
相关企业
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。



示例 1：



输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
示例 2：



输入：root = [2,1,3]
输出：[2,3,1]
示例 3：

输入：root = []
输出：[]


提示：

树中节点数目范围在 [0, 100] 内
-100 <= Node.val <= 100

面试中遇到过这道题?
1/5
是
否
通过次数
1,433,315/1.7M
通过率
82.4%
相关标签
树
深度优先搜索
广度优先搜索
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

    def invertTreeWide(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = [root]
        while q:
            tmp = []
            for node in q:
                left, right = node.left, node.right
                node.left, node.right = right, left
                if left:
                    tmp.append(left)
                if right:
                    tmp.append(right)
            q = tmp
        return root
