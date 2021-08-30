"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
通过次数329,863提交次数946,493

tag: 树 深度优先搜索 二叉搜索树 二叉树
# 需要背诵迭代版本的三种数的遍历
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        curr = None
        for n in self.inorder(root):
            prev = curr
            curr = n
            if (curr is not None) and (prev is not None) and curr <= prev:
                return False
        return True

    def inorder(self, root: TreeNode):
        if not root:
            return
        yield from self.inorder(root.left)
        yield root.val
        yield from self.inorder(root.right)
        return


if __name__ == '__main__':
    root = TreeNode(0, None, TreeNode(-1))
    s = Solution()
    print(s.isValidBST(root))
