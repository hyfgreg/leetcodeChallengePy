"""
208. 实现 Trie (前缀树)
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。


示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True


提示：

1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次
通过次数145,737提交次数203,314

tag: 设计 字典树 哈希表 字符串
背诵 设计题可以统一看看
"""
from typing import List, Optional


class Node:
    def __init__(self):
        self.val = False
        self.next_nodes: List[Optional[Node]] = [None for _ in range(26)]


class Trie:

    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, word: str) -> None:
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node: Node, word: str, i: int) -> Node:
        if node is None:
            node = Node()
        if i == len(word):
            node.val = True
            return node
        c = word[i]
        c_index = self.ch_to_index(c)
        node.next_nodes[c_index] = self._insert(node.next_nodes[c_index], word, i + 1)
        return node

    def search(self, word: str) -> bool:
        node = self._search(self.root, word, 0)
        if node is None:
            return False
        return node.val

    def _search(self, node: Optional[Node], word: str, i: int) -> Optional[Node]:
        if node is None:
            return node
        if i == len(word):
            return node
        c = word[i]
        c_index = self.ch_to_index(c)  # ord('a') == 97
        return self._search(node.next_nodes[c_index], word, i + 1)

    def startsWith(self, prefix: str) -> bool:
        node = self._search(self.root, prefix, 0)
        return bool(node)

    def ch_to_index(self, ch):
        return ord(ch) - 97

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
