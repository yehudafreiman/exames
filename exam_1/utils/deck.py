def create_card(rank:str,suite:str):
    ranks_and_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
    card = {'rank':rank,'suite':suite,'value':ranks_and_values[rank]}
    return card
# print(create_card('5','S'))

def compare_cards(p1_card:dict, p2_card:dict):
    if p1_card['value'] > p2_card['value']:
        return 'p1'
    if p1_card['value'] < p2_card['value']:
        return 'p2'
    else:
        return 'war'
# print(compare_cards(create_card('5','S'), create_card('10','S')))

def create_deck():
    deck = []
    # ranks = [1,2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    # suits = ['H','C','D','S']
    # values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    i = 1
    while i <= 52:
        deck.append(create_card('2','H'))
        i += 1
    return deck
# print(create_deck())
# print(len(create_deck()))

def shuffle(deck:list[dict]):
    deck_shuffled = []
    return deck_shuffled

