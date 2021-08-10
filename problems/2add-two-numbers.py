"""
2. 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。



示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]


提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

tag: 递归 链表 数学
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self._add(l1, l2, 0)

    def _add(self, l1: ListNode, l2: ListNode, addition=0) -> ListNode or None:
        if not l1 and not l2:
            if addition == 0:
                return None
            return ListNode(1)
        if not l2:
            new_val = l1.val + addition
        elif not l1:
            new_val = l2.val + addition
        else:
            new_val = l1.val + l2.val + addition
        addition = 0
        if new_val >= 10:
            new_val -= 10
            addition = 1
        node = ListNode(new_val)
        node.next = self._add(l1.next if l1 else None, l2.next if l2 else None, addition)
        return node


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
    l1 = [0,8,6,5,6,8,3,5,7]
    l2 = [6,7,8,0,8,5,8,9,7]
    l1 = create_list(l1)
    l2 = create_list(l2)
    s = Solution()
    l3 = s.addTwoNumbers(l1, l2)
    while l3:
        print(l3.val)
        l3 = l3.next
