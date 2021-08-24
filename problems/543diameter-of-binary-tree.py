"""
543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。



示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。



注意：两结点之间的路径长度是以它们之间边的数目表示。

通过次数139,488提交次数254,396

tag: 树 深度优先搜索 二叉树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.max_diameter

    def dfs(self, root: TreeNode):
        if not root:
            return 0
        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)
        self.max_diameter = max(left_depth + right_depth, self.max_diameter)
        return max(left_depth, right_depth) + 1
