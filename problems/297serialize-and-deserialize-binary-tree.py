"""
297. 二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。



示例 1：


输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：

输入：root = [1,2]
输出：[1,2]


提示：

树中结点数在范围 [0, 104] 内
-1000 <= Node.val <= 1000
通过次数102,367提交次数183,147

tag: 树 深度优先搜索 广度优先搜索 设计 字符串 二叉树
"""

# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null'
        q = deque()
        q.appendleft(root)
        ret = []
        valid = True
        while q and valid:
            sz = len(q)
            valid = False
            for _ in range(sz):
                node = q.pop()
                if node is not None:
                    ret.append(str(node.val))
                else:
                    ret.append("null")
                if node:
                    if node.left:
                        valid = True
                    q.appendleft(node.left)
                    if node.right:
                        valid = True
                    q.appendleft(node.right)
        return ','.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = [int(i) if i != 'null' else None for i in data.split(',')]
        nodes = [TreeNode(i) if i is not None else None for i in data]
        q = deque()
        if nodes[0] is not None:
            q.appendleft(nodes[0])
        index = 0
        while q and index < len(nodes):
            sz = len(q)
            for _ in range(sz):
                root = q.pop()
                index += 1
                if index == len(nodes):
                    break
                if nodes[index] is not None:
                    root.left = nodes[index]
                    q.appendleft(nodes[index])
                index += 1
                if index == len(nodes):
                    break
                if nodes[index] is not None:
                    root.right = nodes[index]
                    q.appendleft(nodes[index])
        return nodes[0]

    # def _deserialize(self, nodes, start, count):
    #     pass


def print_tree(root: TreeNode):
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == '__main__':
    codec = Codec()
    # data = "1,2,3,null,null,null,4,5"
    # root = codec.deserialize(data)
    # print_tree(root)
    data = "1,2,3,null,4,5,6,7,8,null,9,null,10"
    print(data)
    root = codec.deserialize(data)
    print(codec.serialize(root))
