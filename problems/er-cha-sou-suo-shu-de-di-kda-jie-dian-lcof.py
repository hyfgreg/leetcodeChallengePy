"""
剑指 Offer 54. 二叉搜索树的第k大节点
给定一棵二叉搜索树，请找出其中第k大的节点。



示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4


限制：

1 ≤ k ≤ 二叉搜索树元素个数

通过次数154,083提交次数203,920

tag: 树 深度优先搜索 广度优先搜索 二叉树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        index = 1
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            if index == k:
                return node.val
            index += 1
            node = node.left
