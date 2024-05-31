import ai1
import ai2
from helper import *


def select_player_type(player):
    # select type of player (human/random/ai)
    if player == PLAYER_1:
        if PLAYER_1_TYPE == 'human':
            return human_player
        elif PLAYER_1_TYPE == 'random':
            return random_player
        elif PLAYER_1_TYPE == 'ai':
            return ai1.ai
        else:
            raise ValueError('Unknown player type: ', PLAYER_1_TYPE)

    elif player == PLAYER_2:
        if PLAYER_2_TYPE == 'human':
            return human_player
        elif PLAYER_2_TYPE == 'random':
            return random_player
        elif PLAYER_2_TYPE == 'ai':
            return ai2.ai
        else:
            raise ValueError('Unknown player type: ', PLAYER_2_TYPE)


def play_one_game():
    turn = 0
    arr = initialize_board()
    game_status = get_game_status(arr=arr)
    start_player = select_start_player()

    while game_status == GAME_NOT_FINISHED:
        player = select_player(turn=turn, start_player=start_player)
        output_board(arr=arr)
        output_active_player(player=player)
        player_type = select_player_type(player=player)
        col = select_column(arr=arr, player=player, player_type=player_type)
        arr = place_token(arr=arr, col=col, player=player)
        game_status = get_game_status(arr=arr)
        turn += 1

    output_board(arr=arr)
    output_game_status(game_status)

    return game_status


if __name__ == "__main__":
    player_1_wins = 0
    player_2_wins = 0
    draws = 0

    for i in range(N_GAMES_PLAYED):
        game_status = play_one_game()
        if game_status == PLAYER_1_WINS:
            player_1_wins += 1
        elif game_status == PLAYER_2_WINS:
            player_2_wins += 1
        elif game_status == DRAW:
            draws += 1

        print('Result:', player_1_wins, player_2_wins, draws)

