import logging

# print output (uncomment to display board state)
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# type of player 1/2, can be either "human", "random" or "ai"
PLAYER_1_TYPE = 'ai'
PLAYER_2_TYPE = 'ai'

# total number of games played for evaluation
N_GAMES_PLAYED = 5

# number of rows/columns of the board
N_ROWS = 6
N_COLS = 7

# ID of player 1/2
PLAYER_1 = 1
PLAYER_2 = 2

# status flags for the game outcome
GAME_NOT_FINISHED = 0
PLAYER_1_WINS = PLAYER_1
PLAYER_2_WINS = PLAYER_2
DRAW = 3

# colors for logging output
GREY = '\x1b[38;21m'
BLUE = '\x1b[38;5;39m'
YELLOW = '\x1b[38;5;226m'
RED = '\x1b[38;5;196m'