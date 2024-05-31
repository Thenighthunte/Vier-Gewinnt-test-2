import random
import time
import traceback
import sys
from config import *



def initialize_board():
    # initialize array with 0 values
    return [[0 for _ in range(N_COLS)] for _ in range(N_ROWS)]


def output_board(arr):
    # print board status in human-readable form
    logging.debug('')
    for row in range(N_ROWS-1, -1, -1):
        string = GREY + '| '
        for col in range(N_COLS):
            if arr[row][col] == 0:
                string += '  '
            elif arr[row][col] == 1:
                string += BLUE + 'X '
            elif arr[row][col] == 2:
                string += YELLOW + 'O '
            else:
                raise ValueError('Unknown value: ', arr[row][col])
        string += GREY + '| ' + str(row+1)
        logging.debug(string)
    logging.debug('└ ─ ─ ─ ─ ─ ─ ─ ┘')
    logging.debug('  0 1 2 3 4 5 6  ')


def output_active_player(player):
    # print currently active player
    token = BLUE + 'X' if player == PLAYER_1 else YELLOW + 'O'
    logging.debug(' akt. Spieler: ' + token)


def output_game_status(game_status):
    # print game status
    if game_status == PLAYER_1_WINS:
        logging.debug('Spieler 1 (X) gewinnt')
    elif game_status == PLAYER_2_WINS:
        logging.debug('Spieler 2 (O) gewinnt')
    elif game_status == DRAW:
        logging.debug('Unentschieden')
    elif game_status == GAME_NOT_FINISHED:
        logging.debug('Spiel noch nicht entschieden')
    else:
        raise ValueError('Unknown game status: ', game_status)
    logging.debug('')


def select_start_player():
    # randomly select starting player
    return random.randint(PLAYER_1, PLAYER_2)


def select_player(turn, start_player):
    # select player 1 or player 2 based on start player and turn number
    if turn % 2 == 0:
        return start_player
    else:
        return PLAYER_2 if start_player == PLAYER_1 else PLAYER_1


def is_valid_column(col):
    # check if selected column is present on the board and of type int
    if type(col) != int:
        logging.warning(RED + 'Selected column must be of type int, your type is ' + str(type(col)))
        return False
    elif col < 0 or col >= N_COLS:
        logging.warning(RED + 'Selected column value must be between 0 and ' + str(N_COLS-1) + ', yours is ' + str(col))
        return False
    else:
        return True


def column_is_full(arr, col):
    # return True if selected column is already full
    if arr[N_ROWS-1][col] == 0:
        return False
    else:
        return True


def select_column(arr, player, player_type):
    # first select column with specified player_type
    try:
        col = player_type(arr, player)
        if is_valid_column(col) and not column_is_full(arr, col):
            return col
        else:
            logging.warning(RED + 'Wrong column type and/or value, using random player instead: ' + str(col))
    except:
        logging.warning(RED + 'AI of player ' + str(player) + ' crashed!')
        traceback.print_exc()

    # after a wrong output or a crash use random player
    col = random_player(arr)
    return col


def human_player(arr, player=1):
    # wait for human input
    while True:
        try:
            time.sleep(0.1)
            col = int(input('Bitte Spalte eingeben: '))
            if is_valid_column(col) and not column_is_full(arr, col):
                return col
        except:
            continue


def random_player(arr, player=1):
    # AI that places tokens randomly
    while True:
        col = random.randint(0, N_COLS-1)
        if not column_is_full(arr, col):
            return col


def place_token(arr, col, player):
    # place token in lowermost position in the correct column
    for row in range(N_ROWS):
        if arr[row][col] == 0:
            arr[row][col] = player
            break
    return arr


def get_game_status(arr):
    # infer game status from current board
    victory_player = is_victory(arr)
    if victory_player == PLAYER_1:
        return PLAYER_1_WINS
    elif victory_player == PLAYER_2:
        return PLAYER_2_WINS
    elif is_draw(arr):
        return DRAW
    else:
        return GAME_NOT_FINISHED


def is_draw(arr):
    # check if at least one column is not yet full, then return False
    for col in range(N_COLS):
        if arr[N_ROWS-1][col] == 0:
            return False
    # otherwise return True
    return True


def is_victory(arr):
    # check if any player has four tokens in a row
    for c in range(N_COLS):
        for r in range(N_ROWS):
            # do not check empty cells
            if arr[r][c] == 0:
                continue
            # check for horizontal lines
            if c >= 3 and arr[r][c] == arr[r][c-1] == arr[r][c-2] == arr[r][c-3]:
                return arr[r][c]
            # check for vertical lines
            if r >= 3 and arr[r][c] == arr[r-1][c] == arr[r-2][c] == arr[r-3][c]:
                return arr[r][c]
            # check for diagonal lines (type 1)
            if c >= 3 and r >= 3 and arr[r][c] == arr[r-1][c-1] == arr[r-2][c-2] == arr[r-3][c-3]:
                return arr[r][c]
            # check for diagonal lines (type 2)
            if c <= 3 and r >= 3 and arr[r][c] == arr[r-1][c+1] == arr[r-2][c+2] == arr[r-3][c+3]:
                return arr[r][c]

