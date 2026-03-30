"""108. 将有序数组转换为二叉搜索树
简单
相关标签
premium lock icon
相关企业
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。



示例 1：


输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：


输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。


提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 按 严格递增 顺序排列

面试中遇到过这道题?
1/5
是
否
通过次数
837,140/1M
通过率
80.7%
相关标签
树
二叉搜索树
数组
分治
二叉树
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def bst(nums, l, r):
            if l == r:
                return None
            if r - l == 1:
                return TreeNode(nums[l])
            mid = l + (r - l) // 2
            left = bst(nums, l, mid)
            right = bst(nums, mid + 1, r)
            node = TreeNode(nums[mid])
            node.left = left
            node.right = right
            return node

        return bst(nums, 0, len(nums))
