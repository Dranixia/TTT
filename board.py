"""
Butynets' Danylo
Task 3 Lab 13 UCU
Python 3.8
"""


from linked_binary_tree import BinaryTree
from copy import deepcopy
from random import choice
from TTT.tree_but_not_binary import Tree


class Board:
    """
    Class to represent board and all its processes.
    """
    def __init__(self):
        """
        Initialize a board.
        """
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.prev = None

    def check_win(self, sign):
        """
        Check the situation in game.
        :param sign: str
        :return: str or None
        """
        x = self.board
        for i in range(3):
            if x[i][0] == x[i][1] == x[i][2] == sign:
                return sign
        for i in range(3):
            if x[0][i] == x[1][i] == x[2][i] == sign:
                return sign

        if x[0][0] == x[1][1] == x[2][2] == sign:
            return sign

        if x[2][0] == x[1][1] == x[0][2] == sign:
            return sign

        if not self.available():
            return "Draw"

    def __str__(self):
        """
        Return string to represent current situation on board.
        :return: str
        """
        res = ""
        for i in self.board:
            res += str(i) + "\n"
        return res

    def available(self):
        """
        Return dictionary of available positions.
        :return: dict
        """
        dct = dict()
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 0:
                    if dct.keys():
                        key = max(list(dct.keys())) + 1
                    else:
                        key = 1
                    dct[key] = (x, y)
        return dct

    def bin_tree(self):
        """
        Calculate best move for computer out of 2 random ones.
        :return: Board
        """
        tree = BinaryTree(self.board)

        def recursion(board: Board, tree: BinaryTree):
            possible = board.available()
            if len(possible) == 1:
                board1 = deepcopy(board)
                if self.prev == "x":
                    board1.board[possible[1][0]][possible[1][1]] = "o"
                else:
                    board1.board[possible[1][0]][possible[1][1]] = "x"
                tree.insert_right(board1)

            else:
                x = choice([i for i in possible.keys()])
                new_move1 = possible[x]
                del possible[x]
                new_move2 = possible[choice([i for i in possible.keys()])]
                board1 = deepcopy(board)
                board2 = deepcopy(board)
                if self.prev == "x":
                    next = "o"
                    self.prev = "o"
                else:
                    next = "x"
                    self.prev = "x"
                board1.board[new_move1[0]][new_move1[1]] = next
                board2.board[new_move2[0]][new_move2[1]] = next
                tree.insert_left(board1)
                tree.insert_right(board2)
                recursion(board1, tree.get_left())
                recursion(board2, tree.get_right())
        recursion(self, tree)
        left_tree_points = self.points(tree.left.leaves())
        right_tree_points = self.points(tree.right.leaves())

        if left_tree_points > right_tree_points:
            return tree.left.key
        else:
            return tree.right.key

    def computer(self):
        """
        Process computer's turn.
        :return: None
        """
        self.board = self.bin_tree().board
        print("\nComputer's turn:")
        print(self)

    def human(self):
        """
        Process players turn in game.
        :return: None
        """
        turns = self.available()
        print("Possible moves: " + str(turns))
        move = int(input("Choose a position: "))
        while move not in turns.keys():
            move = int(input("Wrong. Choose a position: "))
        self.board[turns[move][0]][turns[move][1]] = "o"
        self.prev = "o"
        print("Your turn: ")
        print(self)

    @staticmethod
    def points(lst):
        """
        Count points depending on the results of the game,
        finished with such boards.
        :param lst: list
        :return: int
        """
        res = 0
        for i in lst:
            if i.check_win("x") == "x":
                res += 1
            elif i.check_win("o") == "o":
                res -= 1
        return res
