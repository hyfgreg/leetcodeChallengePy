"""
tag: 链表 双指针

给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

 

示例 1：



输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：



输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：



输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
 

提示：

链表中节点的数目范围是 [0, 104]
-105 <= Node.val <= 105
pos 为 -1 或者链表中的一个 有效索引 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

1. hash表，保存运行过的每一个node
2. 快慢指针，一个每次走两步，一个每次走一步，快的追上了慢的，说明肯定有环
3. 自己想的，反转链表，有环的链表一定会反转到起点
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list_node(root: ListNode):
    ret = []
    while root:
        # print(root)
        ret.append(root.val)
        root = root.next
    print(ret)


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        prev = None
        root = head
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            if curr is root:
                return True
        return False


if __name__ == '__main__':

    nums = [3, 2, 0, -4]
    # l2 = [1, 3, 4]
    next = None
    headA = None
    tail = None
    for num in nums[::-1]:
        headA = ListNode(num)
        if tail is None:
            tail = headA
        headA.next = next
        next = headA
    print_list_node(headA)
    tail.next = headA.next.next
    s = Solution()
    print(s.hasCycle(headA))

    root = ListNode(1)
    b = ListNode(2)
    root.next = b
    b.next = root
    print(s.hasCycle(root))

    root =  ListNode(1)
    b = ListNode(2)
    root.next = b
    print(s.hasCycle(root))
