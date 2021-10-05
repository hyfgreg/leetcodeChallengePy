"""
86. 分隔链表
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。



示例 1：


输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
示例 2：

输入：head = [2,1], x = 2
输出：[1,2]


提示：

链表中节点的数目在范围 [0, 200] 内
-100 <= Node.val <= 100
-200 <= x <= 200
通过次数120,252提交次数190,100

tag:
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_dummy = ListNode(-1)
        big_dummy = ListNode(-1)
        small = small_dummy
        big = big_dummy
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        small.next = big_dummy.next
        big.next = None
        return small_dummy.next


def create_node_list(nums):
    dummy = ListNode(-1)
    head = dummy
    for num in nums:
        node = ListNode(num)
        head.next = node
        head = head.next
    return dummy.next


def print_node_list(root: ListNode):
    while root:
        print(root.val)
        root = root.next


if __name__ == '__main__':
    s = Solution()
    head = [1, 4, 3, 2, 5, 2]
    x = 3
    root = create_node_list(head)
    print_node_list(root)
    print("=====" * 10)
    root = s.partition(root, x)
    print_node_list(root)
