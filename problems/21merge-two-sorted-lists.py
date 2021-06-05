"""
tag: 链表 递归

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]


提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
通过次数585,043提交次数885,315

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

归并排序？？？
还有个递归版本的，l1<l2，l1.next = merge(l1.next, l2) 反之同理

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list_node(root: ListNode):
    ret = []
    while root:
        # print(root)
        ret.append(root.val)
        root = root.next
    print(ret)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        root = None
        node = None
        while l1 or l2:
            if l1 is None:
                node.next = l2
                break
            elif l2 is None:
                node.next = l1
                break
            else:
                if l1.val < l2.val:
                    if root is None:
                        root = l1
                        node = l1
                    else:
                        node.next = l1
                        node = node.next
                    l1 = l1.next
                else:
                    if root is None:
                        root = l2
                        node = l2
                    else:
                        node.next = l2
                        node = node.next
                    l2 = l2.next
        return root


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    next = None
    headA = None
    for num in l1[::-1]:
        headA = ListNode(num)
        headA.next = next
        next = headA
    print_list_node(headA)

    next = None
    headB = None
    for num in l2[::-1]:
        headB = ListNode(num)
        headB.next = next
        next = headB
    print_list_node(headB)

    s = Solution()
    print_list_node(s.mergeTwoLists(headA, headB))
