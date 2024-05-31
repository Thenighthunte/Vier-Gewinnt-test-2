"""                                # **** Test Version 1 *******
""" # # import copy
# # import numpy as np
# # from helper import *
# # EMPTY=0
# # def evaluate_window(window, player):
# #     """
# #     Evaluate the score of a window (four adjacent cells) for a given player.
# #     """
# #     score = 0
# #     opponent = 3 - player  # Switch player to get the opponent's ID

# #     if window.count(player) == 4:
# #         score += 100
# #     elif window.count(player) == 3 and window.count(EMPTY) == 1:
# #         score += 5
# #     elif window.count(player) == 2 and window.count(EMPTY) == 2:
# #         score += 2

# #     if window.count(opponent) == 3 and window.count(EMPTY) == 1:
# #         score -= 4

# #     return score

# # def score_position(board, player):
# #     """
# #     Score the entire board for a given player.
# #     """
# #     score = 0

# #     # Score center column
# #     center_array = [int(i) for i in list(board[:, N_COLS // 2])]
# #     center_count = center_array.count(player)
# #     score += center_count * 3

# #     # Score horizontal
# #     for r in range(N_ROWS):
# #         row_array = [int(i) for i in list(board[r, :])]
# #         for c in range(N_COLS - 3):
# #             window = row_array[c:c+4]
# #             score += evaluate_window(window, player)

# #     # Score vertical
# #     for c in range(N_COLS):
# #         col_array = [int(i) for i in list(board[:, c])]
# #         for r in range(N_ROWS - 3):
# #             window = col_array[r:r+4]
# #             score += evaluate_window(window, player)

# #     # Score positively sloped diagonal
# #     for r in range(N_ROWS - 3):
# #         for c in range(N_COLS - 3):
# #             window = [board[r+i][c+i] for i in range(4)]
# #             score += evaluate_window(window, player)

# #     # Score negatively sloped diagonal
# #     for r in range(N_ROWS - 3):
# #         for c in range(N_COLS - 3):
# #             window = [board[r+3-i][c+i] for i in range(4)]
# #             score += evaluate_window(window, player)

# #     return score
# # def get_next_empty_row(board, col):
# #     for row in range(N_ROWS):
# #         if board[row][col] == 0: # the cell is empty
# #             return row
# #     return -1 # the column is full
# # def drop_piece(board, row, col, player):
# #     board[row][col] = player
# # def ai(arr, player):
# #     """
# #     :param arr: current status of the board as type list[list[int]].
# #     The integers can either be 0 (cell empty), 1 (token of player 1) or 2 (token of player 2).
# #     :param player: Integer which is either 1 (turn of player 1) or 2 (turn of player 2).
# #     :return: Integer between 0 and 6 indicating in which row the next token shall be placed.
# #     """

# #     valid_moves = [col for col in range(N_COLS) if not column_is_full(arr, col)]
# #     best_move = -1
# #     best_score = float('-inf')

# #     for move in valid_moves:
# #         temp_board = copy.deepcopy(arr)
# #         row = get_next_empty_row(temp_board, move)
# #         drop_piece(temp_board, row, move, player)
# #         score = score_position(np.array(temp_board), player)
        
# #         if score > best_score:
# #             best_score = score
# #             best_move = move

# #     return best_move """ """

    

# **** Test Version 2 *******


# import copy
# import numpy as np
# from helper import *

# EMPTY = 0

# def evaluate_window(window, player):
#     score = 0
#     opponent = 3 - player

#     if window.count(player) == 4:
#         score += 100
#     elif window.count(player) == 3 and window.count(EMPTY) == 1:
#         score += 5
#     elif window.count(player) == 2 and window.count(EMPTY) == 2:
#         score += 2

#     if window.count(opponent) == 3 and window.count(EMPTY) == 1:
#         score -= 4

#     return score

# def winning_move(board, player):
#     """
#     Check if the current move is a winning move for the given player.
#     """
#     # Check horizontal locations for a win
#     for c in range(N_COLS - 3):
#         for r in range(N_ROWS):
#             if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
#                 return True

#     # Check vertical locations for a win
#     for r in range(N_ROWS - 3):
#         for c in range(N_COLS):
#             if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
#                 return True

#     # Check positively sloped diagonals
#     for r in range(N_ROWS - 3):
#         for c in range(N_COLS - 3):
#             if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
#                 return True

#     # Check negatively sloped diagonals
#     for r in range(N_ROWS - 3):
#         for c in range(3, N_COLS):
#             if board[r][c] == player and board[r+1][c-1] == player and board[r+2][c-2] == player and board[r+3][c-3] == player:
#                 return True

#     return False


# def get_next_empty_row(board, col):
#     for row in range(N_ROWS):
#         if board[row][col] == 0:
#             return row
#     return -1

# def drop_piece(board, row, col, player):
#     board[row][col] = player
# def get_valid_locations(board):
#     """
#     Get a list of valid column indices where a piece can be placed.
#     """
#     valid_locations = []
#     for col in range(N_COLS):
#         if not column_is_full(board, col):
#             valid_locations.append(col)
#     return valid_locations

# def is_terminal_node(board):
#     return winning_move(board, 1) or winning_move(board, 2) or len(get_valid_locations(board)) == 0

# def minimax(board, depth, alpha, beta, maximizing_player):
#     valid_moves = get_valid_locations(board)
#     is_terminal = is_terminal_node(board)

#     if depth == 0 or is_terminal:
#         if is_terminal:
#             if winning_move(board, 2):
#                 return (None, 100000000000000)  # AI wins
#             elif winning_move(board, 1):
#                 return (None, -100000000000000)  # Player wins
#             else:  # Game is over, no more valid moves
#                 return (None, 0)
#         else:  # Depth is zero
#             return (None, winning_move(board, 2))

#     if maximizing_player:
#         value = float('-inf')
#         column = np.random.choice(valid_moves)
#         for col in valid_moves:
#             row = get_next_empty_row(board, col)
#             temp_board = copy.deepcopy(board)
#             drop_piece(temp_board, row, col, 2)
#             new_score = minimax(temp_board, depth - 1, alpha, beta, False)[1]
#             if new_score > value:
#                 value = new_score
#                 column = col
#             alpha = max(alpha, value)
#             if alpha >= beta:
#                 break
#         return column, value
#     else:
#         value = float('inf')
#         column = np.random.choice(valid_moves)
#         for col in valid_moves:
#             row = get_next_empty_row(board, col)
#             temp_board = copy.deepcopy(board)
#             drop_piece(temp_board, row, col, 1)
#             new_score = minimax(temp_board, depth - 1, alpha, beta, True)[1]
#             if new_score < value:
#                 value = new_score
#                 column = col
#             beta = min(beta, value)
#             if alpha >= beta:
#                 break
#         return column, value

# def ai(arr, player):
#     column, _ = minimax(arr, 4, float('-inf'), float('inf'), True)  # Adjust the depth as needed
#     return column