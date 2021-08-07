"""
142. 环形链表 II
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？


示例 1：



输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：



输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：



输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。


提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
通过次数265,981提交次数483,293

tag: 哈希 链表 双指针
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"{self.val}"

    def __repr__(self):
        return self.__str__()


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        return self.doublePointer(head)

    def doublePointer(self, head: ListNode) -> ListNode:
        if not head:
            return head
        s = head
        f = head
        while True:
            if not s:
                return False
            s = s.next
            f = f.next
            if not f:
                return False
            f = f.next
            if s == f:
                f = head
                while not f == s:
                    f = f.next
                    s = s.next
                return f

    def hashTable(self, head: ListNode) -> ListNode:
        if not head:
            return head
        record = set()
        node = head
        while node:
            if id(node) in record:
                return node
            record.add(id(node))
            node = node.next
        return None


if __name__ == '__main__':
    # first = ListNode(3)
    # second = ListNode(2)
    # third = ListNode(0)
    # fourth = ListNode(-4)
    # first.next = second
    # second.next = third
    # third.next = fourth
    # fourth.next = second
    first = ListNode(1)
    first.next = first
    s = Solution()
    print(s.detectCycle(first))