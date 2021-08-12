"""
113. 路径总和 II
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。



示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
示例 2：


输入：root = [1,2,3], targetSum = 5
输出：[]
示例 3：

输入：root = [1,2], targetSum = 0
输出：[]


提示：

树中节点总数在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
通过次数162,519提交次数259,865

tag: 树 深度优先搜索 回溯 二叉树
"""
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return [[root.val]]
            return []
        ret = []
        left_ret = self.pathSum(root.left, targetSum - root.val)
        right_ret = self.pathSum(root.right, targetSum - root.val)
        for sub_ret in left_ret:
            ret.append([root.val] + sub_ret)  # 这样写性能不行
        for sub_ret in right_ret:
            ret.append([root.val] + sub_ret)  # 这样写性能不行
        return ret

    def pathSumDFS(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        ret = []

        def dfs(root: Optional[TreeNode], targetSum: int):
            if root is None:
                return
            path.append(root.val)
            targetSum -= root.val
            if root.left is None and root.right is None and targetSum == 0:
                ret.append(path[:])
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()

        dfs(root, targetSum)
        return ret

    def pathSumBFS(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        ret = []
        q = deque()
        q.appendleft((root, targetSum))
        size = 1
        parent = {id(root): None}

        def get_path(node):
            tmp = []
            while node:
                tmp.append(node.value)
                node = parent[id(node)]
            return tmp[::-1]

        while q:
            new_size = 0
            for _ in range(size):
                node, targetSum = q.pop()
                new_target_sum = targetSum - node.val
                if node.left is None and node.right is None and new_target_sum == 0:
                    ret.append(get_path(node))
                if node.left:
                    new_size += 1
                    parent[id(node.left)] = node
                    q.appendleft((node.left, new_target_sum))
                if node.right:
                    new_size += 1
                    parent[id(node.right)] = node
                    q.appendleft((node.right, new_target_sum))
            size = new_size
        return ret


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    s = Solution()
    print(s.pathSum(root, 1))
