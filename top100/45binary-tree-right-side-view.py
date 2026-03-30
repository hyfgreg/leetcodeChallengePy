"""199. 二叉树的右视图
中等
相关标签
premium lock icon
相关企业
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。



示例 1：

输入：root = [1,2,3,null,5,null,4]

输出：[1,3,4]

解释：



示例 2：

输入：root = [1,2,3,4,null,null,null,5]

输出：[1,3,4,5]

解释：



示例 3：

输入：root = [1,null,3]

输出：[1,3]

示例 4：

输入：root = []

输出：[]



提示:

二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100

面试中遇到过这道题?
1/5
是
否
通过次数
808,341/1.1M
通过率
73.2%
相关标签
树
深度优先搜索
广度优先搜索
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        ret = []
        while q:
            tmp = []
            ret.append(q[-1].val)
            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp
        return ret

    def rightSideViewDFS(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        if not root:
            return ret

        def preorder(root, depth):
            nonlocal ret
            if not root:
                return
            if depth == len(ret):
                ret.append(root.val)
            preorder(root.right, depth=depth + 1)
            preorder(root.left, depth=depth + 1)

        preorder(root, depth=0)
        return ret

    def rightSideViewDFSIter(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        if not root:
            return ret

        stk = [(root, 0)]
        while stk:
            node, depth = stk.pop()
            if not node:
                continue
            if depth == len(ret):
                ret.append(node.val)
            stk.append((node.left, depth + 1))
            stk.append((node.right, depth + 1))
        return ret
