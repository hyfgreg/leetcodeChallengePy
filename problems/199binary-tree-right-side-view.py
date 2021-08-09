"""
199. 二叉树的右视图
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。



示例 1:



输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
示例 2:

输入: [1,null,3]
输出: [1,3]
示例 3:

输入: []
输出: []


提示:

二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100
通过次数126,639提交次数194,513

tag: 树 深度优先搜索 广度优先搜索 二叉树

BFS是一个符合第一直觉的做法
但是DFS很有意思
首先是用stack模拟递归
然后用dict保存每一层第一次被访问的结点的值
然后采用先右再左的先序遍历，第一次被访问的结点一定是最右的结点
cool~！

背诵， 迭代版本的DFS
"""
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = deque()
        q.appendleft(root)
        size = 1
        ret = []
        while q:
            node = None
            new_size = 0
            for _ in range(size):
                node = q.pop()
                if node.left:
                    q.appendleft(node.left)
                    new_size += 1
                if node.right:
                    q.appendleft(node.right)
                    new_size += 1
            ret.append(node.val)
            size = new_size
        return ret


# TODO use DFS
class SolutionDFS:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        depth_dict = dict()
        st = list()
        st.append((root, 0))
        max_depth = -1
        while st:
            node, depth = st.pop()
            max_depth = max(depth, max_depth)
            depth_dict.setdefault(depth, node.val)
            if node.left:
                st.append((node.left, depth + 1))
            if node.right:
                st.append((node.right, depth + 1))

        return [depth_dict[i] for i in range(max_depth + 1)]
