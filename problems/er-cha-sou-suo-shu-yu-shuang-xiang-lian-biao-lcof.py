"""
剑指 Offer 36. 二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。



为了让您更好地理解问题，以下面的二叉搜索树为例：







我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。







特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。



注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

注意：此题对比原题有改动。

通过次数98,427提交次数150,422

tag: 栈 树 深度优先搜索 广度优先搜索 链表 二叉树 双向链表
背诵 中序遍历的递归和迭代两种方式
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        dummy = Node(-1, None, None)
        prev = dummy

        def dfs(node: Node):
            nonlocal prev
            if not node:
                return
            dfs(node.left)
            prev.right = node
            node.left = prev
            prev = node
            dfs(prev.right)

        dfs(root)

        if prev != dummy:
            prev.right = dummy.right
        if dummy.right:
            dummy.right.left = prev
        return dummy.right

    def treeToDoublyListIter(self, root: 'Node') -> 'Node':
        dummy = Node(-1, None, None)
        prev = dummy
        node = root
        st = []
        while node or st:
            while node:
                st.append(node)
                node = node.left
            node = st.pop()
            prev.right = node
            node.left = prev
            prev = node
            node = node.right

        if prev != dummy:
            prev.right = dummy.right

        if dummy.right:
            dummy.right.left = prev

        return dummy.right


if __name__ == '__main__':
    root = Node(4, Node(2, Node(1), Node(3)), Node(5))
    s = Solution()
    s.treeToDoublyListIter(root)
