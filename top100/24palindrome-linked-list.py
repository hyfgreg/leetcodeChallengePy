"""234. 回文链表
简单
相关标签
premium lock icon
相关企业
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。



示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false


提示：

链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9


进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


面试中遇到过这道题?
1/5
是
否
通过次数
1,236,400/2.1M
通过率
58.1%
相关标签
栈
递归
链表
双指针
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"ListNode({self.val})"


"""
1. 遍历全部数值到一个list，然后前后双指针判断
2. 用递归的方法实现1
3. 反转一半的链表，然后对比，然后再反转回来恢复
我试试第3种
"""


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val

        p1 = head
        p2 = head
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        # 1 2
        # 1 2 2 1
        # 1 2 3 2 1
        # 1 2 1
        # 1 1 2 1
        print(p1)
        print(p2)

        prev = None
        curr = p1
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        print(head, head.next, head.next.next)
        print(prev, prev.next, prev.next.next)

        p1 = head
        p2 = prev
        res = True
        while p1 and p2:
            if p1.val != p2.val:
                res = False
                break
            p1 = p1.next
            p2 = p2.next

        curr = prev
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return res


def create(n, good=True):
    half = n // 2
    head = None
    prev = None
    for i in range(n):
        if good:
            if i < half:
                val = i
            else:
                val = (n - 1) - i
        else:
            val = i
        node = ListNode(val)
        if not head:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head


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
    head = create(4, False)
    head = create_list([1, 2])
    walk(head)
    solu = Solution()
    print(solu.isPalindrome(head))
    walk(head)
