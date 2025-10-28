from game_logic import game

if __name__ == '__main__':
    game.init_game()
    game.play_round(game.init_game()["player_1"], game.init_game()["player_2"])
