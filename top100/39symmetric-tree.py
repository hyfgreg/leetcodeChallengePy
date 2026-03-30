"""101. 对称二叉树
简单
相关标签
premium lock icon
相关企业
给你一个二叉树的根节点 root ， 检查它是否轴对称。



示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：


输入：root = [1,2,2,null,3,null,3]
输出：false


提示：

树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100


进阶：你可以运用递归和迭代两种方法解决这个问题吗？


面试中遇到过这道题?
1/5
是
否
通过次数
1,607,822/2.5M
通过率
63.5%
相关标签
树
深度优先搜索
广度优先搜索
二叉树
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = [root.left, root.right]
        while q:
            tmp = []
            for i in range(0, len(q), 2):
                n1 = q[i]
                n2 = q[i+1]
                if n1 and n2:
                    if n1.val != n2.val:
                        return False
                    tmp.append(n1.left)
                    tmp.append(n2.right)
                    tmp.append(n1.right)
                    tmp.append(n2.left)
                elif n1 and not n2:
                    return False
                elif not n1 and n2:
                    return False
            q = tmp
        return True

    def isSymmetricRecurr(self, root: Optional[TreeNode]) -> bool:
        def is_symmetric(left, right):
            if left and right:
                if left.val != right.val:
                    return False
            elif left and not right:
                return False
            elif not left and right:
                return False
            else:
                return True
            return is_symmetric(left.left, right.right) and is_symmetric(
                left.right, right.left
            )

        if not root:
            return True
        return is_symmetric(root.left, root.right)
