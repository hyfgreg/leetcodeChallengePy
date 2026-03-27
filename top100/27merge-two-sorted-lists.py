"""21. 合并两个有序链表
简单
相关标签
premium lock icon
相关企业
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]


提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列

面试中遇到过这道题?
1/5
是
否
通过次数
2,396,716/3.5M
通过率
68.1%
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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2
        p1 = list1
        p2 = list2
        head = None
        prev = None
        while p1 and p2:
            if p1.val < p2.val:
                if not head:
                    head = p1
                if prev:
                    prev.next = p1
                prev = p1
                p1 = p1.next
            else:
                if not head:
                    head = p2
                if prev:
                    prev.next = p2
                prev = p2
                p2 = p2.next
        if p1:
            prev.next = p1
        if p2:
            prev.next = p2
        return head


"""
精彩啊！！！背下来！！！
"""


class SolutionRecurr:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
