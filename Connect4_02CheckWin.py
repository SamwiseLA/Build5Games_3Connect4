# Connect 4 Winner


import numpy as np

board_rows = 6
board_cols = 7


def create_board():
    empty_board = np.zeros((board_rows, board_cols))
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


def winning_move(board):
    global game_over
    row_count = len(board)
    col_count = len(board[0][:])
    #  print(f"Rs:{row_count}: Cs:{col_count}")
    # Check horizontal Locations
    for c in range(col_count - 3):
        # winner = 0
        for r in range(row_count):
            winner = board[r][c] * board[r][c + 1] * board[r][c + 2] * board[r][c + 3]
            if winner in (1, 16):
                print(f"Winner: " + str(turn + 1))
                game_over = True
                return
    # Check vertical Locations
    for c in range(col_count):
        # winner = 0
        for r in range(row_count - 3):
            winner = board[r][c] * board[r + 1][c] * board[r + 2][c] * board[r + 3][c]
            if winner in (1, 16):
                print(f"Winner: " + str(turn + 1))
                game_over = True
                return
    # Check Diagonal Locations Left to right - top down
    for c in range(col_count - 3):
        # winner = 0
        for r in range(row_count - 3):
            winner = board[r][c] * board[r + 1][c + 1] * board[r + 2][c + 2] * board[r + 3][c + 3]
            if winner in (1, 16):
                print(f"Winner: " + str(turn + 1))
                game_over = True
                return
    # Check Diagonal Locations Left to right - bottom up
    for c in range(col_count - 3):
        # winner = 0
        for r in range(3, row_count):
            '''
            Commented Code to Examine Values
            r1 = r
            r2 = r - 1       
            r3 = r - 2
            r4 = r - 3
            c1 = c
            c2 = c + 1
            c3 = c + 2
            c4 = c + 3
            '''
            winner = board[r][c] * board[r - 1][c + 1] * board[r - 2][c + 2] * board[r - 3][c + 3]
            if winner in (1, 16):
                print(f"Winner: " + str(turn + 1))
                game_over = True
                return


board = create_board()
# board[0, 4] = 3
print(board)
game_over = False
turn = 0  # Player 0 or 1
next_player = True

# winning_move(board)


while not game_over:
    i_col = 0
    col = "0"
    is_valid_loc_check = is_valid_loc_and_drop(board, i_col, turn)
    while (not is_valid_loc_check or i_col == 0) and not game_over:
        if not is_valid_loc_check and not next_player:
            print("No Spot Left, Please make another choice...")
            col = "0"
            i_col = 0
        while int(col) not in [1, 2, 3, 4, 5, 6, 7]:
            col = input(f"Player {turn + 1} , Make your selection (1-7): ")
            while col.isalpha() or not col.isdecimal():
                col = input(f"Player {turn + 1}_, Make your selection(1-7): ")
        i_col = int(col)
        #  print(f"[Selection Player {turn + 1}]: {col}")
        is_valid_loc_check = is_valid_loc_and_drop(board, i_col, turn)
        next_player = is_valid_loc_check

    winning_move(board)
    pass

# Change Player
    if not game_over:
        if turn == 0:
            turn = 1
        else:
            turn = 0
    else:
        print(f"The Winner is Player {turn + 1}!")
