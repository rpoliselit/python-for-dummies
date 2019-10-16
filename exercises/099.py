"""
Make a program that a list - called numbers -
and two functions - called raffle and evenSum.
First function raffles five numbers, and puts
them in the list. Second function show the sum
of all even raffle numbers by the previous
function.
"""

from time import sleep
from random import randint

def raffle(num , alist):
    print(f'Raffing {num} values for the list: ', end = '')
    n = 0
    while n < num:
        x = randint(0,100)
        alist.append(x)
        n += 1
        print(f'{x}', end = ' ', flush = True)
        sleep(0.5)
    print('DONE!')

def evenSum(alist):
    sum =  0
    for n in alist:
        if n % 2 == 0:
            sum += n
    print(f'Adding the even numbers from {numbers} yields {sum}.')



numbers = []
raffle(5, numbers)
evenSum(numbers)
