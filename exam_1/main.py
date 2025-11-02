from game_logic import game

if __name__ == '__main__':
    game.init_game()
    while len(game.init_game()["player_1"]["hand"]) > 0 and len(game.init_game()["player_2"]["hand"]) > 0:
        game.play_round(game.init_game()["player_1"], game.init_game()["player_2"])



    # p1_won_pile = len(game.init_game()["player_1"]["won_pile"])
    # p2_won_pile = len(game.init_game()["player_2"]["won_pile"])
    # if p1_won_pile > p2_won_pile:
    #     print(f"The winner is {game.init_game()["player_2"]["name"]}!")
    # if p1_won_pile < p2_won_pile:
    #     print(f"The winner is {game.init_game()["player_2"]["name"]}!")
    # else:
    #     print("draw...")
