"""
114. 二叉树展开为链表
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。


示例 1：


输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [0]
输出：[0]


提示：

树中结点数在范围 [0, 2000] 内
-100 <= Node.val <= 100


进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？

通过次数178,864提交次数246,423

tag: 栈 树 深度优先搜索 链表 二叉树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node: TreeNode):
            if not node:
                return None
            if not node.left and not node.right:
                return node
            if not node.left:
                return dfs(node.right)
            if not node.right:
                node.right = node.left
                node.left = None
                return dfs(node.right)
            right = node.right
            left = node.left
            node.left = None
            node.right = left
            left_tail = dfs(left)
            left_tail.right = right
            return dfs(right)

        dfs(root)


def print_flatten(node: TreeNode):
    while node:
        print(node.left, node.val)
        node = node.right


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    s = Solution()
    s.flatten(root)
    print_flatten(root)
