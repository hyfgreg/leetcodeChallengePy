"""
328. 奇偶链表
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
通过次数126,778提交次数193,170

tag: 链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 拆分链表
        if not head or not head.next:
            return head
        odd_pre = ListNode(-1)
        odd = odd_pre
        even_pre = ListNode(-1)
        even = even_pre
        i = 1
        while head:
            if i % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            i += 1
        odd.next = even_pre.next
        if even.next:
            even.next = None
        return odd_pre.next


def print_list_node(root: ListNode):
    while root:
        print(root.val)
        root = root.next


if __name__ == '__main__':
    s = Solution()
    root = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print_list_node(root)
    root = s.oddEvenList(root)
    print_list_node(root)
