# Set up Conect4 and play on Console


import numpy as np


def create_board():
    empty_board = np.zeros((6, 7))
    return empty_board


def drop_piece(board, col, turn):
    for row in range(5, -1, -1):
        col_pos = col - 1
        check_col_val = board[row][col_pos]
        if int(check_col_val) == 0:
            board[row][col_pos] = turn + 1
            print(f"[ROW: {row} : COL: {col_pos}]")
            print(board)
            return True


def is_valid_loc_and_drop(board, col, turn) -> object:
    top0 = False
    col_y = col - 1
    top_col = board[0, col_y]
    #
    #  Another way to check is: top0 = board[0, col_y] == 0 --> Returned True or False
    #
    if int(top_col) == 0 and col_y != -1:
        top0 = True
        drop_piece(board, col, turn)
#    print(top_col)
    return top0


def get_next_open_row():
    pass


board = create_board()
# board[0, 4] = 3
print(board)
game_over = False
turn = 0  # Player 0 or 1
next_player = True

while not game_over:
    i_col = 0
    col = "0"
    is_valid_loc_check = is_valid_loc_and_drop(board, i_col, turn)
    while not is_valid_loc_check or i_col == 0:
        if not is_valid_loc_check and not next_player:
            print("No Spot Left, Please make another choice...")
            col = "0"
            i_col = 0
        while int(col) not in [1, 2, 3, 4, 5, 6, 7]:
            col = input(f"Player {turn + 1} , Make your selection (1-7): ")
            while col.isalpha() or not col.isdecimal():
                col = input(f"Player {turn + 1}_, Make your selection(1-7): ")
        i_col = int(col)
        print(f"[Selection Player {turn + 1}]: {col}")
        is_valid_loc_check = is_valid_loc_and_drop(board, i_col, turn)
        next_player = is_valid_loc_check

    pass

# Change Player
    if turn == 0:
        turn = 1
    else:
        turn = 0
