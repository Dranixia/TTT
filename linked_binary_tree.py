"""
Butynets' Danylo
Task 3 Lab 13 UCU
Python 3.8
"""


class BinaryTree:
    """
    Class to represent binary tree.
    """
    def __init__(self, root):
        """
        Initialize binary tree.
        """
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        """
        Make a left branch.
        :new_node: object
        :return: None
        """
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.left = self.left
            self.left = temp

    def insert_right(self, new_node):
        """
        Make a right branch.
        :new_node: object
        :return: None
        """
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.right = self.right
            self.right = temp

    def get_right(self):
        """
        Get a right branch.
        :return: BinaryTree
        """
        return self.right

    def get_left(self):
        """
        Get a left branch.
        :return: BinaryTree
        """
        return self.left

    def leaves(self):
        """
        Return list of the leaves.
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
