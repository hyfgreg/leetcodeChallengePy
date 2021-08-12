"""
124. 二叉树中的最大路径和
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。



示例 1：


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


提示：

树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000
通过次数143,991提交次数326,083

树 深度优先搜索 动态规划 二叉树
背诵, 后续遍历
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_value = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self._maxPathSum(root)
        return self.max_value

    def _maxPathSum(self, root: TreeNode):
        if root is None:
            return 0
        # 和0对比，如果0更大，意味着不经过子节点
        left_max = max(self._maxPathSum(root.left), 0)
        right_max = max(self._maxPathSum(root.right), 0)
        self.max_value = max(self.max_value, left_max + right_max + root.val)

        # 返回经过我自己的最大的值，但是不一定经过我的子节点
        return max(left_max, right_max) + root.val


if __name__ == '__main__':
    # root = TreeNode(1, TreeNode(2), TreeNode(3))
    # root = [-10, 9, 20, None, None, 15, 7]
    # root = TreeNode(-10, TreeNode(9),TreeNode(20, TreeNode(15), TreeNode(7)))
    # [-1,-2,10,-6,null,-3,-6]
    root = TreeNode(-1, TreeNode(-2), TreeNode(10))
    s = Solution()
    print(s.maxPathSum(root))
