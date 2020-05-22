class Tree:
    def __init__(self, root):
        self.key = root
        self.siblings = list()

    def add_sibling(self, value):
        self.siblings.append(Tree(value))

    def leaves(self):
        """
        (BinaryTree) -> lst
        Return list of the leaves of the tree.
        """
        lst = []
        def recursion(tree, lst):
            if not tree.siblings:
                lst.append(tree)
            else:
                for sib in self.siblings:
                    recursion(sib, lst)
        recursion(self, lst)
        return lst
