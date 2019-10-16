"""
Make a program that helps a gambler
to bet in lottery. The application
reads the number of tickets, and
generates 6 random numbers between
1 and 60. They can repeat on the
same ticket. Every tickit must be
registered in a compound list.
"""

from random import randint
from time import sleep

tickets = []
bet = []

print(f'{"":-^40}\n{" LOTTERY TICKETS ":*^40}\n{"":-^40}')
num = int(input('Enter the number of lottery tickets: '))
num_bet = 0

print(f'{" MAKEING TICKETS ":=^40}')
for j in range(num):
    for i in range(6):
        while True:
            rand = randint(1,60)
            if rand not in bet:
                bet.append(rand)
                break
    tickets.append(bet[:])
    bet.clear()
    sleep(0.5)
    print(f'Ticket {j+1}: {sorted(tickets[-1])}')
print(f'{"< GOOD LUCK! >":-^40}')
