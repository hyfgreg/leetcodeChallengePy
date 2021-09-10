"""
145. 二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

通过次数290,887提交次数388,142

tag: 栈 树 深度优先搜索 二叉树
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.ret = []
        self.post_order(root)
        return self.ret

    def post_order(self, node: TreeNode):
        if not node:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        self.ret.append(node.val)

    def post_order_iter(self, node: TreeNode):
        # 妈的，背诵！！！
        ret = []
        stack = []
        prev = None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or node.right == prev:
                print(node.val)
                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right

        return ret


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    s.post_order_iter(root)
