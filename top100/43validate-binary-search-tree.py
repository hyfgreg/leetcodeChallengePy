"""98. 验证二叉搜索树
中等
相关标签
premium lock icon
相关企业
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 严格小于 当前节点的数。
节点的右子树只包含 严格大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


示例 1：


输入：root = [2,1,3]
输出：true
示例 2：


输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。


提示：

树中节点数目范围在[1, 104] 内
-231 <= Node.val <= 231 - 1

面试中遇到过这道题?
1/5
是
否
通过次数
1,403,125/3.4M
通过率
40.8%
相关标签
树
深度优先搜索
二叉搜索树
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(root, min_val=float("-inf"), max_val=float("inf")):
            if not root:
                return True
            if root.left and root.right:
                if not (min_val < root.left.val < root.val < root.right.val < max_val):
                    return False
                return is_valid(root.left, min_val, root.val) and is_valid(
                    root.right, root.val, max_val
                )
            if root.left:
                if root.left.val >= root.val:
                    return False
                return is_valid(root.left, min_val, root.val)
            if root.right:
                if root.val >= root.right.val:
                    return False
                return is_valid(root.right, root.val, max_val)
            return min_val < root.val < max_val

        return is_valid(root)

    def isValidBSTBFS(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack, prev = [], float("-inf")
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True
