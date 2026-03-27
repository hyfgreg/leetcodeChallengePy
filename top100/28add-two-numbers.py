"""2. 两数相加
中等
相关标签
premium lock icon
相关企业
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

面试中遇到过这道题?
1/5
是
否
通过次数
2,785,544/6M
通过率
46.7%
相关标签
初级工程师
递归
链表
数学
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        prevhead = ListNode(-1)
        prev = prevhead
        carry = 0
        while l1 or l2:
            if l1 and l2:
                s = l1.val + l2.val + carry
            elif l1:
                if carry:
                    s = l1.val + carry
                else:
                    prev.next = l1
                    break
            else:
                if carry:
                    s = l2.val + carry
                else:
                    prev.next = l2
                    break
            val = s % 10
            carry = s // 10
            node = ListNode(val)
            prev.next = node
            prev = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            prev.next = ListNode(carry)

        return prevhead.next


"""
背下来！！！
"""


class SolutionRecurr:
    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0
    ) -> Optional[ListNode]:
        if l1 is None and l2 is None and carry == 0:  # 递归边界
            return None

        s = carry
        if l1:
            s += l1.val  # 累加进位与节点值
            l1 = l1.next
        if l2:
            s += l2.val
            l2 = l2.next

        # s 除以 10 的余数为当前节点值，商为进位
        return ListNode(s % 10, self.addTwoNumbers(l1, l2, s // 10))
