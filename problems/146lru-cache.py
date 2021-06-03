"""
tag: 设计 链表

运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 

进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

 

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
0 <= key <= 3000
0 <= value <= 104
最多调用 3 * 104 次 get 和 put
"""


# python的实现用的是链表, 很强!
# from functools import lru_cache

# lru_cache


class Node:
    def __init__(self, key:int, value: int):
        self.next: Node or None = None
        self.prev: Node or None = None
        self.key:int = key
        self.value: int = value

    def __str__(self):
        return f'{self.key}__{self.value}'


class LRUCache:

    def __init__(self, capacity: int):
        self.bag = {}
        self.capacity: int = capacity
        self.first: Node or None = None
        self.last: Node or None = None
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.bag:
            node = self.bag[key]
            if node is self.first:
                return node.value
            node.prev.next = node.next
            if node is self.last:
                self.last = node.prev
            else:
                node.next.prev = node.prev
            self.first.prev = node
            node.prev = None
            node.next = self.first
            self.first = node
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.bag:
            node = self.bag[key]
            node.value = value
            self.get(key)
            return
        node = Node(key, value)
        if not self.first:
            self.first = node
            self.last = node
            self.bag[key] = node
            self.count += 1
            return
        node.next = self.first
        self.first.prev = node
        self.first = node
        if self.count == self.capacity:
            if self.last.prev:
                self.last.prev.next = None
            self.bag.pop(self.last.key)
            self.last = self.last.prev
            self.bag[key] = node
            return
        else:
            self.bag[key] = node
            self.count += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    lRUCache = LRUCache(2)
    print("put(1)")
    lRUCache.put(1, 1)
    print(lRUCache.first)
    print(lRUCache.last)
    print("-----")
    print("put(2)")
    lRUCache.put(2, 2)
    print(lRUCache.first)
    print(lRUCache.last)
    print("-----")
    print("get(1)")
    print(lRUCache.get(1))
    print(lRUCache.first)
    print(lRUCache.last)
    print("-----")
    print("put(3)")
    lRUCache.put(3, 3)
    print(lRUCache.first)
    print(lRUCache.last)
    print("-----")
    print("get(2)")
    print(lRUCache.get(2))
    lRUCache.put(4, 4)

    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))
