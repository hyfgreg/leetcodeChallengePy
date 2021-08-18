"""
82. 删除排序链表中的重复元素 II
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。

返回同样按升序排列的结果链表。



示例 1：


输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例 2：


输入：head = [1,1,1,2,3]
输出：[2,3]


提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列

tag: 链表 双指针
todo: 递归？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # if not head:
        #     return head
        prev = ListNode(-1, head)
        curr = prev
        new_head = None
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr = curr.next
            elif not curr.next or curr.val != curr.next.val:
                # curr.val != curr.next.val
                if prev.next == curr:
                    prev = curr
                    if not new_head:
                        new_head = prev
                else:
                    prev.next = curr.next
                curr = curr.next
        return new_head


class SolutionOfficial:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

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


if __name__ == '__main__':
    head = [1, 2, 3, 3, 4, 4, 5]
    head = [1, 1, 1, 2, 3]
    head = [1, 1]
    head = [1]
    head = [1, 2, 2]
    head = []
    head = create_list(head)
    s = Solution()
    head = s.deleteDuplicates(head)
    while head:
        print(head.val)
        head = head.next
