"""
103. 二叉树的锯齿形层序遍历
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
通过次数158,204提交次数276,864

tag: 树 广度优先搜索 二叉树
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if not root:
            return ret
        q: List[TreeNode] = list()
        reverse = False
        q.append(root)
        while q:
            count = len(q)
            tmp = []
            for _ in range(count):
                if reverse:
                    # 当前逆序，从后取node，往前加node
                    node = q.pop()
                    print("reverse", reverse)
                    print("get node ", node.val)
                    tmp.append(node.val)

                    if node.right:
                        q.insert(0, node.right)
                        print("insert right", node.right.val)
                    if node.left:
                        q.insert(0, node.left)
                        print("insert left", node.left.val)

                else:
                    # 当前正序，从前取node，往后加node
                    node = q.pop(0)
                    print("reverse", reverse)
                    print("get node ", node.val)
                    tmp.append(node.val)
                    if node.left:
                        q.append(node.left)
                        print("append left", node.left.val)
                    if node.right:
                        q.append(node.right)
                        print("append right", node.right.val)
            ret.append(tmp)
            reverse = not reverse
            print("=====" * 10)
        return ret


if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    root.left = left
    root.right = right
    right_left = TreeNode(15)
    right_right = TreeNode(7)

    right.left = right_left
    right.right = right_right
    s = Solution()
    print(s.zigzagLevelOrder(root))
