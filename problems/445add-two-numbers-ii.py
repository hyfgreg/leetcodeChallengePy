"""
445. 两数相加 II
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。



示例1：



输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]
示例2：

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[8,0,7]
示例3：

输入：l1 = [0], l2 = [0]
输出：[0]


提示：

链表的长度范围为 [1, 100]
0 <= node.val <= 9
输入数据保证链表代表的数字无前导 0


进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。

通过次数82,486提交次数140,095

tag: 栈 链表 数学
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        st1 = []
        st2 = []
        while l1:
            st1.append(l1.val)
            l1 = l1.next

        while l2:
            st2.append(l2.val)
            l2 = l2.next

        carry = 0
        next_ = None
        while st1 or st2 or carry:
            val1 = st1.pop() if st1 else 0
            val2 = st2.pop() if st2 else 0
            val = val1 + val2 + carry
            if val >= 10:
                carry = 1
                val = val - 10
            else:
                carry = 0
            head = ListNode(val)
            head.next = next_
            next_ = head
        return next_
