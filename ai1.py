import copy
import numpy as np  
from helper import *
import time


EMPTY = 0

def evaluate_window(window, player):
    """
    Bewertet den Punktestand eines Fensters (vier aufeinanderfolgende Zellen) für einen bestimmten Spieler.
    """
    score = 0
    opponent = 3 - player  # Spieler-ID umschalten, um die ID des Gegners zu erhalten

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opponent) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def score_position(arr, player):
    """
    Bewertet das gesamte Spielfeld für einen bestimmten Spieler.
    """
    score = 0

    # Bewertung der Mittelspalte
    center_array = [int(i) for i in list(arr[:, N_COLS // 2])]
    center_count = center_array.count(player)
    score += center_count * 3

    # Bewertung horizontal, vertikal und diagonal
    for r in range(N_ROWS):
        row_array = [int(i) for i in list(arr[r, :])]
        for c in range(N_COLS - 3):
            window = row_array[c:c+4]
            score += evaluate_window(window, player)

    for c in range(N_COLS):
        col_array = [int(i) for i in list(arr[:, c])]
        for r in range(N_ROWS - 3):
            window = col_array[r:r+4]
            score += evaluate_window(window, player)

    for r in range(N_ROWS - 3):
        for c in range(N_COLS - 3):
            # Bewertung positiv geneigte Diagonale
            window = [arr[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, player)

            # Bewertung negativ geneigter Diagonale
            window = [arr[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window, player)

    return score

def get_next_empty_row(arr, col):
    """
    Gibt die nächste leere Reihe in einer Spalte zurück.
    """
    for row in range(N_ROWS):
        if arr[row][col] == 0:
            return row
    return -1  # Die Spalte ist voll

def drop_piece(arr, row, col, player):
    """
    Setzt einen Spielstein in das Spielfeld.
    """
    arr[row][col] = player

def is_winner(arr):
    """
    Überprüft, ob ein Spieler gewonnen hat.
    """
    # Überprüfung auf Gewinn in horizontaler, vertikaler und diagonaler Richtung
    for r in range(len(arr)):
        for c in range(len(arr[0]) - 3):
            if arr[r][c] == arr[r][c + 1] == arr[r][c + 2] == arr[r][c + 3] and arr[r][c] != EMPTY:
                return True

    for c in range(len(arr[0])):
        for r in range(len(arr) - 3):
            if arr[r][c] == arr[r + 1][c] == arr[r + 2][c] == arr[r + 3][c] and arr[r][c] != EMPTY:
                return True

    for r in range(len(arr) - 3):
        for c in range(len(arr[0]) - 3):
            # Überprüfung auf Gewinn in positiv geneigter Diagonalrichtung
            if arr[r][c] == arr[r + 1][c + 1] == arr[r + 2][c + 2] == arr[r + 3][c + 3] and arr[r][c] != EMPTY:
                return True

            # Überprüfung auf Gewinn in negativ geneigter Diagonalrichtung
            if arr[r][c + 3] == arr[r + 1][c + 2] == arr[r + 2][c + 1] == arr[r + 3][c] and arr[r][c + 3] != EMPTY:
                return True

    return False

def is_winning_move(arr, move, player):
    """
    Überprüft, ob ein Zug zu einem Gewinn führt.
    """
    temp_arr = copy.deepcopy(arr)
    row = get_next_empty_row(temp_arr, move)
    drop_piece(temp_arr, row, move, player)
    return is_winner(temp_arr)

start_time = time.time()
max_time = 0.2  # in seconds

while time.time() - start_time < max_time:
      # Führen Sie den Minimax-Algorithmus aus
  
    def minimax(arr, depth, maximizing_player, alpha, beta, player):
        if depth == 0 or is_winner(arr):
            return score_position(np.array(arr), player)

        valid_moves = [col for col in range(N_COLS) if not column_is_full(arr, col)]

        if maximizing_player:
            max_eval = float('-inf')
            for move in valid_moves:
                temp_board = copy.deepcopy(arr)
                row = get_next_empty_row(temp_board, move)
                drop_piece(temp_board, row, move, player)
                eval_score = minimax(temp_board, depth - 1, False, alpha, beta, player)
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in valid_moves:
                temp_board = copy.deepcopy(arr)
                row = get_next_empty_row(temp_board, move)
                drop_piece(temp_board, row, move, 3 - player)  # Switch player for opponent
                eval_score = minimax(temp_board, depth - 1, True, alpha, beta, player)
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval

      

def ai(arr, player):
    start_time = time.time()  # Startzeit messen
    max_time = 0.2  # in seconds
    depth = 1  # Starttiefe
    best_move = -1
    best_score = float('-inf')
    while time.time() - start_time < max_time:
        valid_moves = [col for col in range(N_COLS) if not column_is_full(arr, col)]

        for move in valid_moves:
            temp_board = copy.deepcopy(arr)
            row = get_next_empty_row(temp_board, move)
            drop_piece(temp_board, row, move, player)
            score = minimax(temp_board, depth, False, float('-inf'), float('inf'), player)

            if score > best_score:
                best_score = score
                best_move = move

        depth += 1
    end_time = time.time()  # Endzeit messen
    elapsed_time_seconds = end_time - start_time
    elapsed_time_milliseconds = elapsed_time_seconds * 1000  # Umrechnung in Millisekunden
    print(f"Die Ausführungszeit des nächsten Spielzugs von Spieler {player} ist : {elapsed_time_milliseconds:.2f} Millisekunden")
    print(f"Spieler {player} hat {best_move}  ausgewählt")
    # Konfiguration des Loggings
    def log_progress(arr):
        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write("\n")
            for row in range(len(arr) - 1, -1, -1):
                string =  '| '
                for col in range(len(arr[row])):
                    if arr[row][col] == 0:
                        string += '  '
                    elif arr[row][col] == 1:
                        string +=   'X '
                    elif arr[row][col] == 2:
                        string +=   'O '
                    else:
                        raise ValueError('Unknown value: ', arr[row][col])
                string +=  '| ' + str(row + 1)
                log_file.write(string + "\n")
            log_file.write('└ ─ ─ ─ ─ ─ ─ ─ ┘\n')
            log_file.write('  0 1 2 3 4 5 6  \n')
            log_file.write(f"Die Ausführungszeit des nächsten Spielzugs von Spieler {player} ist : {elapsed_time_milliseconds:.2f} Millisekunden")
            log_file.write(f"Spieler {player} hat {best_move}  ausgewählt")
         
    # Fortschritt in die Datei log.txt schreiben
    log_progress(arr)
    return best_move
    
