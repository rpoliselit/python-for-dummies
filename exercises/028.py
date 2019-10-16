"""
Make a program that the user has to guess a number
between 1 and 5, then returns winner or loser.
"""

from random import randint
w, l = 0, 0

play = 'y'
while play == 'y':

    guess = int(input('Make your guess: '))
    number = randint(1,5)

    if guess == number:
        print('You wins!')
        w += 1
    else:
        print('You lose!\nCorrect answer is {}.'.format(number))
        l += 1

    play = str(input('Play again? [y/n]\n')).strip().lower()

score = 100 * w / (w + l)
print('Score = {:.1f}%.\nW: {}\nL: {}'.format(score,w,l))
