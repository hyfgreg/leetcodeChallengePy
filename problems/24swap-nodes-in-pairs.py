"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]


提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100


进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。）

通过次数307,557提交次数437,478

tag: 递归 链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.swap_iter(head)

    def swap(self, node: ListNode):
        if not node:
            return node
        if not node.next:
            return node
        next_node = node.next
        next_next_node = node.next.next
        next_node.next = node
        node.next = self.swap(next_next_node)
        return next_node

    def swap_iter(self, node: ListNode) -> ListNode:
        if not node:
            return node
        if not node.next:
            return node
        dummy = ListNode(-1, node)
        prev = dummy
        while node and node.next:
            next_node = node.next
            next_next_node = node.next.next

            prev.next = next_node
            next_node.next = node
            node.next = next_next_node

            prev = node
            node = next_next_node
        return dummy.next


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


def print_list_node(root: ListNode):
    while root:
        print(root.val)
        root = root.next


if __name__ == '__main__':
    s = Solution()
    head = [1, 2, 3, 4]
    head = create_list(head)
    head = s.swapPairs(head)
    print_list_node(head)
    print("-----" * 10)
    head = [1]
    head = create_list(head)
    head = s.swapPairs(head)
    print_list_node(head)
    print("-----" * 10)
    head = [1, 2]
    head = create_list(head)
    head = s.swapPairs(head)
    print_list_node(head)
    print("-----" * 10)
    head = [1, 2, 3]
    head = create_list(head)
    head = s.swapPairs(head)
    print_list_node(head)
