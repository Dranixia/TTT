from board import Board


def play():
    """
    Simulate Tic Tac Toe.
    :return: str
    """
    game = Board()
    while True:
        game.human()
        state = game.check_win("o")
        if state:
            return state
        game.computer()
        state = game.check_win("x")
        if state:
            return state


if __name__ == '__main__':
    end = play()
    if end == 'o':
        print('You won!')
    elif end == 'x':
        print('You lost!')
    else:
        print('Draw!')
