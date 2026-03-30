"""94. 二叉树的中序遍历
简单
相关标签
premium lock icon
相关企业
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。



示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]


提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100


进阶: 递归算法很简单，你可以通过迭代算法完成吗？


面试中遇到过这道题?
1/5
是
否
通过次数
2,129,920/2.7M
通过率
78.3%
相关标签
栈
树
深度优先搜索
二叉树
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalMorris(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        while root:
            if not root.left:
                ret.append(root.val)
                root = root.right
                continue
            pre = root.left
            while pre.right and pre.right is not root:
                pre = pre.right

            if not pre.right:
                pre.right = root
                root = root.left
            else:
                pre.right = None
                ret.append(root.val)
                root = root.right
        return ret


    def inorderTraversalIter(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stk = []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            ret.append(root.val)
            root = root.right
        return ret

    def inorderTraversalRecurr(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        def travere(node: Optional[TreeNode]):
            nonlocal ret
            if not node:
                return
            travere(node.left)
            ret.append(node.val)
            travere(node.right)

        travere(root)
        return ret
