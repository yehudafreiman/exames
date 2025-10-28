def create_card(rank:str,suite:str):
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    value = ranks.index(rank) + 2
    return {'rank':rank,'suite':suite,'value':value}

def compare_cards(p1_card:dict, p2_card:dict):
    if p1_card['value'] > p2_card['value']:
        return 'p1'
    if p1_card['value'] < p2_card['value']:
        return 'p2'
    else:
        return 'war'

def create_deck():
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suites = ['H','C','D','S']
    deck = []
    for rank in ranks:
        for suite in suites:
            deck.append(create_card(rank=rank,suite=suite))
    return deck

import random
def shuffle(deck:list[dict]):
    shuffled_deck = create_deck()
    for i in range(1,1001):
        index1 = shuffled_deck[random.randint(1,52)]
        index2 = shuffled_deck[random.randint(1,52)]
        if index1 != index2:
            shuffled_deck[index1], shuffled_deck[index2] == shuffled_deck[index2], shuffled_deck[index1]
    return shuffled_deck