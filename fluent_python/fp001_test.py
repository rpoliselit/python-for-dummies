from fp001_FrenchDeck import Card, FrenchDeck
from random import choice

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

def new_print(string):
    print('_'*30 + '\n' + str(string))


deck = FrenchDeck()

new_print(FrenchDeck.ranks)
new_print(FrenchDeck.suits)

beer_card = Card('K','spades')

new_print(beer_card)
new_print(beer_card.rank)
new_print(beer_card in deck)
new_print(len(deck))
new_print(deck[0])
new_print(choice(deck))

for card in deck:
    if card == deck[0]:
        new_print(card)
    else:
        print(card)

for card in reversed(deck):
    if card == deck[-1]:
        new_print(card)
    else:
        print(card)

for card in sorted(deck, key=spades_high):
    if spades_high(card) == 0:
        new_print(card)
    else:
        print(card)
