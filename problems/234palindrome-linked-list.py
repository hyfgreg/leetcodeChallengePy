"""
234. 回文链表
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。



示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false


提示：

链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9


进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

通过次数295,628提交次数599,980

tag: 栈 递归 链表 双指针
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head.next:
            return True
        mid = self.find_mid(head)
        second_half = self.reverse(mid)
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        # todo 恢复链表
        return True

    def find_mid(self, head: ListNode):
        dummy = ListNode(-1, head)
        slow = dummy
        fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        if not fast:
            return slow
        return slow.next

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


def create_list(l):
    if not l:
        return None
    head = ListNode(-1)
    tail = head
    for i in l:
        node = ListNode(i)
        tail.next = node
        tail = tail.next
    return head.next


def print_nodes(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    nodes = [1, 2, 1]
    head = create_list(nodes)
    s = Solution()
    # print_nodes(head)
    # head = s.reverse(head)
    # print_nodes(head)
    print(s.isPalindrome(head))
