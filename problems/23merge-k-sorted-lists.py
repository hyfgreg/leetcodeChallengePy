"""
23. 合并K个升序链表
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
通过次数296,633提交次数532,547

tag: 链表 分治 堆(优先队列) 归并排序
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        head1 = lists[0]
        for head2 in lists[1:]:
            head1 = self.merge(head1, head2)

        return head1

    def merge(self, head1: ListNode, head2: ListNode):
        if not head1:
            return head2
        if not head2:
            return head1
        head = ListNode(-1)
        tail = head
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
                tail = tail.next
            else:
                tail.next = head2
                head2 = head2.next
                tail = tail.next
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        return head.next


if __name__ == '__main__':
    values = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = [[ListNode(val) for val in value] for value in values]
    for _list in lists:
        root = None
        for _ in _list:
            if not root:
                root = _
            else:
                root.next = _
                root = _
    for _list in lists:
        root = _list[0]
        while root:
            print(root.val)
            root = root.next

    lists = [_[0] for _ in lists]
    print(lists)
    s = Solution()
    root = s.mergeKLists(lists)
    while root:
        print(root.val)
        root = root.next
