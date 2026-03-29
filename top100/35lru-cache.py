"""146. LRU 缓存
中等
相关标签
premium lock icon
相关企业
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。



示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4


提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put

面试中遇到过这道题?
1/5
是
否
通过次数
1,077,835/1.9M
通过率
55.4%
相关标签
设计
哈希表
链表
双向链表
"""

from typing import Optional


class DlinkedNode:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev: Optional["DlinkedNode"] = None
        self.next: Optional["DlinkedNode"] = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()
        self.head = DlinkedNode(0, 0)
        self.tail = DlinkedNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: DlinkedNode):
        node.prev.next = node.next  # type: ignore
        node.next.prev = node.prev  # type: ignore

    def _add_node(self, node):
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def _move_to_tail(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_head(self) -> Optional[DlinkedNode]:
        if self.head.next == self.tail:
            return None
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self._move_to_tail(self.cache[key])
            return

        if len(self.cache) == self.cap:
            self._pop_head()
        node = DlinkedNode(key, value)
        self._add_node(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
