"""
剑指 Offer 52. 两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点。

如下面的两个链表：



在节点 c1 开始相交。



示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。


示例 2：



输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。


示例 3：



输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。


注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
通过次数175,436提交次数269,937

tag: 哈希表 链表 双指针
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNodeMy(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = self.get_length(headA)
        len_b = self.get_length(headB)
        if len_a < len_b:
            return self.get_intersection(headA, len_a, headB, len_b)
        return self.get_intersection(headB, len_b, headA, len_a)

    def get_intersection(self, short: ListNode, short_len: int, long: ListNode, long_len: int) -> ListNode:
        steps = long_len - short_len
        while steps > 0:
            long = long.next
            steps -= 1
        while short and long and short != long:
            short = short.next
            long = long.next
        return short

    def get_length(self, head: ListNode) -> int:
        node = head
        ret = 0
        while node:
            ret += 1
            node = node.next
        return ret

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 背诵， 这个方法可以看看原理，其实和我自己的是一样的，不过更优雅一些。走完了就换到对面的节点
        if not headA or not headB:
            return None
        node_a = headA
        node_b = headB
        while node_a != node_b:
            node_a = node_a.next if node_a else headB
            node_b = node_b.next if node_b else headA
        return node_a
