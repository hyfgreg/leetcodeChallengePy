"""
230. 二叉搜索树中第K小的元素
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。



示例 1：


输入：root = [3,1,4,null,2], k = 1
输出：1
示例 2：


输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3




提示：

树中的节点数为 n 。
1 <= k <= n <= 104
0 <= Node.val <= 104


进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？

通过次数136,526提交次数184,142

tag: 树 深度优先搜索 二叉搜索树 二叉树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0
    k = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # self.k = k
        # self.res = 0
        # self.dfs(root)
        # return self.res
        return self.dfs_iter(root, k)

    def dfs(self, root: TreeNode):
        if not root:
            return False
        ret = self.dfs(root.left)
        if ret:
            return True
        if self.k == 1:
            # print(f"k {self.k}, root.val {root.val}")
            self.res = root.val
            return True
        self.k -= 1
        return self.dfs(root.right)

    def dfs_iter(self, root: TreeNode, k):
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if k == 1:
                return node.val
            k -= 1
            node = node.right


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(s.kthSmallest(root, 1))
