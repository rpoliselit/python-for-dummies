"""
Make a game that plays bucking up
until the player loses, and show
the number of consecutive wins.
"""
from random import randint
from time import sleep

print('{:*^31}\n'.format(' BUCKING UP CHAMPIONSHIP '))
wins = 0
while True:
    choice = ' '
    while choice not in 'EO':
        choice = str(input('Choose [e]ven or [o]dd: ')).strip().upper()[0]
    player = int(input('Pick a number of fingers: '))
    print('CPU is picking its fingers...')
    cpu = randint(0,5)
    sleep(1)
    print(f"""\n{player} vs {cpu}""")
    parity = (player + cpu)%2
    if (parity == 0 and choice == 'E') or (parity != 0 and choice == 'O'):
        print('You win!!!\nOnce again!\n')
        wins += 1
    else:
        print('You lose...')
        break
print(f'GAME OVER! You win {wins} times.')
