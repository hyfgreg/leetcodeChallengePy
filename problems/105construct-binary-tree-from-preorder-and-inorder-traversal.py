"""
105. 从前序与中序遍历序列构造二叉树
给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。



示例 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
示例 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


提示:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均无重复元素
inorder 均出现在 preorder
preorder 保证为二叉树的前序遍历序列
inorder 保证为二叉树的中序遍历序列
通过次数228,186提交次数324,918

tag: 树 数组 哈希 分治 二叉树
todo: https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
      108. 将有序数组转换为二叉搜索树
      进一步，将一个乱序数组转换为二叉搜索树
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode or None:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = 0
        while index < len(inorder):
            if inorder[index] == root.val:
                break
            index += 1
        root.left = self.buildTree(preorder[1:1 + index], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root
