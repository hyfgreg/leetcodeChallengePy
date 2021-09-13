"""
剑指 Offer 22. 链表中倒数第k个节点
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。



示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
通过次数205,599提交次数260,725

tag: 链表 双指针
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        left = head
        right = head
        for _ in range(k-1):
            right = right.next
        while right:
            left = left.next
            right = right.next
        return left


if __name__ == '__main__':
    head = ListNode(1)
    node = head
    for i in range(2, 6):
        next = ListNode(i)
        node.next = next
        node = next
    # node = head
    # while node:
    #     print(node.val)
    #     node = node.next
    s = Solution()
    print(s.getKthFromEnd(head, 3))