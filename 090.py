"""
Make a program that 4 players roll
a dice, and register the result in
a dictionary. Sort this one by knowing
the winner gets the high score of dice.
"""

from random import randint
from time import sleep

game = {}
count = 0

for k in range(1,5):
    game[f'player{k}'] = randint(1,6)

print(f'{" PLAYING DICE ":-^40}')
for p , d in game.items():
    print(f'{p.title()} took {d} on die.')
    sleep(0.5)
print(f'{" RANKING ":*^40}')
for p , d in sorted(game.items(), key = lambda kv : kv[1] , reverse = True):
    count += 1
    print(f'{count}º place: {p} with {d}.')
    sleep(0.5)
