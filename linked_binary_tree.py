class BinaryTree:
    """ Class for binary tree representation. """

    def __init__(self, root):
        """
        (BinaryTree) -> None
        Initialize binary tree.
        """
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        """
        (BinaryTree) -> NoneType
        Insert new node to the left parameter.
        """
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.left = self.left
            self.left = temp

    def insert_right(self, new_node):
        """
        (BinaryTree) -> NoneType
        Insert new node to the right parameter.
        """
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.right = self.right
            self.right = temp

    def get_right(self):
        """
        (BinaryTree) -> obj/NoneType
        Return value of the right parameter.
        """
        return self.right

    def get_left(self):
        """
        (BinaryTree) -> obj/NoneType
        Return value of the left parameter.
        """
        return self.left

    def leaves(self):
        """
        (BinaryTree) -> lst
        Return list of the leaves of the tree.
        """
        lst = []

        def recursion(tree, lst):
            if tree.left is None and tree.right is None:
                lst.append(tree.key)
            else:
                if tree.left is not None:
                    recursion(tree.left, lst)
                if tree.right is not None:
                    recursion(tree.right, lst)

        recursion(self, lst)
        return lst
