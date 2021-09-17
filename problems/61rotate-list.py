"""
61. 旋转链表
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。



示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：


输入：head = [0,1,2], k = 4
输出：[2,0,1]


提示：

链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109
通过次数194,629提交次数465,833

tag: 链表 双指针
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = ListNode(-1, head)
        fast = slow
        steps = k
        while steps > 0:
            fast = fast.next
            steps -= 1
            if fast and fast.next is None:
                length = k - steps
                new_steps = k % length
                fast = slow
                while new_steps > 0:
                    fast = fast.next
                    new_steps -= 1
                break
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = head
        new_head = slow.next
        slow.next = None
        return new_head


def print_list_node(root: ListNode):
    while root:
        print(root.val)
        root = root.next


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
    s = Solution()
    head = [1, 2, 3]
    for i in range(1, 7):
        root = create_list(head)
        print_list_node(s.rotateRight(root, i))
        print("=====" * 10)
