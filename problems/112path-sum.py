"""
112. 路径总和
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。

叶子节点 是指没有子节点的节点。



示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
示例 2：


输入：root = [1,2,3], targetSum = 5
输出：false
示例 3：

输入：root = [1,2], targetSum = 0
输出：false


提示：

树中节点的数目在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
通过次数253,519提交次数482,203

tag: 树 深度优先搜索 二叉树
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum)

    def dfs(self, root: TreeNode, targetSum: int):
        if not root:
            return False
        if not root.left and not root.right:
            if root.val == targetSum:
                return True
            return False
        left_ans = False
        right_ans = False
        if root.left:
            left_ans = self.dfs(root.left, targetSum - root.val)
        if root.right:
            right_ans = self.dfs(root.right, targetSum - root.val)
        return left_ans or right_ans
