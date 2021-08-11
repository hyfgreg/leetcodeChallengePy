"""
143. 重排链表
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

 L0 → L1 → … → Ln-1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例 1:



输入: head = [1,2,3,4]
输出: [1,4,2,3]
示例 2:



输入: head = [1,2,3,4,5]
输出: [1,5,2,4,3]


提示：

链表的长度范围为 [1, 5 * 104]
1 <= node.val <= 1000
通过次数113,646提交次数184,991

tag: 栈 递归 链表 双指针

思路:
1. 遍历，扔到list里，用下标访问结点，重建链表
2. 链表中点+翻转链表+链表合并
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        st = []
        node = head.next
        while node:
            st.append(node)
            node = node.next
        node = head
        while st:
            new_next = st.pop()
            if new_next == node:
                node.next = None
                break
            old_next = node.next
            if old_next == new_next:
                old_next.next = None
                break
            node.next = new_next
            new_next.next = old_next
            node = old_next


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
    head = [1, 2, 3, 4]
    head = [1, 2, 3, 4, 5]
    head = create_list(head)
    s = Solution()
    s.reorderList(head)
    while head:
        print(head.val)
        head = head.next
