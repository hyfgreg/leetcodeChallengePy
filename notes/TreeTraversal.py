from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_recursive(root: TreeNode):
    if not root:
        return
    print(root.val)
    preorder_recursive(root.left)
    preorder_recursive(root.right)


def preorder_iteration(root: TreeNode):
    if not root:
        return
    stack = list()
    node = root
    while stack or root:
        while node:
            print(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right


def inorder_recursive(root: TreeNode):
    if not root:
        return None
    inorder_recursive(root.left)
    print(root.val)
    inorder_recursive(root.right)


def inorder_iteration(root: TreeNode):
    if not root:
        return None
    stack = list()
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.val)
        node = node.right


def postorder_recursive(root: TreeNode):
    if not root:
        return None
    postorder_recursive(root.left)
    postorder_recursive(root.right)
    print(root.val)


def postorder_iteration(root: TreeNode):
    if not root:
        return []
    stack = []
    node = root
    prev = None
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if not node.right or node.right == prev:
            print(node.val)
            prev = node
            node = None
        else:
            stack.append(node)
            node = node.right


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    postorder_iteration(root)
