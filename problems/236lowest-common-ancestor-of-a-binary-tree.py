"""
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”



示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1


提示：

树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。
通过次数230,086提交次数339,662

tag: 树 深度优先搜索 二叉树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == p:
            return p
        if root == q:
            return q
        p_path = self.dfs(root, p)
        q_path = self.dfs(root, q)
        length = min(len(p_path), len(q_path))
        i = 1
        while i < length:
            if p_path[i] != q_path[i]:
                return p_path[i - 1]
            i += 1
        return p_path[i - 1]

    def dfs(self, node: TreeNode, target: TreeNode):
        if not node:
            return []
        if node.val == target.val:
            return [node]
        left = self.dfs(node.left, target)
        right = self.dfs(node.right, target)
        ret = [node]
        if left:
            ret.extend(left)
        elif right:
            ret.extend(right)
        else:
            return []
        return ret


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
这个很牛逼
大概思路是这样的
分别在我的左子树和右子树里找p或者q
如果往左找和往右找都找到了，说明p和q分别在我的左右两颗子树里，那么我就是最近的公共祖先
如果左边没找到，那么都在我的右子树里，用右子树的答案
反之亦然
用一遍dfs就行了
后序遍历
"""


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root == p:
            return root
        if root == q:
            return root
        ans1 = self.lowestCommonAncestor(root.left, p, q)
        ans2 = self.lowestCommonAncestor(root.right, p, q)
        if not ans1:
            return ans2
        if not ans2:
            return ans1
        return root
