class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def init_from_list(cls, l: list):
        if not l:
            return None
        length = len(l)
        nodes = [cls(i) if i is not None else None for i in l]
        for i in range(length):
            root = nodes[i]
            if root is None:
                continue
            l_index = 2 * i + 1
            r_index = 2 * i + 2
            if l_index < length:
                root.left = nodes[l_index]
            if r_index < length:
                root.right = nodes[r_index]
        return nodes[0]

    @classmethod
    def inorder(cls, root):
        if not root:
            return None
        cls.inorder(root.left)
        print(root.val)
        cls.inorder(root.right)


if __name__ == '__main__':
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
    root = TreeNode.init_from_list(root)
    TreeNode.inorder(root)
