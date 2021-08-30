"""
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。



例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
`
通过次数391,123提交次数696,947

tag: 数 深度优先搜索 广度优先搜索 二叉树

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # todo 用广度优先搜索也可以, 同时遍历两颗树
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None:
            return False
        if root1 is not None and root2 is None:
            return False

        return root1.val == root2.val and self.dfs(root1.left, root2.right) and self.dfs(root1.right, root2.left)
