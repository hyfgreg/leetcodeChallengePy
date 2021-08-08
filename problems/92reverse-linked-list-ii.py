"""
92. 反转链表 II
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。


示例 1：


输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
示例 2：

输入：head = [5], left = 1, right = 1
输出：[5]


提示：

链表中节点数目为 n
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


进阶： 你可以使用一趟扫描完成反转吗？

tag: 链表

这道题有什么特别的地方吗。。。？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head.next is None:
            return head
        index = 1
        prev0 = None
        curr = head
        while index < left:
            prev0 = curr
            curr = curr.next
            index += 1
        curr0 = curr

        prev = None
        while index <= right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            index += 1

        if prev0:
            prev0.next = prev
        curr0.next = curr
        if not prev0:
            return prev
        return head
