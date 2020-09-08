# Connect4 Add Animation


import numpy as np
import pygame
import sys
import os
import time

board_rows = 6
board_cols = 7
blue = (0, 0, 255)
black = (50, 50, 50)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)


def create_board():
    empty_board = np.zeros((board_rows, board_cols))
    return empty_board


def drop_piece(board, col, turn):
    for row in range(5, -1, -1):
        col_pos = col - 1
        check_col_val = board[row][col_pos]
        if int(check_col_val) == 0:
            board[row][col_pos] = turn + 1
            print(f"[ROW: {row + 1} : COL: {col_pos + 1}]")
            #  print(board)
            os.system("afplay drop.wav&")
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
                #  print(f"Winner: " + str(turn + 1))
                game_over = True
                return
    # Check vertical Locations
    for c in range(col_count):
        # winner = 0
        for r in range(row_count - 3):
            winner = board[r][c] * board[r + 1][c] * board[r + 2][c] * board[r + 3][c]
            if winner in (1, 16):
                #  print(f"Winner: " + str(turn + 1))
                game_over = True
                return
    # Check Diagonal Locations Left to right - top down
    for c in range(col_count - 3):
        # winner = 0
        for r in range(row_count - 3):
            winner = board[r][c] * board[r + 1][c + 1] * board[r + 2][c + 2] * board[r + 3][c + 3]
            if winner in (1, 16):
                #  print(f"Winner: " + str(turn + 1))
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
                #  print(f"Winner: " + str(turn + 1))
                game_over = True
                return


def draw_board(board):
    for c in range(len(board[0][:])):
        for r in range(len(board)):
            pygame.draw.rect(screen, blue, (c * square_size, (r * square_size) + square_size, square_size, square_size))
            if int(board[r][c]) == 1:
                fill_color = red
            elif int(board[r][c]) == 2:
                fill_color = yellow
            else:
                fill_color = black
            pygame.draw.circle(screen, fill_color, (c * square_size + (square_size / 2),
                                               (r * square_size) + square_size + (square_size / 2)), radius)


board = create_board()
# board[0, 4] = 3
# print(board)
game_over = False
turn = 0  # Player 0 or 1
next_player = True

pygame.init()

square_size = 100

width = len(board[0][:]) * square_size
height = (len(board) + 1) * square_size  # + 1 for top areas above game

size = (width, height)
radius = int(square_size / 2 - 5)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Red Player - Your Turn')

draw_board(board)
pygame.display.update()

#  myfont = pygame.font.SysFont("monospace", 75)
myfont = pygame.font.SysFont("brushscriptttf", 75)

# winning_move(board)

wait_clear = False

time_music_started = 0

while not game_over:

    if not wait_clear:
        if time_music_started == 0:
            time_music_started = time.time()
            os.system("afplay alienxxx.wav&")
            sec_passed_last = 0
        else:
            time_music_current = time.time()
            time_passed = time_music_current - time_music_started
            sec_passed = int(time_passed)
            if sec_passed > sec_passed_last:
                print(f"{int(time_passed)}")
                sec_passed_last = sec_passed
            if time_passed > 24:
                time_music_started = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.system("killall afplay")
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            posx = event.pos[0]
            pygame.draw.rect(screen, black, (0, 0, width, square_size))
            if not wait_clear:
                if turn ==  0 :
                    pygame.draw.circle(screen, red, (posx, int(square_size/2)), radius)
                else:
                    pygame.draw.circle(screen, yellow, (posx, int(square_size / 2)), radius)
                pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == 32 and wait_clear:
                pygame.draw.rect(screen, black, (0, 0, width, square_size))
                board = create_board()
                i_col = 0
                wait_clear = False
                if turn == 0:
                    turn = 1
                    pygame.display.set_caption('Yellow Player - Your Turn')
                else:
                    pygame.display.set_caption('Red Player - Your Turn')
                    turn = 0
                is_valid_loc_check = is_valid_loc_and_drop(board, i_col, turn)
                draw_board(board)
                pygame.display.update()
                winning_move(board)
                if turn == 0:
                    pygame.draw.circle(screen, red, (posx, int(square_size / 2)), radius)
                else:
                    pygame.draw.circle(screen, yellow, (posx, int(square_size / 2)), radius)
                pygame.display.update()
                time_music_started = 0.0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] < square_size * (len(board) + 1):
                # print(event.pos)
                # print(f"col:{int(event.pos[0]/square_size)}")
                i_col = int(event.pos[0]/square_size) + 1
            # Change Player
                if not wait_clear:
                    is_valid_loc_check = is_valid_loc_and_drop(board, i_col, turn)
                    draw_board(board)
                    pygame.display.update()
                    winning_move(board)

                if not wait_clear and is_valid_loc_check:
                    if not game_over:
                        if turn == 0:
                            turn = 1
                            pygame.display.set_caption('Yellow Player - Your Turn')
                        else:
                            pygame.display.set_caption('Red Player - Your Turn')
                            turn = 0
                        if turn == 0:
                            pygame.draw.circle(screen, red, (posx, int(square_size / 2)), radius)
                        else:
                            pygame.draw.circle(screen, yellow, (posx, int(square_size / 2)), radius)
                        pygame.display.update()
                    else:
                        pygame.draw.rect(screen, black, (0, 0, width, square_size))
                        if turn == 0:
                            pygame.display.set_caption('Red Player WINS!!! Press [SPACE BAR] to play again!')
                            label = myfont.render("Red Player Wins!!!", 1, red)
                            screen.blit(label, (40, 10))
                        else:
                            pygame.display.set_caption('Yellow Player WINS!!! Press [SPACE BAR] to play again!')
                            pygame.display.set_caption('Red Player WINS!!! Press [SPACE BAR] to play again!')
                            label = myfont.render("Yellow Player Wins!!!", 1, yellow)
                            screen.blit(label, (40, 10))


                        print(f"The Winner is Player {turn + 1}!")
                        time_music_started
                        os.system("killall afplay")
                        os.system("afplay win.mp3&")
                        draw_board(board)
                        pygame.display.update()
                        winning_move(board)

                        #input("")
                        game_over = False
                        wait_clear = True