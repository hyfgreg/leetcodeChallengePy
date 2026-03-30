"""105. 从前序与中序遍历序列构造二叉树
中等
相关标签
premium lock icon
相关企业
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。



示例 1:


输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
示例 2:

输入: preorder = [-1], inorder = [-1]
输出: [-1]


提示:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均 无重复 元素
inorder 均出现在 preorder
preorder 保证 为二叉树的前序遍历序列
inorder 保证 为二叉树的中序遍历序列

面试中遇到过这道题?
1/5
是
否
通过次数
1,037,093/1.4M
通过率
73.3%
相关标签
树
数组
哈希表
分治
二叉树
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        思路是对的，不过可以改进一点，让index的查询更快一些
        另外可以把build的参数改成开始和结束索引，这样就不用拷贝list了
        """
        value_index_map = {j: i for i, j in enumerate(inorder)}

        def build(preorder, inorder):
            nonlocal value_index_map
            if not preorder:
                return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            root = TreeNode(preorder[0])
            index = value_index_map[preorder[0]]
            root.left = self.buildTree(preorder[1 : 1 + index], inorder[:index])
            root.right = self.buildTree(preorder[1 + index :], inorder[index + 1 :])
            return root

        return build(preorder, inorder)

    def buildTreeIter(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder:
            return None

        index = 0
        root = TreeNode(preorder[0])
        stack = [root]
        for num in preorder[1:]:
            print("pre", num)
            node = TreeNode(num)
            if stack[-1].val != inorder[index]:
                print(
                    f"stack[-1].val: {stack[-1].val}, inorder[{index}]: {inorder[index]}"
                )
                stack[-1].left = node
            else:
                while stack and stack[-1].val == inorder[index]:
                    print(
                        f"stack[-1].val {stack[-1].val} == inorder[{index}]: {inorder[index]}"
                    )
                    parent = stack.pop()
                    index += 1
                print(f"parent: {parent.val}", )
                parent.right = node
            stack.append(node)

            print("=====")
        return


if __name__ == "__main__":
    preorder = [3, 9, 8, 5, 4, 10, 20, 15, 7]
    inorder = [4, 5, 8, 10, 9, 3, 15, 20, 7]
    solu = Solution()
    solu.buildTreeIter(preorder, inorder)
