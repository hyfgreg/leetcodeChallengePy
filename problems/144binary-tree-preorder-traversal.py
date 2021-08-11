"""
144. 二叉树的前序遍历
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。



示例 1：


输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[1,2]
示例 5：


输入：root = [1,null,2]
输出：[1,2]


提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100


进阶：递归算法很简单，你可以通过迭代算法完成吗？

通过次数375,303提交次数534,865

tag: 栈 树 深度优先搜索 二叉树
背诵 两种方法 递归和迭代
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        if not root:
            return ret
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        ret.append(root.val)
        ret.extend(left)
        ret.extend(right)
        return ret


class SolutionIteration:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        if not root:
            return ret
        st = [root]
        while st:
            node = st.pop()
            ret.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return ret


# todo 淦，怎么和我写的不太一样,感觉这个更标准一些
class SolutionAnswer:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if not root:
            return res

        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res
