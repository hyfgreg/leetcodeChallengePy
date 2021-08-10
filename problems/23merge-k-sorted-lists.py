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

背诵: 优先队列，归并排序
注意优先队列中子节点的index的计算, 从0开始和从1开始不一样
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


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


class SolutionDivideAndConquer:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists: List[ListNode], left: int, right: int):
        if left > right:
            return None
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        return self.merge_two_list(self.merge(lists, left, mid), self.merge(lists, mid + 1, right))

    def merge_two_list(self, head1: ListNode, head2: ListNode):
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


class MinPQ:
    Q = []
    N = 0

    def add(self, val):
        self.Q.append(val)
        self.swim(self.N)
        self.N += 1

    def pop(self):
        if self.N == 0:
            raise ValueError("empty PQ")
        self.N -= 1
        self.swap(0, self.N)
        val = self.Q.pop()
        self.sink(0)
        return val

    def sink(self, index):
        left = 2 * index + 1
        while left < self.N:
            right = left + 1
            if right < self.N and self.less(right, left):
                left = right
            if not self.less(left, index):
                break
            self.swap(left, index)
            index = left
            left = 2 * index + 1

    def swim(self, index):
        new_index = (index - 1) // 2
        while index > 0 and self.less(index, new_index):
            self.swap(index, new_index)
            index = new_index
            new_index = (new_index - 1) // 2

    def less(self, p, q):
        return self.Q[p].val < self.Q[q].val

    def swap(self, p, q):
        self.Q[p], self.Q[q] = self.Q[q], self.Q[p]

    def empty(self):
        return self.N == 0

    def __str__(self):
        return str([i.val for i in self.Q])


class SolutionPQ:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = MinPQ()
        head = ListNode(-1)
        tail = head
        for n in lists:
            if n:
                pq.add(n)
                # print(f"add", n)
        while not pq.empty():
            next = pq.pop()
            tail.next = next
            tail = tail.next
            if next.next:
                pq.add(next.next)
        return head.next


if __name__ == '__main__':
    values = [[-6, -3, -1, 1, 2, 2, 2], [-10, -8, -6, -2, 4], [-2], [-8, -4, -3, -3, -2, -1, 1, 2, 3],
              [-8, -6, -5, -4, -2, -2, 2, 4]]
    lists = [[ListNode(val) for val in value] for value in values]
    for _list in lists:
        root = None
        for _ in _list:
            if not root:
                root = _
            else:
                root.next = _
                root = _
    # for _list in lists:
    #     root = _list[0]
    #     while root:
    #         print(root.val)
    #         root = root.next
    #     print("=====" * 10)

    lists = [_[0] for _ in lists]
    print(lists)
    s = SolutionPQ()
    root = s.mergeKLists(lists)
    while root:
        print(root.val)
        root = root.next
