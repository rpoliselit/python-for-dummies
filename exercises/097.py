"""
Make a program that has a function
called counter with three parameters:
start, end, and increment.

The program must performance three
counting via this function:

1 - from 1 to 10 forward one by one.
2 - from 10 to 0 forward two by two.
3 - custom one.
"""

from time import sleep

def counter(start, end, inc):
    print('='*40)
    print(f'Counting from {start} to {end} forward {inc} by {inc}:')
    if start > end:
        end -= 1
        inc *= -1
    elif start < end:
        end += 1
    if inc == 0:
        inc = 1
    for num in range(start, end, inc):
        print(f'{num}', end = ' ', flush = True)
        sleep(0.5)
    print('END!')


counter(1, 10, 1)
counter(10, 0, 2)
print('-'*40)
print('That is your time! Enter custom parameters.')
s = int(input('Start: '))
e = int(input('End: '))
i = abs(int(input('Increment: ')))
counter(s,e,i)
