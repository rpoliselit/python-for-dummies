"""
Make a game that cpu choose a number,
and player must guess. The game runs
until player hit the guess.
"""

from random import randint

cpu = randint(0,10)
guess = player = 0

print('Guess a number between 0 and 10')
while player != cpu:
    player  = int(input())
    guess += 1
    if player > cpu:
        print('Try a lesser one!')
    elif player < cpu:
        print('Try a greather one!')
print('You got it right with ', end = '')
if guess == 1:
    print('the FIRST guess!')
else:
    print('{} hunches!'.format(guess))
