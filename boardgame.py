
def initialize_board(size = 10):
    board = []
    for i in range(size):
        b=0
        board.append(list(range(0+size*(size-i-1), size+size*(size-i-1))))
    return board

board = initialize_board()

for row in board:
    print(row)
