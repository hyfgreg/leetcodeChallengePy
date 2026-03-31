"""208. 实现 Trie (前缀树)
中等
相关标签
premium lock icon
相关企业
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

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

面试中遇到过这道题?
1/5
是
否
通过次数
558,091/767.9K
通过率
72.7%
相关标签
设计
字典树
哈希表
字符串
"""


class TrieNode:
    def __init__(self) -> None:
        self.chhidren = dict()
        self.is_last = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.chhidren:
                node.chhidren[char] = TrieNode()
            node = node.chhidren[char]
        node.is_last = True

    def search(self, word: str) -> bool:
        if not word:
            return False
        node = self.root
        for char in word:
            if char not in node.chhidren:
                return False
            node = node.chhidren[char]
        return node.is_last

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False
        node = self.root
        for char in prefix:
            if char not in node.chhidren:
                return False
            node = node.chhidren[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
