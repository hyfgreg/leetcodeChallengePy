"""
1. 链表，奇数位置按序增长，偶数位置按序递减，如何能实现链表从小到大？（2020.10 字节跳动-后端）[2]
2. 奇偶生序倒序链表的重新排序组合，例如：18365472（2020.08 字节跳动-后端）[3]
3. 1->4->3->2->5 给定一个链表奇数部分递增，偶数部分递减，要求在O(n)时间复杂度内将链表变成递增，5分钟左右（2020.07 字节跳动-测试开发）[4]
4. 奇数位升序偶数位降序的链表要求时间O(n)空间O(1)的排序？(2020.07 字节跳动-后端)[5]
"""


class ListNode:
    def __init__(self, val: int, next: 'ListNode' or None = None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, root: ListNode) -> ListNode:
        """
        1. 拆分链表
        2. 反转偶数链表
        3. 合并链表
        """
        if not root or not root.next:
            return root
        # 1. 拆分奇偶链表
        odd_pre = ListNode(-1, None)
        odd_dummy = odd_pre
        even_pre = ListNode(-1, None)
        even_dummy = even_pre
        i = 1
        while root:
            if i % 2 == 1:
                odd_dummy.next = root
                odd_dummy = odd_dummy.next
            else:
                even_dummy.next = root
                even_dummy = even_dummy.next
            i += 1
            root = root.next

        # 这里很关键，把最后一个节点的next设置为None
        odd_dummy.next = None
        even_dummy.next = None
        # print_list_node(odd_pre.next)
        # print_list_node(even_pre.next)

        # 2. 反转偶数链表
        prev = None
        curr = even_pre.next
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        # 3. 合并升序链表
        dummy = ListNode(-1, None)
        curr = dummy
        odd = odd_pre.next
        even = prev
        # print("fuck")
        # print_list_node(odd)
        # print_list_node(even)
        while odd and even:
            if odd.val < even.val:
                curr.next = odd
                odd = odd.next
            else:
                curr.next = even
                even = even.next
            curr = curr.next
        if odd:
            curr.next = odd
        if even:
            curr.next = even
        return dummy.next


def print_list_node(root: ListNode):
    ret = []
    while root:
        # print(root)
        ret.append(root.val)
        root = root.next
    print(ret)


if __name__ == '__main__':
    root = ListNode(1, ListNode(8, ListNode(3, ListNode(6, ListNode(5, ListNode(4, ListNode(7, ListNode(2, None))))))))
    print_list_node(root)
    s = Solution()
    node = s.solve(root)
    print_list_node(node)
