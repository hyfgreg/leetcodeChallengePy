"""148. 排序链表
中等
相关标签
premium lock icon
相关企业
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。



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


进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？


面试中遇到过这道题?
1/5
是
否
通过次数
901,160/1.3M
通过率
67.7%
相关标签
链表
双指针
分治
排序
归并排序
"""

import heapq
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"ListNode({self.val})"

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def merge(head1: Optional[ListNode], head2: Optional[ListNode]):
            dum = ListNode(-1)
            prev = dum
            while head1 and head2:
                if head1.val < head2.val:
                    prev.next = head1
                    head1 = head1.next
                else:
                    prev.next = head2
                    head2 = head2.next
                prev = prev.next
            if head1:
                prev.next = head1
            if head2:
                prev.next = head2
            return dum.next

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        # print("length", length)
        dummy = ListNode(-1, head)
        sub_length = 1
        while sub_length < length:
            prev, curr = dummy, dummy.next
            # print("sub_length", sub_length)
            while curr:
                head1 = curr
                for i in range(1, sub_length):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                # 此时curr是左边的最后一个
                head2 = curr.next
                curr.next = None  # 断开左边和右边的联系

                # 看看左边的数
                # print("left")
                # walk(head1)
                curr = head2
                for i in range(1, sub_length):
                    if (
                        curr and curr.next
                    ):  # 保证curr不是None，即右边的数量可以比sub_length少
                        curr = curr.next
                    else:
                        break
                # 此时curr是右边的最后一个

                # 把下一组的开头找出来
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None  # 断开这一组和下一组的联系

                # print("right")
                # walk(head2)

                new_head = merge(head1, head2)
                prev.next = new_head
                while prev.next:
                    prev = prev.next  # 这一组的结尾，作为上一组的开头
                curr = succ  # 下一组的开头

            sub_length *= 2
            # print("=====")
        return dummy.next

    def sortListMerge(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        slow = ListNode(-1, head)
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow.next
        slow.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        prev = ListNode(-1)
        curr = prev
        while True:
            if left and right:
                curr.next = left if left.val < right.val else right
                if left.val < right.val:
                    left = left.next
                else:
                    right = right.next
                curr = curr.next
            elif left:
                curr.next = left
                break
            elif right:
                curr.next = right
                break
            else:
                break

        return prev.next


def create_list(val_list: list):
    head = None
    prev = None
    for i in val_list:
        node = ListNode(i)
        if prev:
            prev.next = node
        if not head:
            head = node
        prev = node
    return head


def walk(node):
    while node:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    head = create_list([4, 2, 1, 3, 0])
    solu = Solution()
    ret = solu.sortList(head)
    walk(ret)
