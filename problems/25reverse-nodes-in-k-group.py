"""
tag: 链表

给你一个链表，每  k  个节点一组进行翻转，请你返回翻转后的链表。

k  是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是  k  的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
  

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

示例 2：
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]

示例 3：
输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]

示例 4：
输入：head = [1], k = 1
输出：[1]

提示：

列表中节点的数量在范围 sz 内
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "Node({})".format(self.val)


def print_list_node(root: ListNode):
    ret = []
    while root:
        # print(root)
        ret.append(root.val)
        root = root.next
    print(ret)


class Solution:
    def __init__(self):
        self.k = 0

    def reverseKGroup(self, head: ListNode or None, k: int) -> ListNode:
        self.k = k
        return self._reverseKGroup(head, k)[0]

    def _reverseKGroup(self, head: ListNode or None, k: int) -> Tuple[ListNode or None, int, ListNode or None]:
        # print("deal", head, k)
        if k == 1:
            if head is None or head.next is None:
                return head, k - 1, None
            else:
                return head, k - 1, self._reverseKGroup(head.next, self.k)[0]
        else:
            if head is None or head.next is None:
                # print("wuwuwu")
                return head, k - 1, head
        new_head, node_left, new_next = self._reverseKGroup(head.next, k - 1)
        if node_left > 0:
            # print('haha')
            return head, node_left, head
        head.next.next = head
        head.next = None
        if self.k == k:
            # print("head", head, "new_next", new_next, k)
            head.next = new_next
        return new_head, node_left, new_next


if __name__ == '__main__':
    root = ListNode(0)
    node = root
    for i in range(1, 6):
        new_node = ListNode(i)
        node.next = new_node
        node = new_node
    print_list_node(root)
    s = Solution()
    root = s.reverseKGroup(root, 6)
    print("done")
    print_list_node(root)
