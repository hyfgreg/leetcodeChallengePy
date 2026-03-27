"""206. 反转链表
简单
相关标签
premium lock icon
相关企业
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]


提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000


进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？


面试中遇到过这道题?
1/5
是
否
通过次数
2,777,482/3.6M
通过率
76.4%
相关标签
递归
链表
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseListMeOrigin(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_head = None

        def reverse(node):
            nonlocal new_head
            if node is None:
                new_head = None
                return
            if node.next is None:
                new_head = node
                return
            next = node.next
            node.next = None
            reverse(next)
            next.next = node

        reverse(head)
        return new_head

    """
    递归的方法，直接返回新的头节点就可以了
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        next = head.next
        head.next = None
        next.next = head
        return new_head

    def reverseListIter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
