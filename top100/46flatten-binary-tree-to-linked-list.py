"""114. 二叉树展开为链表
中等
相关标签
premium lock icon
相关企业
提示
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


面试中遇到过这道题?
1/5
是
否
通过次数
831,271/1.1M
通过率
76.2%
相关标签
栈
树
深度优先搜索
链表
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        找左子树的最右节点，把它连到右子树上，然后把左子树变成右子树，左子树清空。就这一个动作，循环重复，整棵树就拉平了！豆包的两句话比官解好理解多了
        """
        if not root:
            return

        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr.left = curr.right
                curr.left = None
            else:
                curr = curr.right
