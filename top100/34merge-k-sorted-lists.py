"""23. 合并 K 个升序链表
困难
相关标签
premium lock icon
相关企业
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。



示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]


提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

面试中遇到过这道题?
1/5
是
否
通过次数
1,213,878/1.9M
通过率
63.6%
相关标签
链表
分治
堆（优先队列）
归并排序
"""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]):
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

    def mergeLists(self, lists: List[Optional[ListNode]], l, r) -> Optional[ListNode]:
        if l == r:
            return None
        if l - r == 1:
            return lists[0]
        mid = l + (r - l) // 2
        left = self.mergeLists(lists, l, mid)
        right = self.mergeLists(lists, mid, r)
        return self.merge(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        return self.mergeLists(lists, 0, len(lists))

    def mergeKListsClassic(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        dummy = ListNode(-1)
        head1 = lists[0]
        for head2 in lists[1:]:
            head1 = self.merge(head1, head2)
            dummy.next = head1
        return dummy.next
