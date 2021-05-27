# -*- coding: utf-8 -*-
import attr


@attr.s(repr=False)
class Node:
    key = attr.ib(type=str)
    value = attr.ib()
    left = attr.ib(type='Node', default=None)
    right = attr.ib(type='Node', default=None)
    N = attr.ib(type=int, default=0)

    def __repr__(self):
        return 'Node(key={}, value={}, N={})'.format(self.key, self.value, self.N)


@attr.s
class BST:
    root = attr.ib(type=Node, default=None)

    def size(self):
        return self._size(self.root)

    def _size(self, node: Node):
        if node is None:
            return 0
        return node.N

    def get(self, key: str) -> any:
        return self._get(self.root, key)

    def _get(self, node: Node, key: str) -> any:
        if node is None:
            return None
        if node.key < key:
            return self._get(node.right, key)
        elif node.key > key:
            return self._get(node.left, key)
        return node.value

    def put(self, key: str, value: any) -> None:
        self.root = self._put(self.root, key, value)

    def _put(self, node: Node, key: str, value: any) -> Node:
        if node is None:
            node = Node(key, value)
        elif node.key > key:
            node.left = self._put(node.left, key, value)
        elif node.key < key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        node.N = self._size(node.left) + self._size(node.right) + 1
        return node

    def min(self):
        if not self.root:
            return None
        return self._min(self.root)

    def _min(self, node: Node):
        if node.left is None:
            return node.key
        else:
            return self._min(node.left)

    def max(self):
        if not self.root:
            return None
        return self._max(self.root)

    def _max(self, node: Node):
        if node.right is None:
            return node.key
        else:
            return self._max(node.right)

    def preorder(self):
        yield from self._preorder(self.root)

    def _preorder(self, node: Node):
        if node is None:
            return
        yield node
        yield from self._preorder(node.left)
        yield from self._preorder(node.right)

    def inorder(self):
        yield from self._inorder(self.root)

    def _inorder(self, node: Node):
        if node is None:
            return
        yield from self._inorder(node.left)
        yield node
        yield from self._inorder(node.right)

    def floor(self, key: str):
        """
        node.key <= key
        """
        n = self._floor(self.root, key)
        if n is not None:
            return n.key
        return None

    def _floor(self, node: Node, key: str) -> Node or None:
        if node is None:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self._floor(node.left, key)
        n = self._floor(node.right, key)
        if n is not None:
            return n.key
        return node

    def select(self, k: int):
        """
        有k个比我小的结点的结点
        排名为k的键（即树中正好有k个小于它的键）
        如果左子树中的结点数t大于k，那么我们就继续（递归地）在左子树中查找排名为 k 的键
        如果 t 等于 k，我们就返回根结点中的键
        如果 t 小于 k，我们就（递归地）在右子树中查找排名为（k-t-1）的键
        """
        return self._select(self.root, k)

    def _select(self, node: Node, k: int):
        if node is None:
            return None
        left_size = self._size(node.left)
        if left_size > k:
            return self._select(node.left, k)
        elif left_size < k:
            return self._select(node.right, k - left_size - 1)
        return node

    def rank(self, key: str):
        """
        返回key的结点的排名, [0, size())
        如果给定的键和根结点的键相等，我们返回左子树中的结点总数 t
        如果给定的键小于根结点，我们会返回该键在左子树中的排名（递归计算）
        如果给定的键大于根结点，我们会返回 t+1（根结点）加上它在右子树中的排名（递归计算）
        """
        return self._rank(self.root, key)

    def _rank(self, node: Node, key: str):
        if node is None:
            return 0
        if node.key > key:
            return self._rank(node.left, key)
        elif node.key < key:
            return 1 + self._size(node.left) + self._rank(node.right, key)
        else:
            return self._size(node.left)

    def delete_min(self):
        """
        不断深入根结点的左子树中直至遇见一个空链接，然后将指向该结点的链接指向该结点的右子树（只需要在递归调用中返回它的右链接即可）
        """
        self.root = self._delete_min(self.root)

    def _delete_min(self, node: Node):
        if node is None:
            return None
        if node.left:
            node.left = self._delete_min(node.left)
            node.N = self._size(node.left) + self._size(node.right) + 1
            return node
        else:
            return node.right

    def delete_max(self):
        self.root = self._delete_max(self.root)

    def _delete_max(self, node: Node):
        if node is None:
            return None
        if node.right:
            node.right = self._delete_max(node.right)
            node.N = self._size(node.left) + self._size(node.right) + 1
            return node
        else:
            return node.left

    def delete(self, key: str):
        """
        如果x有右子结点，它的后继结点就是其右子树的最小结点
        将指向即将被删除的结点的链接保存为 t
        将 x 指向它的后继结点 min(t.right)
        将 x 的右链接（原本指向一棵所有结点都大于 x.key 的二叉查找树）指向 deleteMin(t.right)，也就是在删除后所有结点仍然都大于 x.key 的子二叉查找树；
        将 x 的左链接（本为空）设为 t.left（其下所有的键都小于被删除的结点和它的后继结点）
        """
        self.root = self._delete(self.root, key)

    def _delete(self, node: Node, key: str):
        if node is None:
            return None
        if node.key > key:
            node.left = self._delete(node.left, key)
        elif node.key < key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            right_min: Node = self._min(node.right)
            right_min.right = self._delete_min(node.right)
            right_min.left = node.left
            node = right_min
        node.N = self._size(node.left) + self._size(node.right) + 1
        return node


if __name__ == '__main__':
    keys = "SEACRHMX"
    keys = list(keys)
    bst = BST()
    for value, key in enumerate(keys):
        bst.put(key, value)

    for node in bst.inorder():
        print(node)
    print("======" * 10)
    print("select")
    print(bst.select(0))

    print("======" * 10)
    print("rank")
    print(bst.rank("A"))

    print("======" * 10)
    print("delete_min")
    for _ in range(8):
        print(bst.select(0), bst.size())
        bst.delete_min()

    for value, key in enumerate(keys):
        bst.put(key, value)

    print("======" * 10)
    print("delete_max")
    for _ in range(8):
        print(bst.select(7 - _), bst.size())
        bst.delete_max()

    print(bst.select(0))

    for value, key in enumerate(keys):
        bst.put(key, value)

    print("======" * 10)
    print("delete")
