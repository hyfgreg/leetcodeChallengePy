"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？



示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]


提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
通过次数465,003提交次数1,091,277

tag: 链表 双指针
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = ListNode(-1)
        left.next = head
        right = head
        for i in range(n):
            right = right.next
        while right:
            left = left.next
            right = right.next
        if left.next == head:
            return head.next
        left.next = left.next.next
        return head



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


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    # head = [1]
    head = create_list(head)
    s = Solution()
    head = s.removeNthFromEnd(head, 2)
    while head:
        print(head.val)
        head = head.next
