"""
83. 删除排序链表中的重复元素
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。

返回同样按升序排列的结果链表。



示例 1：


输入：head = [1,1,2]
输出：[1,2]
示例 2：


输入：head = [1,1,2,3,3]
输出：[1,2,3]


提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列
通过次数302,228提交次数561,063

tag: 链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


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


def print_nodes(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    head = [1, 1, 2, 3, 3]
    head = create_list(head)
    print_nodes(head)
    s = Solution()
    head = s.deleteDuplicates(head)
    print("=====" * 10)
    print_nodes(head)
