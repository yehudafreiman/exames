import utils

def create_player(name:str):
    player = {'name':name, 'hand':[],'won_pile':[]}
    if name == '':
        player['name'] = 'AI'
    return player
print(create_player(''))

def init_game():
    player_1 = create_player('yehuda')
    player_2 = create_player('')
    deck = shuffle(create_deck())
    player_1['hand'] = deck[:27]
    player_2['hand'] = deck[27:]
    game = {'deck': deck, 'player_1': player_1, 'player_2': player_2}
    return game

def play_round(p1:dict, p2:dict):
    return None




