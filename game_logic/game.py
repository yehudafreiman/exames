from utils import deck

def create_player(name:str):
    player = {'name':name, 'hand':[],'won_pile':[]}
    if not name:
        player['name'] = 'AI'
    return player


def init_game():
    player_1 = create_player(name='yehuda')
    player_2 = create_player(name="")

    shuffled_deck = deck.shuffle(deck.create_deck())

    player_1['hand'] = shuffled_deck[:27]
    player_2['hand'] = shuffled_deck[27:]

    game = {'deck': shuffled_deck, 'player_1': player_1, 'player_2': player_2}
    return game

def play_round(p1:dict, p2:dict):
    p1_top_card = init_game()["player_1"]["hand"][0]
    p2_top_card = init_game()["player_2"]["hand"][0]
    top_cards = [p1_top_card, p2_top_card]

    higher = deck.compare_cards(p1_top_card, p2_top_card)
    if higher == "p1":
        init_game()["player_1"]["won_pile"].append(top_cards)
        print(f"Player {init_game()["player_1"]["name"]} takes everything!")
    if higher == "p2":
        init_game()["player_2"]["won_pile"].append(top_cards)
        print(f"Player {init_game()["player_2"]["name"]} takes everything!")
    return None




