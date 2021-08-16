"""
148. 排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？


示例 1：


输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：


输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]


提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
通过次数195,181提交次数292,315

tag: 链表 双指针 分治 排序 归并排序
背诵
本质是归并排序的两种写法
递归和迭代
迭代的空间占用更小，因为没有调用栈
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        sub_length = 1
        dummy = ListNode(-1, head)

        while sub_length < length:
            print("sub_length", sub_length)
            prev, curr = dummy, dummy.next
            while curr:
                head1 = curr
                # print("head1", head1.val)
                for _ in range(1, sub_length):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                # print("head2", head2.val if head2 else None)
                curr.next = None
                curr = head2
                for _ in range(1, sub_length):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                if curr:
                    succ = curr.next
                    curr.next = None
                else:
                    succ = None
                merged = self.merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
                # print("-----" * 10)
            sub_length <<= 1
            # print("=====" * 10)
        return dummy.next

    def sortListRecursive(self, head: ListNode) -> ListNode:
        return self.sort_list(head, None)

    def sort_list(self, head, tail):
        # cannot get tail, before tail it ends
        # print("sort", head.val if head else None, tail.val if tail else None)
        if head is None:
            return head
        if head.next == tail:
            # print("head.next==tail")
            head.next = None  # 这一步非常重要，否则merge方法合并的链表是错误的
            return head
        # print("find mid")
        slow, fast = head, head
        while fast != tail:
            # 快慢指针求链表中点，背诵
            slow = slow.next
            fast = fast.next
            if fast == tail:
                break
            fast = fast.next
        mid = slow
        # mid.next = None
        left = self.sort_list(head, mid)
        # print("sort", head.val if head else None, mid.val if mid else None, 'return')
        right = self.sort_list(mid, tail)
        # print("sort", mid.val if mid else None, tail.val if tail else None, 'return')
        return self.merge(left, right)

    def merge(self, head1, head2):
        if not head2:
            return head1
        if not head1:
            return head2
        head = ListNode(-1)
        tail = head
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        return head.next


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
    head = [4, 19, 14, 5, -3, 1, 8, 5, 11, 15]
    head = create_list(head)
    s = Solution()
    head = s.sortListRecursive(head)
    while head:
        print(head.val)
        head = head.next
